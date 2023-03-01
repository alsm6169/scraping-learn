# scraping-learn
Learn scraping website step-by-step
1. 01_wikipedia_tables.py: For scraping using pandas when data on website are in tabular format

2. 02_github_list.py: Using Gazpacho library for scraping. This library is similar to BeautifulSoup but much simpler to use.  

3. 03_1_google_finance.py: Using Selenium to load a site with dynamic content (google finance). 
Note: Since in this way we are providing the input in URL, we really don't need selenium except to wait to check that site is loaded.  
4. 03_2_google_finance_selenium.py: This one uses the power of Selenium for the first time by filling in the text box, submitting the request, waiting for the response and storing the response

5. 04_galaxus_js.py: Similar to 3.2 loading from a marketplace website the most sold product information

6. 05_1_load_more_click.py: Using Selenium quering a website, fetching the result, then clicking on 'load more' button and storing the result again
7. 05_2_next_page_click.py:  Using Selenium quering a website, fetching the result, then clicking on 'next page' button and storing the result again
