# Heyjobs jobs scraper

This is a small app that scraps job ads information from Heyjobs [jobs](https://www.heyjobs.co/en-de/jobs) page and load the data into database.

## How to run:
 - clone the repo.
 - build docker container:
    > docker-compose build --no-cache
    
 - Then, run the following commands:
    >`docker-compose run --rm start_dependencies`
    
    > `docker-compose up scraper`
    
 - After running these command, there should be a table `job_ad` in your postgres docker container with following fields:
    - id
    - uuid
    - title
    
## Testing
 - Run the following cmd for tests:
    > `docker-compose run test` 
