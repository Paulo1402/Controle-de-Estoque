import os
from pathlib import Path

# Caminho relativo ao main.py
BASEDIR = Path(__file__).parent.parent
print('ROOT', BASEDIR, __name__)

# HTML com instruções do aplicativo
HELP = os.path.join(BASEDIR, 'static', 'help.html')

# Constantes para o cálculo do pezinho
DEFAULT_LONG_SKIDS = 0.00306
DEFAULT_SHORT_SKIDS = 0.00405

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
