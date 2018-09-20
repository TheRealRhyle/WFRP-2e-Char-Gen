def generate_character(self):
    charout = genchar.build_random_char()
    print(charout['name'])
    self.txtName.setPlainText(charout['name'])
    self.txtRace.setPlainText(charout['race'])
    self.txtCCareer.setPlainText(charout['career'])
    self.txtAge.setPlainText(str(charout['age']))
    self.txtGender.setPlainText(charout['gender'])
    self.txtEyeColor.setPlainText(charout['eye_color'])
    self.txtWeight.setPlainText(str(charout['weight']) + " lbs")
    self.txtHaircolor.setPlainText(charout['hair_color'])
    self.txtHeight.setPlainText(charout['height'])
    self.txtStarSign.setPlainText(charout['starsign'])
    self.txtNoofSib.setPlainText(str(charout['siblings']))
    self.txtBirthplace.setPlainText(charout['birthplace'])
    self.txtDMarks.setPlainText(charout['marks'])

def exitbutton(self):
    weapon = ['Foil','40','Fencing','SB-2','-','-','Fast, Precise']
    rowPosition = self.tableWidget.rowCount()
    self.tableWidget.insertRow(rowPosition)
    for item in range(len(weapon)):
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, item,
                                 QtWidgets.QTableWidgetItem(str(weapon[item])))



        self.pb_Quit.clicked.connect(self.exitbutton)
        self.pb_Rando.clicked.connect(self.generate_character)

def generate_character(self):
    charout = genchar.build_random_char()
    print(charout['name'])
    self.txtName.setText(charout['name'])
    self.le_Race.setText(charout['race'])
    self.le_CurrentCar.setText(charout['career'])
    self.le_Age.setText(str(charout['age']))
    self.le_Gender.setText(charout['gender'])
    self.le_EyeC.setText(charout['eye_color'])
    self.le_Weight.setText(str(charout['weight']) + " lbs")
    self.le_HairC.setText(charout['hair_color'])
    self.le_Height.setText(charout['height'])
    self.le_StarSign.setText(charout['starsign'])
    self.le_NoofSib.setText(str(charout['siblings']))
    self.le_Birthplace.setText(charout['birthplace'])
    self.le_Distinguish.setText(charout['marks'])

def exitbutton(self):
    exit()

# """
# Add to Ui_MainWindow
# """
#
#
# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
# self.pushButton.clicked.connect(self.exitbutton)
# self.pushButton_2.clicked.connect(self.generate_character)