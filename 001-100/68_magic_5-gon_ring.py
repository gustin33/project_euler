'''
The reason we typically assign the smaller numbers (1 to 5) to the internal nodes and the larger numbers (6 to 10) to the external nodes is due to the way the problem is structured and the goal of maximizing the 16-digit string.

### Considerations for External and Internal Nodes:

1. **Maximizing the String:**
   - The problem asks for the "maximum" 16-digit string. Since each line of the 5-gon ring is represented as a group of three numbers concatenated together, having larger numbers in the external nodes (which appear first in each triplet) generally leads to larger concatenated numbers. This helps in maximizing the overall 16-digit string.

2. **Arrangement and Symmetry:**
   - The problem specifically mentions that the solution should start with the group of three that has the numerically lowest external node. By placing smaller numbers in the external nodes (1 to 5), the potential starting point of the string would be small, making it less likely to produce the maximum possible string.
   - Placing larger numbers (6 to 10) as external nodes increases the chances of generating a higher starting digit, which contributes to a larger final 16-digit string.

3. **Consistency with Examples:**
   - In similar problems, such as the 3-gon ring example provided, the smaller numbers are placed internally to allow for a greater range in external values, which in turn affects the sum and the overall string generation.

### Why Not Use 1-5 Externally?

If we placed 1, 2, 3, 4, 5 as the external nodes, the maximum number at the start of each triplet would be 5. This inherently limits the maximum possible value of the 16-digit string, as the largest digits available (6 to 10) would not be utilized in the first position of each triplet.

### Example:

Consider two configurations:

1. **External nodes: 6, 7, 8, 9, 10** and **Internal nodes: 1, 2, 3, 4, 5**.
   - Potential triplets: \(6, 1, 2\); \(7, 2, 3\); \(8, 3, 4\); \(9, 4, 5\); \(10, 5, 1\).
   - Example string: 6127238349451051.

2. **External nodes: 1, 2, 3, 4, 5** and **Internal nodes: 6, 7, 8, 9, 10**.
   - Potential triplets: \(1, 6, 7\); \(2, 7, 8\); \(3, 8, 9\); \(4, 9, 10\); \(5, 10, 6\).
   - Example string: 167278389491056.

Comparing these, the first configuration has a string starting with "6", whereas the second starts with "1". The first string is more likely to be larger.

### Conclusion:

To maximize the 16-digit string, we should place the larger numbers (6 to 10) in the external nodes and the smaller numbers (1 to 5) in the internal nodes. This ensures that the numerically smallest group of three is as large as possible, maximizing the overall 16-digit string.
'''

from itertools import permutations

def generate_max_16_digit_string():
    max_string = ""
    # External nodes: 6 to 10
    external_nodes = [6, 7, 8, 9, 10]
    # Internal nodes: 1 to 5
    internal_nodes = [1, 2, 3, 4, 5]
    
    for perm in permutations(internal_nodes):
        # Generate each possible 5-gon ring configuration
        # Let's assume the configuration (external, internal):
        # (e1, i1, i2), (e2, i2, i3), (e3, i3, i4), (e4, i4, i5), (e5, i5, i1)
        
        for ex_perm in permutations(external_nodes):
            e1, e2, e3, e4, e5 = ex_perm
            i1, i2, i3, i4, i5 = perm
            
            # Check if it's a magic ring (same sum for each line)
            sum1 = e1 + i1 + i2
            sum2 = e2 + i2 + i3
            sum3 = e3 + i3 + i4 
            sum4 = e4 + i4 + i5
            sum5 = e5 + i5 + i1
            
            if sum1 == sum2 == sum3 == sum4 == sum5:
                # Create the concatenated string, starting with the lowest external node
                if e1 == min(ex_perm):
                    magic_string = f"{e1}{i1}{i2}{e2}{i2}{i3}{e3}{i3}{i4}{e4}{i4}{i5}{e5}{i5}{i1}"
                elif e2 == min(ex_perm):
                    magic_string = f"{e2}{i2}{i3}{e3}{i3}{i4}{e4}{i4}{i5}{e5}{i5}{i1}{e1}{i1}{i2}"
                elif e3 == min(ex_perm):
                    magic_string = f"{e3}{i3}{i4}{e4}{i4}{i5}{e5}{i5}{i1}{e1}{i1}{i2}{e2}{i2}{i3}"
                elif e4 == min(ex_perm):
                    magic_string = f"{e4}{i4}{i5}{e5}{i5}{i1}{e1}{i1}{i2}{e2}{i2}{i3}{e3}{i3}{i4}"
                else:
                    magic_string = f"{e5}{i5}{i1}{e1}{i1}{i2}{e2}{i2}{i3}{e3}{i3}{i4}{e4}{i4}{i5}"
                
                # Check if the string has 16 digits
                max_string = max(max_string, magic_string)
    
    return max_string

# Find the maximum 16-digit string
max_16_digit_string = generate_max_16_digit_string()
print(max_16_digit_string)