import requests
import time
from pymongo import MongoClient

# Verbindung zur MongoDB herstellen
client = MongoClient('mongodb://localhost:27017/')
db = client['domain_database']
domains_collection = db['domains']
invalid_domains_collection = db['invalid_domains']

# Namecheap API-Schlüssel und Benutzername
api_user = 'dein_api_benutzername'
api_key = 'dein_api_schluessel'
client_ip = 'deine_ip_adresse'

# Funktion zur Überprüfung der Domain mit Namecheap API
def check_domain(domain):
    url = f"https://api.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={api_user}&ClientIp={client_ip}&Command=namecheap.domains.check&DomainList={domain}"
    try:
        response = requests.get(url)
        if '<Available>true</Available>' in response.text:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

while True:
    # Domains aus der MongoDB abrufen, sortiert nach der neuesten
    domains = domains_collection.find().sort('_id', -1)

    # Überprüfung der Domains und Sortierung
    for domain_entry in domains:
        domain = domain_entry['domain']
        if not check_domain(domain):
            invalid_domains_collection.insert_one({'domain': domain})
        time.sleep(1)  # 1 Sekunde Pause nach jeder Überprüfung
