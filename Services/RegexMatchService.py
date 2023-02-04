import re

from Models.BaseComment import BaseComment
from Models.Collection import Collection
from Models.CommentsContainer import CommentsContainer


class RegexMatchService:
	def __init__(self, data: BaseComment):
		self.data = data

	@staticmethod
	def __find_matches_with_context(string, context_size):
		return r".{0," + str(context_size) + "}" + string + r".{0," + str(context_size) + "}"

	@staticmethod
	def match(string: str, *, scope=50) -> Collection:
		string_regex_pattern = RegexMatchService.__find_matches_with_context(string, scope)
		text_collection = "\n".join(CommentsContainer().comments.body)
		matches = re.findall(string_regex_pattern, text_collection)
		return Collection(matches)

	@staticmethod
	def match_with_url_after(string: str, *, scope=50) -> Collection:
		url_regex_pattern = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*"
		string_regex_pattern = RegexMatchService.__find_matches_with_context(string, scope)

		text_collection = "\n".join(CommentsContainer().comments.body)
		matches = re.findall(string_regex_pattern + url_regex_pattern, text_collection)
		return Collection(matches)


