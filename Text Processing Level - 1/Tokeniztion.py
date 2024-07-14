import nltk
nltk.download()

para = "tokenization is a fundamental aspect of NLP that prepares text data for further analysis. It transforms raw text into a structured format that machines can understand, enabling a wide range of applications from sentiment analysis to machine translation. Understanding and implementing effective tokenization techniques is crucial for anyone working in the field of NLP, as it directly impacts the performance and accuracy of NLP models. As NLP continues to evolve, so too will the methods and strategies for tokenization, making it an ever-important area of study and development."

#Tokenizing Sentences
sent = nltk.sent_tokenize(para)
print(len(sent))
print(sent)

#Tokenizing Words
word = nltk.word_tokenize(para)
print(len(word))
print(word)