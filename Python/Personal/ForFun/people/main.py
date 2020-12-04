import people as p

x = p.People('Tyler', 28, 'White')
y = p.People('Jamalique', 19, 'Black')
a = p.People('Hose', 99, 'Hispanic')

z = [x, y, a]

for i in z:
    print(i.get_race())