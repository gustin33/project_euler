import itertools
import networkx as nx
from collections import defaultdict
import time

def generate_cubes(limit):
    """Generate a list of cubes for integers from 2 up to the given limit."""
    return [i**3 for i in range(2, limit)]

def build_cube_graph(cubes):
    """Build a graph where nodes are cubes and edges connect nodes with permutable digits."""
    G = nx.Graph()
    G.add_nodes_from(cubes)

    # Dictionary to map sorted digit tuples to cubes
    permutations = defaultdict(list)
    for cube in cubes:
        perm_key = tuple(sorted(str(cube)))
        permutations[perm_key].append(cube)

    # Add edges between nodes with the same permutation key
    for _, cube_list in permutations.items():
        if len(cube_list) > 1:
            for c1, c2 in itertools.combinations(cube_list, 2):
                G.add_edge(c1, c2)

    return G

def find_clique_of_size_n(G, n):
    """Find cliques of size `n` in the graph `G`."""
    cliques = list(nx.find_cliques(G))
    # Filter to get only cliques of the desired size
    return [clique for clique in cliques if len(clique) == n]

def find_lowest_cube_for_n(n, initial_limit):
    """Find the smallest cube for which exactly `n` permutations are also cubes."""
    limit = initial_limit
    smallest_cube = None
    while True:
        cubes = generate_cubes(limit)
        G = build_cube_graph(cubes)

        cliques = find_clique_of_size_n(G, n)
        if cliques:
            # Find the smallest cube in the first valid clique

            smallest_cube = min(cliques[0])
            for clique in cliques:
                sorted_clique = sorted(clique)
                smallest_cube_in_clique = sorted_clique[0]
                if smallest_cube_in_clique < smallest_cube:
                    smallest_cube = smallest_cube_in_clique
                
            return smallest_cube, limit

        # Increase the limit and try again
        print(f"Increasing limit to {limit * 5}")
        limit *= 5

# Run the function
limit = 1000
for n in range(3, 15):
    start = time.time()
    smallest_cube, limit = find_lowest_cube_for_n(n, limit)
    print(f"Smallest cube for clique of size {n}: {smallest_cube}")
    print(f"Time elapsed: {round(time.time()-start, 3)}")
