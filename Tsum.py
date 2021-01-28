def matrixTSum(n, mat):
    total = sum(mat[0])
    for row in mat[1:n]:
        middleNumOfRow = int(n//2)
        total += row[middleNumOfRow]
    return total


def main():
    n = int(input().strip())
    mat = []
    for _ in range(n):
        row = list(map(int, input().strip().split(' ')))
        mat.append(row)
    tSum = matrixTSum(n, mat)
    print(tSum)


if __name__ == "__main__":
    main()
