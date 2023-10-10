def PascalTriangle(p):
    if p <= 0:
        return []
    else:
        triangle = [[1]]
        for a in range(1,p):
            previous = triangle[-1]
            nextcol = [1]

            for t in range(1,a):
                nextcol.append(previous[t-1] + previous[t])
            nextcol.append(1)
            triangle.append(nextcol)
        print(triangle)
        print('\n')

    return triangle

PascalTriangle(5)
