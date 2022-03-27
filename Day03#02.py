#練習：Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
nums = [2,7,11,15]
target = 9

a = 0
b = 0

for a in range(len(nums)):
  if a == b:
    b += 1
    if nums[a] + nums[b] == target:
      print([a, b])
      break
    elif b == len(nums) - 1:
      a += 1
      b = 0
    else:
      b += 1
