import os
import shutil

import openai
from utils import File, Log, get_time_id

from news.core.NewsArticleLibrary import NewsArticleLibrary

WIDTH = 1_600
HEIGHT = int(WIDTH * 9 / 16)
F_FIG = 100
FIG_WIDTH, FIG_HEIGHT = WIDTH // F_FIG, HEIGHT // F_FIG
MAX_ARTICLES = 50

CMD_MESSAGE = dict(
    role="system",
    content='''
You have been given several news article titles by the user.

To test the users knowledge about the most important articles,
PRINT 10 questions and their answers as MARKDOWN.
''',
)

log = Log('build_wordcloud')


def get_content():
    english_articles = NewsArticleLibrary().summary_en
    i_start = 0
    latest_english_articles = list(
        reversed(english_articles[i_start: i_start + MAX_ARTICLES])
    )

    messages = []
    for article in latest_english_articles:
        message = dict(role="user", content=article['original_title'])
        messages.append(message)

    messages.append(CMD_MESSAGE)

    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=messages,
    )
    reply = response['choices'][0]['message']['content']
    return reply


def build_quiz():
    content = get_content()
    time_id = get_time_id()
    file_path = os.path.join('media', 'quiz', f'quiz.{time_id}.md')
    File(file_path).write(content)
    file_path_latest = os.path.join('media', 'quiz', 'quiz.latest.md')
    shutil.copyfile(file_path, file_path_latest)


if __name__ == '__main__':
    build_quiz()
