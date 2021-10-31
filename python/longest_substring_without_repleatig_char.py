def lengthOfLongestSubstring(s: str) -> int:
    char = set()
    res = 0
    for i in range(len(s)):
        if s[i] not in char:
            char.add(s[i])
        else:
            char.remove(s[i])
            char.add(s[i])
        res = max(res, len(char))
    return res


if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcbcaab") == 3
