def main():
    with open('bcount.in', 'r') as f:
        n, q = map(int, f.readline().split())
        arr = [int(f.readline().strip()) for _ in range(n)]
        
        ans = []
        prefix = [(0, 0, 0)]
        for i in range(n):
            one = prefix[i][0]
            two = prefix[i][1]
            three = prefix[i][2]

            if arr[i] == 1:
                one += 1
            elif arr[i] == 2:
                two += 1
            else:
                three += 1
            
            prefix.append((one, two, three))


        for _ in range(q):
            l, r = map(int, f.readline().split())
            one, two, three = prefix[r][0] - prefix[l-1][0], prefix[r][1] - prefix[l-1][1], prefix[r][2] - prefix[l-1][2]
            ans.append((one, two, three))

    with open('bcount.out', 'w') as f:
        for i in range(q):
            f.write(f"{ans[i][0]} {ans[i][1]} {ans[i][2]}\n")


if __name__ == "__main__":
    main()
