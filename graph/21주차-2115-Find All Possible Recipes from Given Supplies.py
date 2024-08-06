class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize data structures
        supply_set = set(supplies)
        recipe_map = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        
        # Build the graph and in-degree count
        for recipe in recipes:
            for ingredient in recipe_map[recipe]:
                if ingredient not in supply_set:
                    graph[ingredient].append(recipe)
                    in_degree[recipe] += 1
        
        # Initialize the queue with recipes that have all ingredients available
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        result = []
        
        # Process the queue
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result