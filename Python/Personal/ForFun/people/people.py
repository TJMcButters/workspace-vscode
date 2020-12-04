class People:

    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race

    def get_name(self):
        return self.name


    def get_age(self):
        return self.age


    def get_race(self):
        if self.race.lower() != 'white':
            return "Ew, I can't believe you're {}".format(self.race)
        else:
            return self.race
