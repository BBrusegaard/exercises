import urllib.request


def generate_urls():
    url_template = "https://www.xboxgamertag.com/leaderboards/"
    urls = []
    for page in range(1720,1722):
        new_url = url_template + str(page) + "/"
        urls.append(new_url)
    return urls
    
def download_url(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')
    
def save_file(filename, contents):
    the_file = open(filename,"w")
    the_file.write(contents)
    the_file.close()
    
def main():
    urls = generate_urls()
    counter = 0
    for url in urls:
        counter += 1
        contents = download_url(url)
        save_file("webpage" + str(counter), contents)
main()