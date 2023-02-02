import json


class BaseComment:
	comment_json: dict
	body: str

	def __init__(self, comment: str):
		self.comment_json = json.loads(comment)

	def __str__(self, indent=4):
		return json.dumps(self.comment_json, indent=indent, sort_keys=True)
