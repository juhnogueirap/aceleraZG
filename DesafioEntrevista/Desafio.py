from tkinter import *
import pygame
import geral
import partes


def parte_1_bottom ():
    pygame.mixer.music.stop()
    texto_parte2.pack_forget()
    texto_parte1.pack(side = LEFT)
    texto_parte1["text"] = f"{partes.parte1()}"
    

def parte_2_bottom ():
    pygame.mixer.music.stop()
    texto_parte1.pack_forget()
    texto_parte2.pack(side = LEFT) 
    texto_parte2["text"] = f"{partes.parte2()}"
    
def play_sound ():
    pygame.mixer.music.load("erguei.mp3")
    pygame.mixer.music.play ()


def musica_completa():
    texto_parte1.pack_forget()
    texto_parte2.pack_forget()
    texto_parte1.pack(side = LEFT)
    texto_parte1["text"] = f"{partes.parte1()}"
    texto_parte2.pack(side = LEFT)
    texto_parte2["text"] = f"{partes.parte2()}"
    play_sound ()



janela = Tk()
janela.title("Desafio da musica")
pygame.init()

texto_orientacao = Label(janela, text = "O que você deseja ouvir? ")
texto_orientacao.pack()

botao_parte1 = Button(janela, text = "Parte I", command=parte_1_bottom)
botao_parte1.pack()

botao_parte2 = Button(janela, text = "Parte II", command=parte_2_bottom)
botao_parte2.pack()

botao_musica = Button(janela, text = "Música completa", command=musica_completa)
botao_musica.pack()

texto_parte1 = Label(janela, text = "")
texto_parte1.pack()

texto_parte2 = Label(janela, text = "")
texto_parte2.pack()


janela.mainloop()