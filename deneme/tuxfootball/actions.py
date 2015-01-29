#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
#bu pspec.xml ve actions.py  happy kity ve github dakı pisilinux deki belgeler kullanılarak oluşturulmuştur
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/tuxfootball/work/ and:
# WorkDir="tuxfootball-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/doc")
    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "src/SFont-README")
# Take a look at the source folder for these file as documentation.


# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("tuxfootball")

# You can use these as variables, they will replace GUI values before build.
# Package Name : tuxfootball
# Version : 0.3.35.0
# Summary : klasik futbol oyunu

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
