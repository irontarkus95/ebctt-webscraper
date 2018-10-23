from bs4 import BeautifulSoup

def scrape_ebctt(fname, lname, street_name):
    url = 'https://www.ebctt.com/electoral-process/registration-look-up/'

    form_data = {
        'firstname': fname,
        'lastname': lname,
        'address': street_name,
        'check-registration': 'Check Registration Polling Station',
    }

    response = requests.get(url, params=form_data)

    soup = BeautifulSoup(response.content, 'html.parser')

    name = soup.find('h2', class_='entry-title post-title').get_text()
    address = soup.find(class_='meta-prep meta-prep-author posted').get_text().strip('\n').lstrip()

    # Scrapes web page and returns top result from query
    return name, address



