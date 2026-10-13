import random


def route_length(tsp, tour):
    # Calculate round-trip tour distance
    return sum(tsp[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


def hill_climbing_tsp(tsp):
    n = len(tsp)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_length = route_length(tsp, current_tour)

    while True:
        best_neighbor = None
        best_length = current_length

        # Generate neighbors by swapping any two cities (2-opt swap)
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = current_tour.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                length = route_length(tsp, neighbor)
                if length < best_length:
                    best_neighbor = neighbor
                    best_length = length

        # Move to neighbor if an improvement is found, else terminate
        if best_length < current_length:
            current_tour = best_neighbor
            current_length = best_length
        else:
            break

    return current_tour, current_length


tsp_matrix = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

solution, length = hill_climbing_tsp(tsp_matrix)
print("Best solution:", solution)
print("Route length:", length)
