import heapq


def min_connection_cost(cables):
    """Return (total_cost, steps) where steps is the join order.

    Each step is a tuple (a, b, a + b).
    """
    heap = list(cables)
    heapq.heapify(heap)

    total_cost = 0
    steps = []
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        joined = first + second
        total_cost += joined
        steps.append((first, second, joined))
        heapq.heappush(heap, joined)

    return total_cost, steps


if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    total, steps = min_connection_cost(cables)

    print(f"Cables: {cables}")
    print("Join order:")
    for i, (a, b, joined) in enumerate(steps, 1):
        print(f"  {i}. {a} + {b} = {joined} (cost {joined})")
    print(f"Minimal total cost: {total}")

    assert total == 58
    assert min_connection_cost([5]) == (0, [])
    assert min_connection_cost([]) == (0, [])
    assert min_connection_cost([1, 2, 3, 4, 5])[0] == 33
