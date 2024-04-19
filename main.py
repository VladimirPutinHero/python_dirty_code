import hello
import work_with_file

hello.Hello()
filename = "aaa"
with open(filename, 'r') as file:
    content = file.read()
    words = content.split(' ')
try:
    sentence = work_with_file.Sentence(content)
    quantity = work_with_file.Quantity_words(words)
    sorted_words = work_with_file.Famous_words(words)
    vowel = work_with_file.Vowel(content)
    consonant = work_with_file.Consonant(content)
    print(f"Количество предложений в файле: {sentence}")
    print(f"Самые часто встречающиеся слова: {sorted_words}")
    print(f"Количество слов в файле: {quantity}")
    print(f"Количество гласных букв: {vowel}")
    print(f"Количество согласных букв: {consonant}")
except FileNotFoundError:
    print("nety")
