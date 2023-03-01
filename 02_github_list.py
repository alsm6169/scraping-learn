import pandas as pd
from gazpacho import get, Soup


def parse(row: Soup) -> (str, str, str, int):
    # print('title: ', row.find('h1', {'class': 'h3 lh-condensed'}).strip())
    # print('description: ', row.find('p', {'class': 'col-9 color-fg-muted my-1 pr-4'}).strip())
    # print('link: ', base_url + row.find('h1', {'class': 'h3 lh-condensed'}).find('a').attrs['href'])
    # print('stars: ', row.find('a', {'href': 'stargazers'}).strip())
    try:
        title = row.find('h1', {'class': 'h3 lh-condensed'}).strip()
        description = row.find('p', {'class': 'col-9 color-fg-muted my-1 pr-4'}).strip()
        link = base_url + row.find('h1', {'class': 'h3 lh-condensed'}).find('a').attrs['href']
        stars = int(row.find('a', {'href': 'stargazers'}).strip().replace(',',''))
    except AttributeError as exp:
        return None, None, None, None

    return title, description, link, stars


base_url = 'https://github.com'
suffix = '/trending/python'
params = {
    'since': 'weekly',
    'spoken_language_code': 'en'
}
header = {'User-Agent': 'gazpacho'}

html = get(base_url+suffix, params=params, headers=header)
# file = open('trending.html', 'w')
# file.write(html)
# file.close()
# exit(0)
# html = open('trending.html', 'r').read()
# print(f'type html {type(html)}')
soup = Soup(html)
# print(f'type soup: {type(soup)}')
box_rows = soup.find('article', {'class': 'Box-row'})
# print('type(box_rows)={}, type(box_rows[0])={}'.format(type(box_rows), type(box_rows[0])))
list_data = []
list_data = [(parse(row)) for row in box_rows]

df_trending = pd.DataFrame(columns=['title', 'description', 'link', 'stars'], data=list_data)
df_trending = df_trending.dropna().sort_values(by=['stars'], ascending=False)
pd.set_option('display.max_columns', None)
print(df_trending[['title', 'description', 'stars']].head(5))
# df_trending.to_csv('./df_trending.csv')

