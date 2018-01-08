import sys 
from PyQt5.QtWidgets import QMessageBox,QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget

''' login '''
class Login :

	''' constructor di python, berisi window template dan main_window '''
	def __init__(self,window,main_window):
		self.window = window
		self.main_window = main_window
		''' event untuk tombol login '''
		self.window.pb_login.clicked.connect(self.login_app)
		self.center(main_window)

	''' fungsi yang berfungsi ketika di klik tombol button login '''
	def login_app(self):
		userid = self.window.le_id.text()
		passwd = self.window.le_password.text()
		QMessageBox.about(self.main_window, "Message Dialog", "UserId or Password incorrect!")

	''' fungsi untuk merubah posisi window berada di tengah '''
	def center(self,window):
		qtRectangle = window.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		window.move(qtRectangle.topLeft())