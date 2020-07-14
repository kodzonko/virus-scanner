class FileHandler:
    scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    scan_params = {'apikey': f'{api_key}'}

    file = input("Proszę podać ścieżkę do pliku: ")
