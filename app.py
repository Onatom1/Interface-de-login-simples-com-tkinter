from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# --------------- Cores ---------------------- #
cor0 = "#f0f3f5"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#FF2100"  # Verde
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"   # Letra

# --------------- Janela ---------------------- #
root = Tk()
root.title('')
root.geometry('310x300')
root.configure(background=cor1)
root.resizable(width=FALSE, height=FALSE)

credenciais = ('admin', 'admin')

# --------------- Função ---------------------- #
def nova_janela():
    l_nome = Label(frame_cima, text="Usuario: " + credenciais[0], height=1,anchor=NE, font=('Ivy 20 '), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=cor2)
    l_linha.place(x=10, y=45)
    
    l_nome = Label(frame_baixo, text="Seja bem-vindo " + credenciais[0], height=1,anchor=NE, font=('Ivy 15 '), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)


def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())
    
    if nome=='admin' and senha=='admin':
        messagebox.showinfo('Login',' Seja Bem-vindo Admin !!!')
    
    # Verificando os dados para permitir o login do usuario
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login',' Seja bem vindo de volta '+credenciais[0])
        
        # Apaga o que tiver no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        
        for widget in frame_cima.winfo_children():
            widget.destroy()
            
        # Chama a função nova janela
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuario ou a palavra passe')


# --------------- Frames ---------------------- #


frame_cima = Frame(root,width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)


frame_baixo = Frame(root, width=310, height=300, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# --------------- Label ---------------------- #
#FrameCima:
l_nome = Label(frame_cima, text='Login', height=1, anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
l_nome.place(x=110, y=-2)

# LOGO
app_img = Image.open('image/log.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cor1, fg=cor4)
app_logo.place(x=10, y=-5)


l_linha = Label(frame_cima, width=275, text='', height=1, anchor=NE, font=('Ivy 1'), bg=cor2)
l_linha.place(x=10, y=40)
#FrameBaixo:

l_nome = Label(frame_baixo, text='Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightbackground=cor1, relief='solid')
e_nome.place(x=14, y=50)
 
l_pass = Label(frame_baixo, text='Password *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=('',15), highlightbackground=cor1, relief='solid')
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, bg=cor2, fg=cor1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)

# Rodapé --------------------------------------------------------------
rodape_label = Label(root, text='By Yury Mota', font=('Verdana 8'), bg=cor1, fg=cor4)
rodape_label.place(relx=0, rely=1.0, anchor=SW, y=-5)








root.mainloop()