# display
#
# permet d'afficher grâce à Turtle les arbres de analyse.py

from turtle import Turtle
from analyse import ArbreBinaire

def afficherArbre(arbre : 'ArbreBinaire', header : str, nom : str = 'Sans titre'):
    window = Turtle()
    window.screen.title(f'Arbre binaire [{nom}]')
    window.screen.tracer(0)
    window.penup()
    
    def tracerNoeud(arbre : 'ArbreBinaire', x : int, y : int, depth : int = 0):
        if arbre is None : return
        window.goto(x, y)
        window.penup()
        window.goto(x, y - 18)
        color = '#000000'
        window.pencolor(color)
        window.write(arbre.tag.nom, align = 'center', font = ('Arial', 12, 'normal'))
        window.goto(x, y - 20)
        if not arbre.arbreGauche is None :
            if arbre.arbreGauche.val() > 50 : color = '#FF0000'
            window.pencolor(color)
            window.pendown()
            tracerNoeud(arbre.arbreGauche, x - 45, y - 36, depth + 1)
            window.goto(x, y - 20)
        color = '#000000'
        if not arbre.arbreDroite is None :
            if arbre.arbreDroite.val() > 50 : color = '#0000FF'
            window.pencolor(color)
            window.pendown()
            tracerNoeud(arbre.arbreDroite, x + 45, y - 36, depth + 1)
            window.goto(x, y - 20)
        window.penup()
    
    window.hideturtle()
    window.goto(0, 30)
    window.write(header, align = 'center', font = ('Arial', 16, 'normal'))
    tracerNoeud(arbre, 0, 20)
    window.screen.screensize(400, 200)
    window.hideturtle()
    window.screen.tracer(1)
    window.screen.mainloop()
