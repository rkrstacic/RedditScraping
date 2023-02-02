from Data.DatasetLoader import DatasetLoader
from Data.DatasetVersionEnum import DatasetVersionEnum
from Services.RegexMatchService import RegexMatchService


def main():
    data = DatasetLoader.load(DatasetVersionEnum.Dataset_2015_12, limit=0)
    matches = RegexMatchService(data).match_with_url_after("reddit", scope=100)
    print(matches)


if __name__ == '__main__':
    main()
