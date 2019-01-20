# first: pip install emoji

from emoji import emojize

print(emojize("It's me, Phika :smile: :grin:",
              use_aliases=True))
print(emojize('Python is :heart: :thumbsup: :lock:',
              use_aliases=True))
print(emojize(":two_hearts: :broken_heart: :couple:",
              use_aliases=True))
print(emojize(":heart_eyes: :v: :boom: :running:",
              use_aliases=True))

print(emojize("Instagram :id: Phika.ir",
              use_aliases=True))

# complete list:
# https://www.webfx.com/tools/emoji-cheat-sheet/
