# slickscraper
Webscraper for Slickdeals.com that stores data in either SQLite or PostgreSQL

Scrapy project, used to scrape info off of slickdeals.net. Scrapes the following:
* Item title
* Item price
* Item old price (if available)
* Item store
* Item link
* Item date (only on the PostgreSQL version)

There are two versions;
* The SQLite is the 1st version (and was created first), does not feature a lasting database (will drop the existing table if it exists), and outputs the information as an SQLite .db file.
* The PostgreSQL is the 2nd version (and was created second), and features a lasting database (pipeline will check if an entry already exists, and if it does, will not write a second one), and features a data column. It can easily be configered to run on a daily process, and a run.py file is included in the folder so it can easily be set up in CRON for example. I personally have it running on a Raspberry Pi, checking every hour.

Common features:
* Data cleaning features (uses .strip and re.sub to remove whitespace and replace html entities). These data cleaning features are defensive, and use try/except.

Room to grow:
* A way to check whether each item is still on sale would be very useful, but I feel it would require other libraries.
