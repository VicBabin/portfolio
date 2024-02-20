import tkinter
import os
from datetime import *
from tkinter import Tk, Button
from PicturesLoader import *
from AccessGithub import *


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class MyWindow(Tk):

    def __init__(self):
        # On appelle le constructeur parent
        super().__init__()

        #Dimension de mon grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Différent styles
        PicturesLoader_button_style = {
            "bg": "green", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 15, "bold")
        }
        AccessGithub_button_style = {
            "bg": "red", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 15, "bold")
        }
        py_label_style = {
            "font": ("Arial", 15)
        }
        print_displayer_style = {
            "bg": "white"
        }


        #Premier label qui affiche la date d'aujourd'hui
        date_label = tkinter.Label(self, text=f"Date : {date.today()}")
        date_label.grid(column=0, row=0, sticky="nw")

        #Fonction qui va permettre d'ouvrir le dossier des photos
        dossier_photos = "C:/Portfolio/VicBabinPortfolio.github.io/docs/assets/images/photos/"
        def ouverture_dossier():
            os.startfile(dossier_photos)

        #Mise en place du bouton qui va ouvrir le dossier des photos
        dossier_photo_button = tkinter.Button(self, text="📁", font=("Segoe UI Emoji", 10), command=ouverture_dossier)
        dossier_photo_button.grid(column=1,row=0, sticky="n")

        #Présentation rapide des noms des scripts
        presentation_label = tkinter.Label(self, text=f"PicturesLoader.py & AccessGithub.py")
        presentation_label.grid(column=2, row=0,sticky="n")


        #Description de l'utilisation du script DisplayPortfolio
        description_label = tkinter.Label(self, text="Ce .exe permet d'importer automatiquement les photos du dossier dans Github\n"
                                                     "tout en les renommant, et les intégre ensuite au fichier html du portfolio. Pour le bon\n"
                                                     "fonctionnement de l'import il est préférable d'utiliser PicturesLoader avant AccessGithub.\n"
                                                     "AccessGithub peut faire freeze l'affichage, ne pas cliquer partout et patienter si cela arrive")
        description_label.grid(column=0, row=1, columnspan=3, sticky="nwe")

        #Séparation esthétique en dessous du label de description
        first_separator = tkinter.Frame(self, height=2, bd=1, relief=tkinter.SUNKEN)
        first_separator.grid(row=1, column=0, sticky="ew", columnspan=3)

        #Ligne avec label,affichage des prints et bouton pour Pictures Loader
        pictures_loader_label = tkinter.Label(self, text=f"PicturesLoader", **py_label_style)
        pictures_loader_label.grid(column=0, row=2)
        pictures_loader_button = tkinter.Button(self, text="Exécuter",command=fonction_PicturesLoader,**PicturesLoader_button_style)
        pictures_loader_button.grid(column=2, row=2, sticky="e")

        # Ligne avec label,affichage des prints et bouton pour Access Github
        access_github_label = tkinter.Label(self, text=f"AccessGithub", **py_label_style)
        access_github_label.grid(column=0, row=3)
        access_github_button = tkinter.Button(self, text="Exécuter",command=fonction_AccessGithub,**AccessGithub_button_style)
        access_github_button.grid(column=2, row=3,sticky="e")


        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("500x500")
        self.resizable(False,False)
        self.configure(bg="#333333", padx=10, pady=10)

        # On ajoute un titre à la fenêtre
        self.title("DisplayerPortfolio")


# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()