import scrapy

class TableSpider(scrapy.Spider):
    name = 'table_conseil'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/conseil-de-letablissement/'
    ]

    def parse(self, response):
        # Select the table
        table = response.xpath('//table[@id="eael-data-table-4c039334"]')
        
        # Iterate over each row in the table body
        rows = table.xpath('.//tbody/tr')
        for row in rows:
            # Extract the text from each cell in the row
            name = row.xpath('./td[1]//div[@class="td-content"]/text()').get().strip()
            responsibility = row.xpath('./td[2]//div[@class="td-content"]/text()').get().strip()

            yield {
                'name': name,
                'responsibility': responsibility
            }
