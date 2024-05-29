class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Initialize the dictionary to store the rankings
        rank_dict = defaultdict(lambda: [0] * len(votes[0]))

        # Populate the dictionary with the votes
        for vote in votes:
            for i, team in enumerate(vote):
                rank_dict[team][i] += 1

        # Sort the teams
        sorted_teams = sorted(rank_dict.keys(), key=lambda x: (
            rank_dict[x], -ord(x)), reverse=True)

        # Convert the sorted list of teams into a string
        return ''.join(sorted_teams)
