top_template = open('top_template.html').read()
bottom_template = open('bottom_template.html').read()

#card
content = open('card.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)
