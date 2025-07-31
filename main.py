from olx_scraper import OLXScraper
from utils import save_to_csv
import time

def main():
    print("Iniciando scraper da OLX...")
    
    # Configurações
    base_url = "https://www.olx.com.br/imoveis/aluguel/estado-sp"
    max_pages = 3  # Número de páginas para raspar (para demonstração)
    
    # Inicializar scraper
    scraper = OLXScraper()
    
    # Coletar dados
    start_time = time.time()
    imoveis = scraper.scrape_olx(base_url, max_pages)
    elapsed_time = time.time() - start_time
    
    # Salvar resultados
    save_to_csv(imoveis, "output/imoveis_olx.csv")
    
    # Resumo
    print(f"\nScraping concluído!")
    print(f"Tempo total: {elapsed_time:.2f} segundos")
    print(f"Total de imóveis coletados: {len(imoveis)}")
    print(f"Dados salvos em: output/imoveis_olx.csv")

if __name__ == "__main__":
    main()