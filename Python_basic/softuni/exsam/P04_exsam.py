count_student = int(input())

otl = 0.0
mn = 0.0
dob = 0.0
slab = 0.0
sr_ocenka = 0

for _ in range(count_student):
    exsam_oc = float(input())
    sr_ocenka += exsam_oc

    if exsam_oc >= 5.00:
        otl += 1
    elif exsam_oc >= 4.00:
        mn += 1
    elif exsam_oc >= 3.00:
        dob += 1
    else:
        slab += 1

print(f'Top students: {(otl / count_student) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(mn / count_student)*100:.2f}%')
print(f'Between 3.00 and 3.99: {(dob / count_student)*100:.2f}%')
print(f'Fail: {(slab / count_student)*100:.2f}%')
print(f'Average: {sr_ocenka / count_student:.2f}')
