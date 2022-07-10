def roundOff(num):

    if (num*10)%10 > 5:
        return int(((num*10)+(10-(num*10))%10)/10)

    else:
        return int(((num*10)-(num*10)%10)/10)

def main():
    num = float(input())
    num = roundOff(num)
    print(num)

if __name__ == "__main__":
    main()