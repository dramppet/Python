encoded_message = input().split()

decoding_message = []

for message in encoded_message:
    if len(message) >= 3:
        decoding_message.append(chr(ord(message[0]) + 1))
        decoding_message.append(len(message) - 2)
        decoding_message.append(chr(ord(message[-1]) + 1))
        decoding_message.append(" ")
    else:
        decoding_message.append(message)

for el in decoding_message:
    print(el,end='')




