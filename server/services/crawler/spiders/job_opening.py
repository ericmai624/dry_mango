import scrapy
import urllib
import json


class JobOpeningSpider(scrapy.Spider):
    name = "job_openings"

    def start_requests(self):
        list = [{"parser": self.parse_kp, "url": self.get_kp_url()}]
        for item in list:
            yield scrapy.Request(url=item["url"], callback=item["parser"])

    def get_kp_url(self):
        base = "https://www.kaiserpermanentejobs.org/search-jobs/results"
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
        return base + "?" + urllib.parse.urlencode(query)

    def parse_kp(self, response):
        results = json.loads(response.body)["results"]
        list = scrapy.Selector(text=results).css("li")
        for item in list:
            print("----- res: ", item.extract())
