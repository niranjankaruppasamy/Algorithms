mapper = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}

def romanToint(val: str) -> int:
	char_list = list(val.upper())
	res = 0
	index = 0
	while index < len(char_list):
		if index+1 >= len(char_list):
			res += mapper.get(char_list[index])
			index+=1
			continue
		if mapper.get(char_list[index]) >= mapper.get(char_list[index+1]):
			res += mapper.get(char_list[index])
		else:
			res += mapper.get(char_list[index+1])
			res -= mapper.get(char_list[index])
			index += 1
		index += 1
	return res


if __name__ == "__main__":
	user_inp = str(input("Enter Valid Roman : "))
	print(romanToint(user_inp))