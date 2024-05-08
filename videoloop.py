from os import environ
environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import predict
from cv2 import flip,cvtColor, line, imread, circle,COLOR_BGR2RGB
from cvzone.HandTrackingModule import HandDetector
hd = HandDetector(maxHands=1)
from customtkinter import CTkImage
from PIL import Image
from threading import Thread
from traceback import format_exc

def Vl(self):
    try:
        _, frame = self.vs.read()
        cv2image = flip(frame, 1)
        hands = hd.findHands(cv2image, draw=False, flipType=True)
        cv2image = cvtColor(cv2image, COLOR_BGR2RGB)
        self.current_image = Image.fromarray(cv2image)
        imgtk = CTkImage(light_image=self.current_image,dark_image=self.current_image,size=(640,480))
        self.panel.imgtk = imgtk
        self.panel.configure(image=imgtk)

        if hands[0]:
            # #print(" --------- lmlist=",hands[1])
            hand = hands[0][0]
            _, _, w, h = hand['bbox']

            white = imread(fr"C:\Users\Harnoor\Documents\LOL\white.jpg")
            # img_final=img_final1=img_final2=0
            print(" ", self.ccc)
            self.ccc += 1
            if hands:
                hand = hands[0][0]
                self.pts = hand['lmList']
                # x1,y1,w1,h1=hand['bbox']

                os = ((400 - w) // 2) - 15
                os1 = ((400 - h) // 2) - 15
                
                for t in range(0, 4, 1):
                    line(white, (self.pts[t][0] + os, self.pts[t][1] + os1), (self.pts[t + 1][0] + os, self.pts[t + 1][1] + os1),
                                (0, 255, 0), 3)
                    
                for t in range(5, 8, 1):
                    line(white, (self.pts[t][0] + os, self.pts[t][1] + os1), (self.pts[t + 1][0] + os, self.pts[t + 1][1] + os1),
                                (0, 255, 0), 3)
                    
                for t in range(9, 12, 1):
                    line(white, (self.pts[t][0] + os, self.pts[t][1] + os1), (self.pts[t + 1][0] + os, self.pts[t + 1][1] + os1),
                                (0, 255, 0), 3)
                    
                for t in range(13, 16, 1):
                    line(white, (self.pts[t][0] + os, self.pts[t][1] + os1), (self.pts[t + 1][0] + os, self.pts[t + 1][1] + os1),
                                (0, 255, 0), 3)
                    
                for t in range(17, 20, 1):
                    line(white, (self.pts[t][0] + os, self.pts[t][1] + os1), (self.pts[t + 1][0] + os, self.pts[t + 1][1] + os1),
                                (0, 255, 0), 3)
                    
                line(white, (self.pts[5][0] + os, self.pts[5][1] + os1), (self.pts[9][0] + os, self.pts[9][1] + os1), (0, 255, 0),
                            3)
                
                line(white, (self.pts[9][0] + os, self.pts[9][1] + os1), (self.pts[13][0] + os, self.pts[13][1] + os1), (0, 255, 0),
                            3)
                
                line(white, (self.pts[13][0] + os, self.pts[13][1] + os1), (self.pts[17][0] + os, self.pts[17][1] + os1),
                            (0, 255, 0), 3)
                
                line(white, (self.pts[0][0] + os, self.pts[0][1] + os1), (self.pts[5][0] + os, self.pts[5][1] + os1), (0, 255, 0),
                            3)
                
                line(white, (self.pts[0][0] + os, self.pts[0][1] + os1), (self.pts[17][0] + os, self.pts[17][1] + os1), (0, 255, 0),
                            3)
                

                for i in range(21):
                    circle(white, (self.pts[i][0] + os, self.pts[i][1] + os1), 2, (0, 0, 255), 1)
                    

                res=white
                self.thread2 = Thread(target=predict.predict(self,res))
                self.thread2.start()

                self.current_image2 = Image.fromarray(res)

                imgtk = CTkImage(light_image=self.current_image2,dark_image=self.current_image2,size=(640,480))

                self.panel2.imgtk = imgtk
                self.panel2.configure(image=imgtk)
                
                self.panel3.configure(text=self.current_symbol, font=self.fnt_nb)
                #self.panel4.configure(text=self.word, font=self.fnt_nb)                 

        self.panel4.configure(text=self.str, font=self.fnt_nb)
    except Exception:
        print("==", format_exc())
    finally:
        self.root.after(1, Vl(self))
