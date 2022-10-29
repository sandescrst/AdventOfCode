import readfile as rd

def windowSum():
    #create comprehensive list from inputs
    mylist = [int(num) for num in rd.dayOne]
    
    count =0
    #comprehansive list of sum of three n elements from zip list
    tupleSum = [sum(tup) for tup in zip(mylist,mylist[1:], mylist[2:])]

    # loop through the zip list and meet the condition if happens increase count by 1
    for sum1, sum2 in zip(tupleSum,tupleSum[1:]):
        if sum2 > sum1:
            count +=1

    return count

print(windowSum())