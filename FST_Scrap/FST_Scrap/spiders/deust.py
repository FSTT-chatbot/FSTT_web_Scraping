import logging
import re
import scrapy

class Deust(scrapy.Spider):
    name = 'Deust'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/biologie-chimie-geologie/',
        'https://fstt.ac.ma/Portail2023/genie-electrique-genie-mecanique/',
        'https://fstt.ac.ma/Portail2023/mathematique-informatique-physique/',
        'https://fstt.ac.ma/Portail2023/mathematiques-informatique-physique-chimie/'
    ]

    def parse(self, response):
        # Extracting the content using css selectors
        name = response.css('h2.elementor-heading-title.elementor-size-default::text').get()
        description = response.css('div#objectifs--tab p::text').get()
        Competences = response.css('div#competences-visees-et-debouches-tab p::text').get()
        def extract_coordinator_info(response):
            coordinator_info = response.xpath('//div[@id="coordinateur-tab"]//p//text() | //div[@id="coordinateur-tab"]/text()').extract()
            if not coordinator_info:
                coordinator_info = response.xpath('//div[@id="coordinateur-tab"]//strong//text()').extract()
            coordinator_info = " ".join([text.strip() for text in coordinator_info if text.strip()])
            return coordinator_info

        coordinator_info = extract_coordinator_info(response)
        if not coordinator_info:
            logging.warning(f"No coordinator info found for URL: {response.url}")

        Coordinnateur_pedagogique_name = ''
        Coordinnateur_pedagogique_email = ''
        name_match = re.search(r'Pr\.\s*([A-Za-z\s\-]+)', coordinator_info)
        if name_match:
            Coordinnateur_pedagogique_name = name_match.group(1).strip()

        email_match = re.search(r'[\w\.-]+@[\w\.-]+', coordinator_info)
        if email_match:
            Coordinnateur_pedagogique_email = email_match.group(0).strip()
        PROGRAMME_s1_1= response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[1]').get().strip()
        PROGRAMME_s1_2 = response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[2]').get().strip()
        PROGRAMME_s1_3= response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[3]').get().strip()
        PROGRAMME_s1_4 = response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[4]').get().strip()
        PROGRAMME_s1_5= response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[5]').get().strip()
        PROGRAMME_s1_6 = response.xpath('//table[@id="Mpro"]/tbody/tr[1]/td/text()[6]').get().strip()
        PROGRAMME_s2_1 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[1]').get().strip()
        PROGRAMME_s2_2 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[2]').get().strip()
        PROGRAMME_s2_3 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[3]').get().strip()
        PROGRAMME_s2_4 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[4]').get().strip()
        PROGRAMME_s2_5 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[5]').get().strip()
        PROGRAMME_s2_6 = response.xpath('//table[@id="Mpro"]/tbody/tr[2]/td/text()[6]').get().strip()
#
        PROGRAMME_s3_1= response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[1]').get().strip()
        PROGRAMME_s3_2 = response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[2]').get().strip()
        PROGRAMME_s3_3= response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[3]').get().strip()
        PROGRAMME_s3_4 = response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[4]').get().strip()
        PROGRAMME_s3_5= response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[5]').get().strip()
        PROGRAMME_s3_6 = response.xpath('//table[@id="Mpro"]/tbody/tr[3]/td/text()[6]').get().strip()
        PROGRAMME_s4_1 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[1]').get().strip()
        PROGRAMME_s4_2 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[2]').get().strip()
        PROGRAMME_s4_3 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[3]').get().strip()
        PROGRAMME_s4_4 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[4]').get().strip()
        PROGRAMME_s4_5 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[5]').get().strip()
        PROGRAMME_s4_6 = response.xpath('//table[@id="Mpro"]/tbody/tr[4]/td/text()[6]').get().strip()


        yield {
            'name': name,
            'description': description,
            'Competences': Competences,
            'Coordinnateur_pedagogique_name': Coordinnateur_pedagogique_name,
            'Coordinnateur_pedagogique_email': Coordinnateur_pedagogique_email,
            'PROGRAMME_s1_1': PROGRAMME_s1_1,
            'PROGRAMME_s1_2': PROGRAMME_s1_2,
            'PROGRAMME_s1_3': PROGRAMME_s1_3,
            'PROGRAMME_s1_4': PROGRAMME_s1_4,
            'PROGRAMME_s1_5': PROGRAMME_s1_5,
            'PROGRAMME_s1_6': PROGRAMME_s1_6,
            'PROGRAMME_s2_1': PROGRAMME_s2_1,
            'PROGRAMME_s2_2': PROGRAMME_s2_2,
            'PROGRAMME_s2_3': PROGRAMME_s2_3,
            'PROGRAMME_s2_4': PROGRAMME_s2_4,
            'PROGRAMME_s2_5': PROGRAMME_s2_5,
            'PROGRAMME_s2_6': PROGRAMME_s2_6,
            'PROGRAMME_s3_1': PROGRAMME_s3_1,
            'PROGRAMME_s3_2': PROGRAMME_s3_2,
            'PROGRAMME_s3_3': PROGRAMME_s3_3,
            'PROGRAMME_s3_4': PROGRAMME_s3_4,
            'PROGRAMME_s3_5': PROGRAMME_s3_5,
            'PROGRAMME_s3_6': PROGRAMME_s3_6,
            'PROGRAMME_s4_1': PROGRAMME_s4_1,
            'PROGRAMME_s4_2': PROGRAMME_s4_2,
            'PROGRAMME_s4_3': PROGRAMME_s4_3,
            'PROGRAMME_s4_4': PROGRAMME_s4_4,
            'PROGRAMME_s4_5': PROGRAMME_s4_5,
            'PROGRAMME_s4_6': PROGRAMME_s4_6,


        }

        # Further data extraction logic for courses can be added here
