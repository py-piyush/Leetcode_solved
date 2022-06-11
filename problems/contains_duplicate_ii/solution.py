class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m={}
        for i,n in enumerate(nums):
            if n in m and abs(i-m[n])<=k:
                return True
            else:
                m[n]=i
        return False