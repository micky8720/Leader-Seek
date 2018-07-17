import nltk
from nltk.corpus import brown, movie_reviews, reuters
from nltk.corpus import webtext
#from gensim import corpora, models, similarities
#from py2cytoscape.data.cyrest_client import CyRestClient
#import matplotlib.pyplot as plt
#import networkx as nx
from sklearn.linear_model import LogisticRegression
from nltk.classify.scikitlearn import SklearnClassifier


nltk.download('webtext')
nltk.download('nps_chat')
#for fileid in webtext.fileids():
    #print fileid, webtext.raw(fileid)

#brown.categories()
#brown.words(categories='news')
#brown.sents(categories=['news', 'editorial', 'reviews'])

# news_text = brown.words(categories='reviews')
# print len(news_text)
# for news in news_text:
#     print news
# fdist = nltk.FreqDist([w.lower() for w in news_text])
# modals = ['can', 'could', 'may', 'might', 'must', 'will',"doesn't","can't","won't","don't", "couldn't","shouldn't","wouldn't"]

#for m in modals:
    #print m + ':', fdist[m]

# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = ['can', 'could', 'may', 'might', 'must', 'will',"doesn't","can't","won't","don't", "couldn't","shouldn't","wouldn't"]
# cfd.tabulate(conditions=genres, samples=modals)
#brown.words(fileids=['A16'])


#users = set()


posts = nltk.corpus.nps_chat.xml_posts()
# for post in posts:
#     users.add(post.get('user'))
#     if post.get('class')== 'Reject' or 'disagree' in post.text.lower():
#         print post.get('user'), ':', post.text, "(",post.get('class'),")"
# print len(users)
# print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
     features = {}
     for word in nltk.word_tokenize(post):
         features['contains({})'.format(word.lower())] = True
     return features

featuresets = [(dialogue_act_features(post.text), post.get('class'))
                for post in posts]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
#classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier = SklearnClassifier(LogisticRegression())
classifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))

dialog_Act_A = []
dialog_Act_B = []
users = []
textsp =  []
textsp1 =  []
data={}
with open('2009_04_28.txt', 'r') as groupA:
    for line in groupA:
        u = line.split('PM):')[0]
        user = u.split(' (')[0]
        text = line.split('PM):')[1]
        textsp.append(text)
        users.append(user)
        dialog_Act_A.append(classifier.classify(dialogue_act_features(text)))
        if((classifier.classify(dialogue_act_features(text)) == "ynQuestion") or (classifier.classify(dialogue_act_features(text)) == "whQuestion") ):
            previous=user
            if(previous in data):
                data[previous]=data[previous]+1
            else:
                data[previous] = 1



groupA.close()
print(dialog_Act_B)
print data

data={}
with open('2009_05_06.txt', 'r') as groupB:
    for line in groupB:
        u = line.split('PM):')[0]
        user = u.split(' (')[0]
        text = line.split('PM):')[1]
        textsp.append(text)
        users.append(user)
        dialog_Act_A.append(classifier.classify(dialogue_act_features(text)))
        if((classifier.classify(dialogue_act_features(text)) == "ynQuestion") or (classifier.classify(dialogue_act_features(text)) == "whQuestion") ):
            previous=user
            if(previous in data):
                data[previous]=data[previous]+1
            else:
                data[previous] = 1



groupB.close()
print(dialog_Act_A)
print data


# print(dialog_Act_B)

print(users)