# Vimbly Web Scraper

### Prerequisities

Install node & scrapy if not already installed since json2csv, a node module which is used to convert json to csv file.

#### Install json2csv  
```sh
npm install -g json2csv
```
### Running Steps
1. cd into the this tool's directory.
2. Run the below commands
3. ```sh
    scrapy crawl vimbly -o output.json
    json2csv -i output.json -o output.csv
    ```
    Output.csv is the output csv file.


