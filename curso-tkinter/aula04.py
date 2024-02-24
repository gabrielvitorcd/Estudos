from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#dfe3ee')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6',highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5 , relwidth=0.96 ,relheight=0.45)

    def widgets_frame1(self):
        ###Criação do botao Limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1,relheight=0.15)

        ###Criação do botao Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        ###Criação do botao Novo
        self.bt_novo = Button(self.frame_1, text='Novo')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        ###Criação do botao Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar')
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        ###Criação do botao Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar')
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ##Criação da label e entrada do Codigo
        self.lb_codigo = Label(self.frame_1 , text='Codigo')
        self.lb_codigo.place(relx= 0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1, background='white')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ##Criação da label e entrada do Nome
        self.lb_nome = Label(self.frame_1 , text='Nome')
        self.lb_nome.place(relx= 0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1, background='white')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.4)

                ##Criação da label e entrada do Telefone
        self.lb_telefone = Label(self.frame_1 , text='Telefone')
        self.lb_telefone.place(relx= 0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1, background='white')
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

                ##Criação da label e entrada do Cidade
        self.lb_cidade = Label(self.frame_1 , text='Cidade')
        self.lb_cidade.place(relx= 0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1, background='white')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)



Application()