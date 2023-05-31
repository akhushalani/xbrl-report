import pdfkit
import os
from pathlib import Path
from io import BytesIO
from urllib.request import Request, urlopen
from zipfile import ZipFile
from urllib.parse import urlparse

def download_and_render(url, name):
    headers = {'User-Agent': 'TestingScript ask9908@me.com', 'Accept-Encoding': 'gzip, deflate', 'Host': 'www.sec.gov'}
    r = Request(url)
    for k, v in headers.items():
        r.add_header(k, v)

    with urlopen(r) as response:
        with ZipFile(BytesIO(response.read())) as zfile:
            directory = f".tmp/{Path(urlparse(url).path).stem}"
            #zfile.extractall(directory)

            report_path = os.path.join(directory, name)
            with open(report_path) as f:
                pdfkit.from_file(f, output_path='output/test_out.pdf', options={"enable-local-file-access": ""})
