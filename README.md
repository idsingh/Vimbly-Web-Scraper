# Vimbly Web Scraper

### Prerequisities

Install node & scrappy if not already installed since json2csv, a node module which is used to convert json to csv file.

#### Install json2csv  
```sh
npm install -g json2csv
```
### Running Steps
1. cd into the this tool's directory.
2. Run the below commands
3. ```
    scrapy crawl vimbly -o output.json
    json2csv -i output.json -o output.csv
    ```
4. Output.csv is the output csv file.


