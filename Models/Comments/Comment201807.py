from Models.BaseComment import BaseComment


class Comment201807(BaseComment):
	archived: bool
	author: str
	author_flair_background_color: str
	author_flair_css_class: None
	author_flair_template_id: None
	author_flair_text: None
	author_flair_text_color: str
	body: str
	can_gild: bool
	can_mod_post: bool
	collapsed: bool
	collapsed_reason: None
	controversiality: int
	created_utc: int
	distinguished: None
	edited: bool
	gilded: int
	id: str
	is_submitter: bool
	link_id: str
	no_follow: bool
	parent_id: str
	permalink: str
	removal_reason: None
	retrieved_on: int
	score: int
	score_hidden: bool
	send_replies: bool
	stickied: bool
	subreddit: str
	subreddit_id: str
	subreddit_name_prefixed: str
	subreddit_type: str

	def __init__(self, comment: str):
		super().__init__(comment)

		self.comment_json = self.comment_json

		self.archived = self.comment_json['archived']
		self.author = self.comment_json['author']
		self.author_flair_background_color = self.comment_json['author_flair_background_color']
		self.author_flair_css_class = self.comment_json['author_flair_css_class']
		self.author_flair_template_id = self.comment_json['author_flair_template_id']
		self.author_flair_text = self.comment_json['author_flair_text']
		self.author_flair_text_color = self.comment_json['author_flair_text_color']
		self.body = self.comment_json['body']
		self.can_gild = self.comment_json['can_gild']
		self.can_mod_post = self.comment_json['can_mod_post']
		self.collapsed = self.comment_json['collapsed']
		self.collapsed_reason = self.comment_json['collapsed_reason']
		self.controversiality = self.comment_json['controversiality']
		self.created_utc = self.comment_json['created_utc']
		self.distinguished = self.comment_json['distinguished']
		self.edited = self.comment_json['edited']
		self.gilded = self.comment_json['gilded']
		self.id = self.comment_json['id']
		self.is_submitter = self.comment_json['is_submitter']
		self.link_id = self.comment_json['link_id']
		self.no_follow = self.comment_json['no_follow']
		self.parent_id = self.comment_json['parent_id']
		self.permalink = self.comment_json['permalink']
		self.removal_reason = self.comment_json['removal_reason']
		self.retrieved_on = self.comment_json['retrieved_on']
		self.score = self.comment_json['score']
		self.score_hidden = self.comment_json['score_hidden']
		self.send_replies = self.comment_json['send_replies']
		self.stickied = self.comment_json['stickied']
		self.subreddit = self.comment_json['subreddit']
		self.subreddit_id = self.comment_json['subreddit_id']
		self.subreddit_name_prefixed = self.comment_json['subreddit_name_prefixed']
		self.subreddit_type = self.comment_json['subreddit_type']
