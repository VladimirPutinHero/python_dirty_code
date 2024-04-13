def Letter(content):
    glas = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    sogl = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    sentence = content
    vowel_count = sum(1 for char in sentence if char in glas)
    consonant_count = sum(1 for char in sentence if char in sogl)
    print(f"Количество гласных букв: {vowel_count}")
    print(f"Количество согласных букв: {consonant_count}")