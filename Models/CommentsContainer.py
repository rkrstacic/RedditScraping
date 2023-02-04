from Models.BaseComment import BaseComment
from Models.Singleton import Singleton


class CommentsContainer(metaclass=Singleton):
	comments: BaseComment

	def save_comments(self, comments: BaseComment) -> None:
		self.comments = comments
