a = str(input())
mass = a.split()
min = 999
for i in range(0,len(mass)):
    if int(mass[i]) > 0:
        if int(mass[i])<min:
            min = int(mass[i])
print(min)
