import readfile as rd

def increaseCount():
    # list comprehension of input data
    list1 = [int(i) for i in rd.dayOne]
    # list two which starts from index 1
    list2 = list1[1:]
    count = 0
    # iterate through the zip list and compare the n value of list2 and list2.. if condition meets increase count by 1
    for num1, num2 in zip(list1,list2):
        if num2 >num1:
            count +=1
    return count

print(increaseCount())
    

