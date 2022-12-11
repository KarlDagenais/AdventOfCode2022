from string import ascii_letters

total=0 #total
with open ("3.txt") as f: #ouvrir le fichier
    lines = f.readlines() #read all lines
for line in range(0, len(lines), 3): #pour chaque ligne, par bond de 3
    common_elements = list(set(lines[line].strip()).intersection(lines[line+1].strip(), lines[line+2].strip())).pop() #trouver les caractères communs aux 3 lignes
    priority = ascii_letters.index(common_elements)+1 #trouver la priorité du caractère
    total += priority #ajouter la valeur ascii au total      
print(total)







