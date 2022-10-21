from time import sleep 

#1 = device, white/gray\
#2 = fight, white/red
#3 = place, blue/green
#4 = secret, blue
#5 = items, pink/blue
#6 = black/red
#7 = sleep, gray/gray

#tree: 森
#rock: ○
#person: ⩀
#chest: ⊞


def colors(msg, num):
    if num == 1: 
        print(f'\033[7;49;94m{msg}\033[m ')
    elif num == 2:
        print(f'\033[7;49;31m{msg}\033[m ')
    elif num == 3:
        print(f'\033[7;49;92m{msg}\033[m ')
    elif num == 4:
        print(f'\033[5;49;34m{msg}\033[m ')
    elif num == 5:
        print(f'\033[7;49;95m{msg}\033[m ')
    elif num == 6:
        print(f'\033[7;49;91m{msg}\033[m')
    else:
        print(f'\033[7;49;90{msg}\033[m')


def game_over():
    print('-='*46)
    print(f'\033[7;49;91m{"Game Over":^92}\033[m', end='')
    print('\033[7;49;91m',end ='')
    print('-='*46)
    print('\033[m')
    exit()


def start(msg):
        staart = False
        while not staart:
            start = input(msg).strip().lower()
            if start == 'start':
                begin()
                return 'start'
            elif start == 'exit':
                return 'exit'
            else:
                print('Please, just type "start" or "exit" ')
        

def line(x = 0):
    if x == 0:
        line ='=~'*107
        colors(line, 4)
    if x == 1:
        line ='=~'*53
        colors(line, 4)       


def short_line():
    line = '~'*15
    colors(line, 4)

def forest(x=0):
    if x == 0:
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀   ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
        print(forest)
    elif x == 1:
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
        print(forest)

    elif x == 2:
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Zz  /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
        print(forest)
    elif x == 3:
        forest = '\033[7;49;91m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森s森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀↞Ÿ ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Ÿ↟  ↞Ÿ⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森\033[m'
        print(forest)

    
def begin():     
    begin= "You wake up in a forest. \
Behind you is a very large rock, it is still daylight. \
You only have the clothes on your body, a blouse, pants and shoes (all cloth). \
To your left is just a dense forest. \
To your right is a chest. \
And in front of you is a road."
    colors(begin,1)
    line()


def begin_1(fc):
    if fc == 'exit':
        print(':(')
        exit()
    else:
        begin_1 = 'Theres not much to do. \
You want to move on. \
Examine the chest or remain lying down?'
    colors(begin_1,1)
    forest()

def begin_choice(fc):
    sucess = False
    cont_nap = 0
    while not sucess:
        line(1)
        msg = '(move on)\n(examine)\n(nap)\n'
        choice = input(msg)
        short_line()
        if choice == 'move on':
            print('You go on along the trail')
            return 1
        elif choice == 'examine':
            print('oi')
        elif choice == 'nap':
            cont_nap += 1
            nap(cont_nap)
            continue
        else:
            print('ERROR: Invalid alternative!')



#=========================================================
def nap(cont_nap):
    cont_nap += 1
    sleep(1)
    if cont_nap == 2:
        print('Zzzzzzz')
        forest(1)
        print("*now woke up*\nYou don't know if you're more tired or more willing")
        short_line()
        return 
    elif cont_nap == 3:
        colors('Zzzzzzzzzzzzz',7)
        forest(2)
        print('*now woke up*\nYou almost fell asleep again')
        short_line()
        return 
    if cont_nap == 4:
        forest(3)
        print('\033[7;49;91mYou fell into such a deep sleep that the Caucaia tribe,\
 known as the "papangus", took you!')
        game_over()



Start = start('Start Game? ')
Start_1 = begin_1(Start)
fisrt_awser = begin_choice(Start_1)
print(fisrt_awser)

#Need to finish "move on" and "examine" options. \
#Remember to be able to go back to the beginning after moving forward!




