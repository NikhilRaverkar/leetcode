class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            dat = target - i
            loc= nums.index(i)
            tmp = nums[loc+1:]
            if dat in tmp :
                return [ loc,tmp.index(dat)+loc+1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
if __name__ =="__main__":
   print( Solution().twoSum([-1,-2,-3,-4,-5],-8))
