class FibonacciDPRecursive(object):
	"""docstring for Fibonacci"""
	def __init__(self, n):
		self.n = n
		self.fibonacci = [None for _ in range(n + 1)]
		self.dp(n)

	def dp(self, k):
		if self.fibonacci[k] is not None:
			return self.fibonacci[k]
		elif k == 0 or k == 1:
			self.fibonacci[k] = k
			return k
		else:
			self.fibonacci[k] = self.dp(k - 1) + self.dp(k - 2)
			return self.fibonacci[k]

	def get_result(self):
		return self.fibonacci
a = FibonacciDPRecursive(10)
print(a.get_result())

