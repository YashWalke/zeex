# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normalize.ui'
#
# Created: Wed Dec 28 03:34:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ColumnNormalizerDialog(object):
    def setupUi(self, ColumnNormalizerDialog):
        ColumnNormalizerDialog.setObjectName("ColumnNormalizerDialog")
        ColumnNormalizerDialog.resize(355, 506)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ColumnNormalizerDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.columnsLabel = QtGui.QLabel(ColumnNormalizerDialog)
        self.columnsLabel.setObjectName("columnsLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.columnsLabel)
        self.listViewColumns = ColumnsListView(ColumnNormalizerDialog)
        self.listViewColumns.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listViewColumns.setObjectName("listViewColumns")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.listViewColumns)
        self.removeSpecialCharactersLabel = QtGui.QLabel(ColumnNormalizerDialog)
        self.removeSpecialCharactersLabel.setObjectName("removeSpecialCharactersLabel")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.removeSpecialCharactersLabel)
        self.trimSpacesLabel = QtGui.QLabel(ColumnNormalizerDialog)
        self.trimSpacesLabel.setObjectName("trimSpacesLabel")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.trimSpacesLabel)
        self.checkBoxTrimSpaces = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxTrimSpaces.setObjectName("checkBoxTrimSpaces")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBoxTrimSpaces)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ColumnNormalizerDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.checkBoxMergeOrSplit = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxMergeOrSplit.setObjectName("checkBoxMergeOrSplit")
        self.gridLayout.addWidget(self.checkBoxMergeOrSplit, 0, 0, 1, 1)
        self.lineEditMergeOrSplitSep = QtGui.QLineEdit(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMergeOrSplitSep.sizePolicy().hasHeightForWidth())
        self.lineEditMergeOrSplitSep.setSizePolicy(sizePolicy)
        self.lineEditMergeOrSplitSep.setObjectName("lineEditMergeOrSplitSep")
        self.gridLayout.addWidget(self.lineEditMergeOrSplitSep, 0, 2, 1, 1)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.replaceSpacesLabel = QtGui.QLabel(ColumnNormalizerDialog)
        self.replaceSpacesLabel.setObjectName("replaceSpacesLabel")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.replaceSpacesLabel)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBoxReplaceSpaces = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxReplaceSpaces.setObjectName("checkBoxReplaceSpaces")
        self.gridLayout_3.addWidget(self.checkBoxReplaceSpaces, 0, 0, 1, 1)
        self.lineEditReplaceSpaces = QtGui.QLineEdit(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditReplaceSpaces.sizePolicy().hasHeightForWidth())
        self.lineEditReplaceSpaces.setSizePolicy(sizePolicy)
        self.lineEditReplaceSpaces.setObjectName("lineEditReplaceSpaces")
        self.gridLayout_3.addWidget(self.lineEditReplaceSpaces, 0, 1, 1, 1)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.gridLayout_3)
        self.setCaseLabel = QtGui.QLabel(ColumnNormalizerDialog)
        self.setCaseLabel.setObjectName("setCaseLabel")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.setCaseLabel)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBoxSetCase = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxSetCase.setObjectName("checkBoxSetCase")
        self.gridLayout_2.addWidget(self.checkBoxSetCase, 0, 0, 1, 1)
        self.comboBoxSetCase = QtGui.QComboBox(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSetCase.sizePolicy().hasHeightForWidth())
        self.comboBoxSetCase.setSizePolicy(sizePolicy)
        self.comboBoxSetCase.setObjectName("comboBoxSetCase")
        self.gridLayout_2.addWidget(self.comboBoxSetCase, 0, 1, 1, 1)
        self.formLayout_2.setLayout(5, QtGui.QFormLayout.FieldRole, self.gridLayout_2)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxDropFillNA = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxDropFillNA.setObjectName("checkBoxDropFillNA")
        self.gridLayout_4.addWidget(self.checkBoxDropFillNA, 0, 1, 1, 1)
        self.lineEditDropFillNA = QtGui.QLineEdit(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDropFillNA.sizePolicy().hasHeightForWidth())
        self.lineEditDropFillNA.setSizePolicy(sizePolicy)
        self.lineEditDropFillNA.setObjectName("lineEditDropFillNA")
        self.gridLayout_4.addWidget(self.lineEditDropFillNA, 0, 2, 1, 1)
        self.comboBoxDropFillNAHow = QtGui.QComboBox(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDropFillNAHow.sizePolicy().hasHeightForWidth())
        self.comboBoxDropFillNAHow.setSizePolicy(sizePolicy)
        self.comboBoxDropFillNAHow.setObjectName("comboBoxDropFillNAHow")
        self.comboBoxDropFillNAHow.addItem("")
        self.comboBoxDropFillNAHow.addItem("")
        self.gridLayout_4.addWidget(self.comboBoxDropFillNAHow, 1, 2, 1, 1)
        self.labelDropFillNAHow = QtGui.QLabel(ColumnNormalizerDialog)
        self.labelDropFillNAHow.setObjectName("labelDropFillNAHow")
        self.gridLayout_4.addWidget(self.labelDropFillNAHow, 1, 1, 1, 1)
        self.formLayout_2.setLayout(6, QtGui.QFormLayout.FieldRole, self.gridLayout_4)
        self.btnUncheckAll = QtGui.QPushButton(ColumnNormalizerDialog)
        self.btnUncheckAll.setObjectName("btnUncheckAll")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.btnUncheckAll)
        self.buttonBox = QtGui.QDialogButtonBox(ColumnNormalizerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelMergeOrSplit = QtGui.QLabel(ColumnNormalizerDialog)
        self.labelMergeOrSplit.setObjectName("labelMergeOrSplit")
        self.gridLayout_6.addWidget(self.labelMergeOrSplit, 0, 0, 1, 1)
        self.comboBoxMergeOrSplit = QtGui.QComboBox(ColumnNormalizerDialog)
        self.comboBoxMergeOrSplit.setObjectName("comboBoxMergeOrSplit")
        self.comboBoxMergeOrSplit.addItem("")
        self.comboBoxMergeOrSplit.addItem("")
        self.gridLayout_6.addWidget(self.comboBoxMergeOrSplit, 0, 1, 1, 1)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.LabelRole, self.gridLayout_6)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.labelDropFillNA = QtGui.QLabel(ColumnNormalizerDialog)
        self.labelDropFillNA.setObjectName("labelDropFillNA")
        self.gridLayout_7.addWidget(self.labelDropFillNA, 0, 0, 1, 1)
        self.comboBoxDropFillNA = QtGui.QComboBox(ColumnNormalizerDialog)
        self.comboBoxDropFillNA.setObjectName("comboBoxDropFillNA")
        self.comboBoxDropFillNA.addItem("")
        self.comboBoxDropFillNA.addItem("")
        self.gridLayout_7.addWidget(self.comboBoxDropFillNA, 0, 1, 1, 1)
        self.formLayout_2.setLayout(6, QtGui.QFormLayout.LabelRole, self.gridLayout_7)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.checkBoxRemoveSpecialChars = QtGui.QCheckBox(ColumnNormalizerDialog)
        self.checkBoxRemoveSpecialChars.setObjectName("checkBoxRemoveSpecialChars")
        self.gridLayout_8.addWidget(self.checkBoxRemoveSpecialChars, 0, 0, 1, 1)
        self.lineEditRemoveSpecialCharsKeeps = QtGui.QLineEdit(ColumnNormalizerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRemoveSpecialCharsKeeps.sizePolicy().hasHeightForWidth())
        self.lineEditRemoveSpecialCharsKeeps.setSizePolicy(sizePolicy)
        self.lineEditRemoveSpecialCharsKeeps.setObjectName("lineEditRemoveSpecialCharsKeeps")
        self.gridLayout_8.addWidget(self.lineEditRemoveSpecialCharsKeeps, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(ColumnNormalizerDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 1, 1, 1)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_8)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btnSaveSettings = QtGui.QPushButton(ColumnNormalizerDialog)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.gridLayout_5.addWidget(self.btnSaveSettings, 0, 0, 1, 1)
        self.comboBoxSettingsFiles = QtGui.QComboBox(ColumnNormalizerDialog)
        self.comboBoxSettingsFiles.setObjectName("comboBoxSettingsFiles")
        self.gridLayout_5.addWidget(self.comboBoxSettingsFiles, 0, 2, 1, 1)
        self.btnLoadSettings = QtGui.QPushButton(ColumnNormalizerDialog)
        self.btnLoadSettings.setObjectName("btnLoadSettings")
        self.gridLayout_5.addWidget(self.btnLoadSettings, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ColumnNormalizerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ColumnNormalizerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ColumnNormalizerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ColumnNormalizerDialog)

    def retranslateUi(self, ColumnNormalizerDialog):
        ColumnNormalizerDialog.setWindowTitle(QtGui.QApplication.translate("ColumnNormalizerDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.columnsLabel.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.listViewColumns.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Columns in the data to be normalized.", None, QtGui.QApplication.UnicodeUTF8))
        self.removeSpecialCharactersLabel.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Remove Special Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.trimSpacesLabel.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Trim Spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTrimSpaces.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - trim spaces from left/right", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Separator", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMergeOrSplit.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - split or merge column(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMergeOrSplitSep.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Separator(s) to split or mege on (e.g:    , (comma)    (space))", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceSpacesLabel.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Replace Spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxReplaceSpaces.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - Replace spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditReplaceSpaces.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "replace spaces with text (e.g:     _     )", None, QtGui.QApplication.UnicodeUTF8))
        self.setCaseLabel.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Set Case", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSetCase.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - set the case upper/lower/proper", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSetCase.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Set Case option lower/upper/proper", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDropFillNA.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - Drop or Fill NA values", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDropFillNA.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Value to use to fill NA values", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNAHow.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "\'all\' drops/fill rows only if all columns are NA.", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNAHow.setItemText(0, QtGui.QApplication.translate("ColumnNormalizerDialog", "any", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNAHow.setItemText(1, QtGui.QApplication.translate("ColumnNormalizerDialog", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDropFillNAHow.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "how", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUncheckAll.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Uncheck all activation options & selected columns.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUncheckAll.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Uncheck All", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMergeOrSplit.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Merge/Split", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMergeOrSplit.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Select Split or Merge", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMergeOrSplit.setItemText(0, QtGui.QApplication.translate("ColumnNormalizerDialog", "Split", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMergeOrSplit.setItemText(1, QtGui.QApplication.translate("ColumnNormalizerDialog", "Merge", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDropFillNA.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Drop/Fill NA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNA.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Drop or fill NA values in selected columns", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNA.setItemText(0, QtGui.QApplication.translate("ColumnNormalizerDialog", "Drop NA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDropFillNA.setItemText(1, QtGui.QApplication.translate("ColumnNormalizerDialog", "Fill NA", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRemoveSpecialChars.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Activate - remove special characters from columns", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditRemoveSpecialCharsKeeps.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "special characters to not remove (e.g \' -%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Keep", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveSettings.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Save a template with all normalization settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveSettings.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadSettings.setWhatsThis(QtGui.QApplication.translate("ColumnNormalizerDialog", "Load a pre-saved .ini template file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadSettings.setText(QtGui.QApplication.translate("ColumnNormalizerDialog", "Load Settings", None, QtGui.QApplication.UnicodeUTF8))

from core.views.dataframe import ColumnsListView
