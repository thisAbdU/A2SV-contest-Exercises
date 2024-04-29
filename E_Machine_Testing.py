# def machine_testing(health, power):
def machine_testing(health, power):
    time = 0
    while sum(health) > health[0]:
        for i in range(1, len(health)):
            health[i] -= power[i - 1]
            if health[i] < 0:
                health[i] = 0
                power[i] = power[i - 1]
        time += 1
    return time

test = int(input())
for t in range(test):
    health = list(map(int, input().split()))
    power = list(map(int, input().split()))
    print(machine_testing(health, power))
    