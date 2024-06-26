# AmazoScrape 

AmazoScrape is a robust web scraping project designed to extract essential details from Amazon product webpages efficiently. This project leverages a powerful tech stack including Django, Redis, Celery, Bright Data, Jupyter Notebook, and Selenium to bypass captchas and ensure accurate data retrieval. All scraped data is stored in a Django-managed SQLite database.

## Key Features

- **Efficient Web Scraping**: Utilizes Selenium for dynamic content extraction and captcha bypassing, ensuring high accuracy and reliability.
- **Asynchronous Task Management**: Employs Celery and Redis for handling asynchronous scraping tasks, optimizing performance, and scalability.
- **Bright Data Integration**: Incorporates Bright Data for rotating proxies, enhancing the ability to scrape without getting blocked.
- **Data Storage**: Uses Django’s ORM to store extracted data in an SQLite database, ensuring easy access and manipulation.
- **Interactive Data Analysis**: Jupyter Notebook integration for seamless data analysis and visualization.
- **Scalable Architecture**: Built with Django to ensure modularity and scalability for future enhancements.
