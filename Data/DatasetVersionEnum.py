from Data.Dataset import Dataset
from Models.Comments.Comment200512 import Comment200512
from Models.Comments.Comment201807 import Comment201807


class DatasetVersionEnum:
	Dataset_2005_12 = Dataset('RC_2005-12', Comment200512)
	Dataset_2018_07 = Dataset('RC_2018-07', Comment201807)
