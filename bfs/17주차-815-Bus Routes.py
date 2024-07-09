class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a graph where each node is a bus stop and edges are the buses that can take you from one stop to another
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)
        
        # BFS initialization
        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])  # (current_stop, number_of_buses_taken)
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            
            # Visit all buses passing through the current stop
            for bus in stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                
                # Check all stops in the current bus route
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        
        return -1