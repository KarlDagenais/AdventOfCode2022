from collections import Counter

with open ('1st.txt', 'r') as elves_list:
    for line in elves_list:
        elf_number=1
        total=0
        dict={}
        for line in elves_list:
            if line.strip()!="": #si la ligne n'est pas vide
                number=int(line) #on convertit la ligne en entier
                total = total + number
            if line.strip()=="": #si la ligne est vide
                dict[elf_number]=total #on ajoute le total à l'elfe
                elf_number += 1 #on passe à l'elfe suivant
                total=0 #le total recommence à 0 à chaque elfe

counter = Counter(dict)

top_3 = counter.most_common(3) #on récupère les 3 elfes dans une liste
total = top_3[0][1] + top_3[1][1] + top_3[2][1] #on additionne les calories des 3 elfes
print(total)