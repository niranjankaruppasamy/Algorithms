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
	res = [0] * len(val)
	for i in range(len(val)):
		res[i] = mapper[val[i]]

	for j in range(len(res) - 1):
		if res[j] < res[j+1]:
			res[j] = res[j] * -1

	return sum(res)


if __name__ == "__main__":
	user_inp = str(input("Enter Valid Roman : "))
	print(romanToint(user_inp))
