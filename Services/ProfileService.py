class Profile:
	def __init__(self, __func, *args):
		import cProfile
		import pstats

		with cProfile.Profile() as pr:
			if args is None:
				__func()
			else:
				__func(*args)

		stats = pstats.Stats(pr)
		stats.sort_stats(pstats.SortKey.TIME)
		stats.print_stats()
