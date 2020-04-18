# slickscraper

Scrapy project, used to scrape info off of slickdeals.net. Scrapes the following:
* Item title
* Item price
* Item old price (if available)
* Item store
* Item link

Exports the info into a SQLite3 .db file, but can also do the -o items.csv export
The .csv and .db files within this repository are example outputs of the scraper (ran on 11:21AM EST March 21st, 2020)

Features:
* SQLite3 .db exporting built in (will delete + create a new table if it exists)
* Data cleaning features (uses .strip and re.sub to remove whitespace and replace html entities). These data cleaning features are defensive, and use try/except.

Room to grow:
* Expand the re.sub formula. It currently uses a list of HTML entities that were the most common in the outputs of this scraper, but there is a chance that another entity could pop up that would not be caught by the cleaner. Importing a more complete table of these entities (or figuring out if there is a better way to clean this) would be useful.
* Maybe figure out a different output? PostgreSQL is not that different in syntax from SQLite3. Definitely doable, but I don't see a reason to change output.
