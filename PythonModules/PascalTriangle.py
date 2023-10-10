#the pascal triangle

def pascal_triangle(n):
    triangle = [[1]]
    if n <= 0:
        return []
    else:
        for count in range(1,n):
            previous = triangle[-1]
            next = [1]
            for counter in range(1,count):
                next.append(previous[counter-1] + previous[counter])
            next.append(1)
            triangle.append(next)
        for row in range(len(triangle)):
            print(triangle[row])
        return triangle

pascal_triangle(5)
