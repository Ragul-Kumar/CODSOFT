import tkinter as tk

class Make:
    def __init__(self):
        self.tasks =[]
      
    def Addtask(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.status_label.config(text="The task was added.")
        else:
            self.status_label.config(text="Please enter a task.")

    def Removetask(self):
        task_to_remove = self.task_entry.get()
        if task_to_remove in self.tasks:
            self.tasks.remove(task_to_remove)
            self.status_label.config(text="The task was removed.")
        else:
            self.status_label.config(text="Task not found.")
        self.task_entry.delete(0, tk.END)

    def showtask(self):
        self.status_label.config(text="Tasks in your library:\n" + "\n\n".join(self.tasks))

def create_gui():
    root = tk.Tk()
    root.configure(bg="#1F2833")
    root.title("Task Manager")
    root.minsize(height=25,width=45,)
    root.geometry("350x450")

    make = Make()

    task_label = tk.Label(root, text="Task Manager ",font="BOLD",padx=15,pady=5,bg="#1F2833",highlightbackground="blue",fg="#C5C6C7")
    task_label.pack(padx=4,pady=12)
  
    task_entry = tk.Entry(root,width=50,)
    task_entry.pack(padx=16,pady=30)


    add_button = tk.Button(root, text="Add", command=make.Addtask , width=20,height=1,bg="teal",fg="lightgray",font=("BradleyHand"))
    add_button.pack(padx=2,pady=10)

    delete_button = tk.Button(root, text="Delete",command=make.Removetask,width=20,height=1,bg="teal",fg="lightgray",font=("BradleyHand"))
    delete_button.pack(padx=2,pady=10)

    show_button = tk.Button(root, text="Show", command=make.showtask, width=20,height=1,bg="teal",fg="lightgray",font="BradleyHand")
    show_button.pack(padx=2,pady=10)

    status_label = tk.Label(root,text="Tasks In Your Library",bg="#1F2833",fg="#C5C6C7",font="bold")
    status_label.pack(padx=12,pady=10,)

    make.task_entry = task_entry
    make.status_label = status_label

    root.mainloop()
   

create_gui()
