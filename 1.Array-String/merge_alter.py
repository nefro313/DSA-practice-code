# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
word1 = "ab"
word2 = "pqrs"

def mergeAlternately(word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        result = ""
        for i in range(n):
            if i >= m:
                result+=word1[i:]
                return result
            result += word1[i]+word2[i]
        if m >n:
            result+=word2[n:]
        return result

print(mergeAlternately(word1,word2))