'''
equal stacks
https://www.hackerrank.com/challenges/equal-stacks/problem
'''

# Example
# # Python program to  
# # demonstrate stack implementation 
# # using list 
  
  
# stack = [] 
  
# # append() function to push 
# # element in the stack 
# stack.append('a') 
# stack.append('b') 
# stack.append('c') 
  
# print('Initial stack') 
# print(stack) 
  
# # pop() fucntion to pop 
# # element from stack in  
# # LIFO order 
# print('\nElements poped from stack:') 
# print(stack.pop()) 
# print(stack.pop()) 
# print(stack.pop()) 
  
# print('\nStack after elements are poped:') 
# print(stack) 
  
# # uncommenting print(stack.pop())   
# # will cause an IndexError  
# # as the stack is now empty 

def equalStacks(s1, s2, s3):
    while not all(elem == sum(s1) for elem in [sum(s1),sum(s2),sum(s3)]):
        sums = [sum(s1),sum(s2),sum(s3)]
        stackIdx = sums.index(max(sums))
        if stackIdx == 0:
            s1.pop(0)
        elif stackIdx == 1:
            s2.pop(0)
        elif stackIdx == 2:
            s3.pop(0)
    sums = [sum(s1),sum(s2),sum(s3)]
    return sum(s1)


a = [3,3,2,1,1,1]
b = [3,4,3,2]
c = [3,1,1,4,1]

s = equalStacks(a,b,c)

print(s)