import googletrans
from googletrans import Translator


djtext="hello i am rahul"
translator=Translator()

oldval=translator.detect(djtext)
print(olval)