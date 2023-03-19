def generate_file_names(names):
    # Находим самое длинное название и его длину
    max_len = len(max(names, key=len))

    # Убираем дублирующиеся символы
    unique_names = []
    for name in names:
        unique_chars = []
        for char in name:
            if char not in unique_chars:
                unique_chars.append(char)
        unique_names.append(''.join(unique_chars))

    # Дополняем каждое название до нужной длины
    padded_names = [name.ljust(max_len, '_') for name in unique_names]

    return print(padded_names)
