import requests
from bs4 import BeautifulSoup


def spider():
    number_of_links = 1
    found = False
    while found is False or number_of_links < 4:
        url = "https://en.wikipedia.org/wiki/Quebec_Route_112"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        found = check_if_usa(url, number_of_links, url)
        if not found:
            for link in soup.findAll('a'):
                href = str(link.get('href'))
                if href.startswith(r"/wiki/"):
                    link_url_1 = "https://en.wikipedia.org"+href
                    check_if_usa(link_url_1, number_of_links, url)
                    if number_of_links is 2:
                        new_url_1(link_url_1, number_of_links)
        number_of_links += 1


def new_url_1(link_url_1, number_of_links):
    source_code = requests.get(link_url_1)
    path_url = link_url_1
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = str(link.get('href'))
        if href.startswith(r"/wiki/") and not href.__contains__("Portal:"):
            link_url_2 = "https://en.wikipedia.org" + href
            check_if_usa(link_url_2, number_of_links, path_url)
            if number_of_links is 3:
                new_url_2(link_url_2, number_of_links)


def new_url_2(link_url_2, number_of_links):
    source_code = requests.get(link_url_2)
    path_url = link_url_2
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = str(link.get('href'))
        if href.startswith(r"/wiki/") and not href.__contains__("Portal:"):
            link_url_3 = "https://en.wikipedia.org" + href
            check_if_usa(link_url_3, number_of_links, path_url)
            if number_of_links is 4:
                new_url_3(link_url_3, number_of_links)


def new_url_3(link_url_3, number_of_links):
    source_code = requests.get(link_url_3)
    path_url = link_url_3
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = str(link.get('href'))
        if href.startswith(r"/wiki/") and not href.__contains__("Portal:"):
            link_url_4 = "https://en.wikipedia.org" + href
            check_if_usa(link_url_4, number_of_links, path_url)


def check_if_usa(url, number_of_links, path_url):
    if url == "https://en.wikipedia.org/wiki/United_States":
        show_results(number_of_links, path_url)
        return True


def show_results(number_of_links, path_url):
    if number_of_links is 1:
        print("You can get to the United States in", number_of_links, "click")
        show_path(path_url)
    else:
        print("You can get to the United States in", number_of_links, "clicks")
        show_path(path_url)
    exit(0)


def show_path(path_url):
    print("Path is \n/wiki/Quebec_Route_112\n"+path_url[24:]+"\n/wiki/United_States")
    quit()


spider()
