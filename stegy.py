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
import subprocess
import shlex
from PyQt4 import QtCore, QtGui
from stegy_ui import Ui_Stegy
from PyQt4.QtGui import QFileDialog,QPixmap,QMessageBox

class Stegyapp(QtGui.QMainWindow,Ui_Stegy):
    def __init__(self, parent =None):
        super(Stegyapp,self).__init__(parent)
        self.setupUi(self)
        self.algo_name = ('rijndael-128','cast-128', 'gost','twofish','arcfour','cast-256','loki97','rijndael-192','saferplus','wake','des','rijndael-256','serpent','xtea','blowfish','enigma','rc2','tripledes')
        self.algo_modes = ('cbc','cfb','ctr','ecb','ncfb','nofb','ofb')
        self.CoverFile = ""
        self.StegoFile = ""
        self.EmbedFile = ""
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

    def showError(self,value):
        QMessageBox.critical(self,"Error",value);

    def embed(self):
        if self.CoverFile == "":
            self.showError("No Cover File Found")
        elif self.EmbedFile == "":
            self.showError("No Embed File Found")
        elif self.pass_lineEdit.text() == "":
            self.showError("No Passphrase entered")
        else:
            covFile = ' -cf "' + self.CoverFile + '"' #Cover File
            embedFile = ' -ef "' + self.EmbedFile + '"' #Embed File
            encRypt = " -e " + self.algo_comboBox.currentText() + " " + self.mode_comboBox.currentText()
            passFrase = " -p " + self.pass_lineEdit.text()
            if self.compress_checkBox.isChecked():
                comPress = " -z " + str(self.complevelspinBox.value())
            else:
                comPress = " -Z"
            if self.nocrc32_checkBox.isChecked():
                checkSum = " -K"
            else:
                checkSum = ""
            if self.efn_checkBox.isChecked():
                origName = " -N"
            else:
                origName = ""
            command = "steghide embed" + covFile + embedFile + encRypt + passFrase + comPress + checkSum + origName
            args = shlex.split(str(command))
            ret_value=subprocess.call(args)
            if ret_value == 0:
                QMessageBox.information(self,"Success","Stego File Created Successfully")
            else:
                self.showError("Error in Creation of Stego File")

    def extract():
        pass
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    stegy = Stegyapp()
    stegy.show()
    app.exec_()
    
