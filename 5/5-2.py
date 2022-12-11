#     [G] [R]                 [P]    
#     [H] [W]     [T] [P]     [H]    
#     [F] [T] [P] [B] [D]     [N]    
# [L] [T] [M] [Q] [L] [C]     [Z]    
# [C] [C] [N] [V] [S] [H]     [V] [G]
# [G] [L] [F] [D] [M] [V] [T] [J] [H]
# [M] [D] [J] [F] [F] [N] [C] [S] [F]
# [Q] [R] [V] [J] [N] [R] [H] [G] [Z]
#  1   2   3   4   5   6   7   8   9 

liste_1 = ["Q", "M", "G", "C", "L"]
liste_2 = ["R", "D", "L", "C", "T", "F", "H", "G"]
liste_3 = ["V", "J", "F", "N", "M", "T", "W", "R"]
liste_4 = ["J", "F", "D", "V", "Q", "P"]
liste_5 = ["N", "F", "M", "S", "L", "B", "T"]
liste_6 = ["R", "N", "V", "H", "C", "D", "P"]
liste_7 = ["H", "C", "T"]
liste_8 = ["G", "S", "J", "V", "Z", "N", "H", "P"]
liste_9 = ["Z", "F", "H", "G"]

def move(a, b, c):
    """Fonction qui déplace les boites

    Args:
        a (int): Le nombre de boites à déplacer
        b (int): Le numéro de colonne d'origine
        c (int): Le numéro de colonne de destination
    """
    list=[] #create a list to store the boxes
    for i in range(int(a)): #for the number of boxes to move
        list.append(globals()[f"liste_{b}"].pop()) #add the box to the list and remove it from the column
    for i in range(int(a)): #for the number of boxes to move
        globals()[f"liste_{c}"].append(list.pop(-1)) #add the box to the column and remove it from the list

        

with open ("5.txt") as f:
    for line in f:
        for char in line:
            sentence = line.strip().split(" ") #remove the \n and split the sentence
        move(sentence[1], sentence[3], sentence[5]) #call the function move with the 3 arguments (number of boxes, column of origin, column of destination)

result1=[liste_1.pop(-1), liste_2.pop(-1), liste_3.pop(-1), liste_4.pop(-1), liste_5.pop(-1), liste_6.pop(-1), liste_7.pop(-1), liste_8.pop(-1), liste_9.pop(-1)] 
        
print(f"Les boîtes sur le dessus des colonnes sont {result1}")
