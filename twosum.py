from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        found = False
        head = 0
        tail = 1
        while head < len(nums) and not found:
            while tail < len(nums) and not found:
                test = nums[head] + nums[tail]
                if test == target:
                    found = True
                else:
                    tail += 1
            head += 1         
        return [nums[head], nums[tail]]

print(twoSum([2,7,11,15], 6))
#print(twoSum([3,2,4], 6))
#print(twoSum([3,3], 6))


