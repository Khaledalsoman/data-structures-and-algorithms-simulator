
from algorithms.search import search
from algorithms.Sort import Sort
from data_structures.queue import queue
def Main():
    list=[]
    list_size=int(input("enter the list size: "))
    for i in range(list_size):
        element=int(input(f'enter element number {i+1}: '))
        list.append(element)
    choose=int(input('Select the method you want to use \n' \
    ' 1.Data structure \n'
    ' 2.Algorithm \n '
    ))
    if choose==1:
        choose_DS=int(input("choose Data structure:\n "
        "1.Linked List \n"
        "2.queue \n"
        "3.stack \n"))
        if choose_DS==1:
            pass
        
        elif choose_DS==2:
            qu=queue(list)
            print(list)
            choice = int(input("choose method to use: \n" \
            "1.enqueue \n" \
            "2.dequeue \n" \
            "3.peek \n" \
            "4.size \n"))
            if choice ==1:
                qu.enqueue(int(input('choose number to enqueue ')))
            if choice ==2:
                qu.dequeue()
            if choice ==3:
                qu.peek()
            if choice ==4:
                qu.size()

    if choose==3:
        ls=search(list)
        ls.linear_Search()
    elif choose==4:
        bs=search(list)
        bs.binary_search()
    elif choose==5:
        bubble=Sort(list)
        bubble.bubble_sort()
Main()