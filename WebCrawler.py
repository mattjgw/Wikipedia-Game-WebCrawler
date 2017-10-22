import requests
from bs4 import BeautifulSoup


def spider():
    number_of_links = 1
    found = False
    while found is False or number_of_links < 3:
        url = "https://en.wikipedia.org/wiki/Rhabdotis_aulica"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        found = check_if_usa(url, number_of_links)
        if not found:
            for link in soup.findAll('a'):
                href = str(link.get('href'))
                if href.startswith(r"/wiki/"):
                    link_url = "https://en.wikipedia.org"+href
                    check_if_usa(link_url, number_of_links)
                    if number_of_links is 2:
                        new_url_2(link_url, number_of_links)
        number_of_links += 1


def new_url_2(link_url, number_of_links):
    source_code = requests.get(link_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = str(link.get('href'))
        if href.startswith(r"/wiki/"):
            link_url = "https://en.wikipedia.org" + href
            check_if_usa(link_url, number_of_links)
            if number_of_links is 3:
                new_url_3(link_url, number_of_links)


def new_url_3(link_url, number_of_links):
    source_code = requests.get(link_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = str(link.get('href'))
        if href.startswith(r"/wiki/"):
            link_url = "https://en.wikipedia.org" + href
            check_if_usa(link_url, number_of_links)


def check_if_usa(url, number_of_links):
    if url == "https://en.wikipedia.org/wiki/United_States":
        show_results(number_of_links, url)
        return True


def show_results(number_of_links, url):
    if number_of_links is 1:
        print("You can get to the United States in", number_of_links, "click")
        #  show_path()
    else:
        print("You can get to the United States in", number_of_links, "clicks")
        #  show_path()
    exit(0)


#  def show_path():



spider()




