# -*- coding: utf-8 -*-
"""
Este programa faz bastante uso da biblioteca tkinter e da
classe Canvas. Há um bom tutorial sobre este assunto no endereço
http://effbot.org/tkinterbook/canvas.htm

Existe uma referência aqui:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

"""

n = ''
from tkinter import *
from graphic_objects import *
import random

window = Tk() # Janela do app
window.title = "Aniquila bolas"
canvas = Canvas(window, width = 2000, height = 500) # área para desenha
canvas.pack()

# Dados para a primeira bola
x = 100
y = 100
radius = 30
bola_bonus = Ball(Point(x,y), 20 ,'purple',20,0,'')
tri_0   = Triangle(Point(70,400), Point(90, 400), Point(80, 380), 'blue')

objetos = [tri_0, bola_bonus] # Lista de bolas, por enquanto com uma só

tiros = []


last_key = ''



# Para que possamos detectar teclas pressionadas
def key_pressed(event):
    m1 = -12
    m2 = 12
    last_key = event.char
    if last_key == 'w':
        tri_0.move(0,m1)
    if last_key == 'a':
        tri_0.move(m1,0)
    if last_key == 'd':
        tri_0.move(m2,0)
    if last_key == 's':
        tri_0.move(0,m2)
    if last_key == ' ':
        tiro = Ball(Point(tri_0.p[2].x, tri_0.p[2].y),3, 'orange', 0, -10, "tiro" )
        tiro.draw(canvas)
        objetos.append(tiro)
        tiros.append(tiro)
        if n == 'bonus':
            tiros.remove(tiro)
            objetos.remove(tiro)
            tiro= Ball(Point(tri_0.p[2].x, tri_0.p[2].y),3, 'purple', 0, -10, "tiro" )
            tiro_2 = Ball(Point(tri_0.p[1].x, tri_0.p[1].y),3, 'purple', -5    , -10, "tiro" )
            tiro_3 = Ball(Point(tri_0.p[0].x, tri_0.p[0].y),3, 'purple', 5, -10, "tiro" )
            tiro.draw(canvas)
            tiro_2.draw(canvas)
            tiro_3.draw(canvas)
            objetos.append(tiro)  
            tiros.append(tiro)
            objetos.append(tiro_2)
            tiros.append(tiro_2)
            objetos.append(tiro_3)
            tiros.append(tiro_3)
            m1 = -20
            m2 = 20
            
          
            
            

# Para que a janela possa ter o foco do teclado
def get_focus(event):
    canvas.focus_set()    
    
canvas.bind("<Key>", key_pressed) 
canvas.bind("<1>", get_focus)

def wait_and_delete(component):
    component.after(20) # espera 20ms
    component.update()
    component.delete(ALL) # deleta tudo que estava na tela para começar o novo frame

acertos = 0
erros = 0
x = 0

while True:
    cores = ('blue','red','purple','black','pink','yellow','orange','grey','green')
    for tiro in tiros:
        for elemento in objetos:
            if not isinstance(elemento, Triangle) and elemento.tipo != "tiro":
                if ((tiro.center.x - elemento.center.x)**2 + (tiro.center.y - elemento.center.y)**2)**(1/2) <= radius:
                    if elemento.color == 'purple':
                        n = 'bonus'
                        tri_0.color = 'black'
                    objetos.remove(elemento)
    a = random.randint(0,2000)
    b = random.randint(30,200)
    c = random.randint(0,2000)
    d = random.randint(30,200)
    v1 = random.randint(-15,15)
    v2 = random.randint(-15,15)
    ball1 = Ball(Point(a,b),radius,'green',v1,0)
    ball2 = Ball(Point(c,d),radius,'red',v2,0)
    if len(objetos) < 100:
        objetos.append(ball1)
        objetos.append(ball2)
    canvas.create_text(50,50, text=last_key, fill="black")
    # Percorre e desenha a lista de bolas
    for elemento in objetos:
        elemento.draw(canvas)
        if elemento != tri_0:
            elemento.move(elemento.velocidade_x,elemento.velocidade_y)
            if elemento.center.x > 2000:
                elemento.center.x = 0
            if elemento.center.x < 0:
                elemento.center.x = 2000
    wait_and_delete(canvas) # Apaga a tela antes do próximo frame


window.mainloop()