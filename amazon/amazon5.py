'''
array left rotation
'''

def leftRotation(arr, rot):
    for _ in range(rot):
        num = arr.pop(0)
        arr.append(num)
    return arr

if __name__ == "__main__":
    myList = [1,2,3,4,5,6,7,8,9]
    print(myList)

    myList = leftRotation(myList, 5)

    print(myList)