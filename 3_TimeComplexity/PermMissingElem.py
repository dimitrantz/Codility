'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''
# 30%
def solutionC(A):
    n = len(A) + 1
    nums = (int((n+1)/2))*n
    
    return nums - sum(A)

# 100%
def solution(A):
    if len(A) == 0:
        return 1
    if (len(A) == 1) and (A[0] != 1):
        return 1
        
    n = len(A) + 1
    nums = int(((n+1)/2)*n)
    for num in A:
        nums -= num
    return nums