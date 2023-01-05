# lire le fichier d'instructions
data=[]
with open ("9.txt", "r") as f:
    for line in f:
        data.append(line.strip())    
        
# identifier coordonnées de départ et les include dans un dictionnaire
coord = {}
coord["s"]=(0,0)

#Créer fonction de mouvement avec en argument les coordonnées de H et T et la prochaine instruction

def mouvement (H, T,  direction):
    """Calcule les nouvelles coordonnées en fonction de la direction et de la distance

    Args:
        depart (tuple): Les coordonnées de départ x, y
        instruction (string): Les instructions du mouvememnt en cours

    Returns:
        coordonnées: tuple des coordonnées de la tail
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
    
    # elif direction == "D": #si la direction est en bas
    #     if yh == yt or yh == yt+1: #si la tête est en haut de la queue ou au même endroit
    #         xh -= 1
    #     
            
            
    return (xh,yh), (xt,yt)

#appeler la fonction de mouvement pour chaque instruction
# for current in data:
#     direction = data[current][0]
#     distance = int(data[current][1:])
#     mouvement(H, T, current)
    
    
#enregistrer la nouvelle position dans un dictionnaire, ajouter 1 à la valeur de la clé si la position existe déjà



#compter le nombre de clées uniques dans le dictionnaire

