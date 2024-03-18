from googletrans import Translator

translator = Translator()

text="デニスは赤毛の猿です"

translation = translator.translate(text, src='auto', dest='en')

print(translation.text)
print(translation.src)