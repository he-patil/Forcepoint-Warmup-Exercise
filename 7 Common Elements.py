def findCommon(arr1,arr2):
    commonArr = []

    i = 0
    j = 0

    while i < min(len(arr1),len(arr2)) and j < min(len(arr1),len(arr2)):
        if arr1[i] == arr2[j]:
            commonArr.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else :
            j+=1

    return commonArr

def main():
    arr1 = input()
    arr2 = input()

    if len(arr1)==0 or len(arr2)==0:
        return

    arr1 = arr1.split(" ")
    arr1 = [int(x) for x in arr1]
    
    arr2 = arr2.split(" ")
    arr2 = [int(x) for x in arr2]

    res = findCommon(arr1, arr2)

    print(res)

if __name__ == "__main__":
    main()