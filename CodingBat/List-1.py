#Problem 1 - first_last6
def first_last6(nums):
  if nums[-1] == 6 or nums[0] == 6:
    return True
  return False

#Problem 2 - same_first_last
def same_first_last(nums):
  if len(nums) >= 1:
    return (nums[0] == nums[-1])
  return False

#Problem 3 - make_pi
def make_pi():
  return [3,1,4]

#Problem 4 - common_end
def common_end(a, b):
  return(a[0] == b[0] or a[-1] == b[-1])

#Problem 5 - sum3
def sum3(nums):
  return(sum(nums))

#Problem 6 - rotate_left3
def rotate_left3(nums):
  """Given an array of ints length 3, return an array with the elements
  rotated left" so {1, 2, 3} yields {2, 3, 1}."""
  x = nums.pop(0)
  nums.append(x)
  return nums

#Problem 7 - reverse3
def reverse3(nums):
  """
  Given an array of ints length 3, 
  return a new array with the elements in reverse order,
  so {1, 2, 3} becomes {3, 2, 1}.
  """
  x = []
  for i in [2,1,0]:
    x.append(nums[i])
  return x

#Problem 8 - max_end3
def max_end3(nums):
  """
  Given an array of ints length 3, figure out which is larger, 
  the first or last element in the array, and set all the other 
  elements to be that value. Return the changed array.
  """
  max = nums[0]
  if nums[-1] > max:
    max = nums[-1]
  nums[0], nums[1], nums[2] = max, max, max
  return nums

#Problem 9 - sum2
def sum2(nums):
  """
  Given an array of ints, return the sum of the first 2 elements in the array. 
  If the array length is less than 2, just sum up the elements that exist, 
  returning 0 if the array is length 0.
  """
  if len(nums) > 1:
    return nums[0] + nums[1]
  else:
    return sum(nums)

#Problem 10 - middle_way
def middle_way(a, b):
  """
  Given 2 int arrays, a and b, each length 3, 
  return a new array length 2 containing their middle elements.
  """
  x = []
  x.append(a[1])
  x.append(b[1])
  return x

#Problem 11 - make_ends
def make_ends(nums):
  """
  Given an array of ints, return a new array length 2 containing the first 
  and last elements from the original array. The original array will be 
  length 1 or more.
  """
  return [nums[0], nums[-1]]

#Problem 12 - has23
def has23(nums):
  """
  Given an int array length 2, return True if it contains a 2 or a 3.
  """
  a, b = nums[0], nums[1]
  return (a == 2 or b == 2 or a == 3 or b == 3)