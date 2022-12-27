def loading_bar(num):
    if num == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f"{num}% [{'%' * (num //10) }{'.' * (10 -num//10)}]")
        print('Still loading...')


number = int(input())

loading_bar(number)