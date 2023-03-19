import random
def shuffle(card, n):
    for i in range(n):
        a = random.randint(0,10)
        r = i + a % (9 -i)
        tmp = card[i]
        card[i] = card[r]
        card[r] = tmp

a = [0,1,2,3,4,5,6,7,8]
shuffle(a,9)
print(a)