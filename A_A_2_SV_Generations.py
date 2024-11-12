n = int(input())
gen = list(map(int, input().split()))

gen.sort()

print(gen[len(gen)//2])