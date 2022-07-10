def reverse(arr):
    #arr = list(arr)

    for i in range(0,int(len(arr)/2)):
        #arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
        arr = arr[0:i] + arr[len(arr)-1-i] + arr[i+1:len(arr)-1-i] + arr[i] + arr[len(arr)-i:len(arr)]

    #arr = ''.join(arr)
    return arr

def main():
    arr = input()
    arr = reverse(arr)
    print(arr)

if __name__ == "__main__":
    main()