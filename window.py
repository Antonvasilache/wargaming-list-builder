from tkinter import Tk, messagebox, Label, Button

class Window:
    def __init__(self, width=1920, height=1080):
        self.root = Tk()
        self.root.title = ("Star Wars Legion List Builder")
        self.root.geometry(f"{width}x{height}")
        self.widgets = []        
        
    def add_label(self, text, font=("Helvetica", 14), pady=20):
        label = Label(self.root, text=text, font=font)
        label.pack(pady=pady)
        self.widgets.append(label)
        
    def add_button(self, text, command, font=("Helvetica", 12), pady=10, padx=50):
        button = Button(self.root, text=text, font=font, command=command)
        button.pack(pady=pady, padx=padx, fill = 'x')
        self.widgets.append(button)
        
    def show_message(self, title, message):
        messagebox.showinfo(title, message)
        
    def clear_widgets(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets.clear()
        
    def start(self):
        self.root.mainloop()