class Sort:
    def __init__(self,arr):
        self.arr=arr
    def bubble_sort(self):
        print(self.arr)
        for i in range(len(self.arr)):
           for j in range(len(self.arr)-1-i):
               if self.arr[j]>self.arr[j+1]:
                   temp=self.arr[j]
                   self.arr[j]=self.arr[j+1]
                   self.arr[j+1]=temp
                   print(self.arr)
                