from RemotePlayerFTP import *
from RemotePlayerPipeline import *
import gobject

mainloop = gobject.MainLoop()
rpftp = RemotePlayerFTP("192.168.160.191", "patito", "patito")
rpp = RemotePlayerPipeline(rpftp)
rpftp.connect()
rpp.start()
mainloop.run()
