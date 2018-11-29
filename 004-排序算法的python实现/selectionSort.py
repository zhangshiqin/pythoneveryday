# 参考：https://mp.weixin.qq.com/s/lwMPKTsni93px4zdS9jDTQ
# 排序方法：选择排序

# 排序算法的逻辑非常简单，首先搜索整个列表，找到最小项的位置，如果该位置不是列表的第1项，就交换这两个位置的元素。然后从列表的第2个元素开始，
# 重复上述过程，直到算法达到整个过程的最后一个位置

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