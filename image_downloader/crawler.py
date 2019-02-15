import logging
from pathlib import Path

import time

from image_downloader.constant import HTTP_HEADER
import requests


class Crawler(object):
    def __init__(self, urls_iterator,download_folder):
        self.urls = urls_iterator
        self.destination_path = Path(download_folder)
        self.delay_time = 1

    def download_image(self, url):
        response = requests.get(url, headers=HTTP_HEADER)
        image_name = url.rsplit('/', 1)[-1]
        if response.status_code == 200:
            with open(self.destination_path.joinpath(image_name), 'wb') as f:
                f.write(response.body)
        else:
            message = '{},{},{}'.format(self.destination_path, url,
                                        response.status_code)
            logging.warning(message)

    def run(self):
        for url in self.urls:
            self.download_image(url)
            time.sleep(self.delay_time)