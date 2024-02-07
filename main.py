from tkinter import *

codes=["HTML", "CSS", "JS"]

def code():
    if(x.get()==0):
        print("You chose HTML! You can build a simple website.")
    elif (x.get() == 1):
        print("You chose CSS! You can add nice visual features to your website so it can stand out.")
    elif(x.get()==2):
        print("You chose JS! You can add functionnality to your webste !")

window = Tk()

htmlImage = PhotoImage(file='img.png')
cssImage = PhotoImage(file='img_1.png')
JsImage =PhotoImage(file='img_2.png')
codeImages = [htmlImage, cssImage, JsImage]

x= IntVar()

for index in range(len(codes)):
    radiobutton = Radiobutton(window, text=codes[index],#adds text to radio buttons
                              variable=x,#groups radiobuttons together if they share the same value
                              value=index,
                              bg="#0000FF", activebackground="#0000FF",
                              padx=25, font= ("Impact", 15),
                              image = codeImages[index],
                              compound='left', command= code)#assigns each radio button to a different value
    radiobutton.pack()
window.mainloop()