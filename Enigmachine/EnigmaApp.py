import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from enigma_interface.true_main_interface import Ui_MainWindow
from enigma_interface.enigma_facts import Ui_MainWindow as FactsWindow
from enigma_interface.comment_utiliser import Ui_MainWindow as UtiliserWindow
from enigma_code.classe_enigma import Enigma
from enigma_code.classe_rotor import Rotor

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"





        #===================================== Reste ========================================
        #===================================== Reste ========================================

class Enigmachine(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.letter_pairs = {}
        self.used_letters = set()

        # Initialisation de la machine Enigma avec des valeurs par défaut
        self.enigma = Enigma(1, 2, 3, 1)  # 3 rotors + 1 réflecteur
        self.ui.QTextEdit_Entree.setReadOnly(True)
        self.ui.QTextEdit_Sortie.setReadOnly(True)
        self.initial_rotor_positions = ("A", "A", "A")
        self.initial_rotor_indices = (0, 0, 0)
        
        # Connexion des boutons aux fenêtres
        self.ui.pushButton.clicked.connect(self.show_utiliser)
        self.ui.pushButton_2.clicked.connect(self.show_facts)
        
        # Connexion des boutons de changement de rotors et réflecteur
        self.ui.pushButton_3.clicked.connect(lambda: self.change_rotor(0))
        self.ui.pushButton_4.clicked.connect(lambda: self.change_rotor(1))
        self.ui.pushButton_5.clicked.connect(lambda: self.change_rotor(2))
        self.ui.pushButton_6.clicked.connect(self.change_reflecteur)

        # Connexion du clavier
        for letter in ALPHABET:
            btn_name = f"Pbtn_{letter}"
            if hasattr(self.ui, btn_name):
                getattr(self.ui, btn_name).clicked.connect(lambda _, l=letter: self.process_input(l))

              
        
        #config des jack pour la position des rotors
        for i in range(1, 4):
            jack_name = f"jack_{i}"
            if hasattr(self.ui, jack_name):
                line_edit = getattr(self.ui, jack_name)
                line_edit.setMaxLength(1)
                line_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Z]")))
                line_edit.setReadOnly(False)

        for letter in ALPHABET:
            line_edit_name = f"lineEdit_{letter}"
            if hasattr(self.ui, line_edit_name):
                line_edit = getattr(self.ui, line_edit_name)
                line_edit.setMaxLength(1)
                line_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Z]")))
                line_edit.setAlignment(QtCore.Qt.AlignCenter)
                line_edit.textChanged.connect(lambda text, l=letter: self.update_letter_pair(l, text))

        # Ajout d'un bouton d'effacement dans la frame ExS
        self.ui.clear_button = QtWidgets.QPushButton("Effacer", self.ui.QFrame_ExS)
        self.ui.clear_button.setGeometry(QtCore.QRect(120, 150, 90, 30))
        self.ui.clear_button.setStyleSheet("QPushButton{\n"
"border: 3px solid rgb(28, 38, 61);\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"border: 3px solid white;\n"
"color: white;\n"
"background-color:  rgb(28, 38, 61);\n"
"border-radius: 20px;\n"
"}")
        self.ui.clear_button.clicked.connect(self.clear_text)
        self.ui.clear_button.show()

        #si les jacks sont modifiés 
        self.ui.jack_1.textChanged.connect(self.mettre_a_jour_positions_rotors)
        self.ui.jack_2.textChanged.connect(self.mettre_a_jour_positions_rotors)
        self.ui.jack_3.textChanged.connect(self.mettre_a_jour_positions_rotors)

        #===================================== Fontions ========================================
        #===================================== Fonctions ========================================



    #===================================== Autre ========================================
    def show_utiliser(self):
        self.utiliser_window = QtWidgets.QMainWindow()
        self.ui_utiliser = UtiliserWindow()
        self.ui_utiliser.setupUi(self.utiliser_window)
        self.utiliser_window.show()
    
    def show_facts(self):
        self.facts_window = QtWidgets.QMainWindow()
        self.ui_facts = FactsWindow()
        self.ui_facts.setupUi(self.facts_window)
        self.facts_window.show()

    def format_text_by_five(self, text):
        text = text.replace(" ", "")
        return " ".join(text[i:i+5] for i in range(0, len(text), 5))


    #===================================== Rotors ========================================
    def mettre_a_jour_positions_rotors(self):
         """
         Cette fonction met à jour les positions des rotors en fonction des valeurs saisies par l'utilisateur.
         """
         lettre_rotor_g = self.ui.jack_1.text() 
         lettre_rotor_c = self.ui.jack_2.text() 
         lettre_rotor_d = self.ui.jack_3.text()

         print(f"Avant mise à jour, positions : {lettre_rotor_g}, {lettre_rotor_c}, {lettre_rotor_d}") 

         if lettre_rotor_g in ALPHABET and lettre_rotor_c in ALPHABET and lettre_rotor_d in ALPHABET:
             self.enigma.Set_Configuration_depart(lettre_rotor_g, lettre_rotor_c, lettre_rotor_d)
             print(f"Après mise à jour, positions rotors : {self.enigma.GetLettreInitRotorGauche()}, {self.enigma.GetLettreInitRotorCentre()}, {self.enigma.GetLettreInitRotorDroite()}")
         else:
             self.msg = QMessageBox()
             self.msg.setWindowTitle("Erreur")
             self.msg.setText("Les positions des rotors doivent être valides!")
             self.msg.setIcon(QMessageBox.Critical)
             self.msg.exec_()



    def change_rotor(self, index):
        # Récupérer les numéros actuels des rotors
        rotor_numbers = [
            self.enigma.GetNumRotorGauche(),
            self.enigma.GetNumRotorCentre(),
            self.enigma.GetNumRotorDroite()
        ]

        # Incrémenter le rotor sélectionné (cycle entre 1 et 5)
        rotor_numbers[index] = (rotor_numbers[index] % 5) + 1  

        # Mettre à jour la machine Enigma avec les nouveaux rotors
        self.enigma = Enigma(rotor_numbers[0], rotor_numbers[1], rotor_numbers[2], self.enigma.GetNumReflecteur())

        # Mise à jour des labels d'affichage
        self.ui.label_53.setText(str(rotor_numbers[0]))  # Rotor gauche
        self.ui.label_54.setText(str(rotor_numbers[1]))  # Rotor centre
        self.ui.label_55.setText(str(rotor_numbers[2]))  # Rotor droite

        print(f"Mise à jour des rotors : Gauche={rotor_numbers[0]}, Centre={rotor_numbers[1]}, Droite={rotor_numbers[2]}")

        #===================================== Plugage ========================================

    def update_letter_pair(self, letter, text):
        if text and text in ALPHABET and text != letter and text not in self.used_letters:
            if letter in self.letter_pairs:
                opposite = self.letter_pairs.pop(letter)
                self.letter_pairs.pop(opposite, None)
                self.used_letters.remove(letter)
                self.used_letters.remove(opposite)
                getattr(self.ui, f"lineEdit_{opposite}").clear()
            
            if text in self.letter_pairs:
                opposite = self.letter_pairs.pop(text)
                self.letter_pairs.pop(opposite, None)
                self.used_letters.remove(text)
                self.used_letters.remove(opposite)
                getattr(self.ui, f"lineEdit_{opposite}").clear()
            
            self.letter_pairs[letter] = text
            self.letter_pairs[text] = letter
            self.used_letters.add(letter)
            self.used_letters.add(text)
            getattr(self.ui, f"lineEdit_{text}").setText(letter)
        elif not text and letter in self.letter_pairs:
            opposite = self.letter_pairs.pop(letter)
            self.letter_pairs.pop(opposite, None)
            self.used_letters.remove(letter)
            self.used_letters.remove(opposite)
            getattr(self.ui, f"lineEdit_{opposite}").clear()

        #===================================== Reflecteurs ========================================

    def change_reflecteur(self):
        reflecteur_num = (self.enigma.GetNumReflecteur() % 2) + 1  # Cycle entre 1 et 2
        self.enigma.SetReflecteur(reflecteur_num)
        print(f"{self.enigma.GetNumReflecteur()}")
        reflecteur_label = "UKW-B" if reflecteur_num == 1 else "UKW-C"
        self.ui.label_57.setText(reflecteur_label)
        print("Réflecteur changé à:", self.enigma.GetNumReflecteur())

    # ===================================== Quand appuyé sur un bouton ========================================
    def process_input(self, letter):
         self.msg = QMessageBox()
         self.msg.setWindowTitle("Erreur !")
         self.msg.setText("Remplir tous les champs!")
         self.msg.setIcon(QMessageBox.Critical)

         if self.ui.jack_1.text() and self.ui.jack_2.text() and self.ui.jack_3.text():
             # Appliquer le cablage des plugs avant d'envoyer dans Enigma
             original_letter = letter
             letter = self.letter_pairs.get(letter, letter)  # Appliquer le câblage avant
             print(f"Lettre après câblage : {original_letter} -> {letter}")
             
             encoded_letter = self.enigma.Decodagelettre(letter)
             print(f"Lettre après codage : {letter} -> {encoded_letter}")

             encoded_letter = self.letter_pairs.get(encoded_letter, encoded_letter)  # Appliquer le câblage inverse
             print(f"Lettre après câblage inverse : {encoded_letter}")
             
             self.ui.QTextEdit_Entree.setPlainText(self.format_text_by_five(self.ui.QTextEdit_Entree.toPlainText() + letter))
             self.ui.QTextEdit_Sortie.setPlainText(self.format_text_by_five(self.ui.QTextEdit_Sortie.toPlainText() + encoded_letter))

             
             label_name = f"label_{encoded_letter}"
             if hasattr(self.ui, label_name):
                 a = getattr(self.ui, label_name)
                 a.setStyleSheet("background-color: red; color: black; border-radius: 10px;")
                 QtCore.QTimer.singleShot(1000, lambda: a.setStyleSheet("background-color: white;\n"
                                                                         "color: black;\n"
                                                                         "border-radius: 10px;"))
         else:
             self.msg.exec_()


    # ===================================== Clear ========================================
    def clear_text(self):
        self.ui.QTextEdit_Entree.clear()
        self.ui.QTextEdit_Sortie.clear()
        self.initial_rotor_positions = ("A", "A", "A")
        self.ui.jack_1.setText("A")
        self.ui.jack_2.setText("A")
        self.ui.jack_3.setText("A")
        self.initial_rotor_indices = (0, 0, 0)
        self.enigma = Enigma(1, 2, 3, 1)
        self.ui.label_53.setText(str("1"))
        self.ui.label_54.setText(str("2"))
        self.ui.label_55.setText(str("3"))
        self.ui.label_57.setText("UKW-B")
        self.letter_pairs.clear()
        self.used_letters.clear()
        for letter in ALPHABET:
            if f"lineEdit_{letter}" != "lineEdit_X":
                getattr(self.ui, f"lineEdit_{letter}").clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Enigmachine()
    window.show()
    sys.exit(app.exec_())