def main():
    with open('maxcross.in', 'r') as f:
        n, k, b = map(int, f.readline().split())
        broken_lights = [int(f.readline().strip()) for _ in range(b)]

        is_broken = [0] * (n + 1)
        for light in broken_lights:
            is_broken[light] = 1


        current_broken = sum(is_broken[1:k+1])
        min_broken = current_broken

        for i in range(2, n - k + 2):
            current_broken = current_broken - is_broken[i - 1] + is_broken[i + k - 1]
            min_broken = min(min_broken, current_broken)

    with open('maxcross.out', 'w') as f:
            f.write(str(min_broken))


if __name__ == "__main__":
    main()