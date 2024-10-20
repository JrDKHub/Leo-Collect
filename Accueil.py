import streamlit as st
import pandas as pd
import requests as rs
from st_aggrid  import GridOptionsBuilder, AgGrid
import datetime


st.set_page_config(
   page_title="Formulaire",
   page_icon="💾",
   layout="wide",
#    initial_sidebar_state="expanded",
)

def draw_agtab(nom_activite_peri):
    
    data = {
    #   'Amplitude'  : ['Fusion','Fusion','Fusion'],
    ' ': ['Nb jours', 'Effectif -6 ans', 'Effectif + 6 ans'],
    'J': [0, 0, 0],
    'F': [0, 0, 0],
    'M': [0, 0, 0],
    'A': [0, 0, 0],
    'M2': [0, 0, 0],
    'J2': [0, 0, 0],
    'J3': [0, 0, 0],
    'A2': [0, 0, 0],
    'S': [0, 0, 0],
    # 'O': ['', '', ''],
    # 'N': ['', '', '']
    }

    # Créer le DataFrame
    df = pd.DataFrame(data)

    # Configurer les options de la grille avec un groupe d'en-têtes
    grid_options = {
        "columnDefs": [
            {
                "headerName": nom_activite_peri,
                "children": [

                    # {
                    #     "field": " Amplitude",
                    #      "headerName": "Amplitude ",
                    #     #  "rowSpan": 3
                    #     # "rowSpan": lambda params: 3 if params.data["Amplitude"] == "Fusion" else 1,
                    # #     "cellClassRules": {
                    # #     'cell-span': "value === 'Fusion'"
                    # # },
                    # },
                    {"field": " ", "headerName": " "},
                    {"field": "J", "headerName": "JANVIER"},
                    {"field": "F", "headerName": "FEVRIER"},
                    {"field": "M", "headerName": "MARS"},
                    {"field": "A", "headerName": "AVRIL"},
                    {"field": "M2", "headerName": "MAI"},
                    {"field": "J2", "headerName": "JUIN"},
                    {"field": "J3", "headerName": "JUILLET"},
                    {"field": "A2", "headerName": "AOUT"},
                    {"field": "S", "headerName": "SEPTEMBRE"},
                    # {"field": "O", "headerName": "OCTOBRE"},
                    # {"field": "N", "headerName": "NOV"},
                ]
            }
        ],
        "defaultColDef": {
            "editable": True,  # Rendre les colonnes éditables
            "sortable": True,  # Colonnes triables
            "filter": True,  # Possibilité d'appliquer des filtres
            "resizable": True  # Colonnes redimensionnables
        },
        "suppressRowTransform": True,
    }

    # Afficher la table Ag-Grid avec les options configurées
    AgGrid(df, grid_options,fit_columns_on_grid_load=True,height=150,theme='streamlit')
    


def show_tabs():
    
    st.header("1- Activités du dispositif")
    with st.expander("Chochez vos activités") :
        
        sep1,sep2,sep3,sep4 = st.columns(4)
        sep1.subheader("Périscolaire")
        peri_matin = sep1.checkbox("Périscolaire Matin",key="peri_matin")
        peri_pause = sep1.checkbox("Pause Méridienne",key="peri_pause")
        peri_soir = sep1.checkbox("Périscolaire Soir",key="peri_soir")
        peri_mercredi = sep1.checkbox("Périscolaire Mercredi",key="peri_mercredi")

        sep2.subheader("Extrascolaire")
        vac_hiver = sep2.checkbox("Vacances Hiver",key="vac_hiver")
        vac_printemps = sep2.checkbox("Vacances Printemps",key="vac_printemps")
        vac_automne = sep2.checkbox("Vacances Automne",key="vac_automne")
        vac_ete = sep2.checkbox("Vacances Eté",key="vac_ete")

        sep3.subheader("Jeune")
        jeune_ado = sep3.checkbox("Ado",key="jeune_ado")

        sep4.subheader("Autres activités")
        exc_cmj = sep4.checkbox("CMJ",key="exc_cmj")
        exc_es = sep4.checkbox("ES",key="exc_es")

        dic_activite = {
            "Périscolaire Matin":peri_matin,
            "Pause Méridienne":peri_pause,
            "Périscolaire Soir":peri_soir,
            "Périscolaire Mercredi":peri_mercredi,
            "Vacances Hiver":vac_hiver,
            "Vacances Printemps":vac_printemps,
            "Vacances Automne":vac_automne,
            "Vacances Eté":vac_ete,
            "Ado":jeune_ado,
            "CMJ":exc_cmj,
            "ES":exc_es
            }
        
    if any(dic_activite.values()) : 
        st.header("2- Etat des fréquentations")
        for key in dic_activite.keys():
            if dic_activite[key]:
                draw_agtab(key)
                amplitude = st.number_input(label="Amplitude horaire",key=f"amplitude_{key}",step=0.5,format="%0.1f",help="En heure")
                "---"
                    

sheet_csv = st.secrets["database_url"]
res = rs.get(url=sheet_csv)
open('database.csv', 'wb').write(res.content)
database = pd.read_csv('database.csv', header=0)

# Create user_state
if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'name_surname': '',
        'password': '',
        'logged_in': False,
        'user_type': '',
        'mail_adress': '',
        'fixed_user_message': ''
    }

if not st.session_state.user_state['logged_in']:
    # Create login form
    st.write('Connectez Vous')
    mail_adress = st.text_input("Nom d'utilisateur")
    password = st.text_input('Mot de passe', type='password')
    submit = st.button('Connexion')

    # Check if user is logged in
    if submit:
        user_ = database[database['mail_adress'] == mail_adress].copy()
        if len(user_) == 0:
            st.error('Utilisateur non trouvable')
        else:
            if user_['mail_adress'].values[0] == mail_adress and user_['password'].values[0] == password:
                st.session_state.user_state['mail_adress'] = mail_adress
                st.session_state.user_state['password'] = password
                st.session_state.user_state['logged_in'] = True
                st.session_state.user_state['user_type'] = user_['user_type'].values[0]
                st.session_state.user_state['mail_adress'] = user_['mail_adress'].values[0]
                st.session_state.user_state['fixed_user_message'] = user_['fixed_user_message'].values[0]
                st.write('Vous êtes connecté')
                st.rerun()
            else:
                st.write("Nom d'utilisateur ou mot de passe invalide")
elif st.session_state.user_state['logged_in']:
    st.write("Bienvenue sur l'application")
    st.write('Vous êtes connecté en tant que:', st.session_state.user_state['mail_adress'])
    # st.write('V:', st.session_state.user_state['user_type'])
    # st.write('Your fixed user message:', st.session_state.user_state['fixed_user_message'])
    "---"
    st.header("Fiche d'identité")

    col1, col2 = st.columns(2)

    col1.write("Métier")
    col2.write("Métier")


    
    col1.write("Territoire")
    col2.write("territoire")
    
    col1.write("Directeur Territorial")
    col2.write("dire_ter")
    col1.write("Directeur De Site")
    col2.write("dir_site")
    col1.write("Code Site")
    col2.write("code_site")
    
    "---"


    if st.session_state.user_state['user_type'] == 'admin':
        # st.write('You have admin rights. Here is the database')
        # st.table(database)
        show_tabs()


