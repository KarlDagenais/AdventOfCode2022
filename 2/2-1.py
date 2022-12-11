with open ('2.txt', 'r') as rps:
    total = 0
    for line in rps:
        them, me = line.split()
        if me == "X":
            total += 1
        if me == "Y":
            total += 2
        if me == "Z":
            total += 3
        if me == "X" and them == "A":
            total += 3
        if me == "Y" and them == "B":
            total += 3
        if me == "Z" and them == "C":
            total += 3
        if me == "X" and them == "C":
            total += 6
        if me == "Y" and them == "A":
            total += 6
        if me == "Z" and them == "B":
            total += 6
    print(total)
   