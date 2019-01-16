# Automatic-Electron-Initializer
Python script to automatically initialize an electron npm project and prepare it for building.

## Requirements
Script requires npm and Python. I used it with Python 3.6 but it should also work with at least python 3.5.
If you want to use Python 2.x please use `electron_auto_init_python2.py`. Warning: I didn't test the Python 2 version, it should work, but eventually you have to change a bit. 

## Usage
Use the auto init with the following command:
```
# Python 3
python electron_auto_init.py project-name
# or
python3 electron_auto_init.py project-name

# Python 2
python electron_auto_init_python2.py project-name
```
Then follow the instructions in the console.

The script creates a simple starting script, modifies the package.json so you can easily start and build your app.

The following commands must be used inside the project folder:
#### Start the app
```
npm start
```

#### Build the app
```
# Windows
npm run package-win

# Mac
npm run package-mac

# Linux
npm run package-linux
```
