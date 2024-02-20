import os
import sys
import tkinter
from tkinter import *
def fonction_PicturesLoader():

# ----- Partie sur l'affichage des prints dans DisplayerPortfolio.py -----#
    def PL_fermer_fenetre():
        fenetre_PL.destroy()

    # Création de la nouvelle fenêtre
    fenetre_PL = tkinter.Tk()
    fenetre_PL.title("PicturesLoader")

    # Widget Text pour afficher les sorties
    text_box = tkinter.Text(fenetre_PL, wrap=tkinter.WORD, width=40, height=10)
    text_box.pack(fill="both", expand=True)

    # Rediriger la sortie standard vers le widget Text
    def PicturesLoader_print_display():
        class PLprintRedirector:
            def __init__(self, widget):
                self.widget = widget

            def write(self, text):
                self.widget.insert(tkinter.END, text)
                self.widget.see(tkinter.END)  # Faire défiler automatiquement vers la fin du texte


        sys.stdout = PLprintRedirector(text_box)

    # Création du bouton "OK" pour fermer la fenêtre
    bouton_ok = tkinter.Button(fenetre_PL, text="OK", command=PL_fermer_fenetre)
    bouton_ok.pack(pady=10)

    # Rediriger la sortie standard vers le widget Text
    PicturesLoader_print_display()

#----- FIN Partie sur l'affichage des prints dans DisplayerPortfolio.py -----#

    #Chemin du dossier de photo et du fichier photos.html
    photos_path = "C:/Portfolio/VicBabinPortfolio.github.io/docs/assets/images/photos/"
    html_path = "C:/Portfolio/VicBabinPortfolio.github.io/docs/photos.html"
    os.getcwd()

    #Suivi des identifiants des images par colonne
    Colonnes = {"Col1" : 1,"Col2":1,"Col3":1}

    #Nombre de photos
    nb_photos = 0


    #On compte les photos qui sont déjà prises en compte par le fichier html (qui ont le nom "Col")
    for i, filename in enumerate(os.listdir(photos_path)):
        if filename[0:3] == "Col":
            Colonnes[filename[0:4]] = Colonnes[filename[0:4]] + 1
            nb_photos += 1
    #Pour les photos qui ne sont pas renommées "Col" (c'est-à-dire les nouvelles) on leur donne un nouveau nom
    for i, filename in enumerate(os.listdir(photos_path)):
        if filename[0:3] != "Col":
            cle_plus_petite_valeur = min(Colonnes, key=Colonnes.get)
            os.rename(photos_path + filename, photos_path + str(cle_plus_petite_valeur+"_"+str(Colonnes[cle_plus_petite_valeur])) + ".jpg")
            Colonnes[cle_plus_petite_valeur] = Colonnes[cle_plus_petite_valeur] + 1
            print("Une nouvelle photo a été renommée !")
            nb_photos +=1

    #-----------------------------------------------------------------------------------#

    #En ecrit nos variables qui seront les balises de notre fichier HTML
    div_principale = '\n        <div class="row">'
    div_colonne = '            <div class="column">'
    balise_image1 = '              <img class="mosaique" src="assets/images/photos/'
    balise_image2 = '">'
    end_div_principale = '        </div>\n'
    end_div_colonne = '            </div>'

    #On regroupe les images par colonne
    images_col1 = []
    images_col2 = []
    images_col3 = []
    for i, filename in enumerate(os.listdir(photos_path)):
        if filename[0:4] == 'Col1':
            images_col1.append(filename)
        elif filename[0:4] == 'Col2':
            images_col2.append(filename)
        elif filename[0:4] == 'Col3':
            images_col3.append(filename)

    #On ecrit les ligens de codes du fichier html en fonction de nos images
    #Ici pour la colonne 1
    script_col = div_principale+"\n"+div_colonne+"\n"
    for each in images_col1:
        script_col = script_col+balise_image1+each+balise_image2+"\n"
    script_col = script_col+end_div_colonne+"\n"
    #Ici pour la colonne 2
    script_col = script_col+div_colonne+"\n"
    for each in images_col2:
        script_col = script_col+balise_image1+each+balise_image2+"\n"
    script_col = script_col+end_div_colonne+"\n"
    #Ici pour la colonne 3
    script_col = script_col+div_colonne+"\n"
    for each in images_col3:
        script_col = script_col+balise_image1+each+balise_image2+"\n"
    script_col = script_col+end_div_colonne+"\n"+end_div_principale

    #-------------------------------------------#

    # On lit le fichier photos.html
    with open(html_path, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # On recherche nos commentaires qui sont de part et d'autres de la mosaïques des photos
    commentaire_debut ="<!--Mosaique des photos-->"
    commentaire_fin = "<!--Affichage de l'image cliquée en grand (cf CSS)-->"

    #On identifier les commentaires
    indice_debut = contenu.find(commentaire_debut)
    indice_fin = contenu.find(commentaire_fin)

    # On vérifie les commentaire sont bien identifiés et on ajoute nos lignes de codes tout en gardant les commentaires
    if indice_debut != -1 and indice_fin != -1:
        #Delete les lignes contenu entre les deux indices
        contenu = (contenu[:indice_debut]+contenu[indice_fin:])

        lignes_a_ajouter = script_col

        #La totalité du code de notre fichier photos.html
        nouveau_contenu = (contenu[:indice_debut]+commentaire_debut+lignes_a_ajouter+contenu[indice_debut:])

        #On écrit tout le code dans notre fichier html
        with open(html_path, 'w', encoding='utf-8') as fichier_modifie:
            fichier_modifie.write(nouveau_contenu)

        print(f"{nb_photos} sont intégrées dans le portfolio")
        print("Le fichier photos.html a été mis à jour avec les nouvelles photos !")
    else:
        print("Commentaires non trouvés, le fichier photos.html n'a pas été changé")
