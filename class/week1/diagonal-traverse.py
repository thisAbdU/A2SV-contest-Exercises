class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        matIndx = {}
        output = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i + j
                if key in matIndx:
                    matIndx[key].append(mat[i][j])
                else:
                    matIndx[key] = [mat[i][j]]

        for key in matIndx:
            if key%2 != 0:
                output.extend(matIndx[key])
            else:
                nums = matIndx[key]
                output.extend(nums[::-1])
        return output