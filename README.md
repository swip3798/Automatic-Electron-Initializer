# Automatic-Electron-Initializer
Python script to automatically initialize an electron npm project and prepare it for building.

## Requirements
Script requires npm and Python 3. I used it with Python 3.6 but it should also work with at least python 3.5.

## Usage
Use the auto init with the following command:
```
python electron_auto_init.py project-name
```
Then follow the instructions in the console.

The script creates a simple starting script, modifies the package.json so you can easily start and build your app.

The following commands must be used inside the project folder
##### Start the app
```
npm start
```

##### Build the app
```
# Windows
npm run package-win

# Mac
npm run package-mac

# Linux
npm run package-linux
```
