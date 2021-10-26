import os


def print_text(text):
    print('Скрпт "{0}" запущен, на диске: {1}  '.format(text, os.path.abspath(os.path.sep)))

print_text('Привет')