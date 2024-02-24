from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela (self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#03cffc")
        self.root.resizable(True, True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=400, height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=2, bg='#121414',
                             highlightbackground='#656c6e',highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)
        self.frame_2 = Frame(self.root, bd=2, bg='#68929e',
                             highlightbackground='#656c6e', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
Application()