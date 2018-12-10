def grayCode(self, n):

	res = [0]

	i = 0

	while i < n:

		res_inv = res[::-1]#求res的反向list(镜像)
		res_inv = [x + pow(2,i) for x in res_inv]

		res = res + res_inv

		i += 1

	return res