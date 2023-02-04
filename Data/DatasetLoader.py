import json
import time

from Data.Dataset import Dataset
from Models.BaseComment import BaseComment
from Models.CommentCollection import CommentCollection


class DatasetLoader:
	@staticmethod
	def load(dataset_version: Dataset, *, limit: int = 10000, debug=False) -> CommentCollection:
		data = []

		with open("Data/Datasets/" + dataset_version.filename + ".txt") as f:
			if not debug:
				for index, line in enumerate(f):
					if index > limit > 0:
						break

					data.append(dataset_version.model(line))
			else:
				print(f"Loading {limit if limit > 0 else 'all'} rows...")
				last_update_time = time.time()
				for index, line in enumerate(f):
					if index > limit > 0:
						break

					data.append(dataset_version.model(line))

					if time.time() - last_update_time > 1:
						print(f"{index}/{limit if limit != 0 else '?'}")
						print(data.__sizeof__(), "Bytes")
						last_update_time = time.time()

		return CommentCollection(data)

	@staticmethod
	def print_class_definition(filename: str) -> None:
		with open("Data/Datasets/" + filename + ".txt") as f:
			import re
			match = re.search("20[0-9]{2}-[0-9]{2}", filename)
			BaseComment(f.readline()).print_class_definition(
				match.group().replace("-", "") if match is not None else match
			)
