class File:
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding='utf-8')
        print(type(self.file))
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()


with File('example.txt', 'w') as file:
    print(type(file))
    print(file.__class__)
    file.write('Всем привет!\n')
