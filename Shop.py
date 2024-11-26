import os
import time
print(100 * '*')
print('1.Start')
print('2.Exit')
s = int(input('Enter your number: '))
os.system('cls')
if s == 1 :
    print(100 * '*')
    print('Welcome to shop')
    time.sleep(5)
    os.system('cls')
else :
    print(100 * '*')
    print('Goodby')
    time.sleep(5)
    quit()
i = 0
ii = 3

cart = []
while i < 100000 :
    xx = 'true'
    print(100 * '*')
    print("1.List of goods")
    print("2.Ruler")
    print("3.Admin")
    print("4.Cart")
    print("5.Exit")
    print(100 * '*')
    d = int(input('Enter your number: '))
    if d == 3:
        iii = 0
        iiii = 1
        print(100 * '*')
        admin = input("Enter your UserName: ")
        file = open("UserName.txt" , "r")
        content = file.read()
        sama = content.split('\n')
        while iii < len(sama):
            if admin == sama[iii]:
                admin_password = input('Enter your password please: ')
                print(100 * '*')
                file1 = open("Password.txt" , "r")
                content1 = file1.read()
                sama1 = content1.split('\n')
                while iiii < len(sama1):
                    if admin_password == sama1[iiii]:
                        print('Welcome admin : ' , sama[iii] )
                        iiii = iiii + len(sama1)
                    else:
                        iiii = iiii + 2
                iii = iii + len(sama)
            else:
                iii = iii + 1
        file.close()
    if d == 4:
        fd = 1
        x = 0
        for fff in range(len(cart)):
            print(fd , ':', cart[x])
            x = x + 1
            time.sleep(5)
            fd = fd + 1
        gg = input("Do you want to order less from your shopping cart (Y or N) ? ")
        if gg == 'y' or gg == 'Y':
            ggg = int(input("Which one do you want to delete (by number):  "))
            ggg = ggg - 1
            if ggg <= len(cart):
                cart.pop(ggg)
            if ggg > len(cart):
                print('Please write a number beeween these numbers (0 :' , len(cart) , ')' )
        else :
            continue
    if d == 1 and xx == 'true':
        while xx == 'true':
            sss = 1
            print(100 * '*')
            ss = 0
            file2 = open("Shop.txt" , "r")
            content2 = file2.read()
            sama2 = content2.split('\n')
            for _ in range(len(sama2)):
                print(sss , ':' , sama2[ss])
                ss = ss + 1
                sss = sss + 1
            print(100 * '*')
            dd = int(input('Enter your number: '))
            if 0 < dd <= len(sama2):
                cart.append(sama2[dd - 1])
                print('Your order has been successfully registered and you can see your order in the shopping cart section.')
                time.sleep(5)
                s = input('Do you have another order (Y or N) ? ')
                if s == 'Y' or s == 'y':
                    continue
                if s == 'n' or s == 'N':
                    xx = 'False'
    if d == 5:
        print(100 * '*')
        print('Goodby')
        time.sleep(5)
        quit()
    if d == 2:
        while ii >= 1:
            print(100 * '*')
            username = input('Enter your UserName: ')
            if username == 'SajjadDavoodi':
                password= input('Enter your Pasword: ')
                if password == '0929273826sS':
                    print("Hello Ruler")
                    time.sleep(5)
                    os.system('cls')
                    rs = 'True'
                    while rs == 'True':
                        print(100 * '*')
                        print('1.Edit product list')
                        print('2.Add admin')
                        print('3.Total buyers')
                        print(100 * '*')
                        divid = int(input("Please Enter your number: "))
                        print(100 * '*')
                        if divid == 1:
                            ff = 0
                            file3 = open("Shop.txt" , "r")
                            content3 = file3.read()
                            sama3 = content3.split('\n')
                            for _ in range(len(sama3)):
                                print(sama3[ff])
                                ff = ff + 1
                        print(100 * '*')
                        print('Do your editing boss')
                        sol = input()
                        file1 = open("Shop.txt" , "w")
                        file1.write(sol)
                        file1.close()
                        print("The edit was successfully registered!")
                        print(100 * '*')
                        time.sleep(5)
                        os.system('cls')
                        print('1.Exit the program')
                        print('2.Return to the main page of the panel')
                        print(100 * '*')
                        fdd = int(input("Enter your number: "))
                        if fdd == 1:
                            print("Goodby!")
                            time.sleep(5)
                            quit()
                        elif fdd == 2:
                            continue
                else:
                    print("Password is not corect")
                    ii = ii - 1
                    print('Number of login attempts: ' , ii)
            else:
                print("UserName is not corect")
                ii = ii - 1
                print('Number of login attempts: ' , ii)


    file1 = open("Shop.txt" , "w")
file1.write("Hello!!")
file1.close()
    

