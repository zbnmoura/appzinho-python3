#!/usr/bin/env python3
#autor: Bruno Neves de Moura
#date writen: 07/10/2016
#date compiled: 07/10/2016


#modelo para salvar o arquivo txt
def salvar_dados():
    a = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    fileD = open(a, "a")#nome do .txt
#data do dia 
    fileD.write("Data: %s/%s/%s\n" % (now.day, now.month, now.year))
#horario
    fileD.write("Horário: ")
    fileD.write("%s\n" % horario.get())
#rota
    fileD.write("Rota: 407\n")
#nome do aluno
    fileD.write("Nome: ")
    fileD.write("%s\n" % nome.get())
#nome da instituiçao
    fileD.write("Instituição: APAE Mauá\n")
#ocorrencia: falta o cancelamento
    fileD.write("Ocorrencia: ")
    fileD.write("%s\n" % ocorrencia.get())
#motivo: particular ou por questoes medicas
    fileD.write("Motivo: ")
    fileD.write("%s\n" % motivo.get())
#nome do operador
    fileD.write("Operador A-B: Jose Ilton Santos\n")
    fileD.write("Operador B-A: Jose Ilton Santos\n\n")
#definiçoes padrao
    nome.set(None)
    motivo.set('Particular')
    ocorrencia.set('Faltou')
#apagar o campo quando concluido
    horario.delete(0, END)
#fechando arquivo de gravação  
    fileD.close()

#ler txt com nomes do aluno 
def ler_nomes(arquivo):
    nome = []
    f = open(arquivo)
    for linha in f:
        nome.append(linha.rstrip())
    f.close()
    nome.sort()
    return nome
#---------------------#
#bibliotecas
from tkinter import *
from datetime import datetime
#variaveis de tempo
global now
now = datetime.now()
app = Tk()
app.title('Email EMTU')
app.geometry('250x322+200+100')
#data do ocorrido
Label(app, text = "Data: %s/%s/%s" % (now.day, now.month, now.year)).pack()
#data = Entry(app)
#data.pack()
#nome dos alunos
Label(app, text = "Nome:").pack()
nome = StringVar()
nome.set(None) 
opçoes = ler_nomes("nomes.txt")
OptionMenu(app, nome, *opçoes).pack()
#horario do corrido
Label(app, text = "Horario: (hh:mm)").pack()
horario = Entry(app)
horario.pack()
#ocorrencia
Label(app, text = "Ocorrencia:").pack()
ocorrencia = StringVar()
ocorrencia.set('Faltou')
Radiobutton(app, variable = ocorrencia, text = 'Faltou', 
            value = 'Faltou').pack()
Radiobutton(app, variable = ocorrencia, text = 'Cancelou', 
            value = 'Cancelou').pack()
#pula linha
Label(app, text = " ").pack()
#motivo 
Label(app, text = "Motivo:").pack()
motivo = StringVar()
motivo.set('Particular')
Radiobutton(app, variable = motivo, text = 'Particular', 
            value = 'Particular').pack()
Radiobutton(app, variable = motivo, text = 'Consulta Médica', 
            value = 'Consulta Médica').pack()
Radiobutton(app, variable = motivo, text = 'Problema de Saude', 
            value = 'Problema de Saude').pack()
#pula linha
Label(app, text = " ").pack()
#salvando e enviando
Button(app, text = "Salvar", command = salvar_dados).pack()
app.mainloop()
