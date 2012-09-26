#!/usr/bin/env python
import sys
import os
from RemotePlayerFTP import *
from RemotePlayerPipeline import *

try:
        import pygtk
        pygtk.require("2.0")
except:
        pass
try:
        import gtk
        import gtk.glade
except:
        sys.exit(1)

class RemotePlayerInterface:
        def __init__(self):
                #Set the Glade file
		#self.__ftp = rpftp
                dic = { "gtk_main_quit" : gtk.main_quit }
                self.gladefile = "../interface/rpinterface.glade"
                self.wTree = gtk.glade.XML(self.gladefile)

                self.window = self.wTree.get_widget("MainWindow")
                self.window.show()
                self.window.connect("destroy", gtk.main_quit)
                dic = { "on_btconnect_clicked" : self.on_btconnect_clicked,
			"on_btclean_clicked" : self.on_btclean_clicked,
			"on_btquit_clicked" : self.on_btquit_clicked,
			"on_btplay_clicked" : self.on_btplay_clicked,
			"on_btpause_clicked" : self.on_btpause_clicked,
			"on_btstop_clicked" : self.on_btstop_clicked}
                self.wTree.signal_autoconnect(dic)
                

        def on_btconnect_clicked(self, widget):
		self.__server = self.wTree.get_widget("enserver").get_text()
		self.__user = self.wTree.get_widget("enuser").get_text()
		self.__password = self.wTree.get_widget("enpassword").get_text()
		self.__ftp = RemotePlayerFTP(self.__server, self.__user, self.__password)
		self.__ftp.connect()
                print "btconnect"

        def on_btclean_clicked(self, widget):
		self.wTree.get_widget("enserver").set_text("")
		self.wTree.get_widget("enuser").set_text("")
		self.wTree.get_widget("enpassword").set_text("")
                print "btclean"

        def on_btquit_clicked(self, widget):
		gtk.main_quit()

        def on_btplay_clicked(self, widget):
		self.__pipeline = RemotePlayerPipeline(self.__ftp)
		self.__pipeline.start()
                print "btplay"

        def on_btpause_clicked(self, widget):
                print "btpause"

        def on_btstop_clicked(self, widget):
		self.__pipeline.stop()
                print "btstop"

if __name__ == "__main__":
        hwg = RemotePlayerInterface()
        gtk.main()
