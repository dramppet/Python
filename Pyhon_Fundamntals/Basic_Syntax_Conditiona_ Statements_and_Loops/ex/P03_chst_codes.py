number_codes = int(input())

for _ in range(number_codes):
    codes = int(input())

    if codes == 88:
        print('Hello')
    elif codes == 86:
        print('How are you?')
    elif codes != 86 and codes < 88:
        print('GREAT!')
    elif codes > 88:
        print('Bye.')
