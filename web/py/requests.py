# -*- coding: utf-8 -*-

# requests
#
# envoie des requêtes à Mistral API
# traite les résultats

import os
import asyncio

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

async def request(description : str):
    """"""
    requests = [ {
        "role": "user",
        "content": f"""Peux-tu me nommer des tableaux / sculptures dont la description est la suivante : \"{description}\".
        Répond dans un tableau JSON où chaque élément est un dictionnaire incluant :
        - le nom du tableau (dans "nom") ;
        - son auteur (dans "auteur") ;
        - sa date de publication (dans "date") ;
        - un lien vers la page wikipédia français du tableau (si possible) (dans "lienWiki") ;
        - un lien vers une image correspondant au tableau (si possible (dans "lienIMG")).
        Construit ton tableau avec 1, 2, 4 ou 6 oeuvres,
        en plaçant en premier celle qui est la plus plausible de correspondre à la description.""",
    } ]
    chat_response = client.chat.complete ( model = "mistral-small-latest",
                                           messages = requests,
                                           response_format = { "type": "json_object" } )
    for choice in chat_response.choices :
        print(choice)
        print(" -> " + str(choice.message.content))
