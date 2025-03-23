from typing import List

def foo(nums: List[int]) -> List[int]:
    product=1
    result=[]
    for i in nums:
        product*=i
    for i in nums:
        result.append(product//i)
    return result

if __name__ == "__main__":
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
