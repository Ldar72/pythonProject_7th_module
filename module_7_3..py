class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with (open(filename, encoding='utf-8') as f):
                content = f.read()
                cleaned_text = content.lower().replace(',', '').replace('.',
                '').replace('=','').replace('!','').replace('?',
                '').replace(';', '').replace(':', '').replace(' - ', '')
                words = cleaned_text.split()

                if len(words) > 0:
                    all_words[filename] = words

        return all_words

    def find(self, word):
        found_words = {}
        for key, value in self.get_all_words().items():
            try:
                index = value.index(word.lower())
                found_words[key] = index + 1
            except ValueError:
                pass

        return found_words

    def count(self, word):
        counted_words = {}
        for key, value in self.get_all_words().items():
            count = value.count(word.lower())
            if count > 0:
                counted_words[key] = count

        return counted_words


if __name__ == "__main__":
    finder1 = WordsFinder('test_file.txt')
    print(finder1.get_all_words())
    print(finder1.find('TEXT'))
    print(finder1.count('teXT'))
    finder2 = WordsFinder('Rudyard Kipling - If.txt')
    print(finder2.get_all_words())
    print(finder2.find('if'))
    print(finder2.count('IF'))
    finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder3.get_all_words())
    print(finder3.find('captain'))
    print(finder3.count('CAptain'))
    finder4 = WordsFinder('Mother Goose - Monday’s Child.txt')
    print(finder4.get_all_words())
    print(finder4.find('child'))
    print(finder4.count('CHILD'))
