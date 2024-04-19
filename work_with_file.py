def Sentence(content):
    sentences = content.split('.')
    return len(sentences)


def Quantity_words(words):
    return len(words)


def Famous_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:5]


def Vowel(content):
    glas = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    sentence = content
    vowel_count = sum(1 for char in sentence if char in glas)
    return vowel_count


def Consonant(content):
    sogl = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    sentence = content
    consonant_count = sum(1 for char in sentence if char in sogl)
    return consonant_count
