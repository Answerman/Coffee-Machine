chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

money = int(input())

n_sheep = money // sheep
if n_sheep == 0:
    n_cow = money // cow
    if n_cow == 0:
        n_pig = money // pig
        if n_pig == 0:
            n_goat = money // goat
            if n_goat == 0:
                n_chicken = money // chicken
                if n_chicken == 1:
                    print(str(n_chicken) + " chicken")
                elif n_chicken > 1:
                    print(str(n_chicken) + " chickens")
                else:
                    print("None")
            elif n_goat == 1:
                print(str(n_goat) + " goat")
            elif n_goat > 1:
                print(str(n_goat) + " goats")
        elif n_pig == 1:
            print(str(n_pig) + " pig")
        elif n_pig > 1:
            print(str(n_pig) + " pigs")
    elif n_cow == 1:
        print(str(n_cow) + " cow")
    elif n_cow > 1:
        print(str(n_cow) + " cows")
if n_sheep == 1:
    print(str(n_sheep) + " sheep")
elif n_sheep > 1:
    print(str(n_sheep) + " sheep")
