from Models.BaseComment import BaseComment


class Comment200512(BaseComment):
	id: str  # Unique

	author: str
	body: str

	subreddit_id: str
	subreddit: str

	score: int
	ups: int

	link_id: str
	parent_id: str

	edited: bool

	controversiality: int
	stickied: bool
	# author_flair_css_class: None
	# author_flair_text: None
	gilded: int
	# distinguished: None
	retrieved_on: int
	created_ut: int

	def __init__(self, comment: str):
		super().__init__(comment)

		self.comment_json = self.comment_json
		self.id = self.comment_json['id']

		self.author = self.comment_json['author']
		self.body = self.comment_json['body']

		self.subreddit_id = self.comment_json['subreddit_id']
		self.subreddit = self.comment_json['subreddit']

		self.score = self.comment_json['score']
		self.ups = self.comment_json['ups']

		self.link_id = self.comment_json['link_id']
		self.parent_id = self.comment_json['parent_id']

		self.edited = self.comment_json['edited']

		self.controversiality = self.comment_json['controversiality']
		self.stickied = self.comment_json['stickied']
		self.author_flair_css_class = self.comment_json['author_flair_css_class']
		self.author_flair_text = self.comment_json['author_flair_text']
		self.gilded = self.comment_json['gilded']
		self.distinguished = self.comment_json['distinguished']

		self.retrieved_on = self.comment_json['retrieved_on']
		self.created_utc = self.comment_json['created_utc']
