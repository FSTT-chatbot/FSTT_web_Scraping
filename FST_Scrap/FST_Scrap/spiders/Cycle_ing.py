import re
import scrapy
import logging

class Cycle(scrapy.Spider):
    name = 'Cycle'
    allowed_domains = ['fstt.ac.ma']
    start_urls = [
        'https://fstt.ac.ma/Portail2023/di-logiciels-et-systemes-intelligents/',
        'https://fstt.ac.ma/Portail2023/genie-electrique-et-managementindustriel/',
        'https://fstt.ac.ma/Portail2023/di-genie-industriel/',
        'https://fstt.ac.ma/Portail2023/di-geoinformation/'
    ]

    def parse(self, response):
        try:
            name = response.css('h2.elementor-heading-title.elementor-size-default::text').get()
            if not name:
                logging.warning(f"No name found for URL: {response.url}")
                name = ''

            def extract_text(selectors):
                texts = []
                for selector in selectors:
                    elements = response.css(selector).getall()
                    if elements:
                        texts.extend(elements)
                return " ".join(texts).strip()

            description_selectors = ['div#objectifs--tab p::text', 'div#objectifs--tab ul li::text', 'div#objectifs--tab ol li::text']
            competences_selectors = ['div#competences-visees-et-debouches-tab p::text', 'div#competences-visees-et-debouches-tab ul li::text', 'div#competences-visees-et-debouches-tab ol li::text']

            description = extract_text(description_selectors) or response.css('div#objectifs--tab::text').get(default='').strip()
            if not description:
                logging.warning(f"No description found for URL: {response.url}")

            Competences = extract_text(competences_selectors) or response.css('div#competences-visees-et-debouches-tab::text').get(default='').strip()
            if not Competences:
                logging.warning(f"No Competences found for URL: {response.url}")

            def extract_coordinator_text(xpath_selector):
                texts = response.xpath(xpath_selector).extract()
                texts = [text.strip() for text in texts if text.strip()]  # Clean and filter out empty texts
                return " ".join(texts)

            coordinator_info = extract_coordinator_text('//div[@id="coordinateur-tab"]//text()')
            if not coordinator_info:
                coordinator_info = extract_coordinator_text('//div[@id="coordinateur-tab"]//p/text()')

            Coordinnateur_pedagogique_name = ''
            Coordinnateur_pedagogique_email = ''
            name_match = re.search(r'Pr\.\s*([A-Za-z\s\-]+)', coordinator_info)
            if name_match:
                Coordinnateur_pedagogique_name = name_match.group(1).strip()

            email_match = re.search(r'[\w\.-]+@[\w\.-]+', coordinator_info)
            if email_match:
                Coordinnateur_pedagogique_email = email_match.group(0).strip()
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

            def extract_programme_text(tr_index, td_index):
                text = response.xpath(f'//table[@id="Mpro"]/tbody/tr[{tr_index}]/td/text()[{td_index}]').get()
                if not text:
                    text = response.xpath(f'//table[@id="Mpro"]/tbody/tr[{tr_index}]/td/p/text()[{td_index}]').get()
                return text.strip() if text else ''

            PROGRAMME_s1_1 = extract_programme_text(1, 1)
            PROGRAMME_s1_2 = extract_programme_text(1, 2)
            PROGRAMME_s1_3 = extract_programme_text(1, 3)
            PROGRAMME_s1_4 = extract_programme_text(1, 4)
            PROGRAMME_s1_5 = extract_programme_text(1, 5)
            PROGRAMME_s1_6 = extract_programme_text(1, 6)
            PROGRAMME_s2_1 = extract_programme_text(2, 1)
            PROGRAMME_s2_2 = extract_programme_text(2, 2)
            PROGRAMME_s2_3 = extract_programme_text(2, 3)
            PROGRAMME_s2_4 = extract_programme_text(2, 4)
            PROGRAMME_s2_5 = extract_programme_text(2, 5)
            PROGRAMME_s2_6 = extract_programme_text(2, 6)
            PROGRAMME_s3_1 = extract_programme_text(3, 1)
            PROGRAMME_s3_2 = extract_programme_text(3, 2)
            PROGRAMME_s3_3 = extract_programme_text(3, 3)
            PROGRAMME_s3_4 = extract_programme_text(3, 4)
            PROGRAMME_s3_5 = extract_programme_text(3, 5)
            PROGRAMME_s3_6 = extract_programme_text(3, 6)
            PROGRAMME_s4_1 = extract_programme_text(4, 1)
            PROGRAMME_s4_2 = extract_programme_text(4, 2)
            PROGRAMME_s4_3 = extract_programme_text(4, 3)
            PROGRAMME_s4_4 = extract_programme_text(4, 4)
            PROGRAMME_s4_5 = extract_programme_text(4, 5)
            PROGRAMME_s4_6 = extract_programme_text(4, 6)
            PROGRAMME_s5_1 = extract_programme_text(5, 1)
            PROGRAMME_s5_2 = extract_programme_text(5, 2)
            PROGRAMME_s5_3 = extract_programme_text(5, 3)
            PROGRAMME_s5_4 = extract_programme_text(5, 4)
            PROGRAMME_s5_5 = extract_programme_text(5, 5)
            PROGRAMME_s5_6 = extract_programme_text(5, 6)
            PROGRAMME_s6 = extract_programme_text(6, 1)

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
                'PROGRAMME_s5_1': PROGRAMME_s5_1,
                'PROGRAMME_s5_2': PROGRAMME_s5_2,
                'PROGRAMME_s5_3': PROGRAMME_s5_3,
                'PROGRAMME_s5_4': PROGRAMME_s5_4,
                'PROGRAMME_s5_5': PROGRAMME_s5_5,
                'PROGRAMME_s5_6': PROGRAMME_s5_6,
                'PROGRAMME_s6': PROGRAMME_s6,
            }

        except Exception as e:
            logging.error(f"Error parsing {response.url}: {str(e)}")
