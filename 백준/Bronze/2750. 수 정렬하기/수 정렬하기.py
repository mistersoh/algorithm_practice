x = int(input())

nums_list = []

for i in range(x):
    nums_list.append(int(input()))

sorted_list = sorted(nums_list)
for i in range(len(sorted_list)):
    print(sorted_list[i])