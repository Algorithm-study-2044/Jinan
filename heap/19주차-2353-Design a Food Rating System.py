class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        cuisine_set = set(cuisines)
        self.data = defaultdict(list)
        self.lookup = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            heapq.heappush(self.data[cuisine], (-rating, food))
            self.lookup[food] = (rating, cuisine)

    # def changeRating(self, food: str, newRating: int) -> None:
    #     cuisine = self.lookup[food]
    #     new_heap = [row for row in self.data[cuisine] if row[1] != food]
    #     new_heap.append((-newRating, food))
    #     heapq.heapify(new_heap)
    #     self.data[cuisine] = new_heap

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.lookup[food]
        self.lookup[food] = (newRating, cuisine)
        self.data[cuisine].remove((-rating, food))  # bottleneck
        self.data[cuisine].append((-newRating, food))
        heapq.heapify(self.data[cuisine])

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
