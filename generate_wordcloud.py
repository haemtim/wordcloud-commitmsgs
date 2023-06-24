from wordcloud import WordCloud
import matplotlib.pyplot as plt
import subprocess
import os

WCDIR='wordcloud/'

with open('commitmsgs.txt', 'w') as f:
    subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=f)
with open('commitmsgs.txt', 'r') as f:
    textParts = f.read().split('\n')

textParts = list(textParts)

for textPart in textParts:
    if "merge" in textPart.lower():
        textParts.remove(textPart)
    elif "wordcloud" in textPart.lower():
        textParts.remove(textPart)
    elif "worldcloud" in textPart.lower:
        textParts.remove(textPart)
    elif "generate_wordcloud" in textPart.lower():
        textParts.remove(textPart)
    elif "yml" in textPart.lower():
        textParts.remove(textPart)

    #if "wordcloud" or "worldcloud" in textPart.lower():
     #   textParts.remove(textPart)

text = ' '.join(textParts)

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(text)

# Display the generated image:
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig('wordcloud.png')
