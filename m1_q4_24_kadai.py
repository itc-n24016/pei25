animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
print(total)
for animal in animals:
    from_D = animal.startswith('D') # animalが'D'で始まる場合true、それ以外をfalseを返す
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
        print(total)
    else:
        total += len(animal)
        print(total)
print(total)
