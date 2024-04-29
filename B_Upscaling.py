def upscaling(n):
    arr = [["0" for i in range( 2 *n)] for j in range(2 *n)]
    for i in range(0, len(arr), 2):
        for j in range(0, len(arr), 2):
            arr[i][j] = "#"
            arr[i][j+1] = "#"
        arr[i + 1][j] = "#"
        
    print(arr)

n =  int(input())
upscaling(n)
