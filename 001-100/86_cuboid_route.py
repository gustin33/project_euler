import math

def project_euler_86(limit):
    L, count, a = limit, 0, 2

    while count < L:
        a += 1
        
        for bc in range(3, 2 * a):
            if (bc * a) % 12 == 0:
                s = math.sqrt(bc * bc + a * a)
                if s.is_integer():  # Check if s is a perfect square
                    min_value = min(bc, a + 1)
                    count += min_value - (bc + 1) // 2

    return a

if __name__ == "__main__":
    limit = 1000000
    result = project_euler_86(limit)
    print(f"Project Euler 86 Solution = {result}")
