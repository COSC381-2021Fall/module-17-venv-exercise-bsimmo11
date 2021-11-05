import pyjokes
import wikipedia
from urllib.request import urlopen

print(pyjokes.get_joke())
print("------------------------------")

print(wikipedia.summary("Ninja", sentences = 2))

print("------------------------------")
page = urlopen("https://catalog.emich.edu/preview_program.php?catoid=36&poid=15190")
print(page.headers)
