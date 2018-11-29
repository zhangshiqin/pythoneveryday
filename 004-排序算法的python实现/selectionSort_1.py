# 排序方法：二元选择排序法（选择排序改进）
# 选择排序法每轮只找最小值，效率较低，可以考虑每次同时寻找最小值和最大值，并且在某一轮如果最小值与最大值相同，说明剩下的数字都相同，可以直
# 接结束。
# 此外，与选择排序不同的是，需要考虑到如果第i轮里，恰好第i个数就是最大值时，先交换minindex和i之后，最大值的下标变成了minindex，这时候应
# 该交换minindex和n-i-1，而不是maxindex和n-i-1。代码如下

def swap(x,i,j):
   """
   交换x的i,j位置元素
   """
   temp = x[i]
   x[i] = x[j]
   x[j] = temp

def selectionSort_1(x):
    i = 0
    while i <= len(x) // 2:
        minindex = i
        maxindex = i
        j = i + 1
        while j < len(x) - i:
            if x[minindex] > x[j]:
                minindex = j
            if x[maxindex] <x[j]:
                maxindex = j
            j += 1
        if x[minindex] == x[maxindex]:
            print(x)
        if minindex != i:
            swap(x,i,minindex)
        if maxindex != len(x) - 1 - i:
            if maxindex != i:
                swap(x,len(x) - 1 - i, maxindex)
            else:
                swap(x,len(x) - 1 - i, minindex)
        i += 1
    print(x)

if __name__ == '__main__':
   x = input("请输入：") #4,1,3,6,2,8
   results =  [int(i) for i in x.split(',')]
   selectionSort_1(results)  #[1,2,3,4,6,8]