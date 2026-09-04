class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        arr=[[] for n in range(len(nums)+1)]
        res=[]
        for n in nums:
            d[n]=d.get(n,0)+1
        for key,val in d.items():
            arr[val].append(key)
        for i in range(len(arr)-1,0,-1):
            res.extend(arr[i])
            if len(res)==k:
                return res
