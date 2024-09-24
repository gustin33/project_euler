import itertools

# Possible arithmetic operations
operations = ['+', '-', '*', '/']

# Generate all possible arithmetic expressions
def apply_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else None

# Evaluate all possible expressions with four digits and return results with expressions
def evaluate_expressions_with_expressions(digits):
    results = {}
    # Permutations of the digits
    for perm in itertools.permutations(digits):
        a, b, c, d = perm
        
        # Add parentheses in all possible ways
        # ((a op b) op c) op d
        for op1, op2, op3 in itertools.product(operations, repeat=3):
            try:
                expr = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
                res = apply_operation(apply_operation(apply_operation(a, b, op1), c, op2), d, op3)
                if res is not None and res == int(res) and res > 0:
                    results[int(res)] = expr
            except:
                pass
            
            # (a op (b op (c op d)))
            try:
                expr = f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
                res = apply_operation(a, apply_operation(b, apply_operation(c, d, op3), op2), op1)
                if res is not None and res == int(res) and res > 0:
                    results[int(res)] = expr
            except:
                pass

            # (a op b) op (c op d)
            try:
                expr = f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
                res = apply_operation(apply_operation(a, b, op1), apply_operation(c, d, op3), op2)
                if res is not None and res == int(res) and res > 0:
                    results[int(res)] = expr
            except:
                pass

    return results

# Find the longest sequence of consecutive integers and print the expressions
def find_longest_consecutive_sequence_with_expressions(digit_set):
    results = evaluate_expressions_with_expressions(digit_set)
    n = 1
    consecutive_results = {}
    
    while n in results:
        consecutive_results[n] = results[n]
        n += 1
    
    return consecutive_results

# Try all combinations of digits and find the best one
def find_best_digit_set_and_print_expressions():
    best_set = None
    longest_sequence = 0
    best_results = {}
    
    for digit_set in itertools.combinations(range(1, 10), 4):
        consecutive_results = find_longest_consecutive_sequence_with_expressions(digit_set)
        consecutive_length = len(consecutive_results)
        if consecutive_length > longest_sequence:
            best_set = digit_set
            longest_sequence = consecutive_length
            best_results = consecutive_results

    # Print the best set and how each number can be formed
    print(f"Best set of digits: {best_set}")
    print(f"Consecutive numbers from 1 to {longest_sequence}:")
    for num, expr in best_results.items():
        print(f"{num} = {expr}")

# Find and print the best set and the expressions for the numbers
find_best_digit_set_and_print_expressions()
