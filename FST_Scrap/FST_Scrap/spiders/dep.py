import scrapy
import logging

class DepartmentSpider(scrapy.Spider):
    name = 'department_spider'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/les-departement/'
    ]

    def parse(self, response):
        try:
            sections = response.css('section.has_eae_slider')
            for section in sections:
                department = section.css('h3.elementor-cta__title::text').get()
                chef_text = section.css('div.elementor-cta__description::text').get()
                chef = chef_text.split(':')[1].strip() if chef_text else None
                email_text = section.css('div.elementor-cta__description').re(r'Email\s*:\s*(\S+@\S+\.\S+)')
                email = email_text[0] if email_text else None

                if not department:
                    logging.warning(f"No department found for URL: {response.url}")

                yield {
                    'url': response.url,
                    'department': department,
                    'chef': chef,
                    'email': email,
                }

        except Exception as e:
            logging.error(f"Error parsing {response.url}: {str(e)}")
