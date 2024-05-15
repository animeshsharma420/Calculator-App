from cal_fun import do_addition,do_multiplication,do_substraction
from area import cal_area_rec
from devied import do_devied
def main():
    print("press 1 for add 2 for substraction 3 for multiplication and 4 for devied 5 for area")
if __name__ == "__main__":
    main()
user_inpt=input("select the function")
a=int(input("enter first number"))    
b=int(input("enter second number"))

if user_inpt=="1":
    result=do_addition(a,b)
    print("result=",result)

elif user_inpt=="2":
    result=do_substraction(a,b)
    print("result=",result)

elif user_inpt=="3":
    result=do_multiplication(a,b)
    print("result=",result)

elif user_inpt=="4":
    result=do_devied(a,b)
    print("result=",result)
elif user_inpt=="5":
    result=cal_area_rec(a,b)
    print("result=",result)
else:
    print("you enter wrong number")

if __name__ == "__main__":
    main()

   