from flask import Flask, render_template, request
import os
import pyttsx3 
from MEDICAL_ASSISTANT import mainCode
import LISTEN
from flask import jsonify 

filenumber=int(os.listdir('saved_conversations')[-1])
print(os.listdir('saved_conversations'))
print(filenumber)
filenumber=filenumber+1
print(filenumber)
file= open('saved_conversations/'+str(filenumber),"w+")
print(file)
file.write('bot : Hi There! I am a medical chatbot. You can begin conversation by typing in a message and pressing enter.\n')
file.close()

app = Flask(__name__)
name = ""
age = ""
gender = ""
deases = ""
symptom = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/welcome")
def greet():
    engine = pyttsx3.init() 
    engine.say('Hi There! I am a medical assistant. You can begin conversation by your voice in a message and pressing enter.')
    engine.say('I can help you find out what\'s going on with a simple medical assisment.')
    engine.runAndWait() 
    return ""
@app.route("/get")
def get_bot_response():
    userText = LISTEN.listening()
    response = str('')
    engine = pyttsx3.init() 
    
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()
    engine.say(response)
    engine.runAndWait() 

    return jsonify({'res':response,'inp':userText})



@app.route("/askname")
def askingname():
    response = mainCode.askName()
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('bot : '+response+'\n')
    appendfile.close()
    engine = pyttsx3.init() 
    engine.say(response)
    engine.runAndWait() 
    return response

@app.route("/askage")
def askingage():
    response = mainCode.askAge()
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('bot : '+response+'\n')
    engine = pyttsx3.init() 
    engine.say(response)
    engine.runAndWait() 
    return response

@app.route("/askgender")
def askinggender():
    response = mainCode.askGender()
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('bot : '+response+'\n')
    engine = pyttsx3.init() 
    engine.say(response)
    engine.runAndWait() 
    return response

@app.route("/asksymptom")
def askingsymptom():
    response ='Can you please discribe your Symptoms'
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('bot : '+response+'\n')
    engine = pyttsx3.init() 
    engine.say(response)
    engine.runAndWait() 
    return response

@app.route("/askdeases")
def askingdeases():
    response = 'Before we ask you your symptoms, we would like to know your health status.'
    response += 'If yout have any existing Medical Conditions or Problems, please provide them here.'
    response += 'If you dont, you can reply with a \'no\''
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('bot : '+response+'\n')
    engine = pyttsx3.init() 
    engine.say(response)
    engine.runAndWait() 
    return response

@app.route("/getname")
def gettingname():
    userText = LISTEN.listening()
    name = userText
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    #engine = pyttsx3.init() 
    #engine.say(response)
    #engine.runAndWait() 
    return userText

@app.route("/getage")
def gettingage():
    userText = LISTEN.listening()
    age = userText
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    #engine = pyttsx3.init() 
    #engine.say(response)
    #engine.runAndWait() 
    return userText

@app.route("/getgender")
def gettinggender():
    userText = LISTEN.listening()
    gender = userText
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
 
    #engine = pyttsx3.init() 
    #engine.say(response)
    #engine.runAndWait() 
    return userText

@app.route("/getdeases")
def gettingdeases():
    userText = LISTEN.listening()
    deases = userText
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    #engine = pyttsx3.init() 
    #engine.say(response)
    #engine.runAndWait() 
    return userText

@app.route("/getsymptom")
def gettingsymptom():
    userText = LISTEN.listening()
    symptom = userText
    
    existingDiseases = mainCode.extDisease(symptom)

    response = "The most suitable medecine is for your Symptom is '"+existingDiseases+"'"
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()
    
    return jsonify({'res':response,'inp':userText})



if __name__ == "__main__":
    app.run()
