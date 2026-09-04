class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res not in d:
                d[nums[i]]=i
            else:
                return [d[res],i]