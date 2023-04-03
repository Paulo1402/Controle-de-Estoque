import sys
import warnings

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QLabel, QProgressBar
from PySide6.QtGui import QIcon, QCloseEvent, QIntValidator
from PySide6.QtCore import QModelIndex, Qt, QRegularExpression, Slot

from ui.MainWindow import Ui_MainWindow
from services import *
from utils import *


# todo FrontEnd
# Definir cores principais para light / dark mode
# Trabalhar na responsividade, aumentar o tamanho dos widgets de campos de forma proporcional
# Definir animação quando alternar páginas na Tab Widget

# todo BackEnd

# todo Refactoring
# Verificar se é necessário decorar com @check_connection funções que alteram o banco de dados

# todo Testes
# Testar CRUD de todas as tabelas
# Testar sistema de backup
# Testar sistema de importação de backup
# Repetir bateria de testes com o app compilado

# todo Bugs


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Cria handler para TableWidget
        tw_cycle_handler = CycleTableWidgetHandler(
            self,
            table_widget=self.tw_cycle,
            remove_button=self.bt_remove_bitola_cycle,
            fields=[
                self.txt_bitola_cycle,
                self.txt_packs_cycle,
                self.txt_volume_cycle
            ]
        )
        
        # Seta handler
        self.tw_cycle.handler = tw_cycle_handler

        # Cria handler para TableWidget
        tw_nfe_handler = NfeTableWidgetHandler(
            self,
            table_widget=self.tw_nfe,
            remove_button=self.bt_remove_bitola_nfe,
            fields=[
                self.cb_cycle_nfe,
                self.cb_bitola_nfe,
                self.txt_volume_nfe,
                self.txt_rework_nfe
            ],
            optional_fields=[self.txt_rework_nfe]
        )
        
        # Seta handler
        self.tw_nfe.handler = tw_nfe_handler

        # Seta ids iniciais
        self._ID_cycle = -1
        self._ID_nfe = -1

        self.backup_worker: DoBackupWorker | None = None
        self.animation = Animation()

        # Abre conexão com o banco de dados
        self.database = DatabaseConnection()
        self.database.connect()

        # Cria widgets de backup
        self.backup_bar = QProgressBar()
        self.backup_label = QLabel('Realizando backup...')

        # Inicialização
        self.init_ui()

        # Seta páginas iniciais
        self.tab_widget_cycle.setCurrentIndex(0)
        self.tab_widget_nfe.setCurrentIndex(0)
        self.mp_cycle_historic.setCurrentIndex(0)
        # self.bt_stock_menu.click()

    @property
    def ID_cycle(self):
        return self._ID_cycle

    # Setter para habilitar / desabilitar campos conforme valor do ID
    @ID_cycle.setter
    def ID_cycle(self, value: int):
        self._ID_cycle = value
        flag = bool(value + 1)

        # self.fr_bitolas_cycle.setDisabled(flag)
        self.rb_kd_cycle.setChecked(not flag)
        self.bt_delete_cycle.setDisabled(not flag)
        self.tab_widget_cycle.setCurrentIndex(0)

        self.handle_status_message('CICLO', value)

    @property
    def ID_nfe(self):
        return self._ID_nfe

    # Setter para habilitar / desabilitar campos conforme valor do ID
    @ID_nfe.setter
    def ID_nfe(self, value: int):
        self._ID_nfe = value
        flag = bool(value + 1)

        # self.fr_bitolas_nfe.setDisabled(flag)
        self.bt_delete_nfe.setDisabled(not flag)
        self.tab_widget_nfe.setCurrentIndex(0)

        self.handle_status_message('NFE', value)

    # Disparado quando a janela é fechada
    def closeEvent(self, event: QCloseEvent):
        if Message.warning_question(self, 'Deseja fechar o aplicativo?') == Message.NO:
            event.ignore()
            return

        self.database.disconnect()
        event.accept()

    # Realiza conexões de signals e slots
    def init_ui(self):
        # Seta título da janela principal
        self.setWindowTitle('CONTROLE DE MADEIRA TRATADA')

        # Conecta botões do menu principal
        self.bt_cycle_menu.clicked.connect(lambda: self.animation.fade_in(self.mp_main, 0))
        self.bt_cycle_menu.clicked.connect(lambda: self.handle_status_message('CICLO', self.ID_cycle))
        self.bt_nfe_menu.clicked.connect(lambda: self.animation.fade_in(self.mp_main, 1))
        self.bt_nfe_menu.clicked.connect(lambda: self.handle_status_message('NFE', self.ID_nfe))
        self.bt_stock_menu.clicked.connect(lambda: self.animation.fade_in(self.mp_main, 2))
        self.bt_stock_menu.clicked.connect(lambda: self.statusbar.clearMessage())
        self.bt_kiln_menu.clicked.connect(
            lambda: GenericDialog(self, self.database, 'ESTUFAS', 'estufa', self.load_kilns).show()
        )
        self.bt_client_menu.clicked.connect(
            lambda: GenericDialog(self, self.database, 'CLIENTES', 'cliente', self.load_clients).show()
        )
        self.bt_exit_menu.clicked.connect(self.close)

        # Conecta botões do menu de tarefas
        self.action_config.triggered.connect(lambda: ConfigurationDialog(self, self.database).show())
        self.action_import_backup.triggered.connect(lambda: ImportBackupDialog(self, self.database).show())
        self.action_dark_theme.triggered.connect(lambda: self.handle_theme('dark'))
        self.action_light_theme.triggered.connect(lambda: self.handle_theme('light'))

        # Adiciona widgets a status bar
        status_bar = self.statusBar()
        status_bar.addPermanentWidget(self.backup_label)
        status_bar.addPermanentWidget(self.backup_bar)

        self.backup_label.setVisible(False)
        self.backup_bar.setVisible(False)

        # Página Ciclo
        self.bt_delete_cycle.setDisabled(True)
        self.bt_edit_cycle_history.setDisabled(True)

        self.bt_new_cycle.clicked.connect(self.new_cycle)
        self.bt_save_cycle.clicked.connect(self.save_cycle)
        self.bt_delete_cycle.clicked.connect(self.delete_cycle)

        self.bt_add_bitola_cycle.clicked.connect(self.tw_cycle.handler.add)
        self.bt_remove_bitola_cycle.clicked.connect(self.tw_cycle.handler.remove)

        self.bt_search_cycle_history.clicked.connect(self.search_cycle_history)
        self.bt_clear_cycle_history.clicked.connect(self.clear_cycle_history)
        self.bt_edit_cycle_history.clicked.connect(self.edit_cycle_history)

        self.tv_cycle_history.setModel(TableModel(date_fields=[3, 4], volume_fields=[7, 8, 9, 10]))
        self.tv_cycle_history.clicked.connect(lambda: self.bt_edit_cycle_history.setDisabled(False))
        self.tv_cycle_history.doubleClicked.connect(self.track_cycle)

        self.tv_track_history.setModel(TableModel(date_fields=[0], volume_fields=[3]))
        self.tv_track_history.doubleClicked.connect(self.track_nfe)

        self.bt_back_track_history.clicked.connect(lambda: self.animation.slide(self.mp_cycle_historic, 0))

        # Página Nfe
        self.bt_delete_nfe.setDisabled(True)
        self.bt_edit_nfe_history.setDisabled(True)

        self.bt_new_nfe.clicked.connect(self.new_nfe)
        self.bt_save_nfe.clicked.connect(self.save_nfe)
        self.bt_delete_nfe.clicked.connect(self.delete_nfe)

        self.bt_add_bitola_nfe.clicked.connect(self.tw_nfe.handler.add)
        self.bt_remove_bitola_nfe.clicked.connect(self.tw_nfe.handler.remove)

        self.cb_cycle_nfe.currentIndexChanged.connect(self.load_nfe_bitola)

        self.bt_search_nfe_history.clicked.connect(self.search_nfe_history)
        self.bt_clear_nfe_history.clicked.connect(self.clear_nfe_history)
        self.bt_edit_nfe_history.clicked.connect(self.edit_nfe_history)

        self.tv_nfe_history.setModel(TableModel(date_fields=[1], volume_fields=[3]))
        self.tv_nfe_history.clicked.connect(lambda: self.bt_edit_nfe_history.setDisabled(False))

        # Página Estoque
        self.bt_discount_stock.setDisabled(True)
        self.bt_leaving_stock.setDisabled(True)

        self.bt_search_stock.clicked.connect(self.search_stock)
        self.bt_clear_stock.clicked.connect(self.clear_stock)

        self.bt_discount_stock.clicked.connect(self.discount_stock)
        self.bt_leaving_stock.clicked.connect(self.leaving_stock)

        self.tv_stock.setModel(TableModel(volume_fields=[5, 6, 7]))
        self.tv_stock.clicked.connect(lambda: self.bt_discount_stock.setDisabled(False))
        self.tv_stock.clicked.connect(lambda: self.bt_leaving_stock.setDisabled(False))

        # Seta validadores
        validator = QIntValidator()
        self.txt_cycle_cycle.setValidator(validator)
        self.txt_packs_cycle.setValidator(validator)
        self.txt_nfe_nfe.setValidator(validator)
        self.txt_packs_nfe.setValidator(validator)
        self.txt_nfe_nfe_history.setValidator(validator)

        validator = VolumeValidator(QRegularExpression(r'\d+,\d{3}'))
        self.txt_volume_nfe.setValidator(validator)
        self.txt_volume_cycle.setValidator(validator)
        self.txt_total_volume_nfe.setValidator(validator)

        validator = BitolaValidator(QRegularExpression(r'(\d{2,3}x){2}\d{3,4}m{2}'))
        self.txt_bitola_cycle.setValidator(validator)
        self.txt_rework_nfe.setValidator(validator)

        validator = DateValidator(
            QRegularExpression(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/[12][0-9]{3}")
        )
        self.cb_date_nfe.setValidator(validator)
        self.cb_entry_date_cycle.setValidator(validator)
        self.cb_exit_date_cycle.setValidator(validator)
        self.cb_entry_date_cycle_history.setValidator(validator)
        self.cb_exit_date_cycle_history.setValidator(validator)
        self.cb_start_date_nfe_history.setValidator(validator)
        self.cb_end_date_nfe_history.setValidator(validator)

        # Carrega tema configurado
        config = get_config()
        theme = config['theme']

        load_theme(theme)

    # Inicia janela principal
    def show(self):
        super().show()

        # Verifica conexão
        if self.database.connection_state == DatabaseConnection.State.DATABASE_NOT_FOUND:
            Message.critical(
                self,
                'CRÍTICO',
                'Erro ao acessar banco de dados!\n'
                'Se seu banco de dados estiver na rede verifique se há conexão com o computador servidor.'
            )
        elif self.database.connection_state == DatabaseConnection.State.NO_DATABASE:
            Message.warning(self, 'ATENÇÃO', 'Insira um banco de dados para usar o programa.')
            self.action_config.trigger()
        else:
            # Cria worker para fazer o backup
            self.backup_worker = DoBackupWorker(self.database)
            self.backup_worker.progress.connect(self.backup_progress)
            self.backup_worker.finished.connect(self.backup_finished)

            # Inicia worker
            self.backup_worker.start()

        # Configura dados
        self.setup_data()

    # Carrega dados
    def setup_data(self):
        # Verifica conexão
        connected = self.database.connection_state == DatabaseConnection.State.CONNECTED

        self.action_import_backup.setDisabled(not connected)
        self.mp_main.setDisabled(not connected)
        self.bt_client_menu.setDisabled(not connected)
        self.bt_kiln_menu.setDisabled(not connected)

        # Carrega dados para dentro do app
        if connected:
            self.load_clients()
            self.load_kilns()
            self.load_cycles()
            self.search_cycle_history()
            self.search_nfe_history()
            self.search_stock()

    # Atualiza widgets de backup
    @Slot()
    def backup_progress(self, progress: int):
        if not self.backup_bar.isVisible():
            self.backup_bar.setVisible(True)
            self.backup_label.setVisible(True)

        self.backup_bar.setValue(progress)

    # Limpa worker e esconde widgets
    @Slot()
    def backup_finished(self):
        self.backup_label.setVisible(False)
        self.backup_bar.setVisible(False)

        self.backup_worker = None

    @Slot()
    def handle_status_message(self, page: str, value: int):
        if value != -1:
            message = f'EDITANDO {page} {value}'
            self.statusbar.showMessage(message)
        else:
            self.statusbar.clearMessage()

    # Lida com a troca de temas
    @Slot()
    def handle_theme(self, theme: str):
        config = get_config()
        config['theme'] = theme

        set_config(config)
        load_theme(theme)

    # Página Ciclo
    # Prepara campos para novo registro
    @Slot()
    def new_cycle(self):
        fields = [
            self.cb_kiln_cycle,
            self.txt_cycle_cycle,
            self.cb_entry_date_cycle,
            self.cb_exit_date_cycle
        ] + self.tw_cycle.handler.fields

        self.tw_cycle.handler.remove_rows()
        clear_fields(fields)

        query = self.database.read(
            table='ciclo',
            fields=['MAX(ciclo)']
        )

        query.first()
        self.txt_cycle_cycle.setText(str(query.value(0) + 1))

        if self.ID_cycle != -1:
            self.load_kilns()
            self.load_cycles()

        self.ID_cycle = -1

    # Salva ciclo na tabela
    @Slot()
    def save_cycle(self):
        # Define modo de interação
        mode = 'INSERT' if self.ID_cycle == -1 else 'UPDATE'

        fields = [
            self.cb_kiln_cycle,
            self.txt_cycle_cycle,
            self.cb_entry_date_cycle,
            self.cb_exit_date_cycle,
        ]

        finality = 'KD' if self.rb_kd_cycle.isChecked() else 'HT'

        # Verifica se há campos em branco
        empty_fields = get_empty_fields(fields)

        if len(empty_fields) > 0:
            Message.warning(self, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            empty_fields[0].setFocus()
            return

        entry_date = parse_date(fields[2].currentText(), '%d/%m/%Y')
        exit_date = parse_date(fields[3].currentText(), '%d/%m/%Y')

        # Verifica se é uma data válida
        if not entry_date or not exit_date:
            Message.warning(self, 'ATENÇÃO', 'Data inválida!')

            i = 2 if not entry_date else 3
            fields[i].setFocus()
            return

        if not self.tw_cycle.rowCount():
            Message.warning(self, 'ATENÇÃO', 'Ao menos uma bitola deve ser especificada para registro.')
            return

        fields = {
            'ciclo': fields[1].text(),
            'estufa': fields[0].currentText(),
            'finalidade': finality,
            'entrada': entry_date,
            'saida': exit_date
        }

        cycle = fields['ciclo']

        # Verifica se o campo ciclo não existe no banco de dados
        if int(cycle) != self.ID_cycle and not self.database.is_unique('ciclo', 'ciclo', cycle):
            Message.warning(self, 'ATENÇÃO', 'Esse ciclo já consta no banco de dados!')

            if self.ID_cycle != -1:
                self.txt_cycle_cycle.setText(str(self.ID_cycle))

            return

        message = 'Deseja editar esse ciclo no banco de dados?'

        if mode == 'INSERT':
            message = message.replace('editar', 'inserir')

        # Faz pergunta de segurança ao usuário, caso não confirme aborta ação
        if Message.warning_question(self, message, Message.YES) == Message.NO:
            return

        # Retorna query com finalidade original
        query = self.database.read(
            table='ciclo',
            fields=['finalidade'],
            clause='WHERE ciclo LIKE ?',
            values=[self.ID_cycle]
        )

        query.first()

        if mode == 'UPDATE' and fields['finalidade'] != query.value(0):
            if Message.warning_question(
                    self,
                    'Se o ciclo atual tiver a finalidade alterada seu registro e de todos seus dependentes '
                    'serão deletados. Deseja continuar?'
            ) == Message.NO:
                return

            self.database.delete('ciclo', f'WHERE ciclo LIKE {self.ID_cycle}')
            mode = 'INSERT'

        try:
            print(mode)
            if mode == 'INSERT':
                self.database.create(table='ciclo', fields=fields)
                message = 'Registro inserido com sucesso.'
            else:
                self.database.update(table='ciclo', fields=fields, clause=f"WHERE ciclo LIKE {self.ID_cycle}")
                message = 'Registro alterado com sucesso.'

            # Insere ou atualiza bitolas na tabela
            for row in range(self.tw_cycle.rowCount()):
                bitola_id = self.tw_cycle.item(row, 0).text()

                bitola = self.tw_cycle.item(row, 1).text()
                packs = self.tw_cycle.item(row, 2).text()
                volume = from_volume_to_float(self.tw_cycle.item(row, 3).text())

                fields = {
                    'ciclo': cycle,
                    'bitola': bitola,
                    'fardos': packs,
                    'volume_tratado': volume
                }

                print(bitola_id, fields)

                if bitola_id == '-1':
                    self.database.create(table='bitola', fields=fields)
                else:
                    self.database.update(table='bitola', fields=fields, clause=f'WHERE bitola_id LIKE {bitola_id}')

            # Prepara para novo registro e avisa usuário
            Message.information(self, 'AVISO', message)
            self.new_cycle()

            # Recria tabelas temporárias e recarrega dados de ciclos
            self.refresh_data()
            self.search_cycle_history()
        except QueryError:
            Message.critical(self, 'CRÍTICO', 'Algo deu errado durante a operação!')

    # Deleta ciclo
    @Slot()
    def delete_cycle(self):
        # Guard clause
        if not Message.warning_question(
                self, 'Deseja deletar esse registro? Todos os registros referentes a esse ciclo serão'
                      ' deletados também.', Message.NO
        ) == Message.YES:
            return

        # Deleta ciclo
        self.database.delete(
            table='ciclo',
            clause=f'WHERE ciclo LIKE {self.ID_cycle}'
        )

        # Alerta usuário e prepara para novo registro
        Message.information(self, 'AVISO', 'Ciclo deletado com sucesso!')
        self.new_cycle()

        # Recria tabelas temporárias e recarrega dados de ciclos
        self.refresh_data()
        self.search_cycle_history()

    # Carrega dados de ciclos para a table view
    @Slot()
    def search_cycle_history(self):
        # Retorna dados dos campos
        kiln = self.cb_kiln_cycle_history.currentText()
        cycle = self.cb_cycle_cycle_history.currentText()
        start_date = parse_date(self.cb_entry_date_cycle_history.currentText(), '%d/%m/%Y', on_fail=DateMinMax.MIN)
        end_date = parse_date(self.cb_exit_date_cycle_history.currentText(), '%d/%m/%Y', on_fail=DateMinMax.MAX)
        bitola = self.txt_bitola_cycle_history.text()
        finality = 'KD' if self.rb_kd_cycle_history.isChecked() else 'HT'

        # Adiciona filtros de forma condicional
        clause = "LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo " \
                 "WHERE entrada >= ? AND saida <= ? AND bitola LIKE '%' || ? || '%' AND finalidade LIKE ?"
        values = [start_date, end_date, bitola, finality]

        if kiln:
            clause += ' AND estufa LIKE ?'
            values.append(kiln)

        if cycle:
            clause += ' AND estoque.ciclo LIKE ?'
            values.append(cycle)

        # Retorna query com registros
        query = self.database.read(
            table='estoque',
            fields=['bitola_id', 'estufa', 'ciclo.ciclo', 'entrada', 'saida', 'finalidade', 'bitola', 'volume_tratado',
                    'volume_vendido', 'residuo', 'estoque'],
            clause=clause,
            values=values
        )

        # Retorna model da table view e seta query
        model: TableModel = self.tv_cycle_history.model()
        model.setQuery(query)

        # Cria cabeçalhos
        headers = [
            'ID', 'ESTUFA', 'CICLO', 'ENTRADA', 'SAÍDA', 'FINALIDADE', 'BITOLA', 'TRATADO',
            'VENDIDO', 'RESÍDUO', 'ESTOQUE'
        ]

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        # Configura colunas
        self.tv_cycle_history.setColumnHidden(0, True)
        self.tv_cycle_history.setColumnHidden(1, True)
        self.tv_cycle_history.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)

        self.bt_edit_cycle_history.setDisabled(True)

    # Limpa campos na página de histórico de ciclos
    @Slot()
    def clear_cycle_history(self):
        self.cb_kiln_cycle_history.setCurrentIndex(0)
        self.cb_cycle_cycle_history.setCurrentIndex(0)

        self.cb_entry_date_cycle_history.setCurrentText('')
        self.cb_exit_date_cycle_history.setCurrentText('')

        self.txt_bitola_cycle_history.clear()
        self.rb_kd_cycle_history.setChecked(True)

        self.bt_edit_cycle_history.setDisabled(True)
        self.tv_cycle_history.clearSelection()

    # Traz dados da página de histórico de ciclos para edição na página de registro
    @Slot()
    def edit_cycle_history(self):
        # Aborta slot caso não haja índices selecionados
        if not self.tv_cycle_history.selectedIndexes():
            return

        # Retorna a linha referente a seleção e o model da table view
        row = self.tv_cycle_history.selectedIndexes()[0].row()
        model = self.tv_cycle_history.model()

        # Retorna dados da table view
        kiln = model.index(row, 1).data()
        cycle = model.index(row, 2).data()
        entry_date = model.index(row, 3).data()
        exit_date = model.index(row, 4).data()
        finality = model.index(row, 5).data()

        # Se estufa não estiver na ComboBox, a adiciona
        if self.cb_kiln_cycle.findText(kiln) == -1:
            self.cb_kiln_cycle.addItem(kiln)

        # Seta dados retornados na página de novo registro
        self.txt_cycle_cycle.setText(str(cycle))
        self.cb_kiln_cycle.setCurrentText(kiln)
        self.cb_entry_date_cycle.setCurrentText(entry_date)
        self.cb_exit_date_cycle.setCurrentText(exit_date)

        if finality == 'KD':
            self.rb_kd_cycle.setChecked(True)
        else:
            self.rb_ht_cycle.setChecked(True)

        # Busca bitolas referentes ao ciclo em questão
        query = self.database.read(
            table='bitola',
            fields=['bitola_id', 'bitola', 'fardos', 'volume_tratado'],
            clause='WHERE ciclo LIKE ?',
            values=[cycle]
        )

        # Remove linhas na table widget caso houver
        self.tw_cycle.handler.remove_rows()

        # Preenche table widget com dados da query
        while query.next():
            row = self.tw_cycle.rowCount()
            self.tw_cycle.insertRow(row)

            for i in range(4):
                value = from_float_to_volume(query.value(i), symbol=False) if i == 3 else str(query.value(i))

                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.tw_cycle.setItem(row, i, item)

        # Atualiza ID_cycle com base no ciclo selecionado
        self.ID_cycle = cycle

    # Mostra informações detalhadas sobre o ciclo em uma nova página
    @Slot()
    def track_cycle(self, index: QModelIndex):
        # Retorna linha
        row = index.row()

        # Mapeia campos
        fields = [
            (self.txt_kiln_track_history, 1),
            (self.txt_cycle_track_history, 2),
            (self.txt_entry_date_track_history, 3),
            (self.txt_exit_date_track_history, 4),
            (self.txt_bitola_track_history, 6)
        ]

        model = self.tv_cycle_history.model()
        bitola_id = model.index(row, 0).data()

        # Seta campos com os dados da página anterior
        if model.index(row, 5).data() == 'KD':
            self.rb_kd_track_history.setChecked(True)
        else:
            self.rb_ht_track_history.setChecked(True)

        for field, col in fields:
            data = model.index(row, col).data()
            field.setText(str(data))

        # Retorna query com dados
        query = self.database.read(
            table='nfe',
            fields=['data', 'nfe.nfe', 'cliente', 'nfe.volume', 'retrabalho'],
            clause="LEFT JOIN nfe_info ON nfe.nfe = nfe_info.nfe "
                   "WHERE bitola_id LIKE ?",
            values=[bitola_id]
        )

        # Retorna model e seta query
        model: TableModel = self.tv_track_history.model()
        model.setQuery(query)

        # Cria cabeçalhos
        headers = ['DATA', 'NFE', 'CLIENTE', 'VOLUME', 'RETRABALHO']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        # Configura colunas
        self.tv_track_history.setColumnHidden(0, True)
        self.tv_track_history.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Retorna query
        query = self.database.read(
            table='residuo',
            fields=['data', 'volume'],
            clause='WHERE bitola_id LIKE ?',
            values=[bitola_id]
        )

        # Seta dados
        if query.next():
            date = parse_date(query.value(0), input_format='%Y-%m-%d', output_format='%d/%m/%Y')
            value = query.value(1)
        else:
            date = ''
            value = 0

        self.txt_leaving_date_track_history.setText(date)
        self.txt_leaving_volume_track_history.setText(from_float_to_volume(value))

        # Retorna query
        query = self.database.read(
            table='estoque',
            fields=['estoque'],
            clause='WHERE bitola_id LIKE ?',
            values=[bitola_id]
        )

        # Seta dados e altera página
        value = query.value(0) if query.next() else 0

        self.txt_stock_volume_track_history.setText(from_float_to_volume(value))
        self.animation.slide(self.mp_cycle_historic, 1)

    # Mostra informações detalhadas sobre a nfe na página de nfe
    @Slot()
    def track_nfe(self, index: QModelIndex):
        # Retorna linha e model
        row = index.row()
        model = self.tv_track_history.model()

        # Retorna dados
        nfe = model.index(row, 1).data()
        client = model.index(row, 2).data()

        # Seta dados
        self.txt_nfe_nfe_history.setText(str(nfe))
        self.cb_client_nfe_history.setCurrentText(client)

        # Faz pesquisa e altera páginas
        self.bt_search_nfe_history.click()

        self.bt_nfe_menu.click()
        self.tab_widget_nfe.setCurrentIndex(1)

    # Página NFE
    # Prepara campos para novo registro
    @Slot()
    def new_nfe(self):
        fields = [
            self.cb_date_nfe,
            self.cb_client_nfe,
            self.txt_nfe_nfe,
            self.txt_total_volume_nfe,
            self.txt_packs_nfe,
            self.cb_foot_nfe
        ] + self.tw_nfe.handler.fields

        self.tw_nfe.handler.remove_rows()
        clear_fields(fields)

        if self.ID_nfe != -1:
            self.load_clients()
            self.load_cycles()

        self.ID_nfe = -1

    # Salva nfe na tabela
    @Slot()
    def save_nfe(self):
        # Define modo de interação
        mode = 'INSERT' if self.ID_nfe == -1 else 'UPDATE'

        fields = [
            self.cb_date_nfe,
            self.cb_client_nfe,
            self.txt_nfe_nfe,
            self.txt_total_volume_nfe,
            self.txt_packs_nfe,
            self.cb_foot_nfe
        ]

        # Verifica se há campos em branco
        empty_fields = get_empty_fields(fields)

        if len(empty_fields) > 0:
            Message.warning(self, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            empty_fields[0].setFocus()
            return

        date = parse_date(fields[0].currentText(), '%d/%m/%Y', '%Y-%m-%d')

        # Verifica se é uma data válida
        if not date:
            Message.warning(self, 'ATENÇÃO', 'Data inválida!')
            fields[0].setFocus()

        # Guard clause
        if not self.tw_nfe.rowCount():
            if Message.warning_question(
                    self,
                    'Não há bitolas tratadas nesse registro, deseja continuar mesmo assim?'
            ) == Message.NO:
                return

        fields = {
            'nfe': fields[2].text(),
            'data': date,
            'cliente': fields[1].currentText(),
            'volume': from_volume_to_float(fields[3].text()),
            'fardos': fields[4].text(),
            'ciclo_pezinho': fields[5].currentText()
        }

        nfe = fields['nfe']

        # Verifica se o campo nfe não existe no banco de dados
        if int(nfe) != self.ID_nfe and not self.database.is_unique('nfe_info', 'nfe', nfe):
            Message.warning(self, 'ATENÇÃO', 'Essa nfe já consta no banco de dados!')

            if self.ID_nfe != -1:
                self.txt_nfe_nfe.setText(str(self.ID_nfe))

            return

        original_bitolas = {}
        original_foot = {}

        print(mode)
        if mode == 'UPDATE':
            # Retorna query com bitolas originais
            query = self.database.read(
                table='nfe',
                fields=['bitola_id, volume'],
                clause='WHERE nfe LIKE ?',
                values=[nfe]
            )

            while query.next():
                bitola_id = str(query.value(0))
                volume = query.value(1)

                original_bitolas[bitola_id] = volume

            # Retorna query com pezinhos originais
            query = self.database.read(
                table='pezinho',
                fields=['bitola_id', 'volume'],
                clause='WHERE nfe LIKE ?',
                values=[nfe]
            )

            while query.next():
                bitola_id = str(query.value(0))
                volume = query.value(1)

                original_foot[bitola_id] = volume

        bitola_list = []

        # Verifica estoque das bitolas
        for row in range(self.tw_nfe.rowCount()):
            bitola_id = self.tw_nfe.item(row, 0).text()
            cycle = self.tw_nfe.item(row, 1).text()
            bitola = self.tw_nfe.item(row, 2).text()
            volume = from_volume_to_float(self.tw_nfe.item(row, 3).text())
            rework = self.tw_nfe.item(row, 4).text()

            stock = self.database.get_stock(bitola_id)

            # Soma estoque atual com estoque anterior caso seja uma edição
            for b, v in original_bitolas.items():
                if b == bitola_id:
                    stock += v

            # Subtrai estoque de bitolas existentes já na tabela
            for b, v, _ in bitola_list:
                if b == bitola_id:
                    stock -= v

            if volume > stock:
                Message.warning(
                    self, 'ATENÇÃO', f'Estoque insuficiente no item {bitola} - Ciclo {cycle}.\n'
                          f'Volume necessário: {from_float_to_volume(volume)}, volume em estoque: '
                          f'{from_float_to_volume(stock)}.'
                )
                return

            bitola_list.append((bitola_id, volume, rework))

        # Verifica estoque do pezinho
        foot_cycle = fields['ciclo_pezinho']

        # Retorna query com bitolas do ciclo do pezinho
        query = self.database.read(
            table='estoque',
            fields=['bitola_id', 'bitola'],
            clause='WHERE ciclo LIKE ? '
                   'GROUP BY bitola_id '
                   'ORDER BY MAX(volume_tratado) DESC',
            values=[foot_cycle]
        )

        # Cria dicionário para armazenar dados da query
        data = {
            'bitola_id': [],
            'bitola': [],
            'stock': []
        }

        # Armazena dados da consulta
        while query.next():
            bitola_id = str(query.value(0))
            bitola = query.value(1)
            stock = self.database.get_stock(bitola_id)

            # Soma estoque de pezinho anterior caso esteja em modo de edição
            for b, v in original_foot.items():
                if b == bitola_id:
                    stock += v

            data['bitola_id'].append(bitola_id)
            data['bitola'].append(bitola)
            data['stock'].append(stock)

        # Retorna volumes para baixa nos pezinhos
        volumes = get_skids_volume(len(data['bitola_id']), int(fields['fardos']))

        # Verifica se há estoque nos pezinhos
        for stock, volume, bitola in list(zip(data['stock'], volumes, data['bitola'])):
            if volume > stock:
                Message.warning(
                    self,
                    'ATENÇÃO',
                    f'Estoque insuficiente na bitola {bitola} do ciclo do pezinho(HT) de número {foot_cycle}. '
                    f'Verifique por favor!\n\nVolume necessário: {from_float_to_volume(volume)}, '
                    f'volume em estoque: {from_float_to_volume(stock)}'
                )
                return

        # Salva dados para inserir posteriormente
        foot_list = list(zip(data['bitola_id'], volumes))

        print(foot_list)

        message = 'Deseja editar essa nfe no banco de dados?'

        if mode == 'INSERT':
            message = message.replace('editar', 'inserir')

        # Faz pergunta de segurança ao usuário, caso não confirme aborta ação
        if Message.warning_question(self, message, Message.YES) == Message.NO:
            return

        try:
            if mode == 'INSERT':
                self.database.create(table='nfe_info', fields=fields)
                message = 'Registro inserido com sucesso.'
            else:
                self.database.update(table='nfe_info', fields=fields, clause=f'WHERE nfe LIKE {self.ID_nfe}')
                message = 'Registro alterado com sucesso.'

            new_bitolas = []

            # Insere ou atualiza bitolas tratadas na tabela de saída por nfe
            for bitola_id, volume, rework in bitola_list:
                fields = {
                    'bitola_id': bitola_id,
                    'nfe': nfe,
                    'volume': volume,
                    'retrabalho': rework
                }
                print(f'{original_bitolas=} - {fields=}')
                new_bitolas.append(bitola_id)

                if bitola_id not in original_bitolas.keys():
                    self.database.create(table='nfe', fields=fields)
                else:
                    self.database.update(table='nfe', fields=fields, clause=f'WHERE bitola_id LIKE {bitola_id}')
            print()
            print(original_bitolas.keys(), new_bitolas)

            # Remove bitolas que foram removidas do registro original
            for bitola_id in original_bitolas.keys():
                if bitola_id not in new_bitolas:
                    print('deleting', bitola_id)
                    self.database.delete(table='nfe', clause=f'WHERE bitola_id LIKE {bitola_id}')

            # Insere ou atualiza bitolas de pezinho na tabela de saída de pezinhos
            for bitola_id, volume in foot_list:
                fields = {
                        'bitola_id': bitola_id,
                        'nfe': nfe,
                        'volume': volume
                    }

                if mode == 'UPDATE':
                    print('deleting', bitola_id, volume)
                    self.database.delete(table='pezinho', clause=f'WHERE nfe LIKE {fields["nfe"]}')

                print(bitola_id, volume)
                self.database.create(table='pezinho', fields=fields)

            # Prepara para novo registro e avisa usuário
            Message.information(self, 'AVISO', message)
            self.new_nfe()

            # Recria tabelas temporárias e recarrega dados de ciclos
            self.refresh_data()
            self.search_nfe_history()
        except QueryError:
            Message.critical(self, 'CRÍTICO', 'Algo deu errado durante a operação!')

    # Deleta nfe
    @Slot()
    def delete_nfe(self):
        # Guard clause
        if Message.warning_question(
                self, 'Deseja deletar esse registro? Todos os registros referentes a essa nfe serão'
                      ' deletados também.', Message.NO
        ) == Message.NO:
            return

        # Deleta nfe
        self.database.delete(
            table='nfe_info',
            clause=f'WHERE nfe LIKE {self.ID_nfe}'
        )

        # Prepara para novo registro e avisa usuário
        Message.information(self, 'AVISO', 'Registro deletado com sucesso.')
        self.new_nfe()

        # Recria tabelas temporárias e recarrega dados de ciclos
        self.refresh_data()
        self.search_nfe_history()

    # Carrega bitolas com base no ciclo selecionado
    @Slot()
    def load_nfe_bitola(self, index: int):
        # Aborta caso não houver ciclo
        if index == -1:
            self.cb_bitola_nfe.clear()
            return

        # Retorna o ciclo atual
        ciclo = self.cb_cycle_nfe.itemText(index)

        data = []
        bitola_id_list = []

        # Retorna query com dados das bitolas do ciclo selecionado
        query = self.database.read(
            table='estoque',
            fields=['bitola_id', 'bitola'],
            clause='WHERE estoque.ciclo LIKE ?',
            values=[ciclo]
        )

        while query.next():
            bitola_id_list.append(str(query.value(0)))
            data.append(str(query.value(1)))

        # Seta id das bitolas como um atributo da classe para ser acessada dentro do handler
        setattr(self.cb_bitola_nfe, 'bitola_id_list', bitola_id_list)

        # Seta bitolas na combobox
        self.cb_bitola_nfe.clear()
        self.cb_bitola_nfe.addItems(data)

    # Faz busca do histórico de NFEs e abastece table view
    @Slot()
    def search_nfe_history(self):
        # Retorna dados dos campos
        nfe = self.txt_nfe_nfe_history.text()
        client = self.cb_client_nfe_history.currentText()
        foot_cycle = self.cb_foot_nfe_history.currentText()
        start_date = parse_date(
            self.cb_start_date_nfe_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MIN
        )
        end_date = parse_date(
            self.cb_end_date_nfe_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MAX
        )

        # Faz o filtro de forma condicional
        clause = "WHERE data >= ? AND data <= ? AND nfe LIKE '%' || ? || '%' AND cliente LIKE '%' || ? || '%'"
        values = [start_date, end_date, nfe, client]

        if foot_cycle:
            clause += ' AND ciclo_pezinho LIKE ?'
            values.append(foot_cycle)

        # Retorna query com os dados
        query = self.database.read(
            table='nfe_info',
            fields=['nfe', 'data', 'cliente', 'volume', 'fardos', 'ciclo_pezinho'],
            clause=clause,
            values=values
        )

        # Seta query no model
        model: TableModel = self.tv_nfe_history.model()
        model.setQuery(query)

        # Seta headers da tabela
        headers = ['NFE', 'DATA', 'CLIENTE', 'VOLUME', 'FARDOS', 'CICLO PEZINHO']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        # Configura colunas
        self.tv_nfe_history.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.bt_edit_nfe_history.setDisabled(True)

    # Limpa os campos de filtro
    @Slot()
    def clear_nfe_history(self):
        self.txt_nfe_nfe_history.clear()
        self.cb_client_nfe_history.setCurrentIndex(0)

        self.cb_start_date_nfe_history.setCurrentText('')
        self.cb_end_date_nfe_history.setCurrentText('')

        self.cb_foot_nfe_history.setCurrentIndex(0)

        self.bt_edit_nfe_history.setDisabled(True)
        self.tv_nfe_history.clearSelection()

    # Traz dados para edição na página de registro
    @Slot()
    def edit_nfe_history(self):
        # Aborta slot caso não haja índices selecionados
        if not self.tv_nfe_history.selectedIndexes():
            return

        # Retorna a linha referente a seleção e o model da table view
        row = self.tv_nfe_history.selectedIndexes()[0].row()
        model = self.tv_nfe_history.model()

        # Retorna dados da table view
        nfe = model.index(row, 0).data()
        date = model.index(row, 1).data()
        client = model.index(row, 2).data()
        volume = model.index(row, 3).data()
        packs = model.index(row, 4).data()
        foot_cycle = model.index(row, 5).data()

        # Adiciona cliente na ComboBox, caso não exista
        if self.cb_client_nfe.findText(client) == -1:
            self.cb_client_nfe.addItem(client)

        # Adiciona pezinho na ComboBox, caso não exista
        if self.cb_foot_nfe.findText(str(foot_cycle)) == -1:
            self.cb_foot_nfe.addItem(str(foot_cycle))

        # Seta dados retornados na página de novo registro
        self.cb_date_nfe.setCurrentText(date)
        self.cb_client_nfe.setCurrentText(client)
        self.txt_nfe_nfe.setText(str(nfe))
        self.txt_total_volume_nfe.setText(str(volume))
        self.txt_packs_nfe.setText(str(packs))
        self.cb_foot_nfe.setCurrentText(str(foot_cycle))

        # Busca bitola referentes a nfe em questão
        query = self.database.read(
            table='bitola',
            fields=['bitola.bitola_id', 'ciclo', 'bitola', 'volume', 'retrabalho'],
            clause='LEFT JOIN nfe ON nfe.bitola_id = bitola.bitola_id '
                   'WHERE nfe LIKE ?',
            values=[nfe]
        )

        # Remove linhas na table widget caso houver
        self.tw_nfe.handler.remove_rows()

        # Preenche table widget com dados da query
        while query.next():
            row = self.tw_nfe.rowCount()
            self.tw_nfe.insertRow(row)

            cycle = str(query.value(1))

            # Adiciona ciclo caso não existir
            if self.cb_cycle_nfe.findText(cycle) == -1:
                self.cb_cycle_nfe.addItem(cycle)

            for i in range(5):
                value = from_float_to_volume(query.value(i), symbol=False) if i == 3 else str(query.value(i))

                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.tw_nfe.setItem(row, i, item)

        # Atualiza ID_nfe com base na nfe selecionada
        self.ID_nfe = nfe

    # Página Histórico
    # Faz busca no estoque e abastece table view
    @Slot()
    def search_stock(self):
        # Retorna dados dos campos
        cycle = self.cb_cycle_stock.currentText()
        bitola = self.cb_bitola_stock.currentText()
        finality = 'KD' if self.rb_kd_stock.isChecked() else 'HT'

        # Faz o filtro de forma condicional
        clause = "LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo " \
                 "WHERE estoque > 0 AND finalidade LIKE ?"
        values = [finality]

        if cycle:
            clause += ' AND estoque.ciclo LIKE ?'
            values.append(cycle)

        if bitola:
            clause += ' AND bitola LIKE ?'
            values.append(bitola)

        # Retorna a query com os dados
        query = self.database.read(
            table='estoque',
            fields=['bitola_id', 'estoque.ciclo',  'finalidade', 'bitola', 'fardos', 'volume_tratado',
                    'volume_vendido', 'estoque'],
            clause=clause,
            values=values
        )

        # Seta query no model
        model: TableModel = self.tv_stock.model()
        model.setQuery(query)

        # Retorna query com o resumo
        query = self.database.read(
            table='estoque',
            fields=['SUM(volume_tratado)', 'SUM(volume_vendido)', 'SUM(estoque)']
        )

        query.first()

        # Retorna valores formatados
        try:
            treatment = from_float_to_volume(query.value(0))
            sold = from_float_to_volume(query.value(1))
            stock = from_float_to_volume(query.value(2))

            # Seta valores
            self.txt_treatment_stock.setText(treatment)
            self.txt_sold_stock.setText(sold)
            self.txt_stock_stock.setText(stock)
        except ValueError:
            pass

        # Seta headers
        headers = ['ID', 'CICLO', 'FINALIDADE', 'BITOLA', 'FARDOS', 'TRATADO', 'VENDIDO', 'ESTOQUE']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        # Configura colunas
        self.tv_stock.setColumnHidden(0, True)
        self.tv_stock.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        self.bt_leaving_stock.setDisabled(True)
        self.bt_discount_stock.setDisabled(True)

    # Limpa os campos de filtro
    @Slot()
    def clear_stock(self):
        self.cb_cycle_stock.setCurrentIndex(0)
        self.cb_bitola_stock.setCurrentIndex(0)

        self.rb_kd_stock.setChecked(True)

        self.bt_leaving_stock.setDisabled(True)
        self.bt_discount_stock.setDisabled(True)
        self.tv_stock.clearSelection()

    # Prepara bitola selecionada para baixa via nfe
    @Slot()
    def discount_stock(self):
        # Guard clause
        if not self.tv_stock.selectedIndexes():
            return

        row = self.tv_stock.selectedIndexes()[0].row()
        model = self.tv_stock.model()

        # Retorna dados da table view
        cycle = model.index(row, 1).data()
        bitola = model.index(row, 2).data()

        # Seta dados retornados na página de novo registro
        self.cb_cycle_nfe.setCurrentText(str(cycle))
        self.cb_bitola_nfe.setCurrentText(bitola)

        # Seta ID_nfe como novo registro
        self.bt_nfe_menu.click()
        self.ID_nfe = -1

    # Faz baixa da bitola selecionada como resíduo
    @Slot()
    def leaving_stock(self):
        # Guard clause
        if not self.tv_stock.selectedIndexes():
            return

        if Message.warning_question(
                self,
                'Deseja declarar o restante dessa bitola como resíduo / mercado interno?'
        ) == Message.NO:
            return

        if Message.warning_question(
                self,
                'Isso irá zerar todo o estoque dessa bitola, deseja continuar?'
        ) == Message.NO:
            return

        row = self.tv_stock.selectedIndexes()[0].row()
        model = self.tv_stock.model()

        # Retorna dados da table view
        bitola_id = model.index(row, 0).data()
        volume = model.index(row, 7).data()
        date = get_today()

        # Insere registro no banco de dados
        self.database.create(
            table='residuo',
            fields={
                'bitola_id': bitola_id,
                'data': date,
                'volume': volume
            }
        )

        # Recarrega dados
        self.refresh_data()
        self.search_stock()

    # Recria tabelas temporárias e recarrega dados de ciclos
    def refresh_data(self):
        self.database.create_temp_table()
        self.load_cycles()

    # Carrega clientes
    def load_clients(self):
        query = self.database.read(
            table='cliente',
            fields=['nome']
        )

        data = []

        while query.next():
            data.append(query.value(0))

        self.cb_client_nfe.clear()
        self.cb_client_nfe_history.clear()

        self.cb_client_nfe.addItems(data)
        self.cb_client_nfe_history.addItems(['', *data])

    # Carrega estufas
    def load_kilns(self):
        query = self.database.read(
            table='estufa',
            fields=['nome']
        )

        data = []

        while query.next():
            data.append(query.value(0))

        self.cb_kiln_cycle.clear()
        self.cb_kiln_cycle_history.clear()

        self.cb_kiln_cycle.addItems(data)
        self.cb_kiln_cycle_history.addItems(['', *data])

    # Carrega ciclos
    def load_cycles(self):
        # Limpa campos
        self.cb_cycle_stock.clear()
        self.cb_cycle_cycle_history.clear()

        self.cb_foot_nfe.clear()
        self.cb_foot_nfe_history.clear()

        self.cb_cycle_nfe.clear()

        # Retorna dados
        query = self.database.read(
            table='estoque',
            fields=['estoque.ciclo', 'bitola', 'finalidade', 'estoque'],
            clause='LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo'
        )

        # Cria sets
        stock_bitolas = set()
        stock_ht_cycles = set()
        stock_kd_cycles = set()
        ht_cycles = set()
        all_cycles = set()

        # Abastece sets
        while query.next():
            cycle = query.value(0)
            bitola = query.value(1)
            finality = query.value(2)
            stock = query.value(3)

            all_cycles.add(cycle)

            if finality == 'HT':
                ht_cycles.add(cycle)

            if stock != '' and stock > 0:
                if finality == 'KD':
                    stock_kd_cycles.add(cycle)
                else:
                    stock_ht_cycles.add(cycle)

                stock_bitolas.add(bitola)

        # Cria set de ciclos em estoque
        stock_all_cycles = stock_kd_cycles.union(stock_ht_cycles)

        # Abastece campos de filtro
        self.cb_bitola_stock.addItem('')
        self.cb_cycle_stock.addItem('')
        self.cb_cycle_cycle_history.addItem('')
        self.cb_foot_nfe_history.addItem('')

        # Abastece campos
        self.cb_cycle_cycle_history.addItems(order_set(all_cycles))
        self.cb_foot_nfe_history.addItems(order_set(ht_cycles))

        self.cb_cycle_nfe.addItems(order_set(stock_kd_cycles))
        self.cb_foot_nfe.addItems(order_set(stock_ht_cycles))

        self.cb_cycle_stock.addItems(order_set(stock_all_cycles))
        self.cb_bitola_stock.addItems(order_set(stock_bitolas))


# Usado para auxiliar na depuração
def exception_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)
    sys.exit(1)


# Inicia o aplicativo
if __name__ == "__main__":
    # Altera id do aplicativo para evitar bugs com o ícone na barra de tarefas
    try:
        # noinspection PyUnresolvedReferences
        from ctypes import windll

        myappid = 'apps.controle_de_estoque.1.0.0'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    # Desativa splash do pyinstaller quando a aplicação carregar
    try:
        # noinspection PyUnresolvedReferences
        import pyi_splash

        pyi_splash.close()
    except ModuleNotFoundError:
        pass

    DEBUG = False

    if not DEBUG:
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Vincula hook para receber logs durante desenvolvimento
    sys.excepthook = exception_hook

    try:
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(u":/icons/assets/stock-48.png"))

        window = MainWindow()
        window.setStyleSheet('')
        window.show()

        sys.exit(app.exec())
    except Exception as e:
        logger = Logger()
        logger.exception('ERROR')
