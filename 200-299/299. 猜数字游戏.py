class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        sl = [0] * 10
        gl = [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sl[int(s)] += 1
                gl[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(sl, gl))
        return "{}A{}B".format(bulls, cows)

