# import streamlit as st
# from calendar import month_abbr
# from datetime import datetime

# # Récupérer l'année et le mois actuels
# this_year = datetime.now().year
# this_month = datetime.now().month

# # Initialiser l'état pour stocker la sélection du mois
# if 'selected_month' not in st.session_state:
#     st.session_state.selected_month = None  # Aucune sélection par défaut

# def reset_month_selection():
#     # Réinitialiser l'état pour que toutes les checkbox soient réactivées
#     st.session_state.selected_month = None

# with st.expander('Report month'):
#     # Sélectionner l'année
#     report_year = st.selectbox("", range(this_year, this_year - 2, -1))

#     # Récupérer les mois en format abbrévié (jan, feb, etc.)
#     month_abbr = month_abbr[1:]

#     # Répartition des mois sur 4 colonnes
#     cols = st.columns(4)

#     for i, month in enumerate(month_abbr):
#         with cols[i % 4]:
#             # Si un mois est déjà sélectionné, les autres deviennent inactifs
#             if st.checkbox(month, key=f"month_{i}", value=(st.session_state.selected_month == month), disabled=(st.session_state.selected_month is not None and st.session_state.selected_month != month)):
#                 st.session_state.selected_month = month  # Mettre à jour la sélection

#     # Ajouter un bouton pour réinitialiser les checkbox
#     if st.button("Réinitialiser la sélection"):
#         reset_month_selection()  # Réinitialiser l'état centralisé

# # Afficher le résultat si un mois a été sélectionné
# if st.session_state.selected_month:
#     st.text(f'{report_year} {st.session_state.selected_month}')
# import streamlit as st
# from calendar import month_abbr
# from datetime import datetime

# # Récupérer l'année et le mois actuels
# this_year = datetime.now().year
# this_month = datetime.now().month

# # Initialiser l'état pour stocker la sélection du mois
# if 'selected_month' not in st.session_state:
#     st.session_state.selected_month = None  # Aucune sélection par défaut

# def reset_month_selection():
#     # Réinitialiser l'état pour que toutes les checkbox soient réactivées
#     st.session_state.selected_month = None

# with st.expander('Report month'):
#     # Sélectionner l'année
#     report_year = st.selectbox("", range(this_year, this_year - 2, -1))

#     # Récupérer les mois en format abbrévié (jan, feb, etc.)
#     month_abbr = month_abbr[1:]

#     # Répartition des mois sur 4 colonnes
#     cols = st.columns(4)

#     for i, month in enumerate(month_abbr):
#         with cols[i % 4]:
#             # Afficher chaque checkbox et désactiver les autres lorsqu'un mois est sélectionné
#             is_checked = (st.session_state.selected_month == month)
#             if st.checkbox(month, key=f"month_{i}", value=is_checked, disabled=(st.session_state.selected_month is not None and not is_checked)):
#                 # Si la case est cochée, on définit le mois comme sélectionné
#                 st.session_state.selected_month = month
#             elif not is_checked and st.session_state.selected_month == month:
#                 # Si on décoche la case, on réinitialise la sélection
#                 st.session_state.selected_month = None

#     # Ajouter un bouton pour réinitialiser les checkboxes
#     if st.button("Réinitialiser la sélection"):
#         reset_month_selection()  # Réinitialiser l'état centralisé

# # Afficher le résultat si un mois a été sélectionné
# if st.session_state.selected_month:
#     st.text(f'{report_year} {st.session_state.selected_month}')

# import streamlit as st
# from calendar import month_abbr
# from datetime import datetime
# import pandas as pd

# # Récupérer l'année et le mois actuels
# this_year = datetime.now().year
# this_month = datetime.now().month

# # Initialiser l'état pour stocker la sélection du mois
# if 'selected_month' not in st.session_state:
#     st.session_state.selected_month = None  # Aucune sélection par défaut

# def reset_month_selection():
#     # Réinitialiser l'état pour que toutes les checkboxes soient réactivées
#     st.session_state.selected_month = None

# def generate_editable_table(selected_month_index):
#     # Créer un tableau avec 13 colonnes (12 mois + Total) et 3 lignes
#     columns = [f"{month_abbr[i]}" for i in range(12)] + ['Total']
#     df = pd.DataFrame(index=range(3), columns=columns)
    
#     # Rendre uniquement la colonne du mois sélectionné éditable
#     for col in df.columns:
#         if col != month_abbr[selected_month_index + 1] and col != 'Total':
#             # Désactiver les autres mois (non sélectionnés)
#             st.dataframe(df.style.set_properties(**{'background-color': 'lightgray'}, subset=[col]))
#         elif col == month_abbr[selected_month_index + 1]:
#             # Autoriser l'édition de la colonne sélectionnée
#             st.write(f"Colonne éditable pour {col}")
#             # Ajouter une entrée editable ici (pour l'instant avec un placeholder simple)
#             for row in df.index:
#                 df.at[row, col] = st.text_input(f"Valeur {col} ligne {row+1}", key=f"{col}_{row}")
    
#     # Calculer et afficher la colonne "Total" (non éditable)
#     df['Total'] = df.apply(lambda row: row[month_abbr[selected_month_index + 1]], axis=1)
#     st.write(df)

# with st.expander('Report month'):
#     # Sélectionner l'année
#     report_year = st.selectbox("", range(this_year, this_year - 2, -1))

#     # Récupérer les mois en format abbrévié (jan, feb, etc.)
#     month_abbr = month_abbr[1:]

#     # Répartition des mois sur 4 colonnes
#     cols = st.columns(4)

#     selected_month_index = None  # Index du mois sélectionné

#     for i, month in enumerate(month_abbr):
#         with cols[i % 4]:
#             # Afficher chaque checkbox et désactiver les autres lorsqu'un mois est sélectionné
#             is_checked = (st.session_state.selected_month == month)
#             if st.checkbox(month, key=f"month_{i}", value=is_checked, disabled=(st.session_state.selected_month is not None and not is_checked)):
#                 st.session_state.selected_month = month
#                 selected_month_index = i

#     # Ajouter un bouton pour réinitialiser les checkboxes
#     if st.button("Réinitialiser la sélection"):
#         reset_month_selection()  # Réinitialiser l'état centralisé

# # Afficher le tableau si un mois est sélectionné
# if st.session_state.selected_month:
#     st.text(f'Tableau pour {st.session_state.selected_month}')
#     generate_editable_table(selected_month_index)

import streamlit as st
import pandas as pd
from st_aggrid  import GridOptionsBuilder, AgGrid
import datetime


st.title("Formulaire de Fréquentation")

year_col, month_col = st.columns(2)

# Sélection de l'année# Création des cases à cocher pour les mois
st.subheader("Mois des fréquentations")

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

selected_period = month_col.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY")

selected_period[1]

months_list = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
# col1, col2, col3, col4 = st.columns(4)

# # Utilisation d'un dictionnaire pour stocker l'état des cases à cocher
# selected_month = None
# month_states = {month: False for month in months}

# def update_month_state(month):
#     month_states[month] = True
#     for m in months:
#         if m != month:
#             month_states[m] = False
#     st.session_state.selected_month = month

# for i, col in enumerate([col1, col2, col3, col4]):
#     for month in months[i*3:(i+1)*3]:
#         if col.checkbox(month, key=f"check_{month}", on_change=update_month_state, args=(month,)):
#             selected_month = month


def draw_agtab(nom_activite_peri,selected_month):
    activite_peri = {
            nom_activite_peri: ["Amplitude Horaire","Nombre d'enfants"],
            "Valeur":[0]*2,
            "Enfants":["- 6 ans","+ 6 ans "],
            selected_month: [0] * 2,
    }
    tableau = pd.DataFrame(activite_peri)  
    gb = GridOptionsBuilder.from_dataframe(tableau)
    gb.configure_column("Valeur", editable=True,cellDataType="number")
    gb.configure_column(selected_month, editable=True)
    # gb.configure_default_column(editable=False)
    grid_options = gb.build()

    return AgGrid(tableau, gridOptions=grid_options,fit_columns_on_grid_load=True,height=100)

selected_month_number = selected_period[1].month
selected_month = months_list[selected_month_number-1]
# Création du tableau AgGrid
if selected_month:
    st.subheader("Choix des activités")
    periscolaire_tab, vacances_tab, Jeune_tab, Autres_tab, masquer = st.tabs(["Périscolaire", "Extrascolaire", "Jeune","Autres activités exceptionnelle","Masquer"])

    with periscolaire_tab :
        "---"
        box, tab = st.columns([0.25,0.75])
        matin = box.checkbox("Périscolaire Matin", False, key="peri_matin")
        
        if matin:
            with tab :
                draw_agtab("Périscolaire Matin",selected_month)
            
            if st.button("Sauvegarder"):
                st.balloons()
        "---"

        "---"
        box1, tab1 = st.columns([0.25,0.75])
        pause_meridienne = box1.checkbox("Pause Méridienne", False, key="peri_pause_meridienne")
        
        if pause_meridienne:
            with tab1 :
                draw_agtab("Périscolaire Matin",selected_month)
            
            if st.button("Sauvegarder"):
                st.balloons()
        "---"

        "---"
        box2, tab2 = st.columns([0.25,0.75])
        soir = box2.checkbox("Périscolaire Soir", False, key="peri_soir")
        
        if soir:
            with tab2 :
                draw_agtab("Périscolaire Matin",selected_month)
            
            if st.button("Sauvegarder"):
                st.balloons()
        "---"

        "---"
        box3, tab3 = st.columns([0.25,0.75])
        mercredi = box3.checkbox("Périscolaire Mercredi", False, key="peri_mercredi")
        
        if mercredi:
            with tab3 :
                draw_agtab("Périscolaire Mercredi",selected_month)
            
            if st.button("Sauvegarder"):
                st.balloons()
        "---"
    with vacances_tab :
            "---"
            box, tab = st.columns([0.25,0.75])
            matin = box.checkbox("Périscolaire Matin", False, key="hiver")
            
            if matin:
                with tab :
                    draw_agtab("Périscolaire Matin",selected_month)
                
                if st.button("Sauvegarder"):
                    st.balloons()
            "---"

            "---"
            box1, tab1 = st.columns([0.25,0.75])
            pause_meridienne = box1.checkbox("Pause Méridienne", False, key="peri_pause_meridienne")
            
            if pause_meridienne:
                with tab1 :
                    draw_agtab("Périscolaire Matin",selected_month)
                
                if st.button("Sauvegarder"):
                    st.balloons()
            "---"

            "---"
            box2, tab2 = st.columns([0.25,0.75])
            soir = box2.checkbox("Périscolaire Soir", False, key="peri_soir")
            
            if soir:
                with tab2 :
                    draw_agtab("Périscolaire Matin",selected_month)
                
                if st.button("Sauvegarder"):
                    st.balloons()
            "---"

            "---"
            box3, tab3 = st.columns([0.25,0.75])
            mercredi = box3.checkbox("Périscolaire Mercredi", False, key="peri_mercredi")
            
            if mercredi:
                with tab3 :
                    draw_agtab("Périscolaire Mercredi",selected_month)
                
                if st.button("Sauvegarder"):
                    st.balloons()
            "---"




    
    vacances = st.popover("Vacances")
    hiver = vacances.checkbox("Vacances d'hiver", True)
    printemps = vacances.checkbox("Vacances de printemps", True)
    ete = vacances.checkbox("Vacances d'été", True)
    automne = vacances.checkbox("Vacances d'automne", True)

    if hiver:
        pass

        
    
    # Création des données du tableau
    # data = {'Péri': [0] * 13, 'Mercredi': [0] * 13, 'Vacances': [0] * 13}
    data = {
    "Mois": selected_month,
    "Péri": [0],  # Exemple de données
    "Mercredi": [0],
    "Vacances": [0]
    }
    accueil_jour = pd.DataFrame(data)
    # accueil_jour = pd.read_csv('./templates/accueil_jours.csv', encoding="latin",delimiter=';')

    # Configuration d'AgGrid
    gb = GridOptionsBuilder.from_dataframe(accueil_jour)
    gb.configure_column("Péri", editable=True)
    gb.configure_column("Mercredi", editable=True)
    gb.configure_column("Vacances", editable=True)
    gb.configure_default_column(editable=False)
    grid_options = gb.build()

    # Affichage du tableau
    st.subheader("Nombre de jours d'accueil")
    # AgGrid(accueil_jour, gridOptions=grid_options, height=300, use_container_width=True)
    AgGrid(accueil_jour, gridOptions=grid_options)




# st.title("Sélecteur de mois interactif")

# # Sélection de l'année
# year = st.selectbox("Sélectionnez une année", range(2022, 2025))

# # Création des cases à cocher pour les mois
# months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
# col1, col2, col3, col4 = st.columns(4)

# # Dictionnaire pour stocker l'état des cases à cocher
# selected_month = None
# month_states = {month: False for month in months}

# def update_month_state(month):
#     month_states[month] = True
#     for m in months:
#         if m != month:
#             month_states[m] = False
#             st.session_state[f"check_{m}"] = False  # Met à jour visuellement les checkboxes
#     # st.rerun()  # Relance l'exécution pour mettre à jour l'affichage

# # Création des checkboxes
# for i, col in enumerate([col1, col2, col3, col4]):
#     for month in months[i*3:(i+1)*3]:
#         col.checkbox(month, key=f"check_{month}", value=month_states[month],
#                      on_change=update_month_state, args=(month,))


# if selected_month:
#     # Création des données du tableau
#     data = {'Péri': [0] * 13, 'Mercredi': [0] * 13, 'Vacances': [0] * 13}
#     df = pd.DataFrame(data, index=months + ['Total'])

#     # Configuration d'AgGrid
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_column(selected_month, editable=True)
#     gb.configure_default_column(editable=False)
#     grid_options = gb.build()

#     # Affichage du tableau
#     AgGrid(df, gridOptions=grid_options, height=300, use_container_width=True)



# Fonction pour créer et afficher le tableau
# def create_and_display_table():
#     if selected_month:
#         # Création des données du tableau
#         data = {'Péri': [0] * 13, 'Mercredi': [0] * 13, 'Vacances': [0] * 13}
#         df = pd.DataFrame(data, index=months + ['Total'])

#         # Configuration d'AgGrid
#         gb = GridOptionsBuilder.from_dataframe(df)
#         gb.configure_column(selected_month, editable=True)
#         gb.configure_default_column(editable=False)
#         grid_options = gb.build()

#         # Affichage du tableau
#         AgGrid(df, gridOptions=grid_options, height=300, use_container_width=True)
#     else:
#         st.write("Veuillez sélectionner un mois pour afficher le tableau.")

# # Appel de la fonction pour créer le tableau (initialement vide)
# create_and_display_table()