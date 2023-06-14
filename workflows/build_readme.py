from utils import File
from workflows.build_quiz import build_quiz

from workflows.build_wordcloud import build_wordcloud


def main():
    quiz_content = File('media/quiz/quiz.latest.txt').read()
    content = f'''
# Sri Lankan News

*Various Insights and Visualizations*

![wordcloud](media/wordcloud/wordcloud.latest.png)

## News Quiz

{quiz_content}



    '''

    File('README.md').write(content)


if __name__ == '__main__':
    build_wordcloud()
    build_quiz()
    main()
