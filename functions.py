import os
from urllib.parse import urlparse


def get_links():
    # Find and extract the content you want from the HTML soup
    links = [link.get('href') for link in soup.find_all('a')]
    print((links))

def extract_directories(link):
    directories = link.split('/')
    # Remove empty strings from list (in case there are extra slashes in the link)
    directories = [d for d in directories if d]
    # Remove the last element (which will be the file name)
    directories = directories[:-1]
    return directories

def convert_to_path(directories):
    path = '/'.join(directories)
    return path

def prepare_path(link):
    path = convert_to_path(extract_directories(link))
    # if not os.path.exists(path):
    #     os.makedirs(path)
    return path



def trim_domain(link, domain):
    same_domain = True
    parsed_link = urlparse(link)
    parsed_domain = urlparse(domain)
    if not parsed_link.netloc:
        return link, same_domain
    elif parsed_link.scheme != parsed_domain.scheme or parsed_link.netloc != parsed_domain.netloc:
        return link, not same_domain
    return parsed_link.path.lstrip('/'), same_domain
