__name_prv = 8

def my_pr():
	print(__name_prv)

	# __name_prv = 9
	# print(__name_prv)

my_pr()

# print(__name__)
# print(__main__)


class FontS():
	def prt(self):
		print('prt')

	def _qwer(self):
		print('qwe')
		self.prt()

	def rt(self):
		self._qwer()

