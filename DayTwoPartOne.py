import readfile as rd


def multiplyCommand():
    forward = 0
    depth = 0
    for command in rd.inputs:
        pos, step = command.split()
        if pos == "forward":
            forward +=int(step)
        if pos == "down":
            depth +=int(step)
        if pos == "up":
            depth -= int(step)

    product = forward * depth
    return product
print(multiplyCommand())

