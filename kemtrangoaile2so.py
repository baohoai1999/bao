while True:
    try:
        a = int(input("Nhap so a ---> "))
        b = int(input("Nhap so b ---> "))
        kq = a/b
    except:
        print("Xay ra loi, moi ban nhap lai!")
    else:
        break
print("Gia tri phan so a/b la ---> ",kq)
