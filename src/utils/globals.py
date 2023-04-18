"""Constantes usadas ao longo do programa."""
import os
from pathlib import Path

APP_NAME = 'Controle de Estoque'

# Caminho relativo ao main.py (.exe quando compilado)
BASEDIR = Path(__file__).parent.parent

# Caminho para criar e manipular arquivos auxiliares (log, config)
APPDATA_DIR = BASEDIR

# Diretórios Windows com restrição de escrita
windows_installation_paths = [
    os.getenv('ProgramFiles(x86)'),
    os.getenv('ProgramW6432')
]

# Caso o app for instalado em um dos diretórios com restrições de escrita no Windows altera o diretório
# para criar arquivos auxiliares.
for path in windows_installation_paths:
    if BASEDIR.is_relative_to(path):
        APPDATA_DIR = os.path.join(os.getenv('APPDATA'), APP_NAME)

        if not os.path.exists(APPDATA_DIR):
            os.mkdir(APPDATA_DIR)

        break

# HTML com instruções do aplicativo
HELP = os.path.join(BASEDIR, 'static', 'help.html')

# Desativa warnings
DEBUG = False

# Constantes para o cálculo do pezinho
DEFAULT_LONG_SKIDS = 0.00306
DEFAULT_SHORT_SKIDS = 0.00405

# Cores dos temas
DARK_COLOR = '#f4d1ae'
LIGHT_COLOR = '#346685'

# Tabelas e campos da tabela
TABLES = {
    'ciclo': ['ciclo', 'estufa', 'finalidade', 'entrada', 'saida'],
    'bitola': ['bitola_id', 'ciclo', 'bitola', 'fardos', 'volume_tratado'],
    'nfe_info': ['nfe', 'data', 'cliente', 'volume', 'fardos', 'ciclo_pezinho'],
    'nfe': ['bitola_id', 'nfe', 'volume', 'retrabalho'],
    'pezinho': ['bitola_id', 'nfe', 'volume'],
    'residuo': ['bitola_id', 'data', 'volume'],
    'estufa': ['nome'],
    'cliente': ['nome']
}

# Tabelas com primary keys automáticas
AUTO_INCREMENTED_TABLES = ['cliente', 'estufa', 'nfe', 'pezinho', 'residuo']
