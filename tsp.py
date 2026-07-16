# Travelling Salesman Problem using Brute Force

from itertools import permutations

# Function to find minimum cost route
def tsp(graph, start):

    n = len(graph)

    # Create list of cities except starting city
    cities = []

    for i in range(n):
        if i != start:
            cities.append(i)

    min_cost = float('inf')
    best_path = []

    # Generate all possible paths
    for path in permutations(cities):

        current_cost = 0
        current_city = start

        # Calculate cost of path
        for city in path:
            current_cost += graph[current_city][city]
            current_city = city

        # Return to starting city
        current_cost += graph[current_city][start]

        # Check minimum cost
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(path) + [start]

    return min_cost, best_path


# Distance matrix
# 0 means same city
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


start_city = 0

cost, path = tsp(graph, start_city)

print("Minimum Cost:", cost)

print("Best Path:")
for city in path:
    print("City", city, end=" ")
