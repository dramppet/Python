anagram = input()
count_word = int(input())



for _ in range(count_word):
    word = input()

    if len(anagram) > len(word) or len(anagram) < len(word):
        print('No')
        continue

    for l in sorted(word):
        if l not in anagram:
            print('No')
            break
        else:
            continue
    else:
        print('Yes')