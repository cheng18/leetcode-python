class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # print(nums)
        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1   
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                # print([nums[i], nums[start], nums[end]])
        return ans
