# Details page update script
import sys

with open('app/src/main/assets/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Original length:', len(text))
