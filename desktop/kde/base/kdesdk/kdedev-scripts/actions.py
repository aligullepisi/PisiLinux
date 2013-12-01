#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    
    #subversion confilicts
    pisitools.remove("/usr/bin/svnrevertlast")
    pisitools.remove("/usr/bin/svnlastchange")
    pisitools.remove("/usr/bin/svnlastlog")
    
    pisitools.dodoc("COPYING*", "README")