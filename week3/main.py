# a = int(input())
# b = int(input())

# while b != 0:
#     a, b = b, a % b

# print(a)

arr = [i for i in range(10)]
target = 11

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found target {target} at index {i}")
        break

else:
    print(f"Target {target} not found in the array")