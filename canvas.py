from tkinter import *
def deleteall():
    canvas.delete(ALL)
root=Tk()
canvas = Canvas(root,width=350,height=250)
canvas.pack()
blackline=canvas.create_line(0,0,110,220)
greenline=canvas.create_line(0,400,100,200,fill="green")
rec=canvas.create_rectangle(100,2020,140,300,fill="white")
button=Button(root,text="Del",command=deleteall)
button.pack()
root.mainloop()
