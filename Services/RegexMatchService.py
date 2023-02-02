import re

from Models.Collection import Collection
from Models.CommentCollection import CommentCollection


class RegexMatchService:
	def __init__(self, data: CommentCollection):
		self.data = data

	@staticmethod
	def __find_matches_with_context(string, context_size):
		return r".{0," + str(context_size) + "}" + string + r".{0," + str(context_size) + "}"

	def match(self, string: str, *, scope=50) -> Collection:
		string_regex_pattern = self.__find_matches_with_context(string, scope)
		text_collection = "\n".join(self.data.get_raw_comments())
		matches = re.findall(string_regex_pattern, text_collection)
		return Collection(matches)

	def match_with_url_after(self, string: str, *, scope=50):
		url_regex_pattern = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*"
		string_regex_pattern = self.__find_matches_with_context(string, scope)

		text_collection = "\n".join(self.data.get_raw_comments())
		matches = re.findall(string_regex_pattern + url_regex_pattern, text_collection)
		return Collection(matches)


