import time

class Person:
    def __init__(self, name, hp, max_hp, attack, defense, ID, time):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.id = ID
        self.time = time


def file_read(listo):
    f = open("chars.txt", "r")
    for x in range(4):
        str1 = f.readline()
        words = str1.split()
        p1 = Person(words[0], int(words[1]), int(words[2]), int(words[3]), int(words[4]), int(words[5]), float(words[6]) )
        print(p1.time)
        listo.append(p1)
    f.close()
    return listo
    

def file_write(listo):
    f = open("chars.txt", "w")
    for x in range(4):
        str1 = listo[x].name + " " + str(listo[x].hp) + " " + str(listo[x].max_hp) + " " + str(listo[x].attack) + " " +  str(listo[x].defense) + " " +  str(listo[x].id) + " " + str(listo[x].time) + "\n"  
        f.write(str1)
    f.close()


def find_index(id, listo):
    for x in range(5):
        if(listo[x].id == id):
            return x


def attack(id1, id2, listo):
    index1 = find_index(id1, listo)
    index2 = find_index(id2, listo)
    attack = listo[index1].attack
    defense = listo[index2].defense
    time1 = listo[index1].time
    currenttime = time.time()
    if((currenttime-time1) > 60):
        damage = attack-defense
        listo[index1].time = currenttime
        if damage > 0:
            listo[index2].hp -= damage
            return damage
        else:
            return 0
    else:
        return 1234567

def get_attack_time(id, listo):
    index = find_index(id, listo)
    time_left = 60 - (time.time() - (listo[index].time))
    return time_left
