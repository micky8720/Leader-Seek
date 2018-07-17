from lib2to3.pgen2 import token
from xml.etree import ElementTree as ET
import collections
import nltk

tree = ET.parse('2009_04_28.txt.xml')
root = tree.getroot()
e = 0

m_Count = 0
l_Count = 0
r_Count = 0
mod_Count = 0
aly_Count = 0
mel_Count = 0
car_Count = 0
ted_Count = 0
Count = 0

Count = 0
# d = {1: 'meg', 2: 'lynn', 3: 'rita', 4: 'moderator', 5: 'alyssa', 6: 'melany', 7: 'caroline', 8: 'ted'}



# get the list of all the noun and participant
p = 0
List_Name = list()
List_Noun = list()
List = ['Hi', 'Ok', 'ok', 'day', 'hahaha', 'haha', 'yeah', 'day', 'Day', 'hehe', 'lol', 'bye', 'yeap', 'lot', 'yea', 'none', 'bc', 'u', 'yeahhhh']
for i in range(len(root[0][0])):
    for j in range(len(root[0][0][i][0])):
        if (root[0][0][i][0][j][0].text in List):
            break
        elif root[0][0][i][0][j][4].text == 'NN' and root[0][0][i][0][0][0].text != root[0][0][i][0][j][0].text and \
                        root[0][0][i][0][j][0].text != ':-RRB-' and root[0][0][i][0][j][0].text != 'PM':
            print (p + 1, root[0][0][i][0][0][0].text, root[0][0][i][0][j][0].text)
            List_Noun.append(root[0][0][i][0][j][0].text)
            List_Name.append(root[0][0][i][0][0][0].text)
            p = p + 1

            # elif root[0][0][i][0][j][4].text =='PRP$':
            #      print(root[0][0][i][0][0][0].text , root[0][0][i][0][j][0].text)

print (List_Noun)

multi_noun = [item for item, count in collections.Counter(List_Noun).items() if count > 1]
print (multi_noun)
print(len(multi_noun), len(List_Noun))
List_Name_in = list()  # all speakers who introduce the topic list
List_Noun_multi = list()
# this is to count or get all participant who introduce the topic
for i in range(len(multi_noun)):
    # print(multi_noun[i])
    for j in range(len(List_Noun)):
        if (multi_noun[i] == List_Noun[j]):
            #print( j,List_Name[j],List_Noun[j])
            List_Name_in.append(List_Name[j])
            List_Noun_multi.append(List_Noun[j])
            break
#print(len(List_Name_in),len(List_Noun_multi))
freq_noun = nltk.FreqDist(List_Noun_multi)
freq = nltk.FreqDist(List_Name_in)
print ([freq])
print ([freq_noun])

