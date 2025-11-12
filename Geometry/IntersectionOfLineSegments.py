def orientation(o, a, b):
    value = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    if value == 0:
        return 0

    return 1 if value > 0 else 2

def on_segment(a, b, c):
    on_x = min(a[0], c[0]) <= b[0] <= max(a[0], c[0])
    on_y = min(a[1], c[1]) <= b[1] <= max(a[1], c[1])

    return on_x and on_y

def intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

print(intersect((1, 1), (10, 1), (1, 2), (10, 2)))
print(intersect((10, 0), (0, 10), (0, 0), (10, 10)))
print(intersect((0, 0), (10, 10), (5, 5), (15, 15)))
print(intersect((0, 0), (5, 5), (6, 6), (10, 10)))

