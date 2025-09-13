def twoSum(num, target):
    s=[]
    if num:
        for i in range(len(num)):
            for j in range(len(num)):
                if i!=j and  num[i]==int(num[i]) and num[j]==int(num[j]) and  num[i]+num[j]==target  :
                    return [i,j]

    return None