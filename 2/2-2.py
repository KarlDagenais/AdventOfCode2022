with open ('2.txt', 'r') as rps:
    total = 0
    for line in rps:
        them, me = line.split()
        if me == "X": #lose #1
            total += 0
            if them == "A": #rock
                total += 3
            if them == "B": #paper
                total += 1
            if them == "C": #scissors
                total += 2
        if me == "Y": #draw #2
            total += 3
            if them == "A": #rock
                total += 1
            if them == "B": #paper 
                total += 2
            if them == "C": #scissors
                total += 3
        if me == "Z": #win #3
            total += 6
            if them == "A": #rock
                total += 2
            if them == "B": #paper
                total += 3
            if them == "C": #scissors
                total += 1
            
    print(total)
    

