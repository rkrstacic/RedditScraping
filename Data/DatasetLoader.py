from Data.Dataset import Dataset
from Models.CommentCollection import CommentCollection


class DatasetLoader:
	@staticmethod
	def load(dataset_version: Dataset, *, limit=0):
		data = []

		with open("Data/Datasets/" + dataset_version.filename + ".txt") as f:
			for index, line in enumerate(f):
				if index > limit > 0:
					break

				data.append(dataset_version.model(line))

		return CommentCollection(data)
