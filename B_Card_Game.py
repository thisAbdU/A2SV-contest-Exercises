def card_game(arr):
    a1, a2, b1, b2 = arr
    wins = 0

    outcomes = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for o in outcomes:
        suneet_wins = 0
        slavic_wins = 0
        
        if o[0] > o[1]:
            suneet_wins += 1
        elif o[0] < o[1]:
            slavic_wins += 1
        
        if o[2] > o[3]:
            suneet_wins += 1
        elif o[2] < o[3]:
            slavic_wins += 1
        
        if suneet_wins > slavic_wins:
            wins += 1
    
    return wins

test = int(input())
for _ in range(test):
    arr = list(map(int, input().split()))
    print(card_game(arr))
