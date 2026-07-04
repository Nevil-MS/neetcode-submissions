class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} # val : index
        for i, num in enumerate(nums):
            diff = target - num     # getting the compliment
            if diff in hmap:        # checking if compliment already in hashmap
                return [hmap[diff], i] 

            hmap[num] = i   # updating hash map
