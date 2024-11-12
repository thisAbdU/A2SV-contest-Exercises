
def main():
    with open('hps.in', 'r') as f:
        n = int(f.readline().strip())

        hoof, paper, siscor = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

        for i in range(1, n + 1):
            hoof[i], paper[i], siscor[i] = hoof[i - 1], paper[i - 1], siscor[i - 1]
            game = f.readline().strip()
            if game == 'H':
                paper[i] += 1
            elif game == 'P':
                siscor[i] += 1
            elif game == 'S':
                hoof[i] += 1

        max_win = 0
        for i in range(n + 1):
            bf = max(hoof[i], paper[i], siscor[i])
            af = max(hoof[n] - hoof[i], paper[n] - paper[i], siscor[n] - siscor[i])
            max_win = max(max_win, af + bf)

        print(max_win)

    with open('hps.out', 'w') as f:
            f.write(str(max_win))


if __name__ == "__main__":
    main()