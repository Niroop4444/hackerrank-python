n = int(input())
arr = map(int, input().split())

unique_sorted = sorted(set(arr), reverse=True)
print(unique_sorted[1])