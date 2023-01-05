# lire le fichier d'instructions
data=[]
with open ("/Users/karldagenais/Documents/VisualStudioCode/AdventOfCode2022/9/9.txt", "r") as f:
    for line in f:
        data.append(line.strip())    
coord = []
H=(0,0)
T=(0,0)
coord.append(T)

#Créer fonction de mouvement avec en argument les coordonnées de H et T et la prochaine instruction

def mouvement (H, T,  direction):
    """Calcule les nouvelles coordonnées en fonction de la direction et de la distance

    Args:
        H (tuple): Les coordonnées de départ x, y de la head
        T (tuple): Les coordonnées de départ x, y de la tail
        instruction (string): Les instructions du mouvememnt en cours

    Returns:
        coordonnées: tuple des coordonnées de la head et de la tail
    """
    xh, yh = H
    xt, yt = T
    if direction == "R": #si la direction est à droite
        if xh == xt or xh == xt-1: #si la tête est à gauche de la queue ou au même endroit
            xh += 1
        elif xh == xt+1: #si la tête est à droite de la queue
            xh += 1
            xt += 1
            yt = yh
             
    elif direction == "L": #si la direction est à gauche
        if xh == xt or xh == xt+1: #si la tête est à droite de la queue ou au même endroit
            xh -= 1
        elif xh == xt-1: #si la tête est à gauche de la queue
            xh -= 1
            xt -= 1
            yt = yh    
            
    elif direction == "U": #si la direction est en haut
        if yh == yt or yh == yt-1: #si la tête est en bas de la queue ou au même endroit
            yh += 1
        elif yh == yt+1: #si la tête est en haut de la queue
            yh += 1
            yt += 1
            xt = xh
    
    elif direction == "D": #si la direction est en bas
        if yh == yt or yh == yt+1: #si la tête est en haut de la queue ou au même endroit
            yh -= 1
        elif yh == yt-1: #si la tête est en bas de la queue
            yh -= 1
            yt -= 1
            xt = xh
       
    return (xh,yh), (xt,yt)

#appeler la fonction de mouvement pour chaque instruction
for current in range(len(data)):
    direction, distance = data[current].split(" ")
    for i in range(int(distance)):
        H, T = mouvement(H, T, direction)
        if not T in coord: #ajoute les coordonnées de la queue à la liste des coordonnées si non présente
            coord.append(T) 


#compter le nombre d'entrées dans la liste
print(f"La première réponse est {len(coord)}")


#partie 2




