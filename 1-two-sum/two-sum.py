class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map={}
        for index,value in enumerate(nums):
            compliment=target-value
            if compliment in prev_map:
                return(prev_map[compliment],index)
            prev_map[value]=index
        return []
            
        