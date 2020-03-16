import random 

def solution(A):
    if len(A) == 0:
        return -1

    num = int(len(A)/2 )
    for i in range(int(len(A)/2)):
        if A[i] == A[i+num]:
            return A[i]
    return -1 


if __name__ == "__main__":

    fives = [5]*6
    B = [1, 3, 2]
    C = [4]
    A = B + fives + C
    #A = [2, 2, 2, 2, 2, 1, 4, 5, 6, 8]
    #A = random. sample(range(-10, 30), 10)
    #A = [1 , 1, 1, 1, 50]
    print(solution(A))