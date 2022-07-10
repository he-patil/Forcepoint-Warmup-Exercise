def find(arr):
    res = {}

    for i in range(0,len(arr)):
        if arr[i] in res:
            res[arr[i]] = res[arr[i]]+1
        else:
            res[arr[i]] = 1

    return res

def main():
    arr = input()
    if len(arr)==0:
        return

    arr = arr.split(" ")
    arr = [int(x) for x in arr]

    res = find(arr)

    print(res)

if __name__ == "__main__":
    main()