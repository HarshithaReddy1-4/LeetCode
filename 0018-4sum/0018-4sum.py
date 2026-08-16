class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                h = n - 1
                while l < h:
                    tar = nums[i] + nums[j] + nums[l] + nums[h]

                    if tar == target:
                        res.append([nums[i], nums[j], nums[l], nums[h]])
                        l += 1
                        h -= 1

                        while l < h and nums[l] == nums[l - 1]:
                            l += 1
                        
                        while  l < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif tar < target:
                        l += 1
                    else:
                        h -= 1
        return res
