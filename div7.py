def main():
    with open('div7.in', 'r') as f:
        arr = [0]
        for i in range(int(f.readline().strip())):
            arr.append((int(f.readline().strip()) + arr[i]) % 7)

        max_len = 0
        occr = {}
        for indx, i in enumerate(arr):
            if i not in occr:
                occr[i] = indx
            else:
                max_len = max(max_len, indx - occr[i])

    with open('div7.out', 'w') as f:
        f.write(str(max_len) + '\n')


if __name__ == "__main__":
    main()