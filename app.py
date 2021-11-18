from flask import Flask, render_template
from flask import request
app = Flask(__name__)
## import libraries
import os
import pywhatkit
from gtts import gTTS
from playsound import playsound

def Whatsapp(p,q):
    Message = str(p)
    Msg1 = str(q)
    Message = Message.split(',')
    Num = str(Message[0])
    Hr = int(Message[1])
    Min = int(Message[2])
    pywhatkit.sendwhatmsg(Num, Msg1, Hr, Min)
def Google(g):
    Search = str(g)
    pywhatkit.search(Search)
def Youtube(y):
    Search = str(y)
    pywhatkit.playonyt(Search)
def text_handwriting(t,l):
    Text = str(t)
    Location = str(l)
    pywhatkit.text_to_handwriting(Text,Location)
def Shutdown(x):
    Time = int(x)
    pywhatkit.shutdown(time=Time)
def Cancel_Shutdown():
    pywhatkit.cancelShutdown()
def Text_to_speech(m):
    Message = str(m)
    speech = gTTS(text = Message)
    speech.save('T2S.mp3')
    playsound('T2S.mp3')
    os.remove('T2S.mp3')
def check1(k, key):
    if key in k.keys():
        Google(k['search_enter'])
def check2(k, key):
    if key in k.keys():
        Youtube(k['video_enter'])
def check3(k, key):
    if key in k.keys():
        Shutdown(k['shutdown_enter'])
def check4(k, key):
    if key in k.keys():
        Text_to_speech(k['ttos_enter'])
def check5(k, key1,key2):
    if key1 in k.keys() and key2 in k.keys():
       text_handwriting(k['text_enter'],k['location_enter'])
def check6(k, key1,key2):
    if key1 in k.keys() and key2 in k.keys():
       Whatsapp(k['number_enter'],k['message_enter']) 
def check7(k, key):
    if key in k.keys():
        Cancel_Shutdown()   
@app.route("/", methods=["GET", "POST"])
def function_one(): 
    if request.form:   
        k=request.form  
        print(request.form) 
        check1(k,'search_enter') 
        check2(k,'video_enter')
        check3(k,'shutdown_enter')
        check4(k,'ttos_enter')    
        check5(k,'text_enter','location_enter')
        check6(k,'number_enter','message_enter')
        check7(k,'shutdown_cancel')
    return render_template('index.html')   #Ever ever remove this
print('loop exited')    
if __name__ == '__main__':
    app.run(debug=True)
    
