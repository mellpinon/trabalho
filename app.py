from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.Table import Table
from tkinter import *

dao = UsuarioDao(Database(Config().config).conn)
lista = dao.selecionarUsuarios()
tela = Table(lista)

class Root:
    def __init__(self, herdar, dao:UsuarioDao) -> None:
        self.herdar = herdar
        self.dao = dao
        frame = Frame(self.herdar)
        frame.pack()
        label1 = Label(frame, text='Bem vindo ao Banco de Dados!')
        label1.pack()
        nome = Label(frame, text='O que deseja fazer?')
        nome.pack()
        inserir = Button(frame, text="Inserir usuário", command = self.inserirUsuario)
        inserir.pack()
        alterar = Button(frame, text="Alterar usuário", command = self.alterarUsuario)
        alterar.pack()
        excluir = Button(frame, text="Excluir usuário", command = self.excluirUsuario)
        excluir.pack()

    def inserirUsuario(self):
        self.iniciar = Toplevel(self.herdar)
        self.obj = Janela1(self.iniciar, self.dao)
    
    def alterarUsuario(self):
        self.iniciar = Toplevel(self.herdar)
        self.obj = Janela2(self.iniciar, self.dao)
        
    def excluirUsuario(self):
        self.iniciar = Toplevel(self.herdar)
        self.obj = Janela3(self.iniciar, self.dao)

class Janela1:
    def __init__(self, herdar, dao: UsuarioDao) -> Usuario:
        self.herdar = herdar
        self.dao = dao

        frame = Frame(self.herdar)
        frame.pack()
        self.n = StringVar()
        self.e = StringVar()
        self.s = StringVar()
        label1 = Label(frame, text='Insira um novo usuário: ')
        label1.pack()
        nome = Label(frame, text='Digite o nome')
        nome.pack()
        entry1 = Entry(frame, textvariable= self.n)
        entry1.pack()
        email = Label(frame, text='Digite o email')
        email.pack()
        entry2 = Entry(frame, textvariable= self.e)
        entry2.pack()
        senha = Label(frame, text='Digite a senha')
        senha.pack()
        entry3 = Entry(frame, textvariable= self.s)
        entry3.pack()
        confirmar = Button(frame, text="Confirmar", command = self.confirmarInsercao)
        confirmar.pack()

    def confirmarInsercao(self):
        usuario = Usuario()
        usuario.nome = self.n.get()
        usuario.email = self.e.get()
        usuario.senha = self.s.get()
        self.dao.inserirUsuario(usuario)

class Janela2:
    def __init__(self, herdar, dao: UsuarioDao) -> Usuario:
        self.herdar = herdar
        self.dao = dao

        frame = Frame(self.herdar)
        frame.pack()
        self.i = IntVar()
        self.n = StringVar()
        self.e = StringVar()
        self.s = StringVar()
        label1 = Label(frame, text='Altere um usuário existente: ')
        label1.pack()
        id = Label(frame, text= 'Digite o ID')
        id.pack()
        entry0 = Entry(frame, textvariable= self.i)
        entry0.pack()
        nome = Label(frame, text='Digite o nome')
        nome.pack()
        entry1 = Entry(frame, textvariable= self.n)
        entry1.pack()
        email = Label(frame, text='Digite o email')
        email.pack()
        entry2 = Entry(frame, textvariable= self.e)
        entry2.pack()
        senha = Label(frame, text='Digite a senha')
        senha.pack()
        entry3 = Entry(frame, textvariable= self.s)
        entry3.pack()
        confirmar = Button(frame, text="Confirmar", command = self.confirmarAlteracao)
        confirmar.pack()

    def confirmarAlteracao(self):
        usuario = Usuario
        usuario.id = self.i.get()
        usuario.nome = self.n.get()
        usuario.email = self.e.get()
        usuario.senha = self.s.get()
        self.dao.alterarUsuario(usuario)

class Janela3:
    def __init__(self, herdar, dao: UsuarioDao) -> Usuario:
        self.herdar = herdar
        self.dao = dao

        frame = Frame(self.herdar)
        frame.pack()
        self.i = IntVar()
        label1 = Label(frame, text='Excluir um usuário: ')
        label1.pack()
        id = Label(frame, text='Digite o ID do usuário que deseja excluir: ')
        id.pack()
        entry1 = Entry(frame, textvariable= self.i)
        entry1.pack()
        confirmar = Button(frame, text="Confirmar", command = self.confirmarExclusao)
        confirmar.pack()

    def confirmarExclusao(self):
        usuario = Usuario()
        usuario.id = self.i.get()
        self.dao.excluirUsuario(usuario)

janela = Tk()
obj = Root(janela, dao)
janela.mainloop()

        
