import json


class BaseComment:
	comment_json: dict
	body: str

	def __init__(self, comment: str):
		self.comment_json = json.loads(comment)

	def __str__(self, indent=4):
		return json.dumps(self.comment_json, indent=indent, sort_keys=True)

	def print_class_definition(self, name=None) -> None:
		if name is None:
			name = "XYZ"

		def get_val_type(v) -> str:
			v = str(type(v))[8:-2]
			return 'None' if v == 'NoneType' else v

		typings = [f"{key}: {get_val_type(val)}" for key, val in sorted(self.comment_json.items())]
		initializations = [f"self.{val} = self.comment_json['{val}']" for val in sorted(self.comment_json)]

		with open("Models/class_template.txt") as f:
			print("".join(f.readlines()).format(
				name=name,
				typing_string="\n\t".join(typings),
				init_string="\n\t\t".join(initializations)),
			)
