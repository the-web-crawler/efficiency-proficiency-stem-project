# import the timeit module to time the algorithms
import timeit
# debugging only
import time

# define number of trials and rounding digit
trials = 100
roundTo = 2

# define a list of 256 items
array = ['KO', 'JG', 'OA', 'PP', 'IF', 'FK', 'HN', 'AP', 'DE', 'KJ', 'AD', 'NI', 'OP', 'NA', 'CP', 'JD', 'AL', 'BD', 'KB', 'ND', 'EJ', 'EH', 'PC', 'DO', 'IE', 'HB', 'LE', 'GO', 'EL', 'DC', 'GB', 'PN', 'EF', 'DB', 'FG', 'PO', 'GJ', 'NM', 'NN', 'DD', 'OE', 'GP', 'LA', 'GL', 'KN', 'FA', 'GG', 'PH', 'NE', 'DG', 'OG', 'IK', 'AF', 'IC', 'BO', 'EM', 'HK', 'HM', 'EG', 'GF', 'EI', 'MH', 'BF', 'KE', 'EC', 'LH', 'ML', 'MK', 'BA', 'OO', 'BB', 'NP', 'MP', 'EB', 'AH', 'NK', 'KC', 'AE', 'OF', 'IG', 'LB', 'IM', 'IO', 'CG', 'JJ', 'LF', 'GM', 'HI', 'PG', 'JH', 'GC', 'DF', 'JF', 'IL', 'II', 'MA', 'PA', 'KM', 'CI', 'LP', 'BH', 'DL', 'DJ', 'CK', 'FH', 'FI', 'HP', 'MM', 'HA', 'MO', 'BE', 'FC', 'CE', 'OC', 'BG', 'IH', 'OH', 'JA', 'FD', 'PM', 'KP', 'MI', 'NH', 'OL', 'AI', 'CB', 'PJ', 'BJ', 'FF', 'JE', 'EA', 'JP', 'GA', 'DP', 'AO', 'ED', 'ME', 'CD', 'EE', 'KG', 'IA', 'HO', 'NJ', 'PB', 'AJ', 'GE', 'CJ', 'AN', 'BM', 'PE', 'EO', 'JB', 'CF', 'HD', 'FP', 'AG', 'PK', 'BI', 'KL', 'CA', 'FE', 'OD', 'GI', 'AB', 'GH', 'LO', 'DN', 'LJ', 'NL', 'LG', 'MF', 'NB', 'KF', 'FM', 'BC', 'DK', 'IP', 'OB', 'JK', 'FJ', 'EK', 'LL', 'PF', 'KD', 'BP', 'AA', 'MD', 'KA', 'LI', 'CN', 'JL', 'JM', 'HH', 'GD', 'LM', 'NG', 'AK', 'CH', 'PL', 'CO', 'MN', 'LN', 'HF', 'EP', 'OJ', 'ID', 'KK', 'DA', 'IJ', 'JN', 'MJ', 'JI', 'NF', 'HG', 'KH', 'DI', 'OM', 'GN', 'CL', 'MB', 'AC', 'FN', 'FB', 'BN', 'DM', 'HC', 'EN', 'GK', 'BK', 'BL', 'HL', 'PD', 'FO', 'IB', 'LC', 'CM', 'LD', 'JO', 'OK', 'KI', 'MC', 'FL', 'HE', 'LK', 'OI', 'MG', 'DH', 'PI', 'JC', 'CC', 'IN', 'NO', 'HJ', 'ON', 'AM', 'NC']

# return time in milliseconds it takes to run a function one hundred times
def printMS (fString, name):
    print (f"{name}: {round(timeit.timeit(fString + '(array)', setup='from __main__ import array, ' + fString, number=trials)/trials*1000, roundTo)} ms")



# insertion sort
def insertion (list):
    # create an empty temporary list
    tempArray = []
    # for each item in the unsorted list...
    for item in list:
        # ...search in the temporary list for where it belongs, then insert it there
        loopLength = range(len(tempArray))
        for i in loopLength:
            if (item < tempArray[i]):
                tempArray.insert(i, item)
                break
        # insert the first item into the temporary list to get started
        if (not item in tempArray):
            tempArray.append(item)
    # the temporary list is now sorted
    return tempArray

# bubble sort
def bubble (list):
    # create a temporary list that is a copy of the unsorted list
    tempList = list[:]
    i = 0
    completed = True
    # while the temporary list is not sorted, loop through each item
    while True:
        i += 1
        # if at the last item and the loop is continued, start back at the beginning
        if (i == 255):
            i = 0
            completed = True
        nI = i+1
        # if the current item and the item on the right need to be swaped, swap them, and continue the loop
        if (tempList[i] > tempList[nI]):
            tempList[i], tempList[nI] = tempList[nI], tempList[i]
            completed = False
        # if the loop was never continued, then the temporary list is now sorted
        if (completed and i == 254): break
    return tempList

# mergesort
def mergesort (useList):
    # create function to merge two lists
    def merge (l1, l2):
        returnList = []
        while True:
            # if one of the two lists is empty, just add the entire other one to save time
            if len(l1) == 0:
                return returnList + l2
            if len(l2) == 0:
                return returnList + l1
            # add the first item out of the two in the first positions of the lists
            f = l1[0] if l1[0] < l2[0] else l2[0]
            returnList.append(f)
            # remove the item that was just added
            if f == l1[0]:
                l1.pop(0)
            else:
                l2.pop(0)
    # create a temporary list that is a copy of the unsorted list
    tempList = useList[:]
    # make each list item its own list consisting of just that one item
    for i in range(len(tempList)):
        tempList[i] = [tempList[i]]
    # while the list has more than one item...
    while len(tempList) > 1:
        tempTempList = []
        # ...merge each two consecutive items into one
        for i in range(0, len(tempList), 2):
            tempTempList.append(merge(tempList[i], tempList[i+1]))
        tempList = tempTempList
    # return the merged list
    return tempList[0]

def gnome (list):
    # create a temporary list that is a copy of the unsorted list
    tempList = list[:]
    # loop through each two items until the end is reached
    index = 0
    while index != len(tempList) - 1:
        # if the items are in the correct order, compare the next two
        if tempList[index] < tempList[index + 1]:
            index += 1
        # if the items are not in the correct order, swap them and compare the previous two
        else:
            tempList[index], tempList[index+1] = tempList[index+1], tempList[index]

            # The next three lines are very satisfying to watch in a terminal :)
            # print("\n\n\n\n\n")
            # print(tempList)
            # time.sleep(0.001)

            # if there are no previous two items to compare, compare the next two instead
            if (index == 0):
                index = 1
            else:
                index -= 1
    # the temporary list is now sorted
    return tempList

def selection (list):
    # create a temporary list that is a copy of the unsorted list 
    tempList = list[:]
    # while the second to last item has not been swapped...
    for index in range(len(tempList) - 2):
        # find minimum number
        min = index
        for i in range(index + 1, len(tempList)):
            if tempList[i] < tempList[min]:
                min = i
        # swap the current item with the minimum unsorted item
        tempList[index], tempList[min] = tempList[min], tempList[index]
    # the temporary list is now sorted
    return tempList

# show output
print (f"\nComparing sort times using different algorithms, sorting the same 256-item list {trials} times per algorithm. Results are displayed as the average time elapsed in milliseconds per trial, rounded to {roundTo} decimal places.\n")
printMS ("insertion", "Insertion Sort")
printMS ("bubble", "Bubble Sort")
printMS ("mergesort", "Merge Sort")
printMS ("gnome", "Gnome Sort")
printMS ("selection", "Selection Sort")

print("\n\nOriginal array:\n")

print(array)

print(f"\nSorted array (sorted in {round(timeit.timeit('array.sort()', setup='from __main__ import array', number=1)*1000, roundTo)} ms):\n")

print(array)
