a = str(input())
mass = a.split()
for i in range(0,len(mass)):
    mass[i] = int(mass[i])
for i in range(0,len(mass)):
    if i%2 == 0 or i ==0:
        print(mass[i])

