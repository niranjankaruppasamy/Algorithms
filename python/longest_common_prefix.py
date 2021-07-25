def longestCommomPrefix(arr: list) -> str:
    arr.sort(reverse=False)
    first = arr[0]
    last = arr[-1]
    ind = 0
    for i in range(min(len(first), len(last))):
    	if first[ind] == last[ind]:
    		ind += 1
    	else:
    		if not ind:
    			return ""
    		else:
    			return first[:ind]
    	if i == min(len(first), len(last)) - 1:
    		return first[:ind]
    return ""


arr = [""]
print(longestCommomPrefix(arr))