# ScrapSpyder
`ScrapSpyder` is a Python package that allows you to scrape and download files from a website.

## Installation
To install `ScrapSpyder`, simply run:
```
pip install scrapspyder
```

## Usage
To use `ScrapSpyder`, create an instance of the `Scraper` class and pass in the URL of the website you want to scrape. You can also specify the destination folder where the downloaded files will be saved, the depth of the crawl, whether to perform a deep scan for assets, and more. Here's an example:

```python
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

## Requirements
This package requires the following Python libraries:
- [requests]
- [beautifulsoup4]

## Contributing
If you find a bug or would like to contribute to the development of `ScrapSpyder`, please open an issue or pull request on [GitHub repository].

## License
`ScrapSpyder` is licensed under the MIT License. See [LICENSE] for more information.


[Github repository]: https://github.com/aliwimo/scrapspyder/
[LICENSE]: https://github.com/aliwimo/scrapspyder/blob/main/LICENSE
[requests]: https://pypi.org/project/requests/
[beautifulsoup4]: https://pypi.org/project/beautifulsoup4/
