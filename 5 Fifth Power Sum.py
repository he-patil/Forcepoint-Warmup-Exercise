def findSum(num,power):
    sum = 0
    while num>0 :
        digit = num%10
        sum+= digit**power
        num= int(num/10)
    
    return sum

def main():
    sum = 0
    power = 6
    
    powerVal = 9**power
    digits = 1
    upperBound = powerVal

    while len(str(upperBound)) > digits:
        upperBound+=powerVal
        digits+=1
        #print(upperBound)

    for i in range(10,upperBound+1):
        if i == findSum(i,power):
            sum+=i

    print(sum)

if __name__ == "__main__":
    main()