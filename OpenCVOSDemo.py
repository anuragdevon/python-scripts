''' This is Simple Operating system program.

    Programmed by : Anurag Kar
    
    Dated-18.12.2019 '''

import cv2

import numpy as np

import getpass 

import time

import sys

from playsound import playsound

from tkinter import *

from tkinter.colorchooser import askcolor



# Turning on the system

print("\nGetting Started :)")

i = 0
while i <= 5 :
    sys.stdout.write('\rloading |')
    time.sleep(0.1)

    sys.stdout.write('\rloading /')
    time.sleep(0.1)

    sys.stdout.write('\rloading -')
    time.sleep(0.1)

    sys.stdout.write('\rloading \\')
    time.sleep(0.1)

    i = i + 1


print("\n")  


# First boot phase

first = np.zeros((1080,1920,4),np.uint8)

first = cv2.imread('first.png',1)
cv2.imshow('Avanzado',first)

playsound('start.wav')

cv2.waitKey(5000) &0xFF
cv2.destroyAllWindows()


# Second boot phase

Logo = np.zeros((1080,1920,4),np.uint8)

Logo = cv2.imread('logo.png',1)
cv2.imshow('Avanzado',Logo)

playsound('logo.mp3')

cv2.waitKey(8000) &0xFF
cv2.destroyAllWindows()


# Third boot phase

On = np.zeros((1080,1920,4),np.uint8)
On = cv2.imread('on.png',1)
cv2.imshow('Avanzado',On)

playsound('on.mp3')

cv2.waitKey(5000) &0xFF
cv2.destroyAllWindows()

playsound('activated.mp3')


# Attempting to log into the system

log = np.zeros((1080,1920,4),np.uint8)

log = cv2.imread('op.png',1)
cv2.imshow('Avanzado',log)

playsound('op.mp3')

if cv2.waitKey(0) & 0xFF == ord('L') : 

    cv2.destroyAllWindows()


    # Moving to terminal

    term = np.zeros((1080,1920,4),np.uint8)

    term = cv2.imread('term.png',1)
    cv2.imshow('Avanzado',term)

    playsound('term.mp3')

    cv2.waitKey(5000) &0xFF
    cv2.destroyAllWindows()

    i = 0
    while i <= 1 :
        i = i + 1
        time.sleep(1)
        print(".")

    print("\n----------\n")   


    # Creating a new userName and password

    j = 0  

    playsound('type.mp3') 

    username = input('\nCreate a new user name : ')

    password = getpass.getpass()

    while(j == 0) :        
        print("Enter the password again, ")
        Password = getpass.getpass()
        if password == Password :
            j = 1

    i = 0
    while i <= 1 :
        i = i + 1
        time.sleep(1)
        print(".")

    playsound('saved.mp3')

    print('\n|Successfully stored!|')

    time.sleep(1)


    # Moving out of terminal

    print('\n----\nMoving out of terminal')

    i = 0
    while i <= 1 :
        i = i + 1
        time.sleep(1)
        print(".")

    print("-----\n")


    # Now getting Face recognition

    #Phase 1

    Facelock = np.zeros((1080,1920,4),np.uint8)

    Facelock = cv2.imread('facelock.png',1)
    cv2.imshow('Avanzado',Facelock)

    playsound('facelock.mp3')

    cv2.waitKey(5000) &0xFF
    cv2.destroyAllWindows()


    # Phase 2

    Ready = np.zeros((1080,1920,4),np.uint8)

    Ready = cv2.imread('ready.png',1)
    cv2.imshow('Avanzado',Ready)

    playsound('ready.mp3')

    cv2.waitKey(3000) &0xFF
    cv2.destroyAllWindows()


    # Phase 3

    Wait = np.zeros((1080,1920,4),np.uint8)
    
    Wait = cv2.imread('wait.png',1)

    playsound('wait.mp3')

    cv2.imshow('Avanzado',Wait)
    cv2.waitKey(7000) &0xFF
    cv2.destroyAllWindows()


    # Phase 4

    Ins = np.zeros((1080,1920,4),np.uint8)

    Ins = cv2.imread('ins.png',1)
    cv2.imshow('Avanzado',Ins)

    playsound('ins.mp3')

    if cv2.waitKey(0) &0xFF == 13 :

        cv2.destroyAllWindows()


    # Phase 5

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)
    
    while True:  

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Video', frame)
        if cv2.waitKey(0) & 0xFF == 27 :

            break

        elif cv2.waitKey(0) & 0xFF == ord('s') :

            cv2.imwrite("Face.png",frame)

    video_capture.release()
    cv2.destroyAllWindows()


    # Face-recognition is now set-up

    Done = np.zeros((1080,1920,4),np.uint8)

    Done = cv2.imread('done.png',1)
    cv2.imshow('Avanzado',Done)

    playsound('done.mp3')

    cv2.waitKey(4000) &0xFF
    cv2.destroyAllWindows()

elif cv2.waitKey(0) & 0xFF == ord('T') :

    cv2.destroyAllWindows()

    turnOff = np.zeros((1080,1920,4),np.uint8)

    turnOff = cv2.imread('turnoff.png',1)
    cv2.imshow('Avanzado',turnOff)

    playsound('turnoff.mp3')

    cv2.waitKey(7000) &0xFF
    cv2.destroyAllWindows()

    i = 0

    while i <= 1 :

        i = i + 1
        time.sleep(1)
        print(".")

    print("\n-----\n|Turned off Successfully!|")

    sys.exit(1)


# Logging out

logOut = np.zeros((1080,1920,4),np.uint8)

logOut = cv2.imread('logout.png',1)
cv2.imshow('Avanzado',logOut)

playsound('logout.mp3')

cv2.waitKey(5000) &0xFF
cv2.destroyAllWindows()


# Attempting to log into the system

# Phase 1

W = np.zeros((1080,1920,4),np.uint8)

W = cv2.imread('w.png',1)
cv2.imshow('Avanzado',W)

cv2.waitKey(2000) & 0xFF
cv2.destroyAllWindows()


# Phase 2

log = np.zeros((1080,1920,4),np.uint8)

log = cv2.imread('op.png',1)
cv2.imshow('Avanzado',log)

playsound('op.mp3')

if cv2.waitKey(0) & 0xFF == ord('L') : 

    cv2.destroyAllWindows()

    #Getting into the options

    List = np.zeros((1080,1920,4),np.uint8)
    List = cv2.imread('list.png',1)

    cv2.imshow('Avanzado',List)
    playsound('list.mp3')

    if cv2.waitKey(0) & 0xFF == ord('P') :

        cv2.destroyAllWindows()
        
        # Moving to terminal

        term = np.zeros((1080,1920,4),np.uint8)

        term = cv2.imread('term.png',1)
        cv2.imshow('Avanzado',term)

        playsound('term.mp3')

        cv2.waitKey(5000) &0xFF
        cv2.destroyAllWindows()

        i = 0
        while i <= 1 :

            i = i + 1
            time.sleep(1)
            print(".")

        print("\n----------\n")
      
        # sound here

        print("Enter the password ",format(username))

        i = 0
        while i <= 1:

            i = i + 1
            time.sleep(1)
            print(".")
        
        passWord = getpass.getpass()

        i = 11

        while i <= 10:

            if passWord != password :

                j = 0
                while j <= 3 :

                    time.sleep(1)
                    print(".")
                    j = j + 1     

                print("\nOops!, Wrong password\n")

                if i == 10 :

                    print("System threat detected !\n")
                    time.sleep(1)
                    print("Erasing memory---")

                    j = 0

                    while j <= 3 :

                        time.sleep(1)
                        print(".")
                        j = j + 1

                    print('''-----Successfully erased!-----''')
                    print("\n-----\nSystem commanded to sudden turn off.")

                    j = 0

                    while j <= 1 :

                        time.sleep(1)
                        print(".")
                        j = j + 1
                    
                    # Turning off

                    turnOff = np.zeros((1080,1920,4),np.uint8)

                    turnOff = cv2.imread('turnoff.png',1)
                    cv2.imshow('Avanzado',turnOff)

                    playsound('turnoff.mp3')

                    cv2.waitKey(7000) & 0xFF
                    cv2.destroyAllWindows()

                    j = 0

                    while j <= 1 :  

                        j = j + 1
                        time.sleep(1)
                        print(".")

                    print("\n-----\n|Turned off Successfully!|")
                    sys.exit(1)

                passWord = getpass.getpass()

                i = i + 1

                if i ==  4 :

                    print('''You have entered wrong password 5 times
                                 For security reasons you have to wait for 25 seconds''')


        # Entering the Workspace...

        print("\n----Moving out of terminal.\n-----\n")
        time.sleep(2)

        #Logged in

        vid = cv2.VideoCapture('welcome.mp4')

        if (vid.isOpened()== False) :

            warNing = np.zeros((1080,1920,4),np.uint8)

            warNing = cv2.imread('warning.png',1)
            cv2.imshow('Avanzado',warNing)

            playsound('alert.mp3')

            cv2.waitKey(7000) & 0xFF
            cv2.destroyAllWindows()

            playsound('cleared.mp3')                

            turnOff = np.zeros((1080,1920,4),np.uint8)

            turnOff = cv2.imread('turnoff.png',1)
            cv2.imshow('Avanzado',turnOff)

            playsound('turnoff.mp3')

            cv2.waitKey(7000) & 0xFF
            cv2.destroyAllWindows()

            print("\n----\nsystem ran into problem :(\n----\n" )
            sys.exit(1)
        
        while(vid.isOpened()) :

            ret,frame = vid.read()

            cv2.imshow('Avanzado', frame)

            if cv2.waitKey(1) & 0xFF == 27 :

                break

        vid.release()
        cv2.destroyAllWindows()  

        # Introducing zoya

        vidi = cv2.VideoCapture('zoya.mp4')

        if (vidi.isOpened() == False) :

            time.sleep(2000)
            print("\n----\nZoya-assisstant needs to be checked and reviewd\n-----\nsystem ran into problem :(\n----\n" )
            sys.exit(1)

        playsound('hi.mp3')
        playsound('this.mp3')
        playsound('zoya.mp3')

        time.sleep(1)

        playsound('iwill.mp3')
        playsound('helping.mp3')

        time.sleep(1)

        playsound('check.mp3')    
        
        while(vidi.isOpened()) :

            ret,frame = vidi.read()

            cv2.imshow('Avanzado',frame)

            if cv2.waitKey(1) & 0xFF == 27 :

                break

        vidi.release()
        cv2.destroyAllWindows() 
        

        # Entering the workspace

        Desk = np.zeros((1080,1920,4),np.uint8)

        Desk = cv2.imread('desk.png',1)
        cv2.imshow('Avanzado',Desk)

        # Paint in avanzado

        if cv2.waitKey(0) & 0xFF == ord('P') :

            class Paint(object) :

                DEFAULT_PEN_SIZE = 5.0
                DEFAULT_COLOR = 'black'

                def __init__(self) :

                    self.root = TK()

                    self.pen_button = Button(self.root, text = 'pen', command = self.use_pen)
                    self.pen_button.grid(row = 0, column = 0)

                    self.brush_button = Button(self.root, text = 'brush', command = self.use_brush)
                    self.brush_button.grid(row = 0, column = 1)

                    self.color_button = Button(self.root, text = 'color', command = self.choose_color)
                    self.color_button.grid(row = 0, column = 2)

                    self.eraser_button = Button(self.root, text = 'eraser', command = self.use_eraser)
                    self.eraser_button.grid(row = 0, column = 3)

                    self.choose_size_button = Scale(self.root, from_ = 1, to = 10, orient = HORIZONTAL)
                    self.choose_size_button.grid(row = 0, column = 4)

                    self.c = Canvas(self.root, bg = 'white', width = 1920, height = 1080)
                    self.c.grid(row = 1, columnspan = 5)

                    self.setup()
                    self.root.mainloop()

                def setup(self) :

                    self.old_x = None
                    self.old_y = None
                    self.line_width = self.choose_size_button.get()
                    self.color = self.DEFAULT_COLOR
                    self.eraser_on = False
                    self.active_button = self.pen_button
                    self.c.bind('<B1-Motion>', self.reset)

                def use_pen(self) :
                    self.activate_button(self.pen_button)

                def use_brush(self) :
                    self.activate_button(self.brush_button)

                def choose_color(self) :
                    self.eraser_on = False
                    self.color = askcolor(color = self.color)[1]

                def use_eraser(self) :
                    self.activate_button(self.eraser_button, eraser_mode = True)

                def activate_button(self, some_button, eraser_mode = False) :
                    self.active_button.config(relief = RAISED)
                    some_button.config(relief = SUNKEN)
                    self.active_button = some_button
                    self.eraser_on = eraser_mode

                def paint(self, event) :
                    self.line_width = self.choose_size_button.get()
                    paint_color = 'white' if self.eraser_on else self.color
                    if self.old_x and self.old_y :

                        self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                        width = self.line_width, fill = paint_color,
                        capstyle = ROUND, smooth =TRUE, splinesteps = 36)
                    
                    self.old_x = event.x
                    self.old_y = event.y

                def reset(self, event) :
                    self.old_x, self.old_y = None, None


            if __name__ == '__main__' :
                Paint()               

        elif cv2.waitKey(0) & 0xFF == ord('L') :
            print("doing")


        elif cv2.waitKey(0) & 0xFF == ord('T') :

            turnOff = np.zeros((1080,1920,4),np.uint8)

            turnOff = cv2.imread('turnoff.png',1)
            cv2.imshow('Avanzado',turnOff)

            playsound('turnoff.mp3')

            cv2.waitKey(7000) & 0xFF
            cv2.destroyAllWindows()

            time.sleep(2)

            print("System deactivated unsuccessfully\n-------\n")

        elif cv2.waitKey(0) & 0xFF == ord('C') :

            cv2.destroyAllWindows()
        
            time.sleep(2)

            print("System deactivated unsuccessfully\n-------\n")

        elif cv2.waitKey(0) & 0xFF == ord('Z') :

            cv2.destroyAllWindows()

            time.sleep(2)

            print("System deactivated unsuccessfully\n-------\n")

            sys.exit(1)
              
     
    elif cv2. waitKey(0) & 0xFF == ord('L') :
        cv2.destroyAllWindows()

        # i will be doing this later...

        sys.exit(1) 

elif cv2.waitKey(0) & 0xFF == ord('T') :

    cv2.destroyAllWindows()

    turnOff = np.zeros((1080,1920,4),np.uint8)

    turnOff = cv2.imread('turnoff.png',1)
    cv2.imshow('Avanzado',turnOff)

    playsound('turnoff.mp3')

    cv2.waitKey(7000) & 0xFF
    cv2.destroyAllWindows()

    i = 0

    while i <= 1 :

        i = i + 1
        time.sleep(1)
        print(".")
        
    print("\n-----\n|Turned off Successfully!|")
    sys.exit(1)

'''

black = (0, 0, 0)
white = (255, 255, 255)

sunset = (253, 72, 47)

greenyellow = (184, 255, 0)
brightblue = (47, 288, 253)
orange = (255, 113, 0)
yellow = (255, 67, 255)

colorChoices = [greenyellow, brightblue, orange, yellow, purple]
'''



    






















    





  