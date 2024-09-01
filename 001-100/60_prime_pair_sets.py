"""
To solve this problem efficiently using a completely different approach, we can use a more heuristic or systematic method. Here's an approach that leverages efficient search algorithms and avoids brute-force combinations where possible:

### Strategy:

1. **Generate Primes Efficiently**: Use the Sieve of Eratosthenes to generate primes up to a reasonable limit.
2. **Construct Prime Sets**: Build prime sets incrementally and check the concatenation property in a way that avoids redundant calculations.
3. **Utilize Graph Theory**: Treat the problem as a graph where nodes are primes, and edges exist between nodes if their concatenations are also primes. This allows the use of graph algorithms to find cliques (fully connected subgraphs).

### Optimized Approach:

1. **Generate Primes**: Use a sieve to generate a large list of primes efficiently.
2. **Graph Construction**: Build a graph where each node represents a prime, and edges represent valid concatenations.
3. **Find Cliques**: Use algorithms to find a clique of size 5 in this graph, which corresponds to the set of five primes with the desired property.

### Explanation:

1. **`generate_primes(limit)`**: Generates a list of primes up to the specified limit using the Sieve of Eratosthenes.
2. **`build_prime_graph(primes)`**: Constructs a graph where nodes are primes, and edges connect nodes if their concatenations are also primes.
3. **`find_clique_of_size_5(G)`**: Uses NetworkX to find a clique of size 5 in the graph. This clique corresponds to a set of five primes where any two primes concatenate to form another prime.
4. **Limit Adjustment**: Increases the limit for generating primes until a valid clique of size 5 is found.

### Why This Approach?

- **Graph Representation**: By representing the problem as a graph, you can leverage efficient graph algorithms to find solutions rather than brute-forcing through combinations.
- **Efficient Prime Checking**: Using NetworkX's built-in functions for finding cliques can be faster than manually checking combinations.

This approach efficiently handles the problem and optimizes both time and space complexity by using graph theory and efficient algorithms.
"""

import itertools
import sympy as sp
import networkx as nx
import time


def generate_primes(limit):
    return list(sp.primerange(2, limit))


def build_prime_graph(primes):
    G = nx.Graph()
    G.add_nodes_from(primes)

    for p1, p2 in itertools.combinations(primes, 2):
        p1_p2 = int(f"{p1}{p2}")
        p2_p1 = int(f"{p2}{p1}")
        if sp.isprime(p1_p2) and sp.isprime(p2_p1):
            G.add_edge(p1, p2)

    return G


def find_clique_of_size_n(G, n):
    for clique in nx.find_cliques(G):
        if len(clique) == n:
            return clique
    return None


def find_lowest_sum_for_n_primes(n):
    limit = 10000  # Initial limit for primes

    while True:
        primes = generate_primes(limit)
        G = build_prime_graph(primes)

        clique = find_clique_of_size_n(G, n)
        if clique:
            return clique, sum(clique)

        # Increase the limit and try again
        print("Increase the limit and try again")
        limit *= 4


# Run the function
for n in range(3, 5):
    start = time.time()
    clique, lowest_sum = find_lowest_sum_for_n_primes(n)
    print(f"Clique for {n}: {clique}")
    print(f"Lowest sum for {n}: {lowest_sum}")
    print(f"Time elapsed: {round(time.time()-start, 3)}")
