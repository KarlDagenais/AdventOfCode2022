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
print(dict[max(dict, key=dict.get)]) #on affiche l'elfe qui a le plus de calories
