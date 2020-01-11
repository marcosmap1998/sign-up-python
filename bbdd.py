import sqlite3
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QVBoxLayout, QPushButton, QFileDialog, QColorDialog, \
    QFontDialog, QMessageBox

def conectar_bbdd(ventana):
    conector = sqlite3.connect('database_sign-up')
    cursor = conector.cursor()

    try:
        cursor.execute('''
            CREATE TABLE data_user(
                username VARCHAR(10) PRIMARY KEY,
                password VARCHAR(20)
            )
        ''')
        conector.commit()
        QMessageBox.information(ventana, 'BBDD','La base de datos ha sido conectada', QMessageBox.Accepted)
    except sqlite3.OperationalError:
        QMessageBox.warning(ventana, 'BBDD','La base de datos ya ha sido conectada', QMessageBox.Close)

def salir(ventana):
    resp = QMessageBox.question(ventana, 'Sing up', '¿Estás seguro de salir?', QMessageBox.Yes | QMessageBox.No)
    if resp == QMessageBox.Yes:
        ventana.destroy()

def crear_user(ventana, t1, t2):
    conector = sqlite3.connect('database_sign-up')
    cursor = conector.cursor()

    try:
        if t1.text() != '' and t2.text() != '':
            cursor.execute("INSERT INTO data_user VALUES ('" + t1.text() + 
            "','" + t2.text() + "')")
            conector.commit()
            QMessageBox.information(ventana, 'Sign up', 'Registro realizado con éxito', QMessageBox.Close)
            t1.clear()
            t2.clear()
        else:
            QMessageBox.information(ventana, 'Sign up', 'Los campos no deben estar vacíos', QMessageBox.Ok)
    except sqlite3.OperationalError:
        QMessageBox.information(ventana, 'Sign up', 'En este momento no es posible hacer el registro', QMessageBox.Ok)
        t1.clear()
        t2.clear()

