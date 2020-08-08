points = set()
print(points)
count = 0
LIMIT = 50
for x1 in range(LIMIT + 1):
    for x2 in range(LIMIT + 1):
        for y1 in range(LIMIT + 1):
            for y2 in range(LIMIT + 1):
                a2 = x1**2 + x2**2
                b2 = (x1-y1)**2 + (x2-y2)**2
                c2 = y1**2 + y2**2
                a = {(x1, x2), (y1, y2)}
                print(f"a: {a}")
                if (a2 == b2 + c2 or b2 == a2 + c2 or c2 == a2 + b2) and not a in points and (x1, x2) != (0,0) and (y1, y2) != (0,0) and (x1, x2) != (y1, y2):
                    points.add(frozenset(a))
                    count += 1

print(f"count: {count}")
