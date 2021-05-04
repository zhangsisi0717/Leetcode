#https://leetcode.com/problems/insert-delete-getrandom-o1/
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_to_val = dict()
        self.val_to_num = dict()
        self.num = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_num:
            return False
        self.val_to_num[val] = self.num
        self.num_to_val[self.num] = val
        self.num +=1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.

        num_to_value = {0:1,1:2}
        value_to_num = {1:0,2:1}

        if we want to move 1, then we find index of 1, which is 0, then we find the last value, which is num_to_value[1]==2
        then we make the index of 2 the same with index of 1, which is 0
                num_to_value = {0:1,1:2}
                value_to_num = {1:0,2:0}

        then, we num_to_value[0] = 2;
        lastly, we remove value_to_num.pop(1)
                   remove num_to_value.pop(last_index)
        """
        if val in self.val_to_num:
            last_value = self.num_to_val[self.num-1]
            pos_of_val = self.val_to_num[val]
            self.val_to_num[last_value] = pos_of_val ##assign position of val to last value
            self.num_to_val[pos_of_val] = last_value
            self.num_to_val.pop(self.num-1)
            self.val_to_num.pop(val)
            self.num -=1
            return True
        return False
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.num_to_val[random.randint(0,self.num-1)]