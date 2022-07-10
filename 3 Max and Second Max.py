def findMax(arr):
    max1 = arr[0] if arr[0]>arr[1] else arr[1]
    max2 = arr[0] if arr[0]<arr[1] else arr[1]

    for i in range(2,len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    return max1, max2

def main():
    arr = input()
    if len(arr)==0:
        return

    arr = arr.split(" ")
    arr = [int(x) for x in arr]

    if len(arr)==1:
        print(str(arr[0])+" & "+str(arr[0]))
        return

    max1, max2 = findMax(arr)

    print(str(max1)+" & "+str(max2))

if __name__ == "__main__":
    main()