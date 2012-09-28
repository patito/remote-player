from ftplib import FTP
import sys, os

class RemotePlayerFTP:
	"""Class to handle FTP features"""
	def __init__(self, server, user, password):
		self.__server = server
		self.__user = user
		self.__password = password

	def __done__(self):
		self.__ftp.quit()

	def connect(self):
		try:
			self.__ftp = FTP(self.__server, 
							 self.__user, 
							 self.__password)
		except:
			print "Can't connect in server."
			sys.exit()
	
	def listfiles(self):
		return self.__ftp.nlst()

	def server(self):
		return self.__server
	
	def user(self):
		return self.__user

	def password(self):
		return self.__password
