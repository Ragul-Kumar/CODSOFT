import tkinter as tk

class To_do_list:
    def __init__(self):
        self.tasks =[]
      
    def Addtask(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.status_label.config(text="The task was added.")
            self.update_task_listbox()  
        else:
            self.status_label.config(text="Please enter a task.")

    def Removetask(self, event=None):
        task_to_remove = self.task_entry.get()
        if task_to_remove in self.tasks:
            self.tasks.remove(task_to_remove)
            self.status_label.config(text="The task was removed.")
            self.update_task_listbox() 
        else:
            self.status_label.config(text="Task not found.")
        self.task_entry.delete(0, tk.END)

    def delete_selected_task(self, event=None):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.status_label.config(text="Task was removed.")
            self.update_task_listbox()
        else:
            self.status_label.config(text="Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, f"{i+1}. {task}")

def create_gui():
    root = tk.Tk()
    root.configure(bg="#1F2833")
    root.title("Task Manager")
    root.minsize(height=25,width=45,)
    root.geometry("350x456")

    make = To_do_list()

    task_label = tk.Label(root, text="Task Manager ",font="BOLD",padx=15,pady=5,bg="#1F2833",highlightbackground="blue",fg="#C5C6C7")
    task_label.pack(padx=4,pady=12)
  
    task_entry = tk.Entry(root,width=50,font=("Helvetica",15))
    task_entry.pack(padx=16,pady=30)

    add_button = tk.Button(root, text="Add", command=make.Addtask , width=20,height=1,bg="teal",fg="lightgray",font=("BradleyHand"))
    add_button.pack(padx=2,pady=10)

    delete_button = tk.Button(root, text="Delete",command=make.Removetask,width=20,height=1,bg="teal",fg="lightgray",font=("BradleyHand"))
    delete_button.pack(padx=2,pady=10)

    status_label = tk.Label(root,text="Tasks In Your Library",bg="#1F2833",fg="#C5C6C7",font="bold")
    status_label.pack(padx=1,pady=10,)

    task_listbox = tk.Listbox(root, width=30, height=15,font=("Helvetica",12,"bold"))
    task_listbox.pack(padx=6,pady=20)

    
    add_button.bind("<Button-1>", make.Addtask)
    delete_button.bind("<Button-1>", make.delete_selected_task)

    make.task_entry = task_entry
    make.status_label = status_label
    make.task_listbox = task_listbox

    root.mainloop()

create_gui()
