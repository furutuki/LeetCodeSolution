class Leaderboard:

    score_board = {}

    def __init__(self):
        self.score_board.clear()

    def addScore(self, playerId: int, score: int) -> None:
        if self.score_board.get(playerId) is None:
            self.score_board[playerId] = score
        else:
            self.score_board[playerId] += score

    def top(self, K: int) -> int:
        arr = sorted(self.score_board.values())
        sum = 0
        for i in range(len(arr) - 1, len(arr) - 1 - K, -1):
            sum += arr[i]
        return sum

    def reset(self, playerId: int) -> None:
        del self.score_board[playerId]


s = Leaderboard()
a = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
b = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

res = []
for i in range(len(a)):
    key = a[i]
    val = b[i]
    if key == "Leaderboard":
        res.append("null")
    elif key == "addScore":
        s.addScore(val[0], val[1])
        res.append("null")
    elif key == "reset":
        res.append("null")
        s.reset(val[0])
    elif key == "top":
        sum = s.top(val[0])
        res.append(sum)
print(res)
