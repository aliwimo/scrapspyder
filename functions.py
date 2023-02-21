def get_links():
    # Find and extract the content you want from the HTML soup
    links = [link.get('href') for link in soup.find_all('a')]
    print((links))