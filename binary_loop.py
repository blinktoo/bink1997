def binart(value,key):
    left = 0
    right = len(value)-1
    while left<=right:
        middle = (left+right)//2
        if value[middle] == key:#查找成功，返回下标
            return middle
        elif value[middle]<key:#在右侧继续查找
            left = middle+1
        else:#则再左侧继续查找
            right = middle-1
    return -1