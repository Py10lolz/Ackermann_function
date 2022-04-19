from copy import deepcopy
from time import sleep
def visualize(a):
	n = a.pop()
	m = a.pop()
	string_repr = f"A({m}, {n})"
	while a != []:
		m = a.pop()
		string_repr = f"A({m}, {string_repr})"
	return string_repr
def ackermann(m, n):
	answer = [m, n]
	orig_m = m
	orig_n = n
	step = 0
	steps = ""
	while len(answer) != 1:
		string_repr = visualize(deepcopy(answer))
		print(string_repr)
		sleep(1/10)
		steps += string_repr+'\n'
		n = answer.pop()
		m = answer.pop()
		if m == 0:
			answer += [n+1]
		elif n == 0:
			answer += [m-1, 1]
		else:
			answer += [m-1,m,n-1]
		step += 1
	print(f"\n\n\nit takes {step} steps to find that the answer to A({orig_m}, {orig_n}) is {answer[0]}")
	with open("/sdcard/calculating_ackermann", "w") as f:
		f.write(steps)
	print("saved the steps in /sdcard/calculating_ackermann")
ackermann(3, 2)