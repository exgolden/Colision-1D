from tkinter import *

#Parametros
WIDTH=700
HEIGHT=100
SPEED=200
SIZE=50
PARTES=1
COLOR_1="#FF0000"
COLOR_2="#0000FF"
COLOR_B="#000000"
#Funciones y Clases
class Objeto:
    def __init__(self, x, color):
        self.color=color
        self.coordinates=[x]
        self.squares=[]
        for x in self.coordinates:
            square=canvas.create_rectangle(x,HEIGHT,(x+SIZE),(HEIGHT-SIZE), fill=color, tag="object")
            self.squares.append(square)
            
def collision(objeto_1, objeto_2):
    x_1=objeto_1.coordinates[0]
    x_2=objeto_2.coordinates[0]
    if(x_1==x_2):
        return True 
    return False

def Game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="Colision", fill="red", tag="Colision")

def Turn(objeto_1, direction, objeto_2):
    x=objeto_1.coordinates[0]
    if (direction=="right"):     
        x+=SIZE
        objeto_1.coordinates.insert(0, x)
        square=canvas.create_rectangle(x,HEIGHT,(x+SIZE),(HEIGHT-SIZE), fill=objeto_1.color, tag="object")
        objeto_1.squares.insert(0,square) 
        del objeto_1.coordinates[-1]
        canvas.delete(objeto_1.squares[-1])
        del objeto_1.squares[-1]
    elif(direction=="left"):
        x-=SIZE
        objeto_1.coordinates.insert(0, x)
        square=canvas.create_rectangle(x,HEIGHT,(x+SIZE),(HEIGHT-SIZE), fill=objeto_1.color, tag="object")
        objeto_1.squares.insert(0,square) 
        del objeto_1.coordinates[-1]
        canvas.delete(objeto_1.squares[-1])
        del objeto_1.squares[-1]
    if collision(objeto_1, objeto_2):
        Game_over()
    else: 
        window.after(SPEED, Turn, objeto_1, direction, objeto_2)        

#GUI
window=Tk()
window.title("Colision en una dimension")
window.resizable(False, False)
canvas=Canvas(window, bg=COLOR_B, height=HEIGHT, width=WIDTH)
canvas.pack()
Objeto_1=Objeto(0, COLOR_1)
Objeto_2=Objeto(WIDTH-SIZE, COLOR_2)
Turn(Objeto_1, "right", Objeto_2)
Turn(Objeto_2, "left", Objeto_1)
window.mainloop()
