for num in range(0,100):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print(num,"khong phai so nguyen to")
            break
        else:
            print(num,"la so nguyen to")
