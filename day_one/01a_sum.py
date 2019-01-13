with open("01_input.txt", "r") as f:
    lines = f.readlines()
    numbers = map(lambda x: int(x.strip()), lines)
    print(sum(numbers))


