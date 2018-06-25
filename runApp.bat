::%windir%\System32\cmd.exe "/K" D:\program\Anaconda3\Scripts\activate.bat D:\program\Anaconda3
::conda activate py36

::call D:\program\Anaconda3\Scripts\activate.bat D:\program\Anaconda3\envs\py35
call D:\program\Anaconda3\Scripts\activate.bat

::python rf1201_reader_tool.py
start pythonw rf1201_reader_tool.py
