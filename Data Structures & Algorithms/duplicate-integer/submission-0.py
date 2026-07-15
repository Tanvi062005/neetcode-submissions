class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set() #sets are unorderd and dont preserve the order so use add instead append
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False