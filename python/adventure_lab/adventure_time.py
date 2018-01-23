"""

This is an adventure game, how exciting!

"""

class Creat:
    def __init__(self, name, location, health):
        self.name = name
        if location == None:
            self.location = 'start'
        else:
            self.location = location
        self.health = health
        self.weapon = Weapon('Bear Hands',None, 1)
        self.sac = []

    def tell_me_about_yourself(self):
        print('''
        
        Yo! My name is {}
        I am currently hanging out at {}
        Right now I have {} life.
        My weapon is a {}, Boo Yeah!
        
        
        
        '''.format(self.name, self.location, self.health, self.weapon.name))

    def pick_up(self, thing):
        if isinstance(thing, Weapon):
            self.weapon = thing
        elif thing is Potion:
            self.sac.append(thing)


class Weapon:
    def __init__(self, name, location, damage):
        self.name = name
        if location == None:
            self.location = 'Picked Up'
        else:
            self.location = location
        self.damage = damage
    def show_off(self):
        print('Check me out! I\'m {} and I do a whopping {} damage baby!'.format(self.name, self.damage))


class Potion:
    def __init__(self, location, health_restored):
        if location == None:
            self.location = 'Picked Up'
        else:
            self.location = location
        self.health_restored = health_restored

Main = {'Finn': Creat('Finn the Human', 'The Treehouse', 100), 'Jake' : Creat('Jake the Dog', 'The Treehouse', 100),
        'BMO': Creat('BMO', 'The Treehouse', 100)}

Weapons = {'Scarlet' : Weapon('The Golden Sword of Battle', None, 5), 'Finn Sword': Weapon('Finn Sword', 'Prismo\'s Place', 1000)}


Main['Finn'].pick_up(Weapons['Scarlet'])

Main['Finn'].tell_me_about_yourself()