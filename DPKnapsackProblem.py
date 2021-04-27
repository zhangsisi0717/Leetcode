def knapsack(weight,value,capacity):

    """
    :param capacity_left: current capacity of the bag
    :param index: consider items[:index+1], first index items
    :return: consider first index items, the maxium value we can get at current capacity
    """
    def dfs(capacity_left,index):
        if capacity_left < 0:
            return -float("inf")

        if capacity_left ==0 or index<0:
            return 0

        x1 = dfs(capacity_left,index-1)  ##not include item[index]
        x2 = dfs(capacity_left-weight[index],index-1) + value[index] ##include item[index]

        return max(x1,x2)

    return dfs(capacity,len(weight)-1)

value = [ 20, 5, 10, 40, 15, 25 ]
weight = [ 1, 2, 3, 8, 7, 4 ]
capacity = 10

knapsack(weight,value,capacity)
