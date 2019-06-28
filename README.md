# Heyjobs jobs scraper

This is a small app that scraps job ads information from Heyjobs [jobs](https://www.heyjobs.co/en-de/jobs) page and load the data into database.

## How to run:
 - run the following commads:
    >`docker-compose run --rm start_dependencies`
    
    > `docker-compose up scraper`
    
 - After running these command, there should be a table `job_ad` with following fields:
    - id
    - uuid
    - title
