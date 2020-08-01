'''
Task:
Write a function that receives two sequences: A and B of integers and returns one sequence C. Sequence C should contain all elements from sequence A (maintaining the order) except those, that are present in sequence B p times, where p is a prime number.

Example:
A=[2,3,9,2,5,1,3,7,10]
B=[2,1,3,4,3,10,6,6,1,7,10,10,10]
C=[2,9,2,5,7,10]
'''

# the function from Task
def MyFunction(A: list, B: list):
    # Create a dictionary with num of repetitions for every number in list B 
    reps = {}
    for b in B:
        if str(b) in reps:
            reps[str(b)] += 1
        else:
            reps[str(b)] = 1
    
    # Iterate over list A and 
    C = []
    for a in A:
        if not isPrime(reps.get(str(a), 0)): C.append(a)

    return C

# function that checks if x is a prime number
def isPrime(x):
    # if x is equal to two return True. If x is smaller than two return False
    if x < 3: return x >= 2

    # if x is even return false:
    if x % 2 == 0: return False

    for n in range(3, x):
        if x % n == 0:
            return False

    return True


if __name__ == "__main__":
    A=[2,3,9,2,5,1,3,7,10]
    B=[2,1,3,4,3,10,6,6,1,7,10,10,10]

    C = MyFunction(A, B)

    print(C)
