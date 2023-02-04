from typing import List
from Models.BaseComment import BaseComment
from Models.Singleton import Singleton


class Comment200512(BaseComment, metaclass=Singleton):
	author: List[str] = []
	author_flair_css_class: List[None] = []
	author_flair_text: List[None] = []
	body: List[str] = []
	controversiality: List[int] = []
	created_utc: List[int] = []
	distinguished: List[None] = []
	edited: List[bool] = []
	gilded: List[int] = []
	id: List[str] = []
	link_id: List[str] = []
	parent_id: List[str] = []
	retrieved_on: List[int] = []
	score: List[int] = []
	stickied: List[bool] = []
	subreddit: List[str] = []
	subreddit_id: List[str] = []
	ups: List[int] = []

	def add_comment(self, comment: dict) -> None:
		super().add_comment(comment)

		self.author.append(self.comment_json[-1]['author'])
		self.author_flair_css_class.append(self.comment_json[-1]['author_flair_css_class'])
		self.author_flair_text.append(self.comment_json[-1]['author_flair_text'])
		self.body.append(self.comment_json[-1]['body'])
		self.controversiality.append(self.comment_json[-1]['controversiality'])
		self.created_utc.append(self.comment_json[-1]['created_utc'])
		self.distinguished.append(self.comment_json[-1]['distinguished'])
		self.edited.append(self.comment_json[-1]['edited'])
		self.gilded.append(self.comment_json[-1]['gilded'])
		self.id.append(self.comment_json[-1]['id'])
		self.link_id.append(self.comment_json[-1]['link_id'])
		self.parent_id.append(self.comment_json[-1]['parent_id'])
		self.retrieved_on.append(self.comment_json[-1]['retrieved_on'])
		self.score.append(self.comment_json[-1]['score'])
		self.stickied.append(self.comment_json[-1]['stickied'])
		self.subreddit.append(self.comment_json[-1]['subreddit'])
		self.subreddit_id.append(self.comment_json[-1]['subreddit_id'])
		self.ups.append(self.comment_json[-1]['ups'])

	def add_batch(self, batch: List[dict]) -> None:
		for comment in batch:
			self.add_comment(comment)
