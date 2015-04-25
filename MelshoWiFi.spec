# -*- mode: python -*-
a = Analysis(['MelshoWiFi.py'],
             pathex=['F:\\zprojects\\soft\\WIFI'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='aWIFIo.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries +
               [('icon.ico', 'icon.ico', 'DATA'),('share.gif', 'share.gif', 'DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='aWIFIo',
               icon='icon.ico')
