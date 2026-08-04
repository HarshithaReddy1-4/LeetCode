class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # maxx, minn = max(nums), min(nums)
        # arr = [0] * 101

        # for i in nums:
        #     arr[i] = i
        
        # res = []
        # for i in range(minn, maxx + 1):
        #     if arr[i] == 0:
        #         res.append(i)
            
        # return res

        s = set(nums)
        return [i for i in range(min(nums), max(nums) + 1) if i not in s]