# https://www.youtube.com/watch?v=AVmzjFX9koM&list=PL_9u0sXf6uYh97O38_0teIqx1WMPfj-xm&index=3&t=99s

def isAnagram(s: str, t: str) -> bool:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1

        return not any(count)


s = "rat"
t = "car"

print(isAnagram(s, t))