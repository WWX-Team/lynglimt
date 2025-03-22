# -*- coding: utf-8 -*-

# requests
#
# envoie des requêtes à Mistral API

import os
import asyncio

from mistralai import Mistral
from json import loads, JSONDecodeError

# Initialisation
os.environ.update({"MISTRAL_API_KEY": None})
api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

# Fonction requête
def request(description : str) -> list :
    """"""
    requests = [ {
        "role": "user",
        "content": f"""Peux-tu me nommer des tableaux / sculptures dont la description est la suivante : \"{description}\".
        Répond dans un tableau JSON où chaque élément est un dictionnaire incluant :
        - le nom du tableau (dans "nom") ;
        - son auteur (dans "auteur") ;
        - sa date de publication (dans "date") ;
        - le type du tableau (peinture à l'huile, fuseau)) ou le composant de la sculpture (dans "type") ;
        - une liste de 5 à 10 mot clés dans un ordre logique décrivant l'œuvre (dans "motsCles") ;
        - un lien vers la page wikipédia français du tableau (si possible) (dans "lienWiki") ;
        - un lien vers une image correspondant au tableau (si possible (dans "lienIMG"), de préférence, sur wikimedia commons).
        Construit ton tableau avec 1, 2, 4 ou 6 oeuvres,
        en plaçant en premier celle qui est la plus plausible de correspondre à la description.""",
    } ]
    chat_response = client.chat.complete(model = "mistral-small-latest", messages = requests, response_format = {"type": "json_object"})
    try    : reponse = loads(chat_response.choices[0].message.content)
    except JSONDecodeError : raise RuntimeError("MistralAI n'a pas retourné de données au format demandé")
    # Une seule requête étant lancée, l'objet chat_response.choices ne contient qu'un unique élément
    return reponse
        
def check(result : list) -> bool :
    """"""
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
