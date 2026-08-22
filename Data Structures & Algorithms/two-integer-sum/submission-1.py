class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iniMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in iniMap:
                return[iniMap[diff], i]
            iniMap[n] = i