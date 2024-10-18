import streamlit as st
import pandas as pd
from datetime import datetime

# Titre de la page
st.title("Sélection du mois avec formulaire dynamique")

# Affichage du sélecteur de mois
# Nous utilisons un sélecteur basé sur une date où l'utilisateur peut choisir une date/mois
date_selectionnee = st.date_input("Sélectionnez un mois", value=datetime.now(), 
                                  min_value=datetime(2020, 1, 1), 
                                  max_value=datetime(2025, 12, 31))

# Extraire uniquement le mois et l'année pour une vue simplifiée
mois_selectionne = date_selectionnee.strftime("%B %Y")  # Par exemple, "Octobre 2024"
st.write(f"Vous avez sélectionné : {mois_selectionne}")

# Affichage conditionnel du formulaire si un mois est sélectionné
if mois_selectionne:
    st.write(f"Formulaire pour {mois_selectionne}")

    # Formulaire multi-champs dynamique pour saisir des données
    nom = st.text_input("Nom")
    email = st.text_input("E-mail")
    commentaire = st.text_area("Commentaire")

    # Bouton de soumission
    if st.button('Soumettre'):
        # Simuler le stockage des données (vous pouvez les stocker dans un fichier ou une base de données)
        donnees = {
            "Nom": nom,
            "E-mail": email,
            "Commentaire": commentaire,
            "Mois": mois_selectionne,
            "Date de soumission": datetime.now()
        }
        
        # Afficher un message de confirmation
        st.success(f"Données soumises avec succès pour le mois {mois_selectionne} !")
        
        # Optionnel : Afficher les données soumises
        st.write(pd.DataFrame([donnees]))
