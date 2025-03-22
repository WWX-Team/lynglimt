# -*- coding: utf-8 -*-

# run
#
# COMMENTAIRE
### Init
print("~ Lynglimt\n")
vSD : list[str] = ['shellSD', 'webSD']
### Gestion de l'argument-requête 
import sys
if len(sys.argv) > 1 : prompt = sys.argv[1]
else                 : raise RuntimeError("run.py fichier nécessite un argument-requête.")
if len(sys.argv) > 2 : forEnv = sys.argv[2]
else                 : forEnv = vSD[0]
if not forEnv in vSD : raise RuntimeError("environnement d'exécution inconnu\nEssayez la commande suivante : ‹python3 run.py 'prompt' 'webSD'›")
### Gestion de la requête
import requete
print(' : Envoi de la requête |', prompt)
promptResutlt = requete.request(prompt)
print(' : Vérification du résultat')
try : 
    requete.check(promptResutlt)
except ValueError as erLog :
    raise RuntimeError(f'Une erreur identifiée a eu lieu ({erLog})')
except :
    raise RuntimeError("erreur inconnue remontée")
### Transformation du résultat en fonction de l'environnement d'exécution
if forEnv == 'shellSD' :
    print(' : Analyse du résultat')
    import analyse
    arbreMotsCles, arbreLogique = analyse.analyse(prompt, promptResutlt)
if forEnv == 'webSD'   : 
    print(' : Export du résultat')