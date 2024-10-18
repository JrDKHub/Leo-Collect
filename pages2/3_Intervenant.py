import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Importation du fichier CSV
df = pd.read_csv('./templates/accueil_jours.csv', encoding="latin",delimiter=';')  # Assurez-vous que le fichier est dans le même répertoire que votre script

# Affichage du tableau avec Ag-Grid
st.title("Tableau des jours d'accueil")
AgGrid(df)
