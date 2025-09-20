
from algorithms.search import search
from algorithms.Sort import Sort
from data_structures.queue import queue
from data_structures.stack import stack
from data_structures.LinkedList import *
from data_structures.trees import *
def Main():
    choose=int(input('Select the method you want to use \n' \
    ' 1.Data structure \n'
    ' 2.Algorithm \n '
    ))
    if choose==1:
        choose_DS=int(input("choose Data structure:\n "
        "1.Linked List \n"
        "2.queue \n"
        "3.stack \n"
        "4.trees \n"))
        if choose_DS==1:
            LinkedList.display()
        elif choose_DS==2:
            queue.display()
        elif choose_DS==3:
            stack.display()
    if choose==2:
        choose_algo=int(input("choose algorithm:\n " \
        "1.Sort \n" \
        "2.Search \n"))
        if choose_algo==1:
            choose_sort=int(input("choose sorting method:\n " \
            "1.Selection Sort \n" \
            "2.Insertion Sort \n" \
            "3.Bubble Sort \n" \
            "4.Merge Sort \n" \
            "5.Quick Sort \n"))
            if choose_sort==1:
                sel=Sort(list)
                sel.selection_sort()
            elif choose_sort==2:
                ins=Sort(list)
                ins.insertion_sort()
            elif choose_sort==3:
                bubble=Sort(list)
                bubble.bubble_sort()
            elif choose_sort==4:
                merge=Sort(list)
                merge.merge_sort()
            elif choose_sort==5:
                print(list)
                quick=Sort(list)
                quick.quick_sort(0,len(list)-1)
        if choose_algo==2:
            choose_sort=int(input("choose searching method:\n " \
            "1.Linear Search \n" \
            "2.Binary Search \n"))
            if choose_sort==1:
                ls=search(list)
                ls.linear_Search()
            elif choose_sort==2:
                bs=search(list)
                bs.binary_search()
   
Main()