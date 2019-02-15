from pathlib import Path

from image_downloader.constant import HTTP_HEADER
import requests


class Crawler(object):
    def __init__(self,urls_file_folder):
        self.destination_path = Path(urls_file_folder)
        if not self.destination_path.is_dir() :
            raise TypeError("Invalid file folder")

    def download(self,url):
        response = requests.get(url, headers=HTTP_HEADER)
        image_name = url.rsplit('/',1)[-1]
        if response.status_code == 200 :
            with open(self.destination_path/image_name,'wb') as f:
                f.write(response.body)
        else:
            # TODO
            pass

