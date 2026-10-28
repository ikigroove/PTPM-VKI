from src.parser import ForumParser

parser = ForumParser()
url = 'https://www.xda-developers.com/i-thought-pi-hole-was-blocking-everything-on-my-network-ipv6-was-letting-half-my-devices-walk-past-it/'

if __name__ == '__main__':
    parser.parse_page(url)