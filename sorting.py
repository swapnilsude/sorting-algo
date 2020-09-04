
#---------------------------------------------------------------------------------------#
#                                   bubble sort                                         #
#---------------------------------------------------------------------------------------#

def bubble_sort(mylist):
    for i in range(len(mylist) - 1):
        check = False
        for j in range(len(mylist) - i - 1):
            if mylist[j] > mylist[j + 1]:
                # swap
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            check = True
        if check == False:
            break
    return mylist
#---------------------------------------------------------------------------------------#
#                                   selection sort                                      #
#---------------------------------------------------------------------------------------#

def selection_sort(mylist):
    for i in range(len (mylist)):
        min_ss = i
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[min_ss]:
                min_ss = j
        # swap
        mylist[i], mylist[min_ss] = mylist[min_ss], mylist[i]
    return mylist

#---------------------------------------------------------------------------------------#
#                                   insertion sort                                      #
#---------------------------------------------------------------------------------------#

def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        save = mylist[i]
        j = i
        while j > 0 and mylist[j - 1] > save:
            mylist[j] = mylist[j - 1]
            j -= 1
        mylist[j] = save
    return mylist
  
#---------------------------------------------------------------------------------------#
#                                       quick sort                                      #
#---------------------------------------------------------------------------------------#

def quick_sort(mylist):
    quick_sort_r(mylist, 0, len(mylist) - 1)
    return mylist

# recursive loop for quick sort
def quick_sort_r(mylist , first, last):
    if last > first:
        pivot = partition(mylist, first, last)
        quick_sort_r(mylist, first, pivot - 1)
        quick_sort_r(mylist, pivot + 1, last)

# partition for quick sort
def partition(mylist, first, last):
    pivot = (first + last)//2
    if mylist[first] > mylist [pivot]:
        mylist[first], mylist[pivot] = mylist[pivot], mylist[first]  # swap
    if mylist[first] > mylist [last]:
        mylist[first], mylist[last] = mylist[last], mylist[first]  # swap
    if mylist[pivot] > mylist[last]:
        mylist[pivot], mylist[last] = mylist[last], mylist[pivot]    # swap
    mylist [pivot], mylist [first] = mylist[first], mylist[pivot]    # swap
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and mylist[i] <= mylist[pivot]:
            i += 1
        while j >= first and mylist[j] > mylist[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            mylist[i], mylist[j] = mylist[j], mylist[i]  # swap
    mylist[j], mylist[pivot] = mylist[pivot], mylist[j]  # swap
    return j

#---------------------------------------------------------------------------------------#
#                                       heap sort                                       # 
#---------------------------------------------------------------------------------------#

def heap_sort(mylist):
    first = 0
    last = len(mylist) - 1
    create_heap(mylist, first, last)
    for i in range(last, first, -1):
        mylist[i], mylist[first] = mylist[first], mylist[i]  # swap
        heap_helper (mylist, first, i - 1)
    return mylist

# create heap
def create_heap(mylist, first, last):
    i = last//2
    while i >= first:
        heap_helper(mylist, i, last)
        i -= 1

# establish heap property
def heap_helper(mylist, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and mylist[k] < mylist[k + 1]:
            k += 1
        if mylist[first] >= mylist[k]:
            break
        mylist[first], mylist[k] = mylist[k], mylist[first]  # swap
        first = k

#---------------------------------------------------------------------------------------#
#                                       merge sort                                      #
#---------------------------------------------------------------------------------------#

def merge_sort(mylist):
    merge_sort_r(mylist, 0, len(mylist) -1)
    return mylist

# recursive function for merge sort
def merge_sort_r(mylist, first, last):
    if first < last:
        pivot = (first + last)//2
        merge_sort_r(mylist, first, pivot)
        merge_sort_r(mylist, pivot + 1, last)
        merge(mylist, first, last, pivot)

# merge for merge_sort_r
def merge(mylist, first, last, pivot):
    helper_list = []
    i = first
    j = pivot + 1
    while i <= pivot and j <= last:
        if mylist [i] <= mylist [j]:
            helper_list.append(mylist[i])
            i += 1
        else:
            helper_list.append(mylist [j])
            j += 1
    while i <= pivot:
        helper_list.append(mylist[i])
        i +=1
    while j <= last:
        helper_list.append(mylist[j])
        j += 1
    for k in range(last - first + 1):
        mylist[first + k] = helper_list [k]