# try:
#     print("try block")
#     num1=int(input("enter first number"))
#     num2=int(input("enter another number"))
#     res=num1/num2
# except:
#     print("execpt block")
#     print("number 1 is not divisible by zerp")
# else:
#     print("Else block")
#     print("output ",res)
# finally:
#     print("exceptions handling program")
try:
    a=int(input("Enter Your Age:"))
    if a<18:
        raise ValueError(a)
except ValueError:
    print(a, "Is less than 18")
else:
    print(a, "Is allowed")
        