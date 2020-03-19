from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
import pyglet
import cv2

t=Tk()
w=Label(t,text="sign lang detector")
button=Button(t, text="CONTINUE",fg="red")
button.pack(side=BOTTOM)
w.pack()
name=simpledialog.askstring("input string","What is your name?")
tkinter.messagebox.showinfo("Welcome","this program enables you to have an \neffective connection with the \npeople having abnormility in hearing")
tkinter.messagebox.showinfo("Results", "Welcome ,%s to the sign language detector." %(name))

animation=pyglet.image.load_animation('simple.gif')
animSprite=pyglet.sprite.Sprite(animation)


w=animSprite.width
h=animSprite.height

window=pyglet.window.Window(width=w, height=h)

r,g,b,alpha = 0.5, 0.5, 0.8, 0.5

pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()
pyglet.app.run()
img1=PhotoImage(file="1_pcmV9IpuhyhvpScQ1Q8W5A.png")
label1=Label(t,image=img1)
label1.pack()




t.mainloop()
