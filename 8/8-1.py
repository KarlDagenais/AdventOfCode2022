#Trouver combien d'arbres sont visibles de l'extérieur de la forêt si 0 est l'arbre le plus petit et 9 le plus grand

with open ('8.txt', 'r') as f:
    data=[]
    for line in f:
        data.append(line.strip())
    
    

rangees = len(data) #nombre de rangees
colonnes = len(data[0]) #nombre de colonnes
visible = rangees*2 + colonnes*2 - 4 #on compte les arbres en bordure
scenic_score=[]

for colonne in range(1, colonnes-1):
    for rangee in range(1, rangees-1):
        arbre = data[rangee][colonne] #l'arbre qui nous intéresse
        
        gauche = [data[rangee][colonne-i] for i in range(1, colonne+1)]  #à gauche de l'arbre
        droite = [data[rangee][colonne+i] for i in range(1, colonnes-colonne)] #à droite de l'arbre
        haut=[data[rangee-i][colonne] for i in (range(1, rangee+1))] #la liste des arbres plus haut que l'arbre
        bas = [data[rangee+i][colonne] for i in range(1, rangees-rangee)] #la liste des arbres plus bas que l'arbre
        
        if arbre > max(haut) or arbre > max(bas) or arbre > max(gauche) or arbre > max(droite):
                visible += 1

        
        score=1
        for side in (gauche, droite, haut, bas):
            compteur=0
            for i in range(len(side)):
                if side[i] < arbre:
                    compteur +=1
                if side[i] >= arbre:
                    compteur+=1
                    break
                    
            score *= compteur
        scenic_score.append(score)
        
     
print(f"La solution du premier problème est: {visible} arbres sont visibles")  #fin du premier problème
print(f"Le score de l'arbre avec le meilleur emplacement est: {max(scenic_score)}")                        


        