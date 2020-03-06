import requests
import xml.etree.ElementTree as ET
from news_crawler.sitemap.sitemap import parse_sitemap
from news_crawler.sitemap.extractor import extract_text_from_url
import pandas as pd
from news_crawler.sitemap.data_elastic import elastic_sitemap


elastic_sitemap("https://www.epitech.eu/sitemap_index.xml",["loc", "lastmod"], sort = "loc", influxdb = True)




