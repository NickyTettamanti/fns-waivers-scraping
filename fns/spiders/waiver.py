import scrapy

class WaiverSpider(scrapy.Spider):
    name = "waiver"
    allowed_domains = ['fns.usda.gov']

    start_urls = [
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/alabama", "https://www.fns.usda.gov/disaster/pandemic/covid-19/alaska",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/arizona", "https://www.fns.usda.gov/disaster/pandemic/covid-19/arkansas",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/california", "https://www.fns.usda.gov/disaster/pandemic/covid-19/colorado",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/connecticut", "https://www.fns.usda.gov/disaster/pandemic/covid-19/delaware",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/florida", "https://www.fns.usda.gov/disaster/pandemic/covid-19/georgia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/hawaii", "https://www.fns.usda.gov/disaster/pandemic/covid-19/idaho",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/illinois", "https://www.fns.usda.gov/disaster/pandemic/covid-19/indiana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/iowa", "https://www.fns.usda.gov/disaster/pandemic/covid-19/kansas",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/kentucky", "https://www.fns.usda.gov/disaster/pandemic/covid-19/louisiana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/maine", "https://www.fns.usda.gov/disaster/pandemic/covid-19/maryland",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/massachusetts", "https://www.fns.usda.gov/disaster/pandemic/covid-19/michigan",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/minnesota", "https://www.fns.usda.gov/disaster/pandemic/covid-19/mississippi",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/missouri", "https://www.fns.usda.gov/disaster/pandemic/covid-19/montana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/nebraska", "https://www.fns.usda.gov/disaster/pandemic/covid-19/nevada",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/new-hampshire", "https://www.fns.usda.gov/disaster/pandemic/covid-19/new-jersey",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/new-mexico", "https://www.fns.usda.gov/disaster/pandemic/covid-19/new-york",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/north-carolina", "https://www.fns.usda.gov/disaster/pandemic/covid-19/north-dakota",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/ohio", "https://www.fns.usda.gov/disaster/pandemic/covid-19/oklahoma",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/oregon", "https://www.fns.usda.gov/disaster/pandemic/covid-19/pennsylvania",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/rhode-island", "https://www.fns.usda.gov/disaster/pandemic/covid-19/south-carolina",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/south-dakota", "https://www.fns.usda.gov/disaster/pandemic/covid-19/tennessee",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/texas", "https://www.fns.usda.gov/disaster/pandemic/covid-19/utah",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/vermont",  "https://www.fns.usda.gov/disaster/pandemic/covid-19/virginia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/washington", "https://www.fns.usda.gov/disaster/pandemic/covid-19/west-Virginia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/wisconsin", "https://www.fns.usda.gov/disaster/pandemic/covid-19/wyoming",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/virgin-islands", "https://www.fns.usda.gov/disaster/pandemic/covid-19/guam",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/district-of-columbia"
    ]

    def parse(self, response):

        # SNAP
        # Pull the table from the url using xpath of table
        SNAPtable_rows = response.xpath('/html/body/div[2]/div/main/div/div/div[2]/div/div/div/section/table[1]/tbody/tr')
        ChildNutritiontable_rows = response.xpath('/html/body/div[2]/div/main/div/div/div[2]/div/div/div/section/table[2]/tbody/tr')
        USDAtable_rows = response.xpath('/html/body/div[2]/div/main/div/div/div[2]/div/div/div/section/table[3]/tbody/tr')
        WICtable_rows = response.xpath('/html/body/div[2]/div/main/div/div/div[2]/div/div/div/section/table[4]/tbody/tr')


        # Loop through each row of the table
        for table_row in SNAPtable_rows[1:]:
            yield {
                # The .// retains the xpath above from table_rows.
                'program' : "SNAP",
                'jurisdiction': response.url.split('covid-19/')[1],
                'date': table_row.xpath('.//td[1]/text()').extract(),
                'request' : table_row.xpath('.//td[2]/text()').extract(),
                'request_receive' : table_row.xpath('.//td[2]/a/text()').extract(),
                'status' : table_row.xpath('.//td[3]/a/text()').extract(),
                'url' : response.url
            }

        for table_row in ChildNutritiontable_rows[1:]:
            yield {
                # The .// retains the xpath above from table_rows.
                'program' : "Child Nutrition",
                'jurisdiction': response.url.split('covid-19/')[1],
                'date': table_row.xpath('.//td[1]/text()').extract(),
                'request' : table_row.xpath('.//td[2]/text()').extract(),
                'request_receive': table_row.xpath('.//td[2]/a/text()').extract(),
                'status' : table_row.xpath('.//td[3]/a/text()').extract(),
                'url' : response.url
            }

        for table_row in USDAtable_rows[1:]:
            yield {
                # The .// retains the xpath above from table_rows.
                'program' : "USDA Foods Programs",
                'jurisdiction': response.url.split('covid-19/')[1],
                'date': table_row.xpath('.//td[1]/text()').extract(),
                'request' : table_row.xpath('.//td[2]/text()').extract(),
                'request_receive': table_row.xpath('.//td[2]/a/text()').extract(),
                'status' : table_row.xpath('.//td[3]/a/text()').extract(),
                'url' : response.url
            }

        for table_row in WICtable_rows[1:]:
            yield {
                # The .// retains the xpath above from table_rows.
                'program' : "WIC",
                'jurisdiction': response.url.split('covid-19/')[1],
                'date': table_row.xpath('.//td[1]/text()').extract(),
                'request' : table_row.xpath('.//td[2]/text()').extract(),
                'request_receive': table_row.xpath('.//td[2]/a/text()').extract(),
                'status' : table_row.xpath('.//td[3]/a/text()').extract(),
                'url' : response.url
            }