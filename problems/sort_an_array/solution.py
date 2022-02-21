class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums)
        # self.mergeSort(nums)
        return nums
    
    '''MergeSort'''
    def mergeSort(self, nums):
        def merge(nums,L,R):
            i = j = k = 0
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
                
        if len(nums)>1:
                mid=len(nums)//2
                L=nums[:mid]
                R=nums[mid:]
                self.mergeSort(L)
                self.mergeSort(R)
                merge(nums,L,R)
        
    '''QuickSort'''
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
