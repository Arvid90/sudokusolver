import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.text = ["foo", "bar"]
        self.labels = tk.Label(self, textvariable=self.text[0])
        self.labels.grid(row=0, column=0)
        self.labels2 = tk.Label(self, textvariable=self.text[1])
        self.labels.grid(row=1, column=1)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=2, column=2)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=2)

    def say_hi(self):
        print("hi there, everyone!")
        self.hi_there["text"] = "Arvif"


root = tk.Tk()
app = Application(master=root)
app.mainloop()
