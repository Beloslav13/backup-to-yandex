import argparse
import yadisk

from data import TOKEN
from processor import Processor

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Путь до каталога/файла который будет забекаплен.")
namespace = parser.parse_args()


def main():
    y = yadisk.YaDisk(token=TOKEN)
    # Проверяет, валиден ли токен
    print(y.check_token())
    processor = Processor(namespace.path)
    processor.get_files()


if __name__ == '__main__':
    print("Run")
    main()
    print("Finish")
