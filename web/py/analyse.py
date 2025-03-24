# -*- coding: utf-8 -*-

# analyse
#
# analyse les résultats d'une requête

### Classes

class Tag :
    """Couple Étiquette / Valeur."""
    
    def __init__(self, nom : str, valeur):
        self.nom : str = nom
        self.val       = valeur
        
    def obtenir(self) -> tuple :
        return (self.nom, self.val)

class Cellule : 
    """Implémentation d'une liste chaînée."""
    
    def __init__(self, nom : str, valeur, suivante : 'Cellule'):
        """cellule représentée par une étiquete [nom : str], associée à une valeur [valeur : any] et à sa cellule suivante [suivante : Cellule, None]."""
        self.tag : 'Tag' = Tag(nom, valeur)
        self.suivante    = suivante
        
    def __getitem__(self, idx) :
        if idx == 0 : return (self.name, self.val)
        if idx > 0 and self is not None : return self.suivante[idx - 1]
        raise IndexError("index en dehors des limites")
    
    def ajouter(self, cellule : 'Cellule'):
        if self.suivante is not None : return self.suivante.ajouter(cellule)
        self.suivante = cellule
        
class ArbreBinaire :
    """Implémentation d'un arbre binaire."""
    
    def __init__(self, nom : str, valeur, gauche : 'ArbreBinaire', droite : 'ArbreBinaire') :
        self.tag : 'Tag' = Tag(nom, valeur)
        self.arbreGauche = gauche
        self.arbreDroite = droite
        
    def obtenir(self) -> tuple :
        return self.tag.obtenir()

### Fonctions

def recherche(sequence : str, texte : str) -> set :
    """Recherche textuelle avec l'agorithme Boyer-Moore.
       Retourne toute les occurences de [sequence : str] dans [texte : str],
       dans un ensemble."""
       
    def table(txt : str):
        """construit la table de décalages de Boyer-Moore :
           ‹d[j][c]› est le plus grand entier ‹k < j› tel que ‹txt[k] == c›,
           s'il existe, et n'est pas défini sinon"""
        d = [{} for _ in range(len(txt))]
        for j in range(len(txt)) :
            for k in range(j):
                d[j][txt[k]] = k
        return d
    
    def decalage(d : list, j : int, c : str):
        """utilise la table [d] lorsque le caractère [j] est [c] au lieu du caractère attendu
           pour obtenir le décalage à suivre"""
        if c in d[j]: return j - d[j][c]
        return j + 1
    
    # Init Variables
    s = set()
    d = table(texte)
    # Boucle de recherche
    i : int = 0
    while i <= len(texte) - len(sequence) :
        # Boucle de recherche à l'indice i
        k = 0
        for j in range(len(sequence) -1, -1, -1) :
            # Si incohérence, on décale l'indice grâce à la table de décalage d
            if texte[i + j] != sequence[j] :
                k = decalage(d, j, texte[i + j])
                break
        # Si cohérence, on sauvegarde la positio,
        if k == 0 :
            s.add(i)
            k += 1
        # Recherche à l'indice suivant (en fonction du décalage)
        i += k
    # Retour
    return s    

def analyse(prompt : str, result : dict) -> tuple :
    """Analyse la prompt à l'aide du résultat :
     - correspondance entre les mots clés et la prompt ;
     - raisonnement de l'IA ;
    Retourne un tuple contenant deux arbres binaires.
    """
    corres = Cellule('A', 0, None)
    path = Cellule('B', 0, None)
    ab_corres = ArbreBinaire(corres.tag.nom, corres.tag.val, None, None)
    ab_path = ArbreBinaire(path.tag.nom, path.tag.val, None, None)

    # Correspondance mots-clés/prompt
    for el in result["motsCles"] :
        if recherche(el, prompt) > 0 :
            corres.ajouter(el, True, None)
        else :
            corres.ajouter(el, False, None)
    
    while corres.suivante is not None :
        corres = corres.suivante
        if corres.tag.val :
            ab_corres.arbreGauche = ArbreBinaire(corres.tag.nom, corres.tag.val, None, None)
            ab_corres = ab_corres.arbreGauche
        else :
            ab_corres.arbreDroite = ArbreBinaire(corres.tag.nom, corres.tag.val, None, None)
            ab_corres = ab_corres.arbreDroite
    
    # "Raisonnement" de l'IA    [[element, 0-100], ...]
    for eL in result["mindpath"] :       # créer "mindpath":list dans result
        path.ajouter(eL[0], eL[1], None)
    
    while path.suivante is not None :
        path = path.suivante
        if path.tag.val >= 50 :
            ab_path.arbreGauche = ArbreBinaire(path.tag.nom, path.tag.val, None, None)
            ab_path = ab_path.arbreGauche
        else :
            ab_path.arbreDroite = ArbreBinaire(path.tag.nom, path.tag.val, None, None)
            ab_path = ab_path.arbreDroite

    return (ab_corres, ab_path)
