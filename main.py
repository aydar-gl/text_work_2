import re


class TextWork:
    def __init__(self):
        self.__text = str()

    @property
    def text(self):
        return self.__text

    def read_file(self, path: str):
        with open(path, 'r') as file:
            self.__text = file.read()

    def print_word_count(self):
        lines = self.__text.split('\n')
        i = 1
        all_count = 0
        for line in lines:
            groups = re.findall(r'[A-Za-zА-Яа-яЁё]+', line)
            count = len(groups)
            print(f'В {i} строке {count} слов. Слова:\n{groups}\n')
            i += 1
            all_count += count
        print(f'Всего слов в файле: {all_count}')


if __name__ == '__main__':
    o = TextWork()
    o.read_file('in.txt')
    print(o.text)
    print(f'\n{"-" * 33}\n')
    o.print_word_count()
