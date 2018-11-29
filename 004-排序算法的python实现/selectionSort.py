
def swap(x,i,j):
   """
   交换x的i,j位置元素
   """
   temp = x[i]
   x[i] = x[j]
   x[j] = temp

def selectionSort(x):
   i = 0
   while i < len(x) - 1 :
      minindex = i
      j = i + 1
      while j < len(x):
         if x[minindex] > x[j] :
            minindex = j
         j += 1
      if minindex != i :
         swap(x,i,minindex)
      i += 1
   print(x)

if __name__ == '__main__':
   x = input("请输入：") #4,1,3,6,2,8
   results =  [int(i) for i in x.split(',')]
   selectionSort(results)  #[1,2,3,4,6,8]