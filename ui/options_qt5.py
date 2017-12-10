# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionsGroup(object):
    def setupUi(self, OptionsGroup):
        OptionsGroup.setObjectName("OptionsGroup")
        OptionsGroup.resize(752, 283)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OptionsGroup.sizePolicy().hasHeightForWidth())
        OptionsGroup.setSizePolicy(sizePolicy)
        OptionsGroup.setMinimumSize(QtCore.QSize(0, 249))
        self.gridLayout = QtWidgets.QGridLayout(OptionsGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.rbZoomMax = QtWidgets.QRadioButton(OptionsGroup)
        self.rbZoomMax.setEnabled(False)
        self.rbZoomMax.setChecked(True)
        self.rbZoomMax.setObjectName("rbZoomMax")
        self.buttonGroup = QtWidgets.QButtonGroup(OptionsGroup)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbZoomMax)
        self.gridLayout.addWidget(self.rbZoomMax, 6, 1, 1, 1)
        self.chkClipTiles = QtWidgets.QCheckBox(OptionsGroup)
        self.chkClipTiles.setObjectName("chkClipTiles")
        self.gridLayout.addWidget(self.chkClipTiles, 3, 0, 1, 2)
        self.chkApplyStyles = QtWidgets.QCheckBox(OptionsGroup)
        self.chkApplyStyles.setChecked(True)
        self.chkApplyStyles.setObjectName("chkApplyStyles")
        self.gridLayout.addWidget(self.chkApplyStyles, 9, 0, 1, 2)
        self.chkMergeTiles = QtWidgets.QCheckBox(OptionsGroup)
        self.chkMergeTiles.setChecked(False)
        self.chkMergeTiles.setObjectName("chkMergeTiles")
        self.gridLayout.addWidget(self.chkMergeTiles, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbZoomManual = QtWidgets.QRadioButton(OptionsGroup)
        self.rbZoomManual.setEnabled(False)
        self.rbZoomManual.setText("")
        self.rbZoomManual.setObjectName("rbZoomManual")
        self.buttonGroup.addButton(self.rbZoomManual)
        self.horizontalLayout.addWidget(self.rbZoomManual)
        self.zoomSpin = QtWidgets.QSpinBox(OptionsGroup)
        self.zoomSpin.setEnabled(False)
        self.zoomSpin.setMaximumSize(QtCore.QSize(70, 16777215))
        self.zoomSpin.setObjectName("zoomSpin")
        self.horizontalLayout.addWidget(self.zoomSpin, 0, QtCore.Qt.AlignLeft)
        self.lblZoomRange = QtWidgets.QLabel(OptionsGroup)
        self.lblZoomRange.setObjectName("lblZoomRange")
        self.horizontalLayout.addWidget(self.lblZoomRange)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 3, 1, 1)
        self.chkLimitNrOfTiles = QtWidgets.QCheckBox(OptionsGroup)
        self.chkLimitNrOfTiles.setChecked(True)
        self.chkLimitNrOfTiles.setObjectName("chkLimitNrOfTiles")
        self.gridLayout_5.addWidget(self.chkLimitNrOfTiles, 1, 0, 1, 1)
        self.spinNrOfLoadedTiles = QtWidgets.QSpinBox(OptionsGroup)
        self.spinNrOfLoadedTiles.setEnabled(True)
        self.spinNrOfLoadedTiles.setMinimumSize(QtCore.QSize(0, 21))
        self.spinNrOfLoadedTiles.setMinimum(1)
        self.spinNrOfLoadedTiles.setMaximum(9999)
        self.spinNrOfLoadedTiles.setProperty("value", 20)
        self.spinNrOfLoadedTiles.setObjectName("spinNrOfLoadedTiles")
        self.gridLayout_5.addWidget(self.spinNrOfLoadedTiles, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNumberTilesInCurrentExtent = QtWidgets.QLabel(OptionsGroup)
        self.lblNumberTilesInCurrentExtent.setObjectName("lblNumberTilesInCurrentExtent")
        self.gridLayout_5.addWidget(self.lblNumberTilesInCurrentExtent, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnResetToBasemapDefaults = QtWidgets.QPushButton(OptionsGroup)
        self.btnResetToBasemapDefaults.setMinimumSize(QtCore.QSize(100, 0))
        self.btnResetToBasemapDefaults.setCheckable(True)
        self.btnResetToBasemapDefaults.setChecked(False)
        self.btnResetToBasemapDefaults.setAutoExclusive(True)
        self.btnResetToBasemapDefaults.setObjectName("btnResetToBasemapDefaults")
        self.horizontalLayout_2.addWidget(self.btnResetToBasemapDefaults)
        self.btnResetToAnalysisDefaults = QtWidgets.QPushButton(OptionsGroup)
        self.btnResetToAnalysisDefaults.setMinimumSize(QtCore.QSize(100, 0))
        self.btnResetToAnalysisDefaults.setCheckable(True)
        self.btnResetToAnalysisDefaults.setAutoExclusive(True)
        self.btnResetToAnalysisDefaults.setObjectName("btnResetToAnalysisDefaults")
        self.horizontalLayout_2.addWidget(self.btnResetToAnalysisDefaults)
        self.btnResetToInspectionDefaults = QtWidgets.QPushButton(OptionsGroup)
        self.btnResetToInspectionDefaults.setMinimumSize(QtCore.QSize(100, 0))
        self.btnResetToInspectionDefaults.setCheckable(True)
        self.btnResetToInspectionDefaults.setAutoExclusive(True)
        self.btnResetToInspectionDefaults.setObjectName("btnResetToInspectionDefaults")
        self.horizontalLayout_2.addWidget(self.btnResetToInspectionDefaults)
        self.btnManualSettings = QtWidgets.QPushButton(OptionsGroup)
        self.btnManualSettings.setMinimumSize(QtCore.QSize(100, 0))
        self.btnManualSettings.setCheckable(True)
        self.btnManualSettings.setChecked(True)
        self.btnManualSettings.setAutoExclusive(True)
        self.btnManualSettings.setObjectName("btnManualSettings")
        self.horizontalLayout_2.addWidget(self.btnManualSettings)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 11, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(OptionsGroup)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.chkSetBackgroundColor = QtWidgets.QCheckBox(OptionsGroup)
        self.chkSetBackgroundColor.setChecked(True)
        self.chkSetBackgroundColor.setObjectName("chkSetBackgroundColor")
        self.gridLayout.addWidget(self.chkSetBackgroundColor, 10, 0, 1, 2)
        self.chkAutoZoom = QtWidgets.QCheckBox(OptionsGroup)
        self.chkAutoZoom.setChecked(True)
        self.chkAutoZoom.setObjectName("chkAutoZoom")
        self.gridLayout.addWidget(self.chkAutoZoom, 4, 0, 1, 2)

        self.retranslateUi(OptionsGroup)
        QtCore.QMetaObject.connectSlotsByName(OptionsGroup)
        OptionsGroup.setTabOrder(self.chkLimitNrOfTiles, self.spinNrOfLoadedTiles)
        OptionsGroup.setTabOrder(self.spinNrOfLoadedTiles, self.chkMergeTiles)
        OptionsGroup.setTabOrder(self.chkMergeTiles, self.chkClipTiles)
        OptionsGroup.setTabOrder(self.chkClipTiles, self.rbZoomMax)
        OptionsGroup.setTabOrder(self.rbZoomMax, self.rbZoomManual)
        OptionsGroup.setTabOrder(self.rbZoomManual, self.zoomSpin)
        OptionsGroup.setTabOrder(self.zoomSpin, self.chkApplyStyles)
        OptionsGroup.setTabOrder(self.chkApplyStyles, self.btnResetToBasemapDefaults)
        OptionsGroup.setTabOrder(self.btnResetToBasemapDefaults, self.btnResetToAnalysisDefaults)
        OptionsGroup.setTabOrder(self.btnResetToAnalysisDefaults, self.btnResetToInspectionDefaults)

    def retranslateUi(self, OptionsGroup):
        _translate = QtCore.QCoreApplication.translate
        OptionsGroup.setWindowTitle(_translate("OptionsGroup", "Options"))
        OptionsGroup.setTitle(_translate("OptionsGroup", "Options"))
        self.rbZoomMax.setText(_translate("OptionsGroup", "Max. Zoom"))
        self.chkClipTiles.setText(_translate("OptionsGroup", "Clip each tile at bounds (slow)"))
        self.chkApplyStyles.setToolTip(_translate("OptionsGroup", "Apply a build-in, predefined QGIS style made for OpenMapTiles (instead of random QGIS default style)"))
        self.chkApplyStyles.setText(_translate("OptionsGroup", "Apply GL JSON style (if specified)"))
        self.chkMergeTiles.setText(_translate("OptionsGroup", "Merge tiles (slow)"))
        self.lblZoomRange.setText(_translate("OptionsGroup", "TextLabel"))
        self.chkLimitNrOfTiles.setToolTip(_translate("OptionsGroup", "<html><head/><body><p>If this option is enabled, only the specified number of tiles will be loaded from the selected source. </p><p>Cached tiles are not affected by this limit. Therefore, there may be more tiles visible when loading is complete.</p></body></html>"))
        self.chkLimitNrOfTiles.setText(_translate("OptionsGroup", "Loaded tile limit"))
        self.lblNumberTilesInCurrentExtent.setText(_translate("OptionsGroup", "(Current extent: n tiles)"))
        self.btnResetToBasemapDefaults.setText(_translate("OptionsGroup", "Base map defaults"))
        self.btnResetToAnalysisDefaults.setText(_translate("OptionsGroup", "Analysis defaults"))
        self.btnResetToInspectionDefaults.setText(_translate("OptionsGroup", "Inspection defaults"))
        self.btnManualSettings.setText(_translate("OptionsGroup", "Manual"))
        self.label_5.setText(_translate("OptionsGroup", "Fix Zoom"))
        self.chkSetBackgroundColor.setText(_translate("OptionsGroup", "Set project background color"))
        self.chkAutoZoom.setText(_translate("OptionsGroup", "Auto reload on change of view"))

