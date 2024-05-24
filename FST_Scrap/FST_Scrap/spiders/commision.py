import scrapy

class commission(scrapy.Spider):
    name = 'commission'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/commission-scientifique/'
    ]

    def parse(self, response):
        # Select the table
        table = response.xpath('//table[@id="eael-data-table-60c2b8f2"]')
        
        # Iterate over each row in the table body
        rows = table.xpath('.//tbody/tr')
        for row in rows:
            # Extract the text from each cell in the row
            membre = row.xpath('./td[1]//div[@class="td-content"]/text()').get().strip()
            Responsabilite = row.xpath('./td[2]//div[@class="td-content"]/text()').get().strip()

            yield {
                'membre': membre,
                'Responsabilité': Responsabilite
            }
