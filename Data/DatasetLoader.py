import time
import json

from Data.Dataset import Dataset
from Models.BaseComment import BaseComment
from Models.CommentsContainer import CommentsContainer


class DatasetLoader:
	@staticmethod
	def load(dataset_version: Dataset, *, nrow: int = 100000, batch_size: int = 10000, debug=False, update_rate=3) -> None:
		batch_size = batch_size if batch_size < nrow else nrow
		data = dataset_version.model()
		with open("Data/Datasets/" + dataset_version.filename + ".txt") as f:
			if debug:
				print(f"Loading {nrow if nrow > 0 else 'all'} rows...")

			last_update_time = time.time()
			for i in range(int(nrow / batch_size)):
				batch = json.loads("[" + ",".join(f.readlines(1000 * batch_size)) + "]")
				data.add_batch(batch)

				if debug and time.time() - last_update_time > update_rate:
					print(f"{i} / {int(nrow / batch_size)}")
					last_update_time = time.time()

		if debug:
			print(f"Loaded {len(data.body)} rows")
		CommentsContainer().save_comments(data)

	@staticmethod
	def print_class_definition(filename: str) -> None:
		with open("Data/Datasets/" + filename + ".txt") as f:
			import re
			match = re.search("20[0-9]{2}-[0-9]{2}", filename)
			BaseComment().print_class_definition(
				json.loads(f.readline()),
				match.group().replace("-", "") if match is not None else match
			)
