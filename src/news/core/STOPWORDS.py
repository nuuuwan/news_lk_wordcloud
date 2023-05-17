import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


nltk_stopwords = stopwords.words('english')


STOPWORDS = nltk_stopwords + ['Sri Lanka', 'Lanka', 'Colombo', 'Sri']
