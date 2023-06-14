from utils import File


def main():
    quiz_content = File('media/quiz/quiz.latest.txt').read()
    content = f'''
# Sri Lankan News
*Various Insights and Visualizations*

## Wordcloud
![wordcloud](media/wordcloud/wordcloud.latest.png)

## News Quiz
{quiz_content}



    '''

    File('README.md').write(content)


if __name__ == '__main__':
    main()
