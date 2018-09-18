'''"take any book (text book) and grab chapter wise text from that. 
You should be able to remove all prepositions , articles, pronouns  
and show only words which are noun,adjectives,verbs.
 And then, from that set of words,
 again the words that are being repeated more should be highlighted with red color
 (5 plus times from the whole text you have selected ),
 repeated medium should get highlighted with blue (3 to 4 times) 
 and repeated less (1 to 2 times) and 
 things that did not get repeated are to be left with normal color without any color change
: Usually this thing is done to identify key words to remember in the text when learning any text .
 Helps students in remembering key words 
 so that they can read only them during revision time for quick rasping of information.'''


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
exist_file = open(r'D:\python\Anaconda_programs\testing1.txt', 'r')
example_sent=exist_file.read()
print(example_sent)
word_tokens = word_tokenize(example_sent)
 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
#print(word_tokens)
#print(filtered_sentence)
sent_str = ""
for i in filtered_sentence:
    sent_str += str(i) + " "
sent_str = sent_str[:-1]
print(sent_str)
from collections import Counter
import re
reg = re.compile('\S{4,}')
s = sent_str
c = Counter(ma.group() for ma in reg.finditer(s))
#print(c)
for K in c:
    #print(K)
    if(c[K]>=1 and c[K]<=2):
         print('\033[00;00m' + K + '\033[m')
    elif(c[K]>=3 and  c[K]<=4):
       print('\033[1;32m"'+ K + '"\033[m')#green
    else:
        print('\033[22;33m"'+ K +'"\033[m')#red
        
  