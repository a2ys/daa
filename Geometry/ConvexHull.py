def ConvexHull(points):
    points = sorted(points, key=lambda p: (p[1], p[0]))
    p0 = points[0]

    import math
    def angle(p):
        return math.atan2(p[1] - p0[1], p[0] - p0[0])

    points = sorted(points, key=angle)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    hull = []
    for p in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()

        hull.append(p)

    return hull

pts = [(0,0),(1,1),(2,2),(2,0),(1,2),(0,2)]
print(ConvexHull(pts))

