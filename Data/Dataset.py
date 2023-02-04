from typing import Type
from Models.BaseComment import BaseComment


class Dataset:
	def __init__(self, filename: str, model: Type[BaseComment]):
		self.filename = filename
		self.model = model
