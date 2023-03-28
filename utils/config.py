import json
import os

# Caminho relativo ao main.py
BASEDIR = os.path.dirname(os.path.dirname(__file__))


# Retorna configurações do aplicativo
def get_config() -> dict:
    path = os.path.join(BASEDIR, 'config.json')

    # Caso o arquivo não exista ou não possa ser validado, cria um arquivo novo
    try:
        with open(path, 'r', encoding='utf8') as f:
            config = json.loads(f.read())

            # Tenta validar o arquivo, caso não consiga, levanta uma exceção
            try:
                _ = config['theme']
                _ = config['database']
                backups = config['backup']

                _ = backups['frequency']
                _ = backups['max_backups']
            except (KeyError, ValueError):
                raise FileNotFoundError
    except (FileNotFoundError, json.JSONDecodeError):
        config = {
            'theme': 'dark',
            'database': None,
            'backup': {
                'frequency': 'weekly',
                'max_backups': 5
            }
        }

        set_config(config)

    return config


# Seta configurações do aplicativo
def set_config(config: dict):
    path = os.path.join(BASEDIR, 'config.json')
    print('set config', config)

    # Por alguma razão às vezes buga quando o arquivo possui contéudo e é aberto usando o modulo os,
    # portanto é necessário limpar o contéudo primeiro
    with open(path, 'w'):
        pass

    # Cria um arquivo com permissões para escrita e leitura.
    # Isso é necessário para quando o aplicativo for compilado e instalado no diretório padrão de apps no Windows,
    # o SO não impedir a manipulação do arquivo de configuração
    with open(os.open(path, os.O_RDWR), 'w', encoding='utf8') as f:
        f.write(json.dumps(config, indent=4))
