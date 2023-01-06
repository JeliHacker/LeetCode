# https://leetcode.com/problems/count-pairs-of-similar-strings/description/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # answer = 0

        # pairs = {}

        # for word in words:
        #     letterSet = set()
        #     for letter in word:
        #         if not letter in letterSet:
        #             letterSet.add(letter)
        
        #     tuple_letter_set = tuple(letterSet)
        #     if tuple_letter_set in pairs:
        #         answer += len(pairs[tuple_letter_set])
        #         pairs[tuple_letter_set].append(tuple_letter_set)
        #     else:
        #         pairs[tuple_letter_set] = [0]
        
        # return answer

        count = 0
        for i in range(len(words)):
            for j in range(i):
                print(f"i, j = {i}, {j}")
                if set(words[i]) == set(words[j]):
                    count +=1
        return count

