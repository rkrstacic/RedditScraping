from Data.DatasetLoader import DatasetLoader
from Data.DatasetVersionEnum import DatasetVersionEnum
from Services.RegexMatchService import RegexMatchService


def main() -> None:
    # DatasetLoader.print_class_definition('RC_2018-07')
    data = DatasetLoader.load(DatasetVersionEnum.Dataset_2018_07)
    matches = RegexMatchService(data).match("hello")
    print(matches)


if __name__ == '__main__':
    main()
