def mostFrequent(arr):
    res = {}
    res[arr[0]] = 1
    max = arr[0]
    maxCount = 1

    for i in range(1,len(arr)):
        if arr[i] in res:
            res[arr[i]] = res[arr[i]]+1
        else:
            res[arr[i]] = 1
        
        if res[arr[i]] > maxCount:
            maxCount = res[arr[i]]
            max = arr[i]

    return max

def main():
    arr = input()
    if len(arr)==0:
        return

    arr = arr.split(" ")
    arr = [int(x) for x in arr]

    res = mostFrequent(arr)

    print(res)

if __name__ == "__main__":
    main()