"""
MIT License

Copyright (c) 2016 Zeke Barge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import zeex.core.utility.pandatools as pandatools
from zeex.core.compat import QtGui
from zeex.core.ui.file_ui import Ui_FileWindow
from zeex.core.utility.widgets import create_standard_item_model
from zeex.core.views.actions.analyze import FileAnalyzerDialog
from zeex.core.views.actions.export import DataFrameModelExportDialog
from zeex.core.views.actions.fields_edit import FieldsEditDialog
from zeex.core.views.actions.merge_purge import MergePurgeDialog
from zeex.core.views.actions.normalize import ColumnNormalizerDialog
from zeex.core.views.actions.split import SplitFileDialog
from zeex.icons import icons_rc
from zeex.core.ctrls.dataframe import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget


class FileTableWindow(QtGui.QMainWindow, Ui_FileWindow):
    """
    A spreadsheet-like window that displays rows and columns
    of the source DataFrame. Menu actions in this window allow the user to make
    updates to the DataFrame and see the changes update in the view.
    """
    def __init__(self, model: DataFrameModel, df_manager, **kwargs):
        QtGui.QMainWindow.__init__(self, parent=kwargs.pop('parent', None))
        self.df_manager = df_manager
        self._df_model = None
        self._df_model_transposed = None
        self._view_transposed = False
        self._widget = DataTableWidget()
        self._widget.setModel(model)
        kwargs['parent'] = self
        self.setupUi(self)
        self.dialog_fields_edit = FieldsEditDialog(model, parent=self)
        self.dialog_export = DataFrameModelExportDialog(df_manager, filename=model.filePath,
                                                        allow_multi_source=False, parent=self)
        self.dialog_split = SplitFileDialog(model, parent=self)
        self.dialog_analyze = FileAnalyzerDialog(model, parent=self)
        self.dialog_normalize = ColumnNormalizerDialog(model, parent=self)
        self.dialog_merge_purge = kwargs.pop('merge_purge_dialog', MergePurgeDialog(df_manager,
                                                                                    source_model=model,
                                                                                    ))
        self.connect_actions()
        self.connect_icons()

    @property
    def widget(self):
        # Overrides the Ui_FileWindow.widget
        return self._widget

    @widget.setter
    def widget(self, x):
        # Prevent the Ui_FileWindow from overriding our widget.
        pass

    @property
    def df_model(self) -> DataFrameModel:
        return self.widget.model()

    @property
    def df(self):
        return self.df_model.dataFrame()

    def connect_actions(self):
        self.actionAnalyze.triggered.connect(self.dialog_analyze.show)
        self.actionDropNaN.triggered.connect(self.drop_nan)
        self.actionEditFields.triggered.connect(self.dialog_fields_edit.show)
        self.actionMergePurge.triggered.connect(self.dialog_merge_purge.show)
        self.actionNormalize.triggered.connect(self.dialog_normalize.show)
        self.actionSave.triggered.connect(self.save)
        self.actionSaveAs.triggered.connect(self.dialog_export.show)
        self.actionSplit.triggered.connect(self.dialog_split.show)
        self.actionTranspose.triggered.connect(self.transpose)
        self.dialog_export.btnBrowseSource.setVisible(False)
        # TODO: Make these actions do something then activate.
        self.actionExecuteScript.setVisible(False)
        self.actionSuppress.setVisible(False)
        self.actionDelete.setVisible(False)
        self.df_model.dataChanged.connect(self.sync)
        self.sync()

    def connect_icons(self):
        self.setWindowIcon(QtGui.QIcon(':/standard_icons/spreadsheet.png'))

    def transpose(self):
        """
        TODO: Give this functionality to the DataFrameModel
        :return:
        """
        rows = self.df_model.dataFrame().index.size
        if rows > 150:
            raise Exception("Max size to transpose is 150 rows to columns.")

        if self._df_model_transposed is None:
            df = pandatools.dataframe_transpose(self.df_model.dataFrame())
            self._df_model_transposed = DataFrameModel(dataFrame=df)
            self._df_model = self.df_model

        if self._view_transposed is True:
            self.widget.setModel(self._df_model)
            self._view_transposed = False
        else:
            self.widget.setModel(self._df_model_transposed)
            self._view_transposed = True

    def drop_nan(self):
        for c in self.df.columns:
            dtype = str(self.df[c].dtype)
            if 'float' in dtype:
                sum = self.df[c].sum()
                if sum == 0 or str(sum) == 'nan':
                    self.df.loc[:, c] = self.df.loc[:, c].apply(lambda x: str(x))

            if str(self.df[c].dtype) == 'object':
                self.df.loc[:, c] = pandatools.series_blank_na(self.df.loc[:, c])
        self.df_model.dataChanged.emit()

    def sync(self):
        fp = self.df_model.filePath
        self.setWindowTitle(fp)
        cb_model = create_standard_item_model([fp])
        self.dialog_export.comboBoxSource.setModel(cb_model)
        self._df_model_transposed = None
        
        if self._df_model is not None:
            self.widget.setModel(self._df_model)

    def save(self):
        self.dialog_export.set_destination_path_from_source()
        self.dialog_export.export()



