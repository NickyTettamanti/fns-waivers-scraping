import scrapy

class WaiverSpider(scrapy.Spider):
    name = "waiver"
    allowed_domains = ['fns.usda.gov']

    start_urls = [
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Alabama", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Alaska",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Arizona", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Arkansas",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/California", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Colorado",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Connecticut", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Delaware",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Florida", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Georgia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Hawaii", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Idaho",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Illinois", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Indiana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Iowa", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Kansas",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Kentucky", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Louisiana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Maine", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Maryland",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Massachusetts", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Michigan",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Minnesota", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Mississippi",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Missouri", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Montana",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Nebraska", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Nevada",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/New-Hampshire", "https://www.fns.usda.gov/disaster/pandemic/covid-19/New-Jersey",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/New-Mexico", "https://www.fns.usda.gov/disaster/pandemic/covid-19/New-York",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/North-Carolina", "https://www.fns.usda.gov/disaster/pandemic/covid-19/North-Dakota",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Ohio", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Oklahoma",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Oregon", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Pennsylvania",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Rhode-Island", "https://www.fns.usda.gov/disaster/pandemic/covid-19/South-Carolina",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/South-Dakota", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Tennessee",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Texas", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Utah",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Vermont",  "https://www.fns.usda.gov/disaster/pandemic/covid-19/Virginia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Washington", "https://www.fns.usda.gov/disaster/pandemic/covid-19/West-Virginia",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Wisconsin", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Wyoming",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/Virgin-Islands", "https://www.fns.usda.gov/disaster/pandemic/covid-19/Guam",
      "https://www.fns.usda.gov/disaster/pandemic/covid-19/District-of-columbia"
    ]


    def parse(self, response):

        # Pull the table from the url using xpath of table
        table_rows = response.xpath('/html/body/div[2]/div/main/div/div/div[2]/div/div/div/section/table[1]/tbody/tr')

        # Loop through each row of the table
        for table_row in table_rows[1:]:

            yield {
                # The .// retains the xpath above from table_rows.
                'date': table_row.xpath('.//td[1]/text()').extract(),
                'request' : table_row.xpath('.//td[2]/text()').extract(),
                'status' : table_row.xpath('.//td[3]/a/text()').extract(),
                    #todo: extract link to .pdf which is sometimes present, see pdf_request() in items.py
                'url' : response.url,
                'jurisdiction' : response.url.split('covid-19/')[1]
            }