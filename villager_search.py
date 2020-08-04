import requests
from bs4 import BeautifulSoup

columns = [
    'name'
    , 'image'
    , 'personality'
    , 'species'
    , 'birthday'
    , 'catchphrase'
    , 'hobbies'
]

def get_villagers():
    villager_url = 'https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)'
    villager_list = []
    page = requests.get(villager_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    sortable_tables = soup.find_all('table', class_='sortable')
    villager_rows = sortable_tables[0].find_all('tr')
    for current_row in villager_rows:
        cells = current_row.find_all('td')
        villager_item = []
        column_pointer = 0
        for c in cells:
            villager_item.append(c.text.strip().strip('"').strip('♂ ').strip('♀ '))
            column_pointer += 1
        villager_list.append(villager_item)
    return villager_list
                
def prompt_for_column():
    print('Which column would you like to search?')
    for i in range (0, len(columns)):
        print('%i.\t%s' % (i, columns[i]))
    search_column = -1
    while int(search_column) < 0 or int(search_column) > len(columns):
        search_column = input('Enter a number between 0 and %i (or Ctrl+C to quit):\t' % len(columns))
    return int(search_column)

def prompt_for_criteria():
    search_criteria = input('\n\nEnter a search term (or Ctrl+C to quit):\t')
    return search_criteria

if __name__ == '__main__':
    search_column = prompt_for_column()
    search_criteria = prompt_for_criteria()
    print('Searching column %s for %s' % (columns[search_column], search_criteria))
    villagers = get_villagers()
    found = []
    for villager in villagers:
        if len(villager) > 0:
            if villager[search_column].upper() == search_criteria.upper():
                found.append(villager)

    print('Found the following villagers:')
    for i in range(0, len(columns)):
        print(columns[i].ljust(10), end='\t')
    print('\n')
    for i in range(0, len(columns)):
        print('-' * len(columns[i].ljust(10)), end='\t')
    print('\n')
    for villager in found:
        for i in range(0, len(columns)):
            print(villager[i].ljust(10), end='\t')
        print('\n') 
