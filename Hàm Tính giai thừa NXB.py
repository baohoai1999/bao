def giaithua(n):
    #Tính giai thừa 1 số nhập từ bàn phím
    if n==1:
       return 1
    else:
       return (n*giaithua(n-1))
num=int(input("nhập số cần tính thứ 1 ! :"))
num1=int(input("nhập số cần tính thứ 2  ! :"))
num2=int(input("nhập số cần tính thứ 3 ! :"))
print("Giai thừa của ",num,"và",num1,"và",num2,"là",giaithua(num),'và',giaithua(num1),'và',giaithua(num2))
