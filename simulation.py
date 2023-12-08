from tkinter import*
simulation = Tk()
simulation.title("Simulation Verrou à code")
simulation.configure(width=1500,height=1200)

Verrou = Canvas(simulation, width=500, height=700, bg="white")
Verrou.place(x=50,y=70)

entree = []
code = [1, 2, 3, 4]

texte = Label(simulation, text=entree, font=('arial', 34, 'bold'), bg="white")

#----- fonctionnement -----#

def affichage(n):

    entree.append(n)
    t = entree
    texte.configure(text=t, fg="black")
    texte.place(x=120,y=140)
    print(entree)

    if n == '':
        entree.clear()
        t = entree
        texte.configure(text=t, fg='black')
        print(entree)

def verification():
    global h
    print(h)
    if entree == code and h == 10.15:
        entree.clear()
        texte.configure(text="PORTE OUVERTE", fg="green")
        texte.place(x=100,y=140)
    else :
        entree.clear()
        texte.configure(text="ACCES REFUSE", fg="red")

def Badge():
    texte.configure(text="PORTE OUVERTE", fg="green")
    texte.place(x=100,y=140)



#----- structure -----#

#armature
Verrou.create_rectangle(5,5,500,700,fill='grey',outline='black',width=4)
Verrou.create_rectangle(15,15,490,690, fill='grey',outline='black', width=2)

#écran
Verrou.create_rectangle(40,40,465,250, fill='white',outline='black',width=1)

#boutons
b1 = Button(simulation, text="1", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=1:affichage(x))
b1.place(x=110,y=350)
b2 = Button(simulation, text="2", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=2:affichage(x))
b2.place(x=250,y=350)
b3 = Button(simulation, text="3", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=3:affichage(x))
b3.place(x=390,y=350)

b4 = Button(simulation, text="4", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=4:affichage(x))
b4.place(x=110,y=450)
b5 = Button(simulation, text="5", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=5:affichage(x))
b5.place(x=250,y=450)
b6 = Button(simulation, text="6", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=6:affichage(x))
b6.place(x=390,y=450)

b7 = Button(simulation, text="7", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=7:affichage(x))
b7.place(x=110,y=550)
b8 = Button(simulation, text="8", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=8:affichage(x))
b8.place(x=250,y=550)
b9 = Button(simulation, text="9", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=9:affichage(x))
b9.place(x=390,y=550)

clear = Button(simulation, text="C", font=('arial', 11, 'bold'), width=10, height=3, bg='red', command=lambda x='':affichage(x))
clear.place(x=110,y=650)
b0 = Button(simulation, text="0", font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=0:affichage(x))
b0.place(x=250,y=650)


#----- Gestion de l'heure -----#

horloge = Canvas(simulation, width=500, height=200, bg="black")
horloge.place(x=800,y=70)

h = 0
def heure(x):
    global h
    h = x
    print(h)
    return h

heure1 = Button(simulation, text='10h15', font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=10.15:heure(x))
heure1.place(x=850,y=120)


heure2 = Button(simulation, text='10h35', font=('arial', 11, 'bold'), width=10, height=3, command=lambda x=10.35:heure(x))
heure2.place(x=1150,y=120)


validation = Button(simulation, text="◄", font=('arial', 11, 'bold'), width=10, height=3, bg='green', command= verification)
validation.place(x=390,y=650)

#----- badge -----#

badge = Button(simulation, text='BADGE', font=('arial', 16, 'bold'), width=20, height=10, bg='black', fg='white', command = Badge)
badge.place(x=850,y=350)


simulation.mainloop()