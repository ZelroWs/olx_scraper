import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import random

class OLXScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.delay_range = (1, 3)  # Delay entre requisições em segundos
    
    def scrape_olx(self, base_url, max_pages=3):
        all_properties = []
        
        for page in range(1, max_pages + 1):
            url = f"{base_url}?o={page}"
            print(f"Processando página {page}...")
            
            try:
                # Requisição HTTP
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                
                # Parse do HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Encontrar todos os anúncios
                listings = soup.find_all('li', class_='sc-1fcmfeb-2')
                
                for listing in listings:
                    property_data = self._extract_property_data(listing)
                    if property_data:
                        all_properties.append(property_data)
                
                # Delay aleatório entre requisições
                time.sleep(random.uniform(*self.delay_range))
                
            except Exception as e:
                print(f"Erro na página {page}: {str(e)}")
                continue
        
        return all_properties
    
    def _extract_property_data(self, listing):
        try:
            # Extrair título
            title = listing.find('h2', class_='sc-1mbetcw-0').get_text(strip=True)
            
            # Extrair preço
            price_element = listing.find('span', class_='sc-ifAKCX')
            price = price_element.get_text(strip=True) if price_element else "Preço não informado"
            
            # Extrair localização
            location = listing.find('span', class_='sc-7l84qu-1').get_text(strip=True)
            
            # Extrair detalhes (área, quartos)
            details = listing.find('div', class_='sc-1j5op1p-0')
            details_text = details.get_text(" | ", strip=True) if details else ""
            
            # Extrair URL do anúncio
            relative_url = listing.find('a')['href']
            full_url = urljoin("https://www.olx.com.br", relative_url)
            
            return {
                'title': title,
                'price': price,
                'location': location,
                'details': details_text,
                'url': full_url,
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except Exception as e:
            print(f"Erro ao extrair dados do anúncio: {str(e)}")
            return None