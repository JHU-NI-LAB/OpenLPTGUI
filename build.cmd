rmdir /s release
md release
cd release
rmdir /s release-win
md release-windows_64x
cd release-windows_64x
python -m PyInstaller -F --collect-submodules=pydicom --noconsole --onefile --windowed ../../main.py --name OpenLPTGUI --icon ../../icons/RuiLab.ico
cd dist
Xcopy .\..\..\..\icons .\icons /E /H /C /I
Xcopy .\..\..\..\fonts .\fonts /E /H /C /I
cd ..
cd ..
cd ..