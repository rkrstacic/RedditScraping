from Data.Dataset import Dataset
from Models.Comment200512 import Comment200512


class DatasetVersionEnum:
	Dataset_2015_12 = Dataset('RC_2005-12', Comment200512)
