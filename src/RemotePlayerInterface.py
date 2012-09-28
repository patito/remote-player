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
			songs = self.__ftp.listfiles()

			store = gtk.ListStore(str)
			for x in range(len(songs)):
				store.append([songs[x]])
			self.__playerViewer = self.wTree.get_widget("listview")
			self.__playerViewer.__init__(store)

			column = gtk.TreeViewColumn("Nome")

			title = gtk.CellRendererText()
			author = gtk.CellRendererText()

			column.pack_start(title, True)
			column.pack_start(author, True)

			column.add_attribute(title, "text", 0)
			column.add_attribute(author, "text", 1)

			self.__playerViewer.append_column(column)
			self.__playerViewer.connect("row-activated", self.item_clicked, None)
			self.__playerViewer.connect("cursor-changed", self.item_selected)

        def on_btclean_clicked(self, widget):
			self.wTree.get_widget("enserver").set_text("")
			self.wTree.get_widget("enuser").set_text("")
			self.wTree.get_widget("enpassword").set_text("")

        def on_btquit_clicked(self, widget):
			gtk.main_quit()

        def on_btplay_clicked(self, widget):
			self.__pipeline = RemotePlayerPipeline(self.__ftp)
			self.__pipeline.start()

        def on_btpause_clicked(self, widget):
			print "btpause"

        def on_btstop_clicked(self, widget):
			self.__pipeline.stop()

        def item_clicked(self, treeview, iter, tvc, foo):
			print "item_clicked"
			model = self.__playerViewer.get_model()
			iter = model.get_iter(iter)
			self.song_name = model.get_value(iter, 0)
			self.__pipeline.start(self.song_name)
			
        def item_selected(self, widget):
			#print self.__playerViewer.get_selection().get_selected_rows()
			model, pathlist = self.__playerViewer.get_selection().get_selected_rows()
			print pathlist[0][0]
    		#for path in pathlist :
        	#tree_iter = model.get_iter(path)
        	#value = model.get_value(tree_iter,0)
        	#print value
