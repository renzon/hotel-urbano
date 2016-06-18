suits = ['spades', 'clubs', 'hearts', 'diamonds']
cards = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

deck = [(c, s) for c in cards for s in suits]

print(deck)
