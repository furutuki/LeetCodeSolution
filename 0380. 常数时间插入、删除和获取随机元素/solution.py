import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.valToIdx = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.valToIdx.__contains__(val):
            return False
        self.nums.append(val)
        self.valToIdx[val] = len(self.nums) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not self.valToIdx.__contains__(val):
            return False
        target_idx = self.valToIdx[val]
        last_idx = len(self.nums) -1
        self.nums[target_idx], self.nums[last_idx] = self.nums[last_idx], self.nums[target_idx]
        self.valToIdx[self.nums[target_idx]] = target_idx
        del self.nums[last_idx]
        del self.valToIdx[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0,len(self.nums) - 1)]
