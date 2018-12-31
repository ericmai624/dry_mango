from os import getcwd, path
import subprocess

spiders = path.join(path.dirname(__file__), "spiders")


def run(spider):
    spider_path = path.join(spiders, spider)
    subprocess.Popen(["scrapy", "runspider", str.format("{}.py", spider_path)])
