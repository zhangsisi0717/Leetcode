a=[-1,-3,10,1,-1,-1,3]

##DP solution: maxsum ending at index i == max_sum ending at index i-1 + array[i] (if sum_ending_at index[i-1] + array[i] > array[i])
##             maxsum ending at index i == array[i] (else: sum_ending_at index[i-1] + array[i] <= array[i] )

def maxSubArray(a): ##Kadane's algorithm
    cur_max = a[0]
    global_max = a[0]
    for i in range(1,len(a)):
        print(i)
        cur_max = max(a[i],cur_max+a[i])
        if cur_max > global_max:
            global_max = cur_max
        print(f"cur_max = {cur_max}")
        print(f"global_max = {global_max}")
    return global_max

maxSubArray(a)