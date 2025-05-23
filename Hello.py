import streamlit as st

# Importation du module
from streamlit_option_menu import option_menu

# AUTHENTIFICATION 

from streamlit_authenticator import Authenticate
# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}
# st.session_state est un objet dans Streamlit qui permet de garder 
# les données entre les interactions de l'utilisateur avec l'application. 
# Cela permet de conserver les informations même lorsque l'utilisateur interagit 
# avec l'application, comme après un rafraîchissement de la page ou un changement d'état.

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)
authenticator.login()

def accueil():
    st.write("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    # On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
    # L'utilisateur peut choisir son moyen de contact préféré parmi trois options
    
    # Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
    with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
        selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Photos"])
        authenticator.logout("Déconnexion")
    # On indique au programme quoi faire en fonction du choix

    if selection == "Accueil":
        st.header("Bienvenue sur ma Page")
        st.image("photo_page.png")

    elif selection == "Photos":
        st.header("Bienvenue sur mon album photo")
        # Création de 3 colonnes 
        col1, col2, col3 = st.columns(3)
        # Contenu de la première colonne : 
        with col1:
            st.subheader("POLE 1")
            st.image("pol1.png")

        # Contenu de la deuxième colonne :
        with col2:
            st.subheader("POLE 2")
            st.image("pol2.png")

        # Contenu de la troisième colonne : 
        with col3:
            st.subheader("POLE 3")
            st.image("pol3.png")
        # ... et ainsi de suite pour les autres pages


if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')









  

