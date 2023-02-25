# ScrapSpyder
`ScrapSpyder` is a Python package that allows you to scrape and download files from a website. It uses the `requests` and `BeautifulSoup` libraries to crawl a website and download all the files (html, css, js, images, etc.) present on it.

<!-- ## Installation
To install Scraper, simply run:
```
pip install scrapspyder
``` -->

## Usage
To use Scraper, create an instance of the Scraper class and pass in the URL of the website you want to scrape. You can also specify the destination folder where the downloaded files will be saved, the depth of the crawl, whether to perform a deep scan for assets, and more. Here's an example:

```
from scraper import Scraper

sc = Scraper(source="https://www.example.com/",
             dest="example",
             depth=1,
             deep_scan=True,
             verbose=True,
             patterns_to_trim=["some-pattern"]
             )
sc.download()
```

This will crawl the website and download all the files to a folder called example.

To translate html pages to other languages; the following examples translates the downloaded html files from English `en` to Hindi `hi`:

```
from scraper import Translator

tr = Translator(source="example", 
                source_lang="en", 
                target_lang="hi", 
                verbose=True
                )
tr.start()

```


## Requirements
This package requires the following Python libraries:
- requests
- beautifulsoup4

## Contributing
If you find a bug or would like to contribute to the development of Scraper, please open an issue or pull request on GitHub.

## License
`ScrapSpyder` is licensed under the MIT License. See `LICENSE` for more information.

