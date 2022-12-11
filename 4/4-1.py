#NB this file has both challences

with open ("4.txt") as f: #ouvrir le fichier
    lines = f.readlines() #read all lines

overlap=0
partial=0

for line in lines:
    elf1_l, elf1_r, elf2_l, elf2_r = map(int, (line.replace("-",",")).split(","))  #split the line into 4 integers
    if elf1_l < elf2_l: #if the left of elf1 is smaller than the left of elf2
        if elf1_r >= elf2_r: #and the right is equal or larger
            overlap +=1 #then it's a complete overlap
            partial +=1 #and a partial overlap
            
        elif elf1_r >= elf2_l: #if the right of elf1 is smaller than the right of elf2
            partial +=1 #then it's a partial overlap
        
        else:
            continue 
    elif elf2_l < elf1_l: #if the left of elf2 is smaller than the left of elf1
        if elf2_r >= elf1_r: #and the right is equal or larger
            overlap +=1
            partial +=1
            
        elif elf2_r >= elf1_l: #if the right of elf2 is smaller than the right of elf1
            partial +=1 #then it's a partial overlap
        else:
            continue
    else:
        overlap +=1
        partial +=1
print(f"There are {overlap} full overlaps")
print(f"There are {partial} partial overlaps")

