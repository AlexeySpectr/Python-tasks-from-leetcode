nums = [3,2,2,3]
val=3
k=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
print(k)
print(len(nums))


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         i = len(nums)
#         while val in nums:
#             nums.remove(val)
#             k += 1
#         k = i - k