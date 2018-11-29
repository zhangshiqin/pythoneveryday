# 冒泡排序
# 冒泡排序从列表的开头处开始，逐个比较一对数据项，如果顺序不对就交换两项位置，直到移动到列表的末尾。这个过程的效果就是将最大的项以冒泡的
# 方式排到算法的末尾。然后算法从列表开头到倒数第二项重复这一过程，依次类推

def swap(x,i,j):
   """
   交换x的i,j位置元素
   """
   temp = x[i]
   x[i] = x[j]
   x[j] = temp

def BubbleSort(x):
    j = len(x) - 1
    while j > 0:
        i = 0
        while i < j:
            if x[i] > x[i + 1]:
                swap(x,i,i+1)
            i += 1
        j -= 1
    print(x)

if __name__ == '__main__':
   x = input("请输入：") #4,1,3,6,2,8
   results =  [int(i) for i in x.split(',')]
   BubbleSort(results)  #[1,2,3,4,6,8]