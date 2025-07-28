N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
# arr_1 = [item for item in data_1]

for index in range(N):
    arr_1.append(data_1[index])
print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

arr_2 = data_2.split()
for item in arr_2:
    if int(item) % 2 != 0:
        print(item)
    