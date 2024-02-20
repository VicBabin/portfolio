from github import *
import tkinter
import sys
import threading
from datetime import *
import os

def fonction_AccessGithub():

# #----- Partie sur l'affichage des prints dans DisplayerPortfolio.py -----#
    def AG_fermer_fenetre():
        fenetre_AG.destroy()

    # Création de la nouvelle fenêtre
    fenetre_AG = tkinter.Tk()
    fenetre_AG.title("AccessGithub")

    # Widget Text pour afficher les sorties
    text_box = tkinter.Text(fenetre_AG, wrap=tkinter.WORD, width=40, height=10)
    text_box.pack(fill="both", expand=True)

    # Rediriger la sortie standard vers le widget Text
    def AccessGithub_print_display():
        class AGprintRedirector:
            def __init__(self, widget):
                self.widget = widget

            def write(self, text):
                self.widget.insert(tkinter.END, text)
                self.widget.see(tkinter.END)
                fenetre_AG.update_idletasks()  # Mise à jour de l'interface utilisateur

        sys.stdout = AGprintRedirector(text_box)


    # Fonction pour exécuter AccessGithub_print_display() dans un thread séparé
    def execute_AG_print_display():
        threading.Thread(target=AccessGithub_print_display).start()

    # Création du bouton "OK" pour fermer la fenêtre
    bouton_ok = tkinter.Button(fenetre_AG, text="OK", command=AG_fermer_fenetre)
    bouton_ok.pack(pady=10)

    # Rediriger la sortie standard vers le widget Text
    AccessGithub_print_display()

#----- FIN Partie sur l'affichage des prints dans DisplayerPortfolio.py -----#

    #Input identifiant et token
    print("Connexion à Github...")
    ajd = date.today()
    print(ajd)

    identifiant = "VicBabin"
    #Token de 90 jours à compter du 11/02
    token = "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"

    #Utilisation du token d'accès
    git = Github(token)

    #Connexion (affichage de message pour la bonne connexion ou non)
    try:
        #Connexion de l'utilisateur
        user = git.get_user()
        #Message de connexion
        print("Vous êtes connecté en tant que :", user.login)
    except Exception as Echec:
        #Message d'erreur
        print("Une erreur s'est produite lors de la connexion à GitHub :", str(Echec))
        print("Vérifier si le token d'activation est toujours actif via Github : Profil > Settings > Developper settings")

    nom_repo = "Portfolio"
    repo = git.get_user(identifiant).get_repo(nom_repo)

    chemin_docs_local = "D:/portfolio/"
    chemin_docs_github = "docs/"

    black_list = ["desktop_background.JPG",
                  "LinkedIn_icon.png",
                  "mobile_background.png",
                  "styles.css",
                  "nav_barre.js",
                  "script.js",
                  "carte_chernobyl_BABIN_Victor.png",
                  "styles.css",
                  "nav_barre.js,"
                  "script.js"]

    compte_update = 0
    compte_crea = 0


    for dossier_racine, _, fichiers in os.walk(chemin_docs_local):
        for nom_fichier in fichiers:
            chemin_fichier_local = os.path.join(dossier_racine, nom_fichier)
            chemin_fichier_github = os.path.relpath(chemin_fichier_local, chemin_docs_local)
            chemin_fichier_github = os.path.join(chemin_docs_github, chemin_fichier_github)
            # Lisez le contenu du fichier local
            contenu_fichier = open(chemin_fichier_local, 'rb').read()

            # Vérifiez si le fichier existe déjà dans le dossier GitHub
            if nom_fichier not in black_list:
                try:
                    fichier_github = repo.get_contents(chemin_fichier_github.replace("\\","/"))
                    #On update le fichier
                    repo.update_file(chemin_fichier_github.replace("\\","/"), f"Update du {ajd}", contenu_fichier, fichier_github.sha)
                    print(f"Updated Github file {chemin_fichier_github} with local file {chemin_fichier_local}")
                    compte_update += 1
                except Exception as Creation:
                    #On crée le fichier car il n'a pas été possible d'update un fichier du même nom
                    repo.create_file(chemin_fichier_github.replace("\\","/"), f"Import du {ajd}", contenu_fichier)
                    print(f"Github file created {chemin_fichier_github} with local file {chemin_fichier_local}")
                    compte_crea += 1

    print(f"Mise à jour terminée : {compte_crea} fichier(s) créé(s), {compte_update} fichier(s) update")