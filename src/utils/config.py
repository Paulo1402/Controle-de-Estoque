import json
import os

from utils import BASEDIR, DEFAULT_SHORT_SKIDS, DEFAULT_LONG_SKIDS, ConfigSection


# Retorna configurações do aplicativo
def get_config(section: ConfigSection = ConfigSection.ALL) -> dict:
    path = os.path.join(BASEDIR, 'config.json')

    # Caso o arquivo não exista ou não possa ser validado, cria um arquivo novo
    try:
        with open(path, 'r', encoding='utf8') as f:
            config = json.loads(f.read())

            # Tenta validar o arquivo, caso não consiga, força o tratamento
            app = config['app']
            database = config['database']

            _ = app['theme']
            _ = app['short_skids']
            _ = app['long_skids']

            _ = database['name']
            _ = database['backup_frequency']
            _ = database['max_backups']
    except (FileNotFoundError, KeyError, ValueError, json.JSONDecodeError):
        config = {
            'app': {
                'theme': 'dark',
                'short_skids': DEFAULT_SHORT_SKIDS,
                'long_skids': DEFAULT_LONG_SKIDS
            },
            'database': {
                'name': '',
                'backup_frequency': 'weekly',
                'max_backups': 5
            }
        }

        set_config(config)

    # Retorna objeto de configuração de acordo com a sessão requerida
    if section == ConfigSection.APP:
        return config['app']
    elif section == ConfigSection.DATABASE:
        return config['database']

    return config


# Seta configurações do aplicativo
def set_config(config: dict, section: ConfigSection = ConfigSection.ALL):
    # Retorna objeto de config completo caso se esteja setando apenas uma sessão
    if section != ConfigSection.ALL:
        old_config = get_config()

        section_name = 'app' if section == ConfigSection.APP else 'database'
        old_config[section_name] = config

        config = old_config

    path = os.path.join(BASEDIR, 'config.json')
    print('set config', config)

    # Devido bugs durante desenvolvimento, aparentemente é necessário limpar o conteúdo do arquivo antes de abrir-lo
    # com previlégios
    with open(path, 'w'):
        pass

    # Cria um arquivo com permissões para escrita e leitura para o SO não impedir a manipulação após compilado e
    # instalado na pasta de aplicativos do Windows
    with open(os.open(path, os.O_RDWR), 'w', encoding='utf8') as f:
        f.write(json.dumps(config, indent=4))