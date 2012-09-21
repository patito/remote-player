from RemotePlayerFTP import *
from RemotePlayerPipeline import *
import gobject

rpftp = RemotePlayerFTP("192.168.25.13", "patito", "patito")
rpp = RemotePlayerPipeline(rpftp)
rpftp.connect()
rpftp.listfiles()
#rpp.start()
mainloop = gobject.MainLoop()
mainloop.run()
