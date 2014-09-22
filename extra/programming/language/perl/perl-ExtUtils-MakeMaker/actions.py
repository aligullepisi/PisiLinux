#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    
    #remove dirs because conflicted perl-docs
    pisitools.removeDir("/usr/share/man/")
    #remove dirs because conflicted perl
    pisitools.removeDir("/usr/bin")
      
    pisitools.dodoc("Changes", "MANIFEST", "README")