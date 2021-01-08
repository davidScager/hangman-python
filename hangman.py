from time import sleep
from string import ascii_uppercase

# list of screens
screen = ['''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |
|    _________    |
|    |/    |      |
|    |     O      |
|    |    /|\     |
|    |     ^      |
|    |    / \     |
|    |\           |
|   ------------  |
|   |/        \|  |
|_________________|

''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |O
|    __________   |O
|    |/           |O
|    |            |O
|    |            |O
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |O
|    |/    |      |O
|    |            |O
|    |            |O
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |O
|    |     O      |O
|    |            |O
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |O
|    |     |      |O
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |X
|    |    /|      |O
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |X
|    |    /|\     |X
|    |            |O
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |X
|    |    /|\     |X
|    |     ^      |X
|    |            |O
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |X
|    |    /|\     |X
|    |     ^      |X
|    |    /       |X
|    |\           |O
|   ------------  |
|   |/        \|  |
|_________________|
''', '''
         o
 -~H-A-N-G-M-A-N~-
 ________^________
|                 |X
|    __________   |X
|    |/    |      |X
|    |     O      |X
|    |    /|\     |X
|    |     ^      |X
|    |    / \     |X
|    |\           |X
|   ------------  |
|   |/        \|  |
|_________________|
''']

# Start screen
print(screen[0])

# use a screen counter, which updates when player guesses wrong.
count = 1

# set a word and turn into a list of letters.
# maybe use arrays instead?
s1 = input("Pick a word (all caps, spaces in between):")
#use a random word selector using 'wordListEnglish3000.txt'
#find a way to allow player to set word normally
l1 = [x for x in s1.split()]
length = len(l1)

# create list of underscores with l1 length
l2 = []
while length > 0:
    l2.append("_")
    length -= 1
# Create an alphabet overview
l3 = list(ascii_uppercase)


# Create Tkinter GUI with buttons, text input bar
# screens as labels that can be updated

# function found online to get all locations of a in l1
def list_duplicates_of(seq, item):
    start = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start + 1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start = loc
    return locs


# Start while loop for main part of the game
while l2 != l1:
    # print the current screen
    print(screen[count], " ".join(l2), '\n\n', " ".join(l3), '\n')
    # check game over condition
    if screen[count] == screen[9]:
        print('''You're hanged man!
         Game Over''')
        break
    # give the player due warning
    if screen[count] >= screen[7]:
        print("Carefull now...")
    # Request input
    a = input("Guess a letter(caps):")
    # check if a is in l1 and insert into l2
    try:
        # check if you already guessed that letter
        if a in l2:
            print("You already tried this letter.")
            sleep(1)
            pass
        elif a in l1:
            print("Good guess!")
            sleep(1)
            # use function to get locations of a in l1
            l4 = list_duplicates_of(l1, a)
            for i in l4:
                del l2[i]
                l2.insert(i, a)
            # Replace guessed letter in alphabet overview with "_".
            for x in l3:
                if x == a:
                    j = int(l3.index(x))
            l3.remove(a)
            l3.insert(j, "_")
        else:
            print("Bad luck, mate!\nOne step closer to the noose.")
            sleep(1)
            count += 1
            for x in l3:
                if x == a:
                    j = l3.index(x)
            l3.remove(a)
            l3.insert(j, "_")
    except ValueError:
        # check for ValueError and continue with the while loop afterwards.
        print("You already tried this letter.")
        sleep(1)

# I should turn this into functions called display and game so I can unit test them.
# still prints alphabet list
if l2 == l1:
    print(screen[count], "~", " ".join(l2), "~", '''\n    Well done!\nYou escaped the noose.''')
    end = input("Start a new game? (y/n)")
else:
    end = input("Start a new game? (y/n)")

# if end==y:
# start from the beginning of the script.
