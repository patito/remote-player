import pygst
pygst.require("0.10")
import gst
from RemotePlayerFTP import *

class RemotePlayerPipeline:
	"""Class to handle gstreamer pipeline"""
	def __init__(self, rpftp):
		self.__remoteftp = rpftp
		self.__pipeline = gst.Pipeline("player")
		source = gst.element_factory_make("gnomevfssrc", "gvfs-source")
		decoder = gst.element_factory_make("mad", "mp3-decoder")
		sink = gst.element_factory_make("alsasink", "alsa-output")
		
		self.__pipeline.add(source, decoder, sink)
		gst.element_link_many(source, decoder, sink)

		bus = self.__pipeline.get_bus()
		bus.add_signal_watch()
		bus.connect("message", self.bus_call)

	def bus_call(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS:
			self.__pipeline.set_state(gst.STATE_NULL)
		elif t == gst.MESSAGE_ERROR:
			self.player.set_state(gst.STATE_NULL)
			err, debug = message.parse_error()
			print "Error: %s" % err, debug

	def start(self):
		filepath = "ftp://" + self.__remoteftp.user() + ":"\
				    + self.__remoteftp.password() + "@"\
				    + self.__remoteftp.server() + "/home/patito/teste.mp3"
		self.__pipeline.get_by_name("gvfs-source").set_property("location", filepath)
		self.__pipeline.set_state(gst.STATE_PLAYING)

	def __done__(self):
		print "done"

	def cancel(self):
		print "cancel"		
