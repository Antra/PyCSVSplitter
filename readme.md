# CSV Splitter
I need something to split a CSV file into multiple files -- in this case it's to split every single row into separate files.

There are two different methods here:
- ```main.py``` is using Python's own capabilities - it's forked from a Gist: https://gist.github.com/jrivero/1085501
- ```main1.py``` is using Pandas (probably a bit slower, but works for my purposes)

# Notes
## Installer
Using `pyinstaller` to generate a Windows executable for systems without Python installed.  
Run `pyinstaller --onefile yourprogram.py` in the program folder to generate a `dist` subdirectory with the executable.