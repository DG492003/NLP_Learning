import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer

para = "tokenization is a fundamental aspect of NLP that prepares text data for further analysis. It transforms raw text into a structured format that machines can understand, enabling a wide range of applications from sentiment analysis to machine translation. Understanding and implementing effective tokenization techniques is crucial for anyone working in the field of NLP, as it directly impacts the performance and accuracy of NLP models. As NLP continues to evolve, so too will the methods and strategies for tokenization, making it an ever-important area of study and development."

#sentence tokenization
sent = nltk.sent_tokenize(para)
#creating stemming object
stemmer = PorterStemmer()

for i in range(len(sent)):
    words = nltk.word_tokenize(sent[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sent[i] = " ".join(words)
    print(sent[i])