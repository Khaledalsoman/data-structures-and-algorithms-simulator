
from algorithms.search import search
list=[]
list_size=int(input("enter the list size: "))
for i in range(list_size):
    element=int(input(f'enter element number {i+1}: '))
    list.append(element)
choose=int(input('Select number of the method you want to follow \n' \
'3. linear search \n'
'4.binary search \n '))
if choose==3:
    ls=search(list)
    ls.linear_Search()
if choose==4:
    bs=search(list)
    bs.binary_search()