# analyse
#
# analyse les résultats d'une requête

### Classes

class Tag :
    """Couple Nom / Valeur [Étiquette]."""
    
    def __init__(self, nom : str, valeur):
        self.nom : str = nom
        self.val       = valeur
        
    def obtenir(self) -> tuple :
        """retourne le couple de l'étiquette"""
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
        """équivalent d'append, complexité égale à la longueur de la liste chaînée"""
        if self.suivante is not None : return self.suivante.ajouter(cellule)
        self.suivante = cellule
        
    def val(self)  -> any : return self.tag.obtenir()[1]
    def name(self) -> any : return self.tag.obtenir()[0]
        
    def estDerniere(self) -> bool:
        """retourne un booléen indiquant s'il s'agit de la dernière cellule"""
        return self.suivante is None
    
    def obtenirSuivante(self) -> 'Cellule' :
        """retourne la cellule suivante"""
        return self.suivante
        
class ArbreBinaire :
    """Implémentation d'un arbre binaire."""
    
    def __init__(self, nom : str, valeur, gauche : 'ArbreBinaire' = None, droite : 'ArbreBinaire' = None) :
        self.tag : 'Tag' = Tag(nom, valeur)
        self.arbreGauche = gauche
        self.arbreDroite = droite
        
    def obtenir(self) -> tuple :
        """retourne l'étiquette associée au nœud de l'arbre"""
        return self.tag.obtenir()
    
    def val(self)  -> any : return self.tag.obtenir()[1]
    def name(self) -> any : return self.tag.obtenir()[0]
    
    def estFeuille(self) -> bool :
        """retourne un booléen indiquant si le nœud est une feuille"""
        return self.arbreDroite is None and self.arbreGauche is None

### Fonctions

def recherche(sequence : str, texte : str) -> set :
    """Recherche textuelle avec l'agorithme Boyer-Moore.
       Retourne toute les occurences de [sequence : str] dans [texte : str],
       dans un ensemble."""
       
    def table(sequence : str):
        """construit la table de décalages de Boyer-Moore :
           ‹d[j][c]› est le plus grand entier ‹k < j› tel que sequence[k] == c›,
           s'il existe, et n'est pas défini sinon"""
        d = [{} for _ in range(len(sequence))]
        for j in range(len(sequence)) :
            for k in range(j):
                d[j][sequence[k]] = k
        return d
    
    def decalage(d : list, j : int, c : str):
        """utilise la table [d] lorsque le caractère [j] est [c] au lieu du caractère attendu
           pour obtenir le décalage à suivre"""
        if c in d[j]: return j - d[j][c]
        return j + 1
    
    # Init Variables
    s = set()
    d = table(sequence)
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
        # Si cohérence, on sauvegarde la position,
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
    # Init données
    MotCles = Cellule('Résultat', 0, None)
    Logique = Cellule('Résultat', 0, None)
    arbreMotCles = ArbreBinaire(MotCles.name(), MotCles.val(), None, None)
    arbreLogique = ArbreBinaire(Logique.name(), Logique.val(), None, None)
    # Correspondance mots-clés/prompt
    for el in result["motsCles"] :
        if len(recherche(el.lower(), prompt.lower())) > 0 :
            MotCles.ajouter(Cellule(el, 100, None))
        else :
            MotCles.ajouter(Cellule(el, 0, None))
    # Construction de l'abre par effet de bord
    arbreMotClesCopy = arbreMotCles
    MotCles = MotCles.obtenirSuivante()
    while not MotCles.estDerniere() :
        arbreMotClesCopy.arbreDroite = ArbreBinaire(MotCles.name(), MotCles.val(), None, None)
        arbreMotClesCopy.arbreGauche = ArbreBinaire('Ø', 100 - MotCles.val(), None, None)
        if MotCles.val() == 100 : arbreMotClesCopy = arbreMotClesCopy.arbreDroite
        else                    : arbreMotClesCopy = arbreMotClesCopy.arbreGauche
        MotCles = MotCles.obtenirSuivante()
    # Pseudo Raisonnement de l'IA [[element, 0-100], [bla, 0-100], …]
    for eL in result["mindpath"] :
        if not len(eL) == 2: raise RuntimeError('Mistral a rencontré un problème, veuillez réessayer.')
        Logique.ajouter(Cellule(eL[0], eL[1], None))
    # Construction de l'abre par effet de bord
    arbreLogiqueCopy = arbreLogique
    Logique = Logique.obtenirSuivante()
    while not Logique.estDerniere() :
        arbreLogiqueCopy.arbreDroite = ArbreBinaire(Logique.name(), Logique.val(), None, None)
        arbreLogiqueCopy.arbreGauche = ArbreBinaire('Ø', 100 - Logique.val(), None, None)
        if Logique.val() >= 50 : arbreLogiqueCopy = arbreLogiqueCopy.arbreDroite
        else                   : arbreLogiqueCopy = arbreLogiqueCopy.arbreGauche
        Logique = Logique.obtenirSuivante()
    # Retour
    return (arbreMotCles, arbreLogique)
