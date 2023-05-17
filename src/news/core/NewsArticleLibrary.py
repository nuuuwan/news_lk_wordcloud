from functools import cached_property
from urllib.parse import urljoin

from utils import WWW, TSVFile

URL_SUMMARY = urljoin(
    'https://raw.githubusercontent.com',
    'nuuuwan/news_lk3_data/main/reports/summary.tsv',
)
HASH_SALT = '123019839120398'
HASH_LENGTH = 8


class NewsArticleLibrary:
    @cached_property
    def summary(self):
        content = WWW(URL_SUMMARY).download()
        d_list = TSVFile(content).read()
        d_list = sorted(d_list, key=lambda x: x['time_str'], reverse=True)
        return d_list

    @cached_property
    def summary_en(self):
        return [d for d in self.summary if d['original_lang'] == 'en']
