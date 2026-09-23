nums = [1,2,3,3]

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        self.nums = nums
        
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False


hasduplicate = Solution()   
hasduplicate.hasDuplicate(nums)