fish = 1
while True:
    total = fish
    enough_fish = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) //5 * 4
        else:
            enough_fish = False
            break
    if enough_fish:
        print(fish)
        break
    fish += 1
 