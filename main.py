def decoder():
    f = open("klucz.txt", 'r')
    lines = f.readlines()
    index = 5

    for x in lines:
        for char in x.strip():
            if char == "R":
                if index % 3 != 0:
                    index += 1
            elif char == "U":
                if index >= 4:
                    index -= 3
            elif char == "D":
                if index < 7:
                    index += 3
            elif char == "L":
                if index not in [1, 4, 7]:
                    index -= 1

        print("klucz: ", index)


decoder()
