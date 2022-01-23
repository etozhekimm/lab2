n = int(input("Enter year: "))
i = n - 1984
c = i % 12
d = i % 10
animals = ['mouse', 'cow', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'chicken', 'dog', 'pig']
colors = ['green', 'green', 'red', 'red', 'yellow', 'yellow', 'white', 'white', 'black', 'black']
if i <= 11:
    anim = animals[i]
else:
    anim = animals[c]
if i <= 9:
    col = colors[i]
else:
    col = colors[d]

print("The {0} year is the year of {1} {2}.".format(n, col, anim))