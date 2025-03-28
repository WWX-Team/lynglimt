# run
#
# Shell du projet

### Init

print("~ Lynglimt\n")
vSD : list[str] = ['shellSD', 'printSD', 'fileSD']

### Gestion de l'argument-requête 

import sys
if len(sys.argv) > 1 : prompt = sys.argv[1]
else                 : raise RuntimeError("run.py fichier nécessite un argument-requête.")
if len(sys.argv) > 2 : forEnv = sys.argv[2]
else                 : forEnv = vSD[0]
if not forEnv in vSD : raise RuntimeError("environnement d'exécution inconnu\nEssayez la commande suivante : ‹python3 run.py 'prompt' 'fileSD'›")

### Gestion de la requête

import requete
print(' : Envoi de la requête | «', prompt, '»')
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
    import analyse
    import display
    from turtle import Terminator, TurtleScreen
    i = 0
    for item in promptResutlt :
        print(f' : Analyse  du résultat [{i}]')
        arbreMotsCles, arbreLogique = analyse.analyse(prompt, item)
        print(f' : Affichage du résultat [{i}]')
        title = f'« {item['nom']} » par {item['auteur']} ({item['date']})'
        print(f' [{i}] {title}')
        print('   : Mots Clés')
        try : display.afficherArbre(arbreMotsCles, title, 'Mots clés')
        except Terminator : print('   | fermé')
        TurtleScreen._RUNNING = True # Évite la fermeture de fenêtre intempestive
        print('   : Logique')
        try : display.afficherArbre(arbreLogique, title, 'Logique IA')
        except Terminator : print('   | fermé')
        TurtleScreen._RUNNING = True # De Même
        i += 1
        
if forEnv == 'printSD'   : 
    print(' : Résultat\n' + str(promptResutlt))
    
if forEnv == 'fileSD'   : 
    from json import dump
    print(' : Export du résultat')
    dump(promptResutlt, open('results.json', 'w'), indent = '    ', separators = '\n')
