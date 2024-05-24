import scrapy

class present(scrapy.Spider):
    name = 'present'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/presentation/'
    ]

    def parse(self, response):
        # Use XPath to find <p> tags that contain <strong> with a nested <u> tag
        paragraphs = response.xpath('//div[contains(@class, "elementor-text-editor") and contains(@class, "elementor-clearfix")]//p[.//strong/u]')
        
        for paragraph in paragraphs:
            # Extract all <u> tags within <strong> tags inside the <p>
            u_texts = paragraph.xpath('.//strong/u/text()').getall()
            for u_text in u_texts:
                # Extract the next sibling <p> tag text
                next_paragraph = paragraph.xpath('following-sibling::p[1]')
                next_paragraph_text = next_paragraph.xpath('text()').get()

                yield {
                    'presentation': u_text.strip(),
                    'description': next_paragraph_text.strip() if next_paragraph_text else None
                }
