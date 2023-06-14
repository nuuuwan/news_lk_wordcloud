import os
import webbrowser

from utils import File, Time, TimeFormat
from workflows.build_quiz import build_quiz
from workflows.build_wordcloud import build_wordcloud


def get_time_str():
    return TimeFormat('%B %d, %Y - %I:%M%p').stringify(Time.now())


def main():
    quiz_content = File('media/quiz/quiz.latest.txt').read()
    time_str = get_time_str()
    content = f'''
# Sri Lankan News

*Various Insights and Visualizations as of {time_str}*

![wordcloud](media/wordcloud/wordcloud.latest.png)

## News Quiz

{quiz_content}



    '''

    File('README.md').write(content)


if __name__ == '__main__':
    build_wordcloud()
    build_quiz()
    main()
    os.system('git add .')
    os.system('git commit -m "updated readme"')
    os.system('git push origin main')
    webbrowser.open('https://github.com/nuuuwan/news_lk_wordcloud')
