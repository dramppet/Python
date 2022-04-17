n=int(input())
n=str(n)
single_digit=['one','two','three','four','five','six','seven','eight','nine']
tens_digit=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
double_digit=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]
if len(n)==1:
    n=int(n)
    print(single_digit[n-1].capitalize())
elif len(n)==2:
    n=int(n)
    if n<20:
        print(tens_digit[n-10].capitalize())
    elif n>19:
        a=str(n)
        first_digit=int(a[0])
        second_digit=int(a[1])
        print(double_digit[first_digit-2].capitalize(),single_digit[second_digit-1])
elif len(n)==3:
    n=int(n)
    a=str(n)
    first_digit=int(a[0])
    second_digit=int(a[1])
    third_digit=int(a[2])
    print(single_digit[first_digit-1].capitalize(),'hundred','and', double_digit[second_digit-2],single_digit[third_digit-1])