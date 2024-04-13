import hello
import words_sentence
import letter

hello.Hello()
filename = "aaa"
with open(filename, 'r') as file:
    content = file.read()
try:
    words_sentence.words_Sentence(filename)
    letter.Letter(content)
except FileNotFoundError:
    print("nety")