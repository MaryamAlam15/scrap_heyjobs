import re

import requests
from bs4 import BeautifulSoup

from constants import AD_ANCHOR, UUID_REGEX, TITLE


def parse_page(web_link):
    """
    parse the given web link and extract job title and uuid.
    :param web_link:
    :return: job_uuids, job_titles
    """
    job_uuids = []
    job_titles = []

    page_resp = requests.get(web_link)

    if page_resp.status_code == 200:
        page_content = BeautifulSoup(page_resp.content, 'html.parser')
        ad_anchor = page_content.select(AD_ANCHOR)

        for ad in ad_anchor:
            uuid = re.search(UUID_REGEX, ad['href']).group(1)
            title = ad.find(TITLE).getText()
            job_uuids.append(uuid)
            job_titles.append(title)
    else:
        print('error while parsing the page.')

    return job_uuids, job_titles
