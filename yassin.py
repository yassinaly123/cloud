import nltk
from nltk.corpus import stopwords
def main():
    nltk.download('stopwords')
    with open("paragraphs.txt", 'r') as file:
        paragraph = file.read().replace('\n', ' ')
        stopWords = stopwords.words('english')
        paragraph = paragraph.lower()
        paragraph = ' '.join([word for word in paragraph.split() if word not in stopWords])
    word_freq = {}
    for word in paragraph.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print(word_freq[:100])

if _name_ == '_main_':
    main()