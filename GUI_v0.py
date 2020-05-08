
from tkinter import *
window = Tk()
 
window.title("Cennik zadaszeń")
window.geometry('320x320')

lblszer = Label(window, text="Szerokość:",font = 24)
lblszer.grid(column=0, row=0)
szer = Entry(window,width=10)
szer.grid(column=1, row=0)



lblglb = Label(window, text="Głębokość:",font = 24)
lblglb.grid(column=0, row=2)
glb = Entry(window,width=10)
glb.grid(column=1, row=2)

lblobc = Label(window, text="Strefa śniegowa:",font = 24)
lblobc.grid(column=0, row=4)
obc = Entry(window,width=10)
obc.grid(column=1, row=4)

lblcena = Label(window, text="Cena",font = 24)
lblcena.grid(column=0, row=6)

def liczenie():
    szer1 = float(szer)
    glb1 = float(glb)
    a = szer1 * glb1
    lblcena.configure(text = a)
btn = Button(window, text="Oblicz!", command=liczenie)
btn.grid(column=3, row=0)

window.mainloop()