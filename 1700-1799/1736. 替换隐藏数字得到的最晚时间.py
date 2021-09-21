class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i in range(len(time)):
            if time[i] == ":":
                continue
            elif time[i] != "?":
                continue
            else:
                if i == 0 and time[i + 1] == "?":
                    time[i] = '2'
                elif i == 0 and int(time[i + 1]) < 4:
                    time[i] = '2'
                elif i == 0:
                    time[i] = '1'
                elif i == 1 and int(time[i - 1]) < 2:
                    time[i] = '9'
                elif i == 1:
                    time[i] = '3'
                elif i == 3:
                    time[i] = "5"
                elif i == 4:
                    time[i] = '9'
        return "".join(time)


print("?".isnumeric())
so = Solution()
print(so.maximumTime(time="2?:?0"))
