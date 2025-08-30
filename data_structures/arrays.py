class arrays:
    def __init__(self):
        self.list=[]
    def arr(self):
        elements=int(input("enter number of elemnts: "))
        for i in range(elements):
            element=int(input(f'enter element {i+1}: '))
            self.list.append(element)
        print(self.list)
        return self.list


        
