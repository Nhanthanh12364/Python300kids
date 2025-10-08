from math import*
prime = [True] * 101
def sieve():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(101)+1):
        if prime[i]:
            for j in range(i**2, 101, i):
                prime[j] = False
if __name__ == '__main__':
    sieve()
    for i in range(1,101):
        if prime[i]:
            print(i, end = ' ')






