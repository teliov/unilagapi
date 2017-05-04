__author__ = 'teliov'

import urllib2, codecs
import re
from bs4 import BeautifulSoup as bs
import hashlib
import datetime

BASE_URL = "https://new.unilag.edu.ng/news/"


class UnilagScrap:

    def __init__(self, debug=False):
        self.base_url = BASE_URL
        self.debug = debug

    def get_news_items(self):
        news_items = []
        try:
            html = urllib2.urlopen(self.base_url)
            soup = bs(html, "html.parser")
            targets = soup.find_all("div", class_="fusion-post-content post-content")
            #date_format = "2017-05-02T15:15:20+0000"
            date_format ="%Y-%m-%dT%H:%M:%S"
            for target in targets:
                target_h2 = target.find("h2", class_="entry-title")
                target_h2_a = target_h2.find("a")
                target_link = target_h2_a['href']
                target_title = target_h2_a.get_text()
                target_p_meta = target.find("p", class_="fusion-single-line-meta")
                date_span = target_p_meta.find("span", class_="updated")
                target_date = date_span.get_text()
                content = target.find("div", class_="fusion-post-content-container").get_text()
                date_regex = "(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)(\+|-)(\d+):(\d+)"
                #target_date = re.sub(date_regex, "\g<1>-\g<2>-\g<3>T\g<4>:\g<5>:\g<6>\g<7>\g<8>\g<9>", target_date)
                target_date = re.sub(date_regex, "\g<1>-\g<2>-\g<3>T\g<4>:\g<5>:\g<6>", target_date)
                slug_regex = "http?s://.+/(.+)?/"
                slug = re.match(slug_regex, target_link).group(1)

                date_updated = datetime.datetime.strptime(target_date, date_format)
                news_obj = {
                    "title": target_title,
                    "link": target_link,
                    "date_format_string": date_format,
                    "date_updated": date_updated,
                    "intro_text": content,
                    "slug": slug,
                    "news_hash": hashlib.md5(slug+target_date).hexdigest()
                }

                news_items.append(news_obj)

            return news_items
        except urllib2.URLError:
            if self.debug:
                print "UrlError"
            return None
