#!/usr/bin/python
# Copyright (C) 2012 Sibi <sibi@psibi.in>
#
# This file is part of PyStegy.
#
# PyStegy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStegy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStegy.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt4 import QtCore, QtGui
from stegy_ui import Ui_Stegy
from PyQt4.QtGui import QFileDialog,QPixmap

class Stegyapp(QtGui.QMainWindow,Ui_Stegy):
    def __init__(self, parent =None):
        super(Stegyapp,self).__init__(parent)
        self.setupUi(self)
        self.algo_name = ('rijndael-128','cast-128', 'gost','twofish','arcfour','cast-256','loki97','rijndael-192','saferplus','wake','des','rijndael-256','serpent','xtea','blowfish','enigma','rc2','tripledes')
        self.algo_modes = ('cbc','cfb','ctr','ecb','ncfb','nofb','ofb')
        for aname in self.algo_name:
            self.algo_comboBox.addItem(aname)

    def getCoverFile(self):
        self.CoverFile = QFileDialog.getOpenFileName(self,"Get Cover File", ".", "Cover Files (*.jpg *.bmp *.wav *.au)")
        if self.CoverFile != "":
            if self.CoverFile.endsWith("wav") or self.CoverFile.endsWith("au"):
                pixmap = QPixmap("./images/audio.png")
                self.cover_label.setPixmap(pixmap)
            else:
                pixmap = QPixmap(self.CoverFile)
                self.cover_label.setPixmap(pixmap)

    def getEmbedFile(self):
        self.EmbedFile = QFileDialog.getOpenFileName(self, "Get Embed File", ".", "Embed Files (*)")

    def changeModeEntries(self):
        self.mode_comboBox.clear()
        if self.algo_comboBox.currentText() == "arcfour" or self.algo_comboBox.currentText() == "wake" or self.algo_comboBox.currentText() == "enigma":
            self.mode_comboBox.addItem("stream")
        else:
            for entries in self.algo_modes:
                self.mode_comboBox.addItem(entries)

    def getStegoFile(self):
        self.StegoFile = QFileDialog.getOpenFileName(self, "Get Embed File", ".", "Stego Files (*.jpg *.bmp *.wav *.au")
        if self.StegoFile != "":
            self.est_lineEdit.setText(self.StegoFile)

    def embed():
        pass

    def extract():
        pass
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    stegy = Stegyapp()
    stegy.show()
    app.exec_()
    
