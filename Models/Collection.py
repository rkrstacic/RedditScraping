class Collection:
	def __init__(self, data: list):
		self.data = data

	def __repr__(self):
		return "Collection:\n" + "\n".join([f"{i}: {d}" for i, d in enumerate(self.data)])

