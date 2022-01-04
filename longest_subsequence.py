def longest_subsequence(text1, text2):
    l1 = len(text1)
    l2 = len(text2)
    mapp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
 
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if text1[i-1] == text2[j-1]:
                mapp[i][j] = 1 + mapp[i-1][j-1]
            else:
                mapp[i][j] = max(mapp[i][j-1], mapp[i-1][j])                
    return mapp[l1][l2]

if __name__ == "__main__":
	str1 = "abcde"
	str2 = "ace"
	assert longest_subsequence(str1, str2) == 3
