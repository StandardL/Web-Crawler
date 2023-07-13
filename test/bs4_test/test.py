from bs4 import BeautifulSoup

with open("./test.html", encoding='utf-8') as file:
    html_doc = file.read()  # read the file

soup = BeautifulSoup(html_doc, 'html.parser')  # parse the file

div_node = soup.find("div", id="u1")

links = div_node.find_all("a")  # replace soup by div_node
for link in links:
    print(link.name, link['href'], link.get_text())

img = div_node.find("img")
print(img["src"])
