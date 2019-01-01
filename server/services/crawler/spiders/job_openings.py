from datetime import datetime
from database import db
from scrapy import Request, Selector, Spider
from time import mktime
from urllib import parse
import json


class JobOpeningSpider(Spider):
    name = "job_openings"

    def start_requests(self):
        list = [{"parser": self.parse_kp, "url": self.get_kp_url()}]
        for item in list:
            yield Request(url=item["url"], callback=item["parser"])

    def get_domain(self, key):
        map = {"kaiser": "https://www.kaiserpermanentejobs.org"}
        return map[key]

    def get_url(self, key, *args):
        list = [self.get_domain(key)]
        for arg in args:
            if arg[0] == "/":
                arg = arg[1:]
            list.append(arg)
        return "/".join(list)

    def get_kp_url(self):
        base = self.get_url("kaiser", "/search-jobs/results")
        query = {
            "ActiveFacetID": 0,
            "CurrentPage": 1,
            "Distance": 20,
            "Keywords": "nurse",
            "Location": "California, US",
            "Latitude": 37.25022,
            "Longitude": -119.75126,
            "LocationType": 3,
            "LocationPath": "6252001-5332921",
            "OrganizationIds": 641,
            "RecordsPerPage": 100000,
            "SearchResultsModuleName": "Search Results",
            "SearchFiltersModuleName": "Search Filters",
            "SortCriteria": 0,
            "SortDirection": 1,
            "SearchType": 1,
            "ShowRadius": False,
        }
        return str.format("{pathname}?{qs}", pathname=base, qs=parse.urlencode(query))

    def parse_kp(self, response):
        results = json.loads(response.body)["results"]
        positions = Selector(text=results).css("li")
        ids = set([])
        results = []
        for item in positions:
            id = item.css("a::attr(data-job-id)").extract_first()
            if id in ids:
                continue
            ids.add(id)
            data = {
                "id": id,
                "location": item.css("p.job-location::text").extract_first(),
                "position": item.css("h2::text").extract_first(),
                "post_date": self.normalize_date(
                    date=item.css("p.job-date-posted::text").extract_first(),
                    format="%m/%d/%Y",
                ),
                "url": self.get_url(
                    "kaiser", item.css("a::attr(href)").extract_first()
                ),
            }
            results.append(data)

    def normalize_date(self, *, date, format):
        timetuple = datetime.strptime(date, format).timetuple()
        return mktime(timetuple)

    def persist(self):
        return
