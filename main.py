import argparse

from processor import Processor

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Путь до каталога/файла который будет забекаплен.")
namespace = parser.parse_args()


def main():
    processor = Processor(namespace.path)
    processor.run()


if __name__ == '__main__':
    print("Run")
    main()
    print("Finish")
