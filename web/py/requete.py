# requests
#
# envoie (et traite) des requêtes à Mistral API

import os

from mistralai import Mistral
from json import loads, JSONDecodeError

# Initialisation
os.environ.update({"MISTRAL_API_KEY": "CLÉ-API"}) # CLÉ À INSÉRER
api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

# Fonction requête
def request(description : str) -> list :
    """envoie une requêtre à Mistrai Console et vérifie le bon format des données apparant"""
    requests = [ {
        "role": "user",
        "content": f"""Peux-tu me nommer des tableaux / sculptures dont la description est la suivante : \"{description}\".
        Répond dans un tableau JSON où chaque élément est un dictionnaire incluant :
        - le nom du tableau (dans "nom") ;
        - son auteur (dans "auteur") ;
        - sa date de publication (dans "date") ;
        - le type du tableau (peinture à l'huile, fuseau)) ou le composant de la sculpture (dans "type") ;
        - une liste de 5 à 10 mot clés dans un ordre logique décrivant l'œuvre (dans "motsCles") ;
        - une liste de couple de données (dans "mindpath") contenant respectivement :
            - un élément de la description
            - un entier compris entre 0 et 100 correspondant à la présence ou non de l'extrait précédent dans l'oeuvre choisie ; 
            et contenant de préférence tous les éléments de la description ;
        - un lien vers la page wikipédia français du tableau (dans "lienWiki") ;
        Place en premier celle qui est la plus plausible de correspondre à la description.
        VEILLE À NE PAS UTILISER PLUSIEURS FOIS LE MÊME TABLEAU.""",
    } ]
    chat_response = client.chat.complete(model = "mistral-small-latest", messages = requests, response_format = {"type": "json_object"})
    try    : reponse = loads(chat_response.choices[0].message.content)
    except JSONDecodeError : raise RuntimeError("MistralAI n'a pas retourné de données au format demandé")
    # Une seule requête étant lancée, l'objet chat_response.choices ne contient qu'un unique élément
    return reponse
        
def check(result : list) -> bool :
    """vérifie en profondeur le bon format d'un résultat de requête"""
    if not isinstance(result, list) :
        raise ValueError("résultat n'est pas une liste")
    keys = ["nom", "date", "auteur"]
    for i in range(len(result)) :
        hell = result[i]
        if not isinstance(hell, dict) :
            raise ValueError(f"résultat[{i}] n'est pas un dictionnaire")
        for arh in keys :
            if not arh in hell :
                raise ValueError("résultat[{i}] ne contient pas la clé ['{arh}']")
    return True
