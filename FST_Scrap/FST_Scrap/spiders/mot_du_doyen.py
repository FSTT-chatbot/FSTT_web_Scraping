import scrapy
import logging

class Doyen_word(scrapy.Spider):
    name = 'Doyen_word'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        "https://fstt.ac.ma/Portail2023/mot-du-doyen/"
    ]

    def parse(self, response):
        try:
            # Extract the text content from the specified div
            mot_du_doyen = response.css('div.elementor-text-editor.elementor-clearfix').get(default='')
            mot_du_doyen_text = ''.join(response.css('div.elementor-text-editor.elementor-clearfix *::text').getall()).strip()

            if not mot_du_doyen_text:
                logging.warning(f"No text found in 'mot_du_doyen' for URL: {response.url}")

            yield {
                'mot_du_doyen': mot_du_doyen_text,
            }

        except Exception as e:
            logging.error(f"Error parsing {response.url}: {str(e)}")
