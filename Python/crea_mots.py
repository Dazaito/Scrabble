from os import chdir
from itertools import product
from tkinter import *
import tkinter as tk
import pathlib

'''Creation de la fenetre'''

scrabble = tk.Tk()
scrabble.title("Aide au Scrabble")
scrabble.geometry("1920x1080")
scrabble.config(cursor="right_ptr", bg='#eadcab')

Texte1 = Label(scrabble, text='Bonjour, quelles lettres avez vous ?',
               bg='#eadcab',
               height=10, font=("Courier", 30))

Texte1.pack()

Texte2 = Label(scrabble, text='Ecrivez vos lettres en minuscule et sans espaces. '
                              'Cliquez ensuite sur le bouton "Valider" avant de cliquer sur le bouton "Lancer"',
               bg='#eadcab',
               font=("Bahnschrift SemiBold", 20))
Texte2.pack()

recup = tk.Entry(scrabble, width=50,)
recup.pack(pady=40)

def recuperation():
    lettres_donnees = recup.get()
    '''Fonction récuperation.
    recupere les lettres tapées par l'utilisateur on utilise la variable
     "lettres_donnees" pour les reutiliser
     '''
    return lettres_donnees

def import_mots_acceptes():  # import liste mots acceptés au scrabble
    global os
    chdir(pathlib.Path(__file__).parent.absolute())
    fichier = open("mots.txt", "r")
    infos = fichier.readlines()
    fichier.close()
    liste_tous_mots = []
    for element in infos:  # decoupe les mots
        un_mot = element.rstrip('\n')
        lettre_mot = []
        for i in range(0, len(un_mot)):  # découpe pour toutes les lettres
            lettre_mot.append(un_mot[i])
        liste_tous_mots.append(lettre_mot)

    return liste_tous_mots

def crea_mots():
    liste_tous_mots = import_mots_acceptes()
    lettres_recup = recuperation()
    possibilites = [loop for loop in product(lettres_recup, repeat=len(lettres_recup))]
    # tranforme le tuple en liste
    liste_poss = [list(row) for row in possibilites]
    nouv_mots = []
    for b1 in range(len(liste_tous_mots)):
        for b2 in range(len(liste_poss)):
            if liste_tous_mots[b1] == liste_poss[b2] and liste_tous_mots[b1] not in nouv_mots:
                nouv_mots.append(liste_tous_mots[b1])
    liste_crea = nouv_mots

    val_lettre = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1,
                  "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1,
                  "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}
    points_par_mots = []
    for b3 in range(len(liste_crea)):
        mot_actuel = 0
        for b4 in range(len(liste_crea[b3])):
            mot_actuel += val_lettre[liste_crea[b3][b4]]
        points_par_mots.append(mot_actuel)
    maxvalue = 0
    for b5 in range(len(points_par_mots)):
        print(maxvalue)
        print(points_par_mots[b5])
        if maxvalue < points_par_mots[b5]:
            maxvalue = points_par_mots[b5]
    maxpos = points_par_mots.index(maxvalue)  # position du mot marque + points
    meilleur_mot = liste_crea[maxpos]

    soluce = tk.Tk()
    soluce.title("Solution")
    soluce.geometry("1920x1080")
    soluce.config(bg='#eadcab')
    str_meilleur_mot = ''.join(meilleur_mot)
    Texte3 = Label(soluce, text='Le meilleur mot est '+ str_meilleur_mot+ ', il vous fait marquer '+ str(maxvalue)+
                                ' points !',
                   bg='#eadcab',
                   fg="black",
                   height=30,
                   font=("Courier", 30))
    Texte3.pack()
    soluce.mainloop()

'''Creation et placement du bouton valider qui s'activ quand on appuie 
et du widget entry, assigne à la fonction crea_mots'''

btn = tk.Button(scrabble, height=1, width=30,
                text="Valider", font=("Lucida Console", 15),
                bg='#ffd133',
                command=recuperation,
                activeforeground="#8A3324",
                activebackground="#eadcab", padx=15, pady=15)

btn2 = tk.Button(scrabble, height=2, width=40,
                 text="Lancer", font=("Lucida Console", 15),
                 bg='#ffd133',
                 command=crea_mots,
                 activeforeground="#8A3324",
                 activebackground="#eadcab", padx=30, pady=30)

btn.pack()
btn2.pack()

scrabble.mainloop()
