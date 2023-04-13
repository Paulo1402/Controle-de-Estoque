"""Constantes usadas ao longo do programa."""
import os
from pathlib import Path

# Caminho relativo ao main.py
BASEDIR = Path(__file__).parent.parent

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
