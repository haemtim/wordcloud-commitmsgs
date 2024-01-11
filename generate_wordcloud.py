from wordcloud import WordCloud
import matplotlib.pyplot as plt
import subprocess
import os

WCDIR='wordcloud/'

with open('commitmsgs.txt', 'w') as f:
    subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=f)
with open('commitmsgs.txt', 'r') as f:
    textParts = f.read().split('\n')

filteredTextParts = []

for textPart in textParts:
    if "merge" not in textPart.lower() and "wordcloud" not in textPart.lower() and "worldcloud" not in textPart.lower() and "generate_wordcloud" not in textPart.lower() and "yml" not in textPart.lower() and "add " not in textPart.lower() and "automatic" not in textPart.lower() and "push" not in textPart.lower() and "build" not in textPart.lower() and "and" not in textPart.lower():
        filteredTextParts.append(textPart)

text = ' '.join(filteredTextParts)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(text)

# Display the generated image:
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig('wordcloud.png')
