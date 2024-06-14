
#Average
class Solution1(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(0, len(nums)):
            while self.scanList(i, nums):
                nums[i] += 1
                counter += 1
        return counter
    
    def scanList(self, i, nums):
        for j in range(0, len(nums)):
            if nums[i] == nums[j]:
                if i != j:
                    return True
        return False
    
# Fast
class Solution2(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        nums.sort()
        
        for i in range (1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i] + 1
                nums[i] += increment
                counter += increment
                
        
        return counter
    

# Fastest
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()
        
        counter = 0
        next_unique = nums[0]

        # Iterate through the array
        for num in nums:
            if num < next_unique:
                counter += next_unique - num
            next_unique = max(next_unique, num) + 1

        return counter



        

if __name__ == '__main__':
    sol = Solution()
    A = [3,2,1,2,1,7]
    res = sol.minIncrementForUnique(A)
    print(res)