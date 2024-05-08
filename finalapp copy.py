# Importing Libraries
from warnings import filterwarnings
import videoloop as video_loop
filterwarnings("ignore")
from logging import disable, WARNING
disable(WARNING)
from threading import Thread
from math import sqrt
from cv2 import VideoCapture,destroyAllWindows
from os import environ
environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from pyttsx3 import init
from keras.models import load_model #type:ignore
from cvzone.HandTrackingModule import HandDetector
hd = HandDetector(maxHands=1)
from customtkinter import CTk, CTkLabel, CTkButton

offset=29

environ["THEANO_FLAGS"] = "device=cuda, assert_no_cpu_op=True"

# Application :
class Application:

    def __init__(self):
        self.vs = VideoCapture(0)
        self.current_image = None
        self.model = load_model(fr"C:\Users\Harnoor\Documents\LOL\models\final_model.h5")

        self.prev_char=""
        self.count=-1
        self.ten_prev_char=[" "," "," "," "," "," "," "," "," "," ",]

        print("Loaded model from disk")

        self.root = CTk()
        self.root.title("GestoSpeech")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("1300x700")

        fnt=("Courier", 30, "bold")
        self.fnt_nb=("Courier", 30)

        self.panel = CTkLabel(self.root,text="", width=480, height=640)
        self.panel.place(x=100, y=3)

        self.panel2 = CTkLabel(self.root,text="", width=480, height=640)  # initialize image panel
        self.panel2.place(x=800, y=3)

        self.T = CTkLabel(self.root,text="")
        self.T.place(x=60, y=5)
        self.T.configure(text="GestoSpeech", font=fnt)

        self.panel3 = CTkLabel(self.root,text="")  # Current Symbol
        self.panel3.place(x=280, y=585)

        self.T1 = CTkLabel(self.root,text="")
        self.T1.place(x=10, y=580)
        self.T1.configure(text="Character :", font=fnt)

        self.panel4 = CTkLabel(self.root,text="")  # Sentence
        self.panel4.place(x=260, y=632)

        self.T3 = CTkLabel(self.root,text="")
        self.T3.place(x=10, y=632)
        self.T3.configure(text="Sentence :", font=fnt)

        self.speak = CTkButton(self.root)
        self.speak.place(x=1150, y=630)
        self.speak.configure(text="Speak", font=self.fnt_nb, command=self.speak_fun)

        self.clear = CTkButton(self.root)
        self.clear.place(x=1000, y=630)
        self.clear.configure(text="Clear", font=self.fnt_nb, command=self.clear_fun)

        self.str = " "
        self.ccc=0
        self.word = " "
        self.current_symbol = "C"

        self.thread = Thread(target=video_loop.Vl(self))
        self.thread.start()

    def distance(self,x,y):
        return sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
              
    def speak_fun(self):
        self.speak_engine=init()
        self.speak_engine.setProperty("rate",100)
        voices=self.speak_engine.getProperty("voices")
        self.speak_engine.setProperty("voice",voices[0].id)
        self.speak_engine.say(self.str)
        self.speak_engine.runAndWait()
        
    def clear_fun(self):
        self.str=" "

    def destructor(self):

        print("Closing Application...")
        print(self.ten_prev_char)
        self.root.destroy()
        self.vs.release()
        destroyAllWindows()

print("Starting Application...")

App = Thread(target=(Application()).root.mainloop())
App.start()