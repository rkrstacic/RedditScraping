from Models.BaseComment import BaseComment


class Comment200904(BaseComment):
	id: str  # Unique

	author: str
	body: str

	subreddit_id: str
	subreddit: str

	score: int
	ups: int
	downs: int

	link_id: str
	parent_id: str

	edited: bool
	name: str

	controversiality: int
	# score_hidden: None
	# author_flair_css_class: None
	# author_flair_text: None
	gilded: int
	# distinguished: None
	retrieved_on: int
	# archived: None
	created_ut: int

	def __init__(self, comment: str):
		super().__init__(comment)

		self.comment_json = self.comment_json
		self.body = self.comment_json['body']
