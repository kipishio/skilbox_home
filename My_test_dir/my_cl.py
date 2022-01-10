class As:
	def __init__(self):
		self.qqq = 9

	def pr(self):
		print('Привет')

class Bs(As):
	def __init__(self):
		super(Bs, self).__init__()
		self.ww = 10

	def pr(self):
		super(Bs, self).pr()
		print('пока')

bs = Bs()
print(bs.qqq)

bs.pr()

@log_methods("%a %d %Y - %H:%M:%S", decor_func_cls)