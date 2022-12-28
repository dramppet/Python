version = [int(x) for x in input().split(".")]

version[-1] += 1
if  version[-1] > 9:
    version[-2] +=1
    version[-1] = 0
    if version[-2] > 9:
        version[-3] += 1
        version[-2] = 0

print(*version,sep=".")