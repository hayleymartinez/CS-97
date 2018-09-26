def partition(v, l):
    '''Takes a value v and a list l and partitions l into a
    list of elements that are equal to v and a list of all other
    elements.'''
    if len(l) == 0:
        return [[], []] 
    else:
        head = l[0]
        tail = l[1:] 
        partition_tail = partition(v, tail) 
        base_equal = partition_tail[0]
        base_other = partition_tail[1] 
        if v == head: 
            equal_list = [head] + base_equal
            other_list = base_other 
        else:
            equal_list = base_equal
            other_list = [head] + base_other
        return [equal_list, other_list]
    

def countDistinct(l):
    '''Takes a list l and returns the number of distinct elements
    in the list.'''
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        part_list = partition(head, tail)
        new_list = part_list[1]
        return 1 + countDistinct(new_list)


def selectionSort(l):
    '''Takes a list and returns a list containing the same elements
    but sorted from least to greatest.'''
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        min_num = min(l)
        part_list = partition(min_num, l)
        min_num_list = part_list[0]
        new_list = part_list[1]
        return min_num_list + selectionSort(new_list)


# for use in mergesort below; do not edit
def merge(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])

# for this problem, I looked at the Wikipedia page for merge sort for help
# understanding the algorithm logic
def mergeSort(l):
    '''Takes a list and returns a list containing the same elements
    but sorted from least to greatest.'''
    if l[1:] == []:
        return l 
    else:
        # split list into equal parts
        list1 = l[:len(l)//2] 
        list2 = l[len(l)//2:]
        # recursively sort each list
        m_list1 = mergeSort(list1) 
        m_list2 = mergeSort(list2)
        # merge lists
        merged = merge(m_list1, m_list2)
        return merged











 
        
