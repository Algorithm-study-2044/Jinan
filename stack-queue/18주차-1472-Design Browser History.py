class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]  # Initialize the history with the homepage
        self.current_index = 0     # Start at the homepage

    def visit(self, url: str) -> None:
        # Truncate the history to the current position and add the new URL
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        # Move back but not beyond the start of the history
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        # Move forward but not beyond the end of the history
        self.current_index = min(
            len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
