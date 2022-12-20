#!/usr/bin/env python3

if __name__ == "__main__":
    import time
    import random
    from random import seed


    #seed the random generator with the current time, so the output will differ each time one uses the script
    seed(time.time())

   #load the contents of 'nomen.txt', 'between.txt', 'nomen2.txt' into the corresponding variables
    with open('nomen.txt') as f:
        lines1 = f.readlines()

    with open('between.txt') as f:
        lines2 = f.readlines()

    with open('nomen2.txt') as f:
        lines3 = f.readlines()

    #strip leading and trailing whitespaces from the words
    lines1 = list(map(lambda w: w.strip(),lines1))
    lines2 = list(map(lambda w: w.strip(),lines2))
    lines3 = list(map(lambda w: w.strip(),lines3))
    
    #write 100 prompts into the console by concatenating three random words from the lists
    for j in range(1,100):
        ran1 = random.randrange(0,len(lines1))
        ran2 = random.randrange(0,len(lines2))
        ran3 = random.randrange(0,len(lines3))
        print(f"Dein Prompt ist: {lines1[ran1]} {lines2[ran2]} {lines3[ran3]}")
