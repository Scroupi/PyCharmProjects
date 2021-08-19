import math
def get_inp():
    while True:
        try:
            print("Time 1  ", end=" ")
            num1M = int(input("Mins: "))
            print("        ",end=" ")
            num1S = int(input("Seconds: "))
            print()
            break
        except ValueError:
            print(" You can enter only numbers, retard!")

    while True:
        sign = input("Sub or add?' - or + ': ")
        if sign == "+" or sign == "-":
            break

    while True:
        try:
            print("Time 2  ", end=" ")
            num2M = int(input("Mins: "))
            print("        ", end=" ")
            num2S = int(input("Seconds: "))
            break
        except ValueError:
            print(" You can enter only numbers, retard!")
        break
    resolver(num1M,num1S,num2M,num2S,sign)

def resolver(num1M,num1S,num2M,num2S,sign):

    if sign == "-":
        res_sec = num1S - num2S
        res_min = num1M - num2M
        if res_sec < 0:
            res_min -= 1
            res_sec = 60 - abs(res_sec)

    if sign == "+":
        res_sec = num1S + num2S
        res_min = num1M + num2M
        if res_sec > 60:
            res_min += 1
            res_sec = res_sec - 60



    print("\nResult: "+str(res_min)+ " " + str(res_sec))