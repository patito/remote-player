from RemotePlayerFTP import *
from RemotePlayerPipeline import *
import gobject

rpftp = RemotePlayerFTP("192.168.160.191", "patito", "patito")
rpp = RemotePlayerPipeline(rpftp)
rpp.start()
mainloop = gobject.MainLoop()
mainloop.run()
