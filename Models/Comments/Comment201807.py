from typing import List
from Models.BaseComment import BaseComment
from Models.Singleton import Singleton


class Comment201807(BaseComment, metaclass=Singleton):
	archived: List[bool] = []
	author: List[str] = []
	author_flair_background_color: List[str] = []
	author_flair_css_class: List[None] = []
	author_flair_template_id: List[None] = []
	author_flair_text: List[None] = []
	author_flair_text_color: List[str] = []
	body: List[str] = []
	can_gild: List[bool] = []
	can_mod_post: List[bool] = []
	collapsed: List[bool] = []
	collapsed_reason: List[None] = []
	controversiality: List[int] = []
	created_utc: List[int] = []
	distinguished: List[None] = []
	edited: List[bool] = []
	gilded: List[int] = []
	id: List[str] = []
	is_submitter: List[bool] = []
	link_id: List[str] = []
	no_follow: List[bool] = []
	parent_id: List[str] = []
	permalink: List[str] = []
	removal_reason: List[None] = []
	retrieved_on: List[int] = []
	score: List[int] = []
	score_hidden: List[bool] = []
	send_replies: List[bool] = []
	stickied: List[bool] = []
	subreddit: List[str] = []
	subreddit_id: List[str] = []
	subreddit_name_prefixed: List[str] = []
	subreddit_type: List[str] = []

	def add_comment(self, comment: dict) -> None:
		super().add_comment(comment)

		self.archived.append(self.comment_json[-1]['archived'])
		self.author.append(self.comment_json[-1]['author'])
		self.author_flair_background_color.append(self.comment_json[-1]['author_flair_background_color'])
		self.author_flair_css_class.append(self.comment_json[-1]['author_flair_css_class'])
		self.author_flair_template_id.append(self.comment_json[-1]['author_flair_template_id'])
		self.author_flair_text.append(self.comment_json[-1]['author_flair_text'])
		self.author_flair_text_color.append(self.comment_json[-1]['author_flair_text_color'])
		self.body.append(self.comment_json[-1]['body'])
		self.can_gild.append(self.comment_json[-1]['can_gild'])
		self.can_mod_post.append(self.comment_json[-1]['can_mod_post'])
		self.collapsed.append(self.comment_json[-1]['collapsed'])
		self.collapsed_reason.append(self.comment_json[-1]['collapsed_reason'])
		self.controversiality.append(self.comment_json[-1]['controversiality'])
		self.created_utc.append(self.comment_json[-1]['created_utc'])
		self.distinguished.append(self.comment_json[-1]['distinguished'])
		self.edited.append(self.comment_json[-1]['edited'])
		self.gilded.append(self.comment_json[-1]['gilded'])
		self.id.append(self.comment_json[-1]['id'])
		self.is_submitter.append(self.comment_json[-1]['is_submitter'])
		self.link_id.append(self.comment_json[-1]['link_id'])
		self.no_follow.append(self.comment_json[-1]['no_follow'])
		self.parent_id.append(self.comment_json[-1]['parent_id'])
		self.permalink.append(self.comment_json[-1]['permalink'])
		self.removal_reason.append(self.comment_json[-1]['removal_reason'])
		self.retrieved_on.append(self.comment_json[-1]['retrieved_on'])
		self.score.append(self.comment_json[-1]['score'])
		self.score_hidden.append(self.comment_json[-1]['score_hidden'])
		self.send_replies.append(self.comment_json[-1]['send_replies'])
		self.stickied.append(self.comment_json[-1]['stickied'])
		self.subreddit.append(self.comment_json[-1]['subreddit'])
		self.subreddit_id.append(self.comment_json[-1]['subreddit_id'])
		self.subreddit_name_prefixed.append(self.comment_json[-1]['subreddit_name_prefixed'])
		self.subreddit_type.append(self.comment_json[-1]['subreddit_type'])

	def add_batch(self, batch: List[dict]) -> None:
		for comment in batch:
			self.add_comment(comment)
