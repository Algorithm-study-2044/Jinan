class Solution:
    coors = [(x, y) for x in range(3)
             for y in range(4) if (x, y) != (0, 3) and (x, y) != (2, 3)]
    moves = [(x, y) for x in (2, -2) for y in (1, -1)] + [(y, x)
                                                          for x in (2, -2) for y in (1, -1)]
    next_coors = {}

    def get_next_coors(self, coor: (int, int)) -> list((int, int)):
        if coor in self.next_coors:
            return self.next_coors[coor]
        res = []
        for move in self.moves:
            next_coor = (coor[0] + move[0], coor[1] + move[1])
            if next_coor in self.coors:
                res.append(next_coor)
        return res

    def get_phones(self, n: int):
        res = {coor: 1 for coor in self.coors}
        for _ in range(n-1):
            temp = {coor: 0 for coor in self.coors}
            for coor, cnt in res.items():
                for n_coor in self.get_next_coors(coor):
                    temp[n_coor] += cnt
            res = temp
        return res

    def knightDialer(self, n: int) -> int:
        return sum(self.get_phones(n).values()) % (10 ** 9 + 7)
