import json
from typing import List


class BaseComment:
	comment_json: List[dict] = []
	body: List[str] = []

	def __init__(self):
		pass

	def add_comment(self, comment: dict) -> None:
		self.comment_json.append(comment)

	def add_batch(self, comment: str) -> None:
		raise NotImplementedError()

	def __repr__(self, indent=4):
		return json.dumps(self.comment_json, indent=indent, sort_keys=True)

	@staticmethod
	def print_class_definition(data: dict, name=None) -> None:
		if name is None:
			name = "XYZ"

		def get_val_type(v) -> str:
			v = str(type(v))[8:-2]
			return 'None' if v == 'NoneType' else v

		typings = [f"{key}: List[{get_val_type(val)}] = []" for key, val in sorted(data.items())]
		initializations = [f"self.{val}.append(self.comment_json[-1]['{val}'])" for val in sorted(data)]

		with open("Models/class_template.txt") as f:
			print("".join(f.readlines()).format(
				name=name,
				typing_string="\n\t".join(typings),
				init_string="\n\t\t".join(initializations)),
			)
