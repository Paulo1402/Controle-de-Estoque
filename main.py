import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PySide6.QtGui import QIcon, QCloseEvent, QIntValidator
from PySide6.QtCore import QModelIndex, Qt, QSortFilterProxyModel, QRegularExpression

from ui.MainWindow import Ui_MainWindow
from services import *
from utils import *


# todo Bloquear adição e remoção de bitolas ao editar, forçar deletar ciclo / nfe para inserir
# todo Verificar se há estoque disponível para cada item de madeira tratada
# todo Verificar se há estoque disponível para pezinho

# todo QValidator com auto fix
# todo Adicionar efeito de transição ao trocar de páginas no multi-page


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Cria handles para TableWidget
        self.tw_cycle_handler = TableWidgetHandler(
            self,
            self.tw_cycle,
            self.bt_remove_bitola_cycle,
            [
                self.txt_bitola_cycle,
                self.txt_packs_cycle,
                self.txt_volume_cycle
            ],
            volume_field=self.txt_volume_nfe
        )

        self.tw_nfe_handler = TableWidgetHandler(
            self,
            self.tw_nfe,
            self.bt_remove_bitola_nfe,
            [
                self.cb_cycle_nfe,
                self.cb_bitola_nfe,
                self.txt_volume_nfe,
                self.txt_rework_nfe
            ],
            volume_field=self.txt_volume_nfe
        )

        self._ID_cycle = -1
        self._ID_nfe = -1

        self.animation = None

        # Abre conexão com o banco de dados
        self.database = DatabaseConnection()
        self.database.connect()

        # Inicialização
        self.init_ui()

        # Seta página inicial
        self.bt_cycle_menu.click()
        self.new_cycle()

    @property
    def ID_cycle(self):
        return self._ID_cycle

    @ID_cycle.setter
    def ID_cycle(self, value):
        self._ID_cycle = value
        flag = bool(value + 1)

        self.tw_cycle.setDisabled(flag)
        self.bt_delete_cycle.setDisabled(not flag)
        self.tab_widget_cycle.setCurrentIndex(0)

    @property
    def ID_nfe(self):
        return self._ID_nfe

    @ID_nfe.setter
    def ID_nfe(self, value):
        self._ID_nfe = value

    def closeEvent(self, event: QCloseEvent):
        # if Message.warning_question(self, 'Deseja fechar o aplicativo?') == Message.NO:
        #     event.ignore()
        #     return

        self.database.disconnect()
        event.accept()

    def init_ui(self):
        # Seta título da janela principal
        self.setWindowTitle('CONTROLE DE MADEIRA TRATADA')

        # Conecta botões do menu principal
        self.bt_cycle_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(0))
        self.bt_nfe_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(1))
        self.bt_stock_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(2))
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

        # Página Ciclo
        self.bt_delete_cycle.setDisabled(True)
        self.bt_edit_cycle_history.setDisabled(True)

        self.bt_new_cycle.clicked.connect(self.new_cycle)
        self.bt_save_cycle.clicked.connect(self.save_cycle)
        self.bt_delete_cycle.clicked.connect(self.delete_cycle)

        self.bt_add_bitola_cycle.clicked.connect(self.tw_cycle_handler.add)
        self.bt_remove_bitola_cycle.clicked.connect(self.tw_cycle_handler.remove)

        self.bt_search_cycle_history.clicked.connect(self.search_cycle_history)
        self.bt_clear_cycle_history.clicked.connect(self.clear_cycle_history)
        self.bt_edit_cycle_history.clicked.connect(self.edit_cycle_history)

        self.tv_cycle_history.setModel(TableModel(date=[3, 4], volume=[7, 8, 9, 10]))
        self.tv_cycle_history.clicked.connect(lambda: self.bt_edit_cycle_history.setDisabled(False))
        self.tv_cycle_history.doubleClicked.connect(self.track_cycle)

        self.tv_track_history.setModel(TableModel(date=[0], volume=[3]))
        self.tv_track_history.doubleClicked.connect(self.track_nfe)

        self.bt_back_track_history.clicked.connect(lambda: self.mp_cycle_historic.setCurrentIndex(0))

        # Página Nfe
        self.bt_delete_nfe.setDisabled(True)
        self.bt_delete_nfe.setDisabled(True)

        self.bt_new_nfe.clicked.connect(self.new_nfe)
        self.bt_save_nfe.clicked.connect(self.save_nfe)
        self.bt_delete_nfe.clicked.connect(self.delete_nfe)

        self.bt_add_bitola_nfe.clicked.connect(self.tw_nfe_handler.add)
        self.bt_remove_bitola_nfe.clicked.connect(self.tw_nfe_handler.remove)

        self.cb_cycle_nfe.currentIndexChanged.connect(self.load_nfe_bitola)

        self.bt_search_nfe_history.clicked.connect(self.search_nfe_history)
        self.bt_clear_nfe_history.clicked.connect(self.clear_nfe_history)
        self.bt_edit_nfe_history.clicked.connect(self.edit_nfe_history)

        self.tv_nfe_history.setModel(TableModel(date=[1], volume=[3]))
        self.tv_nfe_history.clicked.connect(lambda: self.bt_edit_nfe_history.setDisabled(False))

        # Página Estoque
        self.bt_discount_stock.setDisabled(True)
        self.bt_leaving_stock.setDisabled(True)

        self.bt_search_stock.clicked.connect(self.search_stock)
        self.bt_clear_stock.clicked.connect(self.clear_stock)

        self.bt_discount_stock.clicked.connect(self.discount_stock)
        self.bt_leaving_stock.clicked.connect(self.leaving_stock)

        # proxy_model = QSortFilterProxyModel()
        # proxy_model.setSourceModel(TableModel(volume=[4, 5, 6, 7]))
        # self.tv_stock.setModel(proxy_model)

        self.tv_stock.setModel(TableModel(volume=[4, 5, 6, 7]))
        self.tv_stock.setSortingEnabled(True)

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

    def start_app(self):
        # Verifica conexão após iniciar janela principal
        if self.database.connection_state == DatabaseConnection.State.DATABASE_NOT_FOUND:
            Message.critical(
                self,
                'CRÍTICO',
                'Erro ao acessar banco de dados!\n'
                'Se seu banco de dados estiver na rede verifique se há conexão com a internet.'
            )
        elif self.database.connection_state == DatabaseConnection.State.NO_DATABASE:
            Message.warning(self, 'ATENÇÃO', 'Insira um banco de dados para usar o programa.')
            self.action_config.trigger()

        # Configura dados
        self.setup_data()

    def setup_data(self):
        # Verifica conexão
        connected = self.database.connection_state == DatabaseConnection.State.CONNECTED

        self.action_import_backup.setDisabled(not connected)
        self.mp_main.setDisabled(not connected)

        # Carrega dados para dentro do app
        if connected:
            self.load_clients()
            self.load_kilns()
            self.load_cycles()

    # Página Ciclo
    def new_cycle(self):
        fields = [
            self.cb_kiln_cycle,
            self.txt_cycle_cycle,
            self.cb_entry_date_cycle,
            self.cb_exit_date_cycle
        ] + self.tw_cycle_handler.fields

        clear_fields(fields)

        self.rb_kd_cycle.setChecked(True)
        self.ID_cycle = -1

        query = self.database.read(
            table='ciclo',
            fields=['MAX(ciclo)']
        )

        query.first()
        self.txt_cycle_cycle.setText(str(query.value(0) + 1))

        for row in range(self.tw_cycle.rowCount()):
            self.tw_cycle.removeRow(row)

    def save_cycle(self):
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

        entry_date = parse_date(fields[2].currentText(), '%d/%m/%Y', '%Y-%m-%d')
        exit_date = parse_date(fields[3].currentText(), '%d/%m/%Y', '%Y-%m-%d')

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

        message = 'Deseja editar esse ciclo no banco de dados?'

        # Modo de Insert
        if self.ID_cycle == -1:
            if not self.database.is_unique('ciclo', 'ciclo', fields['ciclo']):
                Message.warning(self, 'ATENÇÃO', 'Esse ciclo já consta no banco de dados!')
                return

            message = message.replace('editar', 'inserir')

        # Faz pergunta de segurança ao usuário, caso não confirme aborta ação
        if Message.warning_question(self, message, Message.YES) == Message.NO:
            return

        try:
            # Modo de Insert
            if self.ID_cycle == -1:
                self.database.create(table='ciclo', fields=fields)
                message = 'Registro inserido com sucesso.'

                # Insere bitolas na tabela
                for row in range(self.tw_cycle.rowCount()):
                    bitola = self.tw_cycle.item(row, 1).text()
                    packs = self.tw_cycle.item(row, 2).text()
                    volume = self.tw_cycle.item(row, 3).text()

                    self.database.create(
                        table='bitola',
                        fields={
                            'ciclo': fields['ciclo'],
                            'bitola': bitola,
                            'fardos': packs,
                            'volume_tratado': volume
                        }
                    )
            # Modo de Update
            else:
                self.database.update(table='history', fields=fields, clause=f"WHERE ciclo LIKE {self.ID_cycle}")
                message = 'Registro alterado com sucesso.'

            # Prepara para novo registro e avisa usuário
            Message.information(self, 'AVISO', message)
            self.new_cycle()

            # Recria tabelas temporárias
            self.database.create_temp_table()
        except QueryError:
            Message.critical(self, 'CRÍTICO', 'Algo deu errado durante a operação!')

    def delete_cycle(self):
        # Guard clause
        if not Message.warning_question(
                self, 'Deseja deletar esse registro? Todos os registros referentes esse ciclo serão'
                      ' deletados também e precisarão serem inseridos novamente.', Message.NO
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

    def search_cycle_history(self):
        # Retorna dados dos campos
        kiln = self.cb_kiln_cycle_history.currentText()
        cycle = self.cb_cycle_cycle_history.currentText()
        start_date = parse_date(
            self.cb_entry_date_cycle_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MIN
        )
        end_date = parse_date(
            self.cb_exit_date_cycle_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MAX
        )
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

        # Esconde colunas que não são necessárias visualmente
        self.tv_cycle_history.setColumnHidden(0, True)
        self.tv_cycle_history.setColumnHidden(1, True)
        self.tv_cycle_history.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)

    def clear_cycle_history(self):
        self.cb_kiln_cycle_history.setCurrentIndex(0)
        self.cb_cycle_cycle_history.setCurrentIndex(0)

        self.cb_entry_date_cycle_history.setCurrentText('')
        self.cb_exit_date_cycle_history.setCurrentText('')

        self.txt_bitola_cycle_history.clear()
        self.rb_kd_cycle_history.setChecked(True)

        self.bt_edit_cycle_history.setDisabled(True)
        self.tv_cycle_history.clearSelection()

    def edit_cycle_history(self):
        # Aborta slot caso não haja indexes selecionados
        if not self.tv_cycle_history.selectedIndexes():
            return

        # Retorna a linha referente a seleção e o model da table view
        row = self.tv_cycle_history.selectedIndexes()[0].row()
        model = self.tv_cycle_history.model()

        # Retorna dados da table view
        bitola_id = model.index(row, 0).data()
        kiln = model.index(row, 1).data()
        cycle = model.index(row, 2).data()
        entry_date = model.index(row, 3).data()
        exit_date = model.index(row, 4).data()
        finality = model.index(row, 5).data()

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
            clause='WHERE bitola_id LIKE ?',
            values=[bitola_id]
        )

        # Remove linhas na table widget caso exista alguma
        for row in range(self.tw_cycle.rowCount()):
            self.tw_cycle.removeRow(row)

        # Preenche table widget com dados da query
        while query.next():
            row = self.tw_cycle.rowCount()
            self.tw_cycle.insertRow(row)

            for i in range(4):
                self.tw_cycle.setItem(row, i, QTableWidgetItem(str(query.value(i))))

        # Atualiza ID_cycle com base no ciclo em selecionado
        self.ID_cycle = cycle

    def track_cycle(self, index: QModelIndex):
        row = index.row()

        fields = [
            (self.txt_kiln_track_history, 1),
            (self.txt_cycle_track_history, 2),
            (self.txt_entry_date_track_history, 3),
            (self.txt_exit_date_track_history, 4),
            (self.txt_bitola_track_history, 6)
        ]

        model = self.tv_cycle_history.model()
        bitola_id = model.index(row, 0).data()

        if model.index(row, 5).data() == 'KD':
            self.rb_kd_track_history.setChecked(True)

        for field, col in fields:
            data = model.index(row, col).data()
            field.setText(str(data))

        query = self.database.read(
            table='nfe',
            fields=['data', 'nfe.nfe', 'cliente', 'nfe.volume', 'retrabalho'],
            clause="LEFT JOIN nfe_info ON nfe.nfe = nfe_info.nfe "
                   "WHERE bitola_id LIKE ?",
            values=[bitola_id]
        )

        model: TableModel = self.tv_track_history.model()
        model.setQuery(query)

        headers = ['DATA', 'NFE', 'CLIENTE', 'VOLUME', 'RETRABALHO']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        self.tv_track_history.setColumnHidden(0, True)
        self.tv_track_history.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        query = self.database.read(
            table='residuo',
            fields=['data', 'volume'],
            clause='WHERE bitola_id LIKE ?',
            values=[bitola_id]
        )

        if query.next():
            date = parse_date(query.value(0), input_format='%Y-%m-%d', output_format='%d/%m/%Y')
            value = query.value(1)
        else:
            date = ''
            value = 0

        self.txt_leaving_date_track_history.setText(date)
        self.txt_leaving_volume_track_history.setText(from_float_to_volume(value))

        query = self.database.read(
            table='estoque',
            fields=['estoque'],
            clause='WHERE bitola_id LIKE ?',
            values=[bitola_id]
        )

        value = query.value(0) if query.next() else 0

        self.txt_stock_volume_track_history.setText(from_float_to_volume(value))
        self.mp_cycle_historic.setCurrentIndex(1)

    def track_nfe(self, index: QModelIndex):
        row = index.row()
        model = self.tv_track_history.model()

        nfe = model.index(row, 1).data()
        client = model.index(row, 2).data()

        self.txt_nfe_nfe_history.setText(str(nfe))
        self.cb_client_nfe_history.setCurrentText(client)

        self.bt_search_nfe_history.click()

        self.mp_main.setCurrentIndex(1)
        self.tab_widget_nfe.setCurrentIndex(1)

    # Página NFE
    def new_nfe(self):
        fields = [
            self.cb_date_nfe,
            self.cb_client_nfe,
            self.txt_nfe_nfe,
            self.txt_total_volume_nfe,
            self.txt_packs_nfe,
            self.cb_foot_nfe
        ] + self.tw_nfe_handler.fields

        clear_fields(fields)

        for row in range(self.tw_nfe.rowCount()):
            self.tw_nfe.removeRow(row)

        self.ID = -1

    def save_nfe(self):
        fields = [
            self.cb_date_nfe,
            self.cb_client_nfe,
            self.txt_nfe_nfe,
            self.txt_volume_nfe,
            self.txt_packs_nfe,
            self.cb_foot_nfe
        ]

        # Verifica se há campos em branco
        empty_fields = get_empty_fields(fields)

        if len(empty_fields) > 0:
            Message.warning(self, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            empty_fields[0].setFocus()
            return

        if not self.tw_nfe.rowCount():
            if Message.warning_question(
                    self,
                    'Não há bitolas tratadas nesse registro, deseja continuar mesmo assim?'
            ) == Message.NO:
                return

    def delete_nfe(self):
        pass

    def load_nfe_bitola(self, index: int):
        if index == -1:
            self.cb_bitola_nfe.clear()
            return

        ciclo = self.cb_cycle_nfe.itemText(index)

        query = self.database.read(
            table='estoque',
            fields=['bitola'],
            clause='WHERE estoque.ciclo LIKE ?',
            values=[ciclo]
        )

        data = []

        while query.next():
            data.append(query.value(0))

        self.cb_bitola_nfe.clear()
        self.cb_bitola_nfe.addItems(data)

    def search_nfe_history(self):
        nfe = self.txt_nfe_nfe_history.text()
        client = self.cb_client_nfe_history.currentText()
        foot_cycle = self.cb_foot_nfe_history.currentText()
        start_date = parse_date(
            self.cb_start_date_nfe_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MIN
        )
        end_date = parse_date(
            self.cb_end_date_nfe_history.currentText(), '%d/%m/%Y', '%Y-%m-%d', on_fail=DateMinMax.MAX
        )

        clause = "WHERE data >= ? AND data <= ? AND nfe LIKE '%' || ? || '%' AND cliente LIKE '%' || ? || '%'"
        values = [start_date, end_date, nfe, client]

        if foot_cycle:
            clause += ' AND ciclo_pezinho LIKE ?'
            values.append(foot_cycle)

        query = self.database.read(
            table='nfe_info',
            fields=['nfe', 'data', 'cliente', 'volume', 'fardos', 'ciclo_pezinho'],
            clause=clause,
            values=values
        )

        model: TableModel = self.tv_nfe_history.model()
        model.setQuery(query)

        headers = ['NFE', 'DATA', 'CLIENTE', 'VOLUME', 'FARDOS', 'CICLO PEZINHO']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        self.tv_nfe_history.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

    def clear_nfe_history(self):
        self.txt_nfe_nfe_history.clear()
        self.cb_client_nfe_history.setCurrentIndex(0)

        self.cb_start_date_nfe_history.setCurrentText('')
        self.cb_end_date_nfe_history.setCurrentText('')

        self.cb_foot_nfe_history.setCurrentIndex(0)

        self.bt_edit_nfe_history.setDisabled(True)
        self.tv_nfe_history.clearSelection()

    def edit_nfe_history(self):
        pass

    # Página Histórico
    def search_stock(self):
        cycle = self.cb_cycle_stock.currentText()
        bitola = self.cb_bitola_stock.currentText()
        finality = 'KD' if self.rb_kd_stock.isChecked() else 'HT'

        clause = "LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo " \
                 "WHERE estoque > 0 AND finalidade LIKE ?"
        values = [finality]

        if cycle:
            clause += ' AND estoque.ciclo LIKE ?'
            values.append(cycle)

        if bitola:
            clause += ' AND bitola LIKE ?'
            values.append(bitola)

        query = self.database.read(
            table='estoque',
            fields=['bitola_id', 'estoque.ciclo', 'bitola', 'fardos', 'volume_tratado', 'volume_vendido', 'residuo',
                    'estoque', 'finalidade'],
            clause=clause,
            values=values
        )

        model: TableModel = self.tv_stock.model().sourceModel()
        model.setQuery(query)

        headers = ['ID', 'CICLO', 'BITOLA', 'FARDOS', 'TRATADO', 'VENDIDO', 'RESÍDUO', 'ESTOQUE', 'FINALIDADE']

        for i, header in enumerate(headers):
            model.setHeaderData(i, Qt.Orientation.Horizontal, header)

        self.tv_stock.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

    def clear_stock(self):
        self.cb_cycle_stock.setCurrentIndex(0)
        self.cb_bitola_stock.setCurrentIndex(0)

        self.rb_kd_stock.setChecked(True)

        self.bt_leaving_stock.setDisabled(True)
        self.bt_discount_stock.setDisabled(True)
        self.tv_stock.clearSelection()

    def discount_stock(self):
        pass

    def leaving_stock(self):
        pass

    # Dados
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

        # model = ListModel()
        # model.setQuery(query)
        #
        # self.cb_kiln_cycle.setModel(model)
        # self.cb_kiln_cycle_history.setModel(model)

    def load_cycles(self):
        query = self.database.read(
            table='ciclo',
            fields=['ciclo']
        )

        data = []

        while query.next():
            data.append(str(query.value(0)))

        self.cb_cycle_stock.clear()
        self.cb_cycle_cycle_history.clear()

        self.cb_cycle_stock.addItems(['', *data])
        self.cb_cycle_cycle_history.addItems(['', *data])

        query = self.database.read(
            table='estoque',
            fields=['estoque.ciclo'],
            clause='LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo '
                   'WHERE estoque > 0 AND finalidade LIKE ?',
            values=['HT'],
            distinct=True
        )

        data = []

        while query.next():
            data.append(str(query.value(0)))

        self.cb_foot_nfe.clear()
        self.cb_foot_nfe_history.clear()

        self.cb_foot_nfe.addItems(data)
        self.cb_foot_nfe_history.addItems(['', *data])

        query = self.database.read(
            table='estoque',
            fields=['estoque.ciclo'],
            clause='LEFT JOIN ciclo ON estoque.ciclo = ciclo.ciclo '
                   'WHERE estoque > 0 AND finalidade LIKE ?',
            values=['KD'],
            distinct=True
        )

        data = []

        while query.next():
            data.append(str(query.value(0)))

        self.cb_cycle_nfe.clear()
        self.cb_cycle_nfe.addItems(data)


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

    # Vincula hook personalizado para receber logs durante desenvolvimento
    sys.excepthook = exception_hook

    qt = QApplication(sys.argv)
    qt.setStyle('Fusion')
    qt.setWindowIcon(QIcon(u":/icons/assets/stock-48.png"))

    app = App()
    app.show()
    app.start_app()

    sys.exit(qt.exec())
