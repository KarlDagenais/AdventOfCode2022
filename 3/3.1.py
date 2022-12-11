#split lines in halves
#find common items in both halves
#add the sum of their "priorities"
from string import ascii_letters

total=0 #total
with open ("3.txt") as f: #ouvrir le fichier
    lines = f.readlines() #read all lines
for line in lines: #pour chaque ligne
    items = [] #liste vide pour éviter les doublons
    a,b = line[:(len(line)//2)], line[(len(line)//2):] #diviser la ligne en deux
    for i in a: #pour chaque caractère dans la première moitié
        if i in b: #si le caractère est dans la deuxième moitié
            if i not in items:    
                items.append(i) #ajouter le caractère à la liste pour cette ligne
                priority = ascii_letters.index(i)+1 #trouver la priorité du caractère
                total += priority #ajouter la valeur ascii au total
print(total)                              
