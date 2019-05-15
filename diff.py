import numpy as np

def diff(a, b):
	N = len(a)
	M = len(b)

	MAX = max(0, M+N)
	V = np.zeros((2*MAX+1), np.int)

	dist = -1

	for D in range(MAX):
		for k in range(-D, D+1, 2):
		    if k == -D or k != D and V[k-1] < V[k+1]:
		        x = V[k+1]
		    else:
		        x = V[k-1] + 1

		    y = x - k

		    while x < N and y < M and (y < 0 or a[x] == b[y]):
		        x += 1
		        y += 1

		    V[k] = x

		    if x >= N and y >= M:
		        dist = D
		        break

		if dist != -1:
		    break

	return dist


if __name__ == '__main__':
	a = 'abcabba'
	b = 'cbabac'
	dist = diff(a, b)
	assert dist == 5

	a = 'abcabc'
	b = 'bcbd'
	dist = diff(a, b)
	assert dist == 4

	a = 'abcabc'
	b = 'abc'
	dist = diff(a, b)
	assert dist == 3
