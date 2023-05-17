import os

import openai
from utils import Log

from news.core.NewsArticleLibrary import NewsArticleLibrary

WIDTH = 1_600
HEIGHT = int(WIDTH * 9 / 16)
F_FIG = 100
FIG_WIDTH, FIG_HEIGHT = WIDTH // F_FIG, HEIGHT // F_FIG

MAX_ARTICLES = 100

log = Log('build_wordcloud')


def main():
    english_articles = NewsArticleLibrary().summary_en
    len(english_articles)
    i_start = 0
    latest_english_articles = list(
        reversed(english_articles[i_start: i_start + MAX_ARTICLES])
    )

    messages = []
    for article in latest_english_articles:
        message = dict(role="user", content=article['original_title'])
        messages.append(message)
    cmd_message = dict(
        role="system",
        content='''
You have been given several news article headlines by the user.
To test the users knowledge about the most important articles,
PRINT 10 questions with short, specific answers.
    ''',
    )
    messages.append(cmd_message)

    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=messages,
    )
    reply = response['choices'][0]['message']['content']
    print(reply)


if __name__ == '__main__':
    main()
