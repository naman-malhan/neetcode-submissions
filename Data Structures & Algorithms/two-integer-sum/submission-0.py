class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## Brute force approach

        # if len(nums) == 0: return [];
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         print(nums[i] + nums[j], "i +j")
        #         if(nums[i] + nums[j] == target):
        #             return [i, j]
        # return []

        ## Optimised Approach 

        myDict = {};
        for i in range(len(nums)):
            if(target - nums[i]) in myDict:
                return [myDict[target - nums[i]], i]
            myDict[nums[i]] = i
        
        return []