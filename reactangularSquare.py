from itertools import product


def rectangularSquare(n, wall, queries):
    result = []
    for query in queries:
        x, y, l, b = query
        x1 = list(range(x-l, x+l+1))
        y1 = list(range(y-b, y+b+1))

        # using list comprehension...[(a,b) for a in x1 for b in y1]
        cells = list(product(x1, y1))

        cost = 0
        for a, b in cells:
            cost += wall[a][b]

        result.append(cost)

    return result


if __name__ == "__main__":
    n = int(input())
    cost = []
    query = []
    for _ in range(n):
        row = list(map(int, input().strip().split(' ')))
        cost.append(row)

    q = int(input())
    for _ in range(q):
        row = list(map(int, input().strip().split(' ')))
        query.append(row)

    result = rectangularSquare(n, cost, query)
    print(result, sep="\n")
