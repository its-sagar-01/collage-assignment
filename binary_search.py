def bubblesort(bubble):
    for i in bubble:
        for j in range(len(bubble)-i-1):
            if bubble[j] > bubble[j+1]:
                bubble[j], bubble[j+1] = bubble[j+1], bubble[j]
    return bubble
                
def binarysearch(bubble, key,low, high):
    mid = (high + low)//2
    if bubble[mid] == key:
        return True
    elif bubble[mid] < key:
        return binarysearch(bubble, key, mid + 1, high)
    else:
        return binarysearch(bubble, key, low, mid - 1)

n = int(input("Enter the number of elements: "))
bubble = []
for i in range(n):
    bubble.append(int(input("Enter the element: ")))

key = int(input("Enter the number you find: "))
bubble = bubblesort(bubble)
low, high = 0, n-1
x = binarysearch(bubble, key, low, high)
if x == True:
    print(f"{key} is present in the list")
else:
    print(f"{key} is not present in the list")