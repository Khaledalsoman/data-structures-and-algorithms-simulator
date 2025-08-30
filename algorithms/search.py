
class search:
    def __init__(self,arr):
        self.arr=arr
    
    def linear_Search(self):
        target=int(input('enter number you want to find '))
        for i in range(len(self.arr)):
            if self.arr[i]== target:
                print("the target",target,'is in',i,'index')
                return i
        print("target not found")
        return -1
    def binary_search(self):
        target=int(input('enter number you want to find '))
        low=0
        high=len(self.arr)-1
        while(low<=high):
            mid=(high + low) // 2
            if self.arr[mid]==target:
                print("the target",target,'is in',mid,'index')
                return mid
            elif self.arr[mid]>target:
                high=mid-1
            elif self.arr[mid]<target:
                low=mid+1
        return -1
