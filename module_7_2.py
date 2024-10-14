def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        for i, string in enumerate(strings):
            current_position = f.tell()
            f.write(string + '\n')

            strings_positions[(i + 1, current_position)] = string

    return strings_positions


info = [
    'I am not here to mock anybody',
    'Используйте хоть какую-нибудь кодировку.',
    'Because there are 100500 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Проверка словаря:
strings_positions = dict(result)
print(strings_positions)
