import random


class Parrot_Bot:
    miss_dict = []

    def __init__(self):
        self.miss_dict.append('オハヨー')
        self.miss_dict.append('オソヨー')
        self.miss_dict.append('ハイヨー')
        print('ピーチャン「コンニチハ！ ボク、ピーチャン！」')

    def get_word(self, c):
        miss_word_len = len(self.miss_dict)
        for i in range(10 - miss_word_len):
            self.miss_dict.append(c)

    def make_response(self):
        response = random.choice(self.miss_dict)
        print(f'ピーチャン>{response}')


if __name__ == "__main__":
    parrot_bot = Parrot_Bot()
    c = input('あなた> ')
    parrot_bot.get_word(c)
    parrot_bot.make_response()
