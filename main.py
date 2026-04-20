import re

class EmojiParser:
    def __init__(self):
        self.emoji_pattern = re.compile(r'[:][a-zA-Z0-9_]+[:]')

    def parse(self, text):
        return self.emoji_pattern.sub(r'\\\1', text)

# Misol:
parser = EmojiParser()
text = "Men :smile: va :heart: sevaman"
print(parser.parse(text))
```

```python
import re

class EmojiParser:
    def __init__(self):
        self.emoji_pattern = re.compile(r'[:][a-zA-Z0-9_]+[:]')

    def parse(self, text):
        return self.emoji_pattern.sub(r'\\\1', text)

# Misol:
parser = EmojiParser()
text = "Men :smile: va :heart: sevaman"
print(parser.parse(text))
