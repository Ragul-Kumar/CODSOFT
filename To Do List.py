#from tkinter import *
#root =Tk()
from tkinter import *

root=Tk()

class make():
    def __init__(self):
        self.task=[]

    def Addtask(self):
        task=input(str("Enter your task :"))
        self.task.append(task)
        print("The task was added .")

show=Button(root,text="SHOW",command=make)
show.pack()    


task=make()
task.Addtask()

root.mainloop()