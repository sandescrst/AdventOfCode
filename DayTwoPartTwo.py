# input import
import readfile as rd

def PartTwo():
    forward = 0
    depth = 0
    aim = 0
    #itreate thorught the list
    for command in rd.inputs:
        # split the command in list and assign as position and step
        pos, step = command.split()

        # find the right command and do the job accordingly
        if pos == "forward":
            if aim >0:
                depth  += (int(step) *aim)
            forward +=int(step)
        if pos == "down":
            aim +=int(step)
        if pos == "up":
            aim -= int(step)

    # product of  depth and forward
    product = depth*forward
        
    return product

print(PartTwo())