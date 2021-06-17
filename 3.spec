# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['3.1+', 'Collecting pyinstaller', '  Using cached https:\\files.pythonhosted.org\\packages\\b6\\27\\a006fcadba0db30819c968eb8decb4937cda398ca7a44d8874172cdc228a\\pyinstaller-4.3.tar.gz', '  Installing build dependencies: started', "  Installing build dependencies: finished with status 'done'", '  Getting requirements to build wheel: started', "  Getting requirements to build wheel: finished with status 'done'", '    Preparing wheel metadata: started', "    Preparing wheel metadata: finished with status 'done'", 'Requirement already satisfied, skipping upgrade: setuptools in c:\\users\\leona\\appdata\\local\\programs\\python\\python38\\lib\\site-packages (from pyinstaller) (41.2.0)', 'Collecting pywin32-ctypes>=0.2.0; sys_platform == win32 (from pyinstaller)', '  Using cached https:\\files.pythonhosted.org\\packages\\9e\\4b\\3ab2720f1fa4b4bc924ef1932b842edf10007e4547ea8157b0b9fc78599a\\pywin32_ctypes-0.2.0-py2.py3-none-any.whl', 'Collecting altgraph (from pyinstaller)', '  Using cached https:\\files.pythonhosted.org\\packages\\ee\\3d\\bfca21174b162f6ce674953f1b7a640c1498357fa6184776029557c25399\\altgraph-0.17-py2.py3-none-any.whl', 'Collecting pefile>=2017.8.1; sys_platform == win32 (from pyinstaller)', '  Using cached https:\\files.pythonhosted.org\\packages\\36\\58\\acf7f35859d541985f0a6ea3c34baaefbfaee23642cf11e85fe36453ae77\\pefile-2019.4.18.tar.gz', 'Collecting pyinstaller-hooks-contrib>=2020.6 (from pyinstaller)', '  Using cached https:\\files.pythonhosted.org\\packages\\27\\c7\\58a634d861e4744ac62dca4a4992ace8def8b05dab91e6b25e5043e79acf\\pyinstaller_hooks_contrib-2021.1-py2.py3-none-any.whl', 'Collecting future (from pefile>=2017.8.1; sys_platform == win32->pyinstaller)', '  Using cached https:\\files.pythonhosted.org\\packages\\45\\0b\\38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9\\future-0.18.2.tar.gz', 'Building wheels for collected packages: pyinstaller', '  Building wheel for pyinstaller (PEP 517): started', "  Building wheel for pyinstaller (PEP 517): finished with status 'done'", '  Created wheel for pyinstaller: filename=pyinstaller-4.3-cp38-none-any.whl size=2457297 sha256=5b201669290d71b5f69f806a562a56135b2fd1cd81153bb8307dacb7fb2305c6', '  Stored in directory: C:\\Users\\leona\\AppData\\Local\\pip\\Cache\\wheels\\4e\\d9\\60\\db7ac8941a22cb24131ec3cf40d094b9984518671f85b93780', 'Successfully built pyinstaller', 'Installing collected packages: pywin32-ctypes, altgraph, future, pefile, pyinstaller-hooks-contrib, pyinstaller', '  Running setup.py install for future: started', "    Running setup.py install for future: finished with status 'done'", '  Running setup.py install for pefile: started', "    Running setup.py install for pefile: finished with status 'done'", 'Successfully installed altgraph-0.17 future-0.18.2 pefile-2019.4.18 pyinstaller-4.3 pyinstaller-hooks-contrib-2021.1 pywin32-ctypes-0.2.0'],
             pathex=['C:\\Users\\leona\\Documents\\MeusProjetos\\TabelaIMC'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='3')
