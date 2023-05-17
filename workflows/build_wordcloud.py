import os

import matplotlib.pyplot as plt
from utils import SECONDS_IN, Log, Time
from wordcloud import WordCloud

from news.core.NewsArticleLibrary import NewsArticleLibrary
from news.core.STOPWORDS import STOPWORDS

WIDTH = 1_600
HEIGHT = int(WIDTH * 9 / 16)
F_FIG = 100
FIG_WIDTH, FIG_HEIGHT = WIDTH // F_FIG, HEIGHT // F_FIG

DELTA_TIME_WINDOW = SECONDS_IN.DAY * 1

log = Log('build_wordcloud')


def main():
    english_articles = NewsArticleLibrary().summary_en
    time_cutfoff = Time.now().ut - DELTA_TIME_WINDOW
    latest_english_articles = [
        article
        for article in english_articles
        if float(article['time_ut']) > time_cutfoff
    ]

    text = ' '.join(
        [article['original_title'] for article in latest_english_articles]
    )
    wordcloud = WordCloud(
        width=WIDTH, height=HEIGHT, stopwords=STOPWORDS
    ).generate(text)

    image_path = 'wordcloud.png'
    n_latest_articles = len(latest_english_articles)

    plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(image_path)
    log.info(f'Saved wordcloud for {n_latest_articles} to {image_path}')
    os.startfile(image_path)


if __name__ == '__main__':
    main()
