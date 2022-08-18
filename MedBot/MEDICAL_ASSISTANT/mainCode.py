import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import random
import sys
from nltk.corpus import stopwords


#greeting file
gr = pd.read_csv('MEDICAL_ASSISTANT/Greeting_Dataset.csv', engine='python')
gr = np.array(gr)
gd = gr[:,0]

#thankyou file
tu = pd.read_csv('MEDICAL_ASSISTANT/ThankYou.csv', engine='python')
tu = np.array(tu)
td = gr[:,0]

#welcome file
wc = pd.read_csv('MEDICAL_ASSISTANT/Welcome Dataset.csv', engine='python')
wc = np.array(wc)
wd = wc[:,0]

#age file
ag = pd.read_csv('MEDICAL_ASSISTANT/AGE Dataset.csv', engine='python')
ag = np.array(ag)
ad = ag[:,0]

#bye file
by = pd.read_csv('MEDICAL_ASSISTANT/BYE Dataset.csv', engine='python')
by = np.array(by)
bd = by[:,0]

#name file
nm = pd.read_csv('MEDICAL_ASSISTANT/Name Dataset.csv', engine='python')
nm = np.array(nm)
nd = nm[:,0]

def stopWords(text):
    #text is a sentence
    stopw = set(stopwords.words('english'))
    filtered = []
    words = word_tokenize(text)
    for i in words:
        if i not in stopw:
            filtered.append(i)
    return filtered

def stemming(text):
    #text could be a sent or word
    ps = PorterStemmer()
    empty = []
    for w in text:
        empty.append(w)
    return empty
        

def getName(text):
    #text is a/many sentence
    #takes the user response and returns name of the user
    filtered = stopWords(text)
    stemmed = stemming(filtered)
##    print("stemmed",stemmed)
    tag = nltk.pos_tag(stemmed)
    #print(tag)
    noun=[]
    for i in range(len(tag)):
##        print(tag[i][1])
        if ((str(tag[i][1])=='NN' or str(tag[i][1])=='NNP') and str(tag[i][0])!='name'):
            noun.append(tag[i][0])
##    print(noun)
##    chunkGram = r"""Chunk: {<NN+>*}  """
##    chunkParser = nltk.RegexpParser(chunkGram)
##    chunked = chunkParser.parse(tag)
##    print(chunked)
##    for i in chunked:
##        if i != ('name', 'NN'):
##            name = i
##            print('i=',i[0])
##
##    print(name[0])
    return text

def greet():
    k = random.randint(0,len(gd)-1)
    print(gd[k%11])

def askName():
    k = random.randint(0,len(nd)-1)
    return nd[k]

def askAge():
    k = random.randint(0,len(ad)-1)
    return ad[k]

def getAge(age):
  
    try:
        age = int(age)
        if age<=10 or age>=50:
      
            print('[INFO]Please contact nearby doctor')
            sys.exit(0)
    except Exception as e:
        print('[ERROR]Please enter valid age')
        sys.exit(0)
    return age

def askGender():
    return 'Are you a Male or a Female?'

def sorry():
    print('I\'m sorry I could not understand that. Let\'s try again.')

def getGender(text):
    #text is a sentence(string)
    #expected output: 'Male' or 'Female'
    filtered = stopWords(text)
    flag=0
    for i in filtered:
        if i.lower()=='male' or i.lower()=='female':
            gender = i
            flag=1
    if flag!=1:
        return 0
    else:
        return gender

def getEmail():
    inp = input()
##    sent = sent_tokenize(input)
##    words = word_tokenize(inp)
##    for i in words:
##        if '@' in i:
##            email = i
    #tokenizing not working :(
    return inp

def smokeAndAlc():
    print('Do you smoke?')
    inp1 = input()
    res1=0
    for i in inp1:
        stem = stemming(i)
        if 'yes' in stem or 'yea' in stem or 'yeah' in stem:
            res1=1
    print('Do you consume Alcohol?')
    inp2 = input()
    res2=0
    for i in inp2:
        stem = stemming(i)
        if 'yes' in stem or 'yea' in stem or 'yeah' in stem:
            res2=1
    return (res1*10)+res2

def getZip():
    inp = input()
    #tok = word_tokenize()
    code=0
    for i in inp:
        try:
            code =code*10+int(i)
        except Exception as e:
            continue
    return code

def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num

def getDeases(syms):
    dfs = []
    df = pd.read_csv('MEDICAL_ASSISTANT/final dataset.csv', engine='python')
    print(df)
    for sym in syms:
        df1 = df['DESEASE'][df['SYMTOM'].str.contains(sym.lower())]
        if len(list(df1)) > 0:
            dfs.extend(list(df1))
    des = most_frequent(dfs)
    return des
def getMedicine(des):
    df = pd.read_csv('MEDICAL_ASSISTANT/DATASET.csv', engine='python')
    df1 = df['MEDICINE'][df['DISEASE']==des]
    print(df1)
    return list(df1)[0]

def extDisease(inp):
    filtered_sentence = []
    word_tokens = word_tokenize(inp)
    stop_words = set(stopwords.words('english')) 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w)
    print(filtered_sentence)
    des = getDeases(filtered_sentence)
    med = getMedicine(des)
    return med
  

def getSymptoms():
    text = input()
    filtered = stopWords(text)
    stemmed = stemming(filtered)
    print(stemmed)
    
'''
#Starting the conversation 
greet()
print('I\'m MedBot, your personal health assistant.')
print("I can help you find out what's going on with a simple symptom assisment.")
ufName = askName()
name = getName(ufName)
ufAge = askAge()
age = getAge(20)
ufGender = askGender()
gender = getGender(ufGender)
while gender==0:
    sorry()
    ufGender = askGender()
    gender = getGender(ufGender)
print('To help you keep a record of your symptoms and enable us to provide you with better assistance, we would like you to provide us with your email. This is mandatory.')
email = getEmail()
print('Your ZipCode would enable us to provide personalised suggestions for hospitals. This is mandatory.')
zip = getZip()
sa=smokeAndAlc()
#sa = (smoke*10)+alc

##print('name = {}, age = {}'.format(name[0],age))
#print Everything
##print(name, age, gender, email, zip, sa, existingDiseases)
print('Okay {} '.format(name[0]))


existingDiseases = extDisease()

print("The most suitable medecine is for your Symptom is '"+existingDiseases+"'")
'''