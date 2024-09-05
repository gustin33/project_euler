import itertools
import sys
import time

def figurate_number(sides, n):
    """Generate a figurate number based on the number of sides and index."""
    return n * ((sides - 2) * n - (sides - 4)) // 2

def build_numbers():
    """Build a table of 4-digit figurate numbers."""
    print("Building table of figurate numbers...")
    numbers = [[set() for _ in range(100)] for _ in range(9)]
    for sides in range(3, 9):
        print(f"Generating {sides}-sided figurate numbers...")
        for n in itertools.count(1):
            num = figurate_number(sides, n)
            if num >= 10000:
                break
            if num >= 1000:
                numbers[sides][num // 100].add(num)
    return numbers

def find_solution_sum(begin, current, sidesused, total_sum, numbers):
    """Recursively find a cyclic figurate number set."""
    if sidesused == 0b111111000:  # All figurate types used
        if current % 100 == begin // 100:
            print(f"Cycle found with sum: {total_sum}")
            return total_sum
    else:
        for sides in range(4, 9):
            if (sidesused >> sides) & 1 != 0:
                continue
            for num in numbers[sides][current % 100]:
                sys.stdout.write(f"\rExploring: current={current}, num={num}, sidesused={bin(sidesused)}")
                sys.stdout.flush()
                result = find_solution_sum(begin, num, sidesused | (1 << sides), total_sum + num, numbers)
                if result is not None:
                    return result
        return None

def compute():
    """Compute the cyclic figurate numbers of the given cycle length."""
    numbers = build_numbers()

    print("Starting search for cyclic figurate numbers...")
    # Do search
    for i in range(10, 100):
        sys.stdout.write(f"\rChecking numbers starting with {i}...")
        sys.stdout.flush()
        for num in numbers[3][i]:
            sys.stdout.write(f"\rStarting search with number: {num}")
            sys.stdout.flush()
            result = find_solution_sum(num, num, 1 << 3, num, numbers)
            if result is not None:
                return str(result)
    raise AssertionError("No solution found")

if __name__ == "__main__":
    print(compute())
