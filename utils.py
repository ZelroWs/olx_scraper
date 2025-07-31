import csv
import json

def save_to_csv(data, filename):
    """Salva os dados em um arquivo CSV"""
    if not data:
        print("Nenhum dado para salvar!")
        return
    
    keys = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    
    print(f"Dados salvos com sucesso em {filename}")

def save_to_json(data, filename):
    """Salva os dados em um arquivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Dados salvos com sucesso em {filename}")