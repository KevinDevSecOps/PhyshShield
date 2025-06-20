import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

def scan_url(url):
    """Escanea una URL con VirusTotal."""
    params = {
        'apikey': config['virustotal']['api_key'],
        'url': url
    }
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
    return response.json()

def get_report(resource):
    """Obtiene el reporte de una URL escaneada."""
    params = {
        'apikey': config['virustotal']['api_key'],
        'resource': resource
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
    return response.json()
