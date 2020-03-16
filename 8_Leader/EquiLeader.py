import random 

def solution(A):
    if len(A) == 0:
        return []
    
    indices = []
    for i in range( len(A)):
        if sum(A[:i]) == sum(A[i+1:]):
            #return i
            indices.append(i)
            
    #in case you want return them all
    if len(indices):
        return indices
    return -1

def equ(A):
    if len(A) == 0:
        return []
    indices = []
    sum_r = sum(A)
    sum_l = 0

    for i in range(len(A)):
        sum_r -= A[i]
        if sum_r == sum_l:
            #return i
            indices.append(i)
        sum_l +=A[i]

    #in case you want return them all
    if len(indices):
        return indices
    return -1
    
    



if __name__ == "__main__":

    
    #A = [-1, 3, -4, 5, 1, -6, 2, 1]
    #A = random. sample(range(-10, 30), 10)
    A = [1 , -1, 2, -2, 3, -3, 4, -4, 1]
    print (A)
    print(solution(A))
    print(equ(A))
