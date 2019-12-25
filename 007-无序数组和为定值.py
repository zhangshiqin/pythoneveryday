
# 6sum问题
def Sum6(arr, target):
    res = []
    for i, value1 in enumerate(arr):
        for j, value2 in enumerate(arr[i + 1:]):
            for k, value3 in enumerate(arr[i + 2:]):
                for g, value4 in enumerate(arr[i + 3:]):
                    for j, value5 in enumerate(arr[i + 4:]):
                        if (target - value1 - value2 - value3 - value4 - value5) in arr[i+4:]:
                            tmp = [value1, value2, value3, value4, value5, target - value1 - value2 - value3 - value4 - value5]
                            tmp.sort()
                            res.append(tuple(tmp))
    res = list(set(res))
    print(res)
 
if __name__ == '__main__':
    arr = [int(i) for i in range(5,30)]
    target = 100
    Sum6(arr, target)
