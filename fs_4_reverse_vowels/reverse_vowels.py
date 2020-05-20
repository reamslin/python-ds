def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = []
    for char in s:
        if char.lower() in "aeiou":
            vowels.append(char)
    
    rev_vowels = vowels[::-1]
    vowel_count = 0
    new_s = ''
    for char in s:
        if char.lower() in "aeiou":
            new_s += rev_vowels[vowel_count]
            vowel_count += 1
        else: new_s += char
    return new_s


