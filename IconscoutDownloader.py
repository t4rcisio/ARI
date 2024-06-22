from bs4 import BeautifulSoup
import requests

class IconscoutDownloader:
    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            meta = soup.find('meta', property="og:video")
            if meta:
                return meta['content']

            meta = soup.find('meta', property="og:image")
            if meta:
                return meta['content']

            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# Example usage:

while True:
    url = input()
    content = IconscoutDownloader.get(url)
    print(content)
