# Reddit dataset scraper tool 

This project was built for scraping Reddit datasets.
Datasets this project was built on: https://files.pushshift.io/reddit/comments/

To unpack the .zstd files you can use:
- Windows: https://sourceforge.net/projects/zstandard.mirror/
- Mac: https://formulae.brew.sh/formula/zstd

## How to use

To use this tool and work with desired dataset follow these steps:

1. Download one of the datasets
2. Unpack the dataset file using ZStandard tool (above-mentioned)
3. Move the unpacked file to `~/Data/Datasets`
5. Load the data with one of the Comment models from `~/Models/Comments`. Example: `DatasetLoader.load(DatasetVersionEnum.Dataset_2018_07, limit=10000)`

#### Adding new Comment model
If specific Comment model doesn't exist, you can add it by doing the following:

1. In `./Models/Comments` add new Python file called `CommentYYYYMM.py` (instead of `YYYY` and `MM` use the year and the month of the dataset). To get class definition based on your specific database there is a helper function `DatasetLoader.print_class_definition` that prints out the code you can copy and paste into the file. 

Example: 
```python
from Data.DatasetLoader import DatasetLoader

def main() -> None:
    DatasetLoader.print_class_definition('RC_2018-07')
```
Output:
```
from typing import List
from Models.BaseComment import BaseComment
from Models.Singleton import Singleton


class Comment201807(BaseComment, metaclass=Singleton):
    archived: List[bool] = []
    author: List[str] = []
    ...

    def __init__(self, comment: dict) -> None:
        super().__init__(comment)

        self.comment_json = self.comment_json

        self.archived = self.comment_json['archived']
        self.author = self.comment_json['author']
        ...

    def add_batch(self, batch: List[dict]) -> None:
        for comment in batch:
            self.add_comment(comment)

```
 
2. In the class DatasetVersionEnum located in `./Data` add new enum case. Example:

```python
from Data.Dataset import Dataset
from Models.Comments.Comment201807 import Comment201807

class DatasetVersionEnum:
    Dataset_2018_07 = Dataset('RC_2018-07', Comment201807)
```

## Current limitations

The project is not optimized for big datasets. Recommended load limit=1000000. Loading 1 million rows takes ~30 seconds (depends on machine) and ~2.5Gb of RAM.

Also, as of right now, this project is only compatible with datasets from: https://files.pushshift.io/reddit/comments/


## Possible improvements

Dynamic loading and unloading (depending on the use case, it may not be necessary to keep the old data in the memory)
