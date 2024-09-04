class Check:
    def __init__(self,number):
        self.num = number

    def isArmstrong(self):
        temp = self.num
        res = 0

        while(temp != 0):
            rem = temp%10
            res += rem**3
            temp //= 10

        if self.num == res:
            print(self.num,"is a Armstrong number")
        else:
            print(self.num,"is not a Armstrong number")

if __name__ == "__main__":
    num = int(input("Enter a number :"))
    check_Armstrong = Check(num)
    check_Armstrong.isArmstrong()
    
