import scrapy


class NursingJobsSpider(scrapy.Spider):
    name = "nursing_jobs"

    def start_requests(self):
        urls = [
            "https://www.kaiserpermanentejobs.org/search-jobs/nurse/California%2C%20US/641/1/3/6252001-5332921/37x25022/-119x751259/20/2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        job_list = response.css("section#search-results-list")[0].extract()
        print("------ job list: ", job_list)
        self.log(response.url)
