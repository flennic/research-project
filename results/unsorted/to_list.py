res = []

with open("sem_dev_loop.txt", "r") as file:
    for line in file:
        res.append(float(line.split()[1]))

print(res)
