'''
Author: Rys Ben
Guess number interactively.
'''

import random

def main():
    small=int(input("Enter the small number: "))
    large=int(input("Enter the large number: "))
    number=random.randint(small,large)
    count=0
    while 1:
        count+=1
        n=int(input("Who am I: "))
        if n>number:
            print("too large")
        elif n<number:
            print("too samll")
        else:
            print("Got it after %s retries!" % count)
            break

if __name__ == "__main__":
    main()
