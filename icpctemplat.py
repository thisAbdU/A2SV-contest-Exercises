def main():
    with open('bcount.in', 'r') as f:
        n, q = map(int, f.readline().split())
        arr = [int(f.readline().strip()) for _ in range(n)]
        
        ans = []
        prefix = [(0, 0, 0)]
        

        for _ in range(q):
            l, r = map(int, f.readline().split())

    with open('bcount.out', 'w') as f:
        for i in range(q):
            f.write(f"{ans[i][0]} {ans[i][1]} {ans[i][2]}\n")


if __name__ == "__main__":
    main()