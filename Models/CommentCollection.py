from typing import List
from Models.BaseComment import BaseComment
from Models.Collection import Collection


class CommentCollection(Collection):
	def __init__(self, comments: List[BaseComment]):
		super().__init__(comments)

	def get_raw_comments(self) -> List[str]:
		return [comment.body for comment in self.data]

