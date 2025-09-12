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

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            print(self.arr)  # print current state
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
        return self.arr

    def selection_sort(self):
        print(self.arr)
        for i in range(len(self.arr)):
            min_index=i
            for j in range(i+1,len(self.arr)):
                if self.arr[j]<self.arr[min_index]:
                    min_index=j
            if min_index!=i:
                self.arr[i],self.arr[min_index]=self.arr[min_index],self.arr[i]
                print(self.arr)

    def insertion_sort(self):
        print(self.arr)
        for i in range(1,len(self.arr)):
            key=self.arr[i]
            j=i-1
            while j>=0 and self.arr[j]>key:
                self.arr[j+1]=self.arr[j]
                j-=1
            self.arr[j+1]=key
            print(self.arr)

    def merge_sort(self, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1
            print(self.arr)
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)

            L = self.arr[low:mid+1]
            R = self.arr[mid+1:high+1]
            i = j = 0
            k = low

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self.arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                self.arr[k] = R[j]
                j += 1
                k += 1

            print(self.arr)
        return self.arr








