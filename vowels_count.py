def count_vowels(text: str) -> int:
    """
    Возвращает количество гласных букв (a, e, i, o, u) в строке text.
    Регистр не учитывается.
    """
    vowels = set('aeiou')
    return sum(1 for char in text.lower() if char in vowels)
