#方法1

class Solution(object):
    def grayCode(self, n):

        return map(lambda x: int(x, 2), self.gray(n))

    def gray(self, n):
        res = []
        if n == 0:
            res = ["0"]
        elif n == 1:
            res = ["0", "1"]
        else:
            temp = self.gray(n - 1)
            res = ['0' + x for x in temp] + ['1' + x for x in temp[::-1]]
        return res




#方法2
def grayCode(self, n):

	res = [0]

	i = 0

	while i < n:

		res_inv = res[::-1]#求res的反向list(镜像)
		res_inv = [x + pow(2,i) for x in res_inv]

		res = res + res_inv

		i += 1

	return res
	
#方法3
def grayCode(self, n):
	res=[]
	size=1<<n
	for i in range(size):
		res.append((i>>1)^i)
	return res
#或直接return [i ^ (i >> 1) for i in range(1 << n)]