p = int(input())
num_list = list(map(int, input().split()))
num_count = dict()

for i in num_list:
    if i in num_count.keys():
        num_count[i] += 1
    else:
        num_count[i] = 1

for x in num_count.keys():
    if num_count[x] != p:
        print(x)
        break
