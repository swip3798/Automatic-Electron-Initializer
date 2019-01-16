'''
Python script which creates a basic electron project, prepares it for building and adds basic javascript and html files to get a quick start

Requires npm and python 3.x to run, tested only on Python 3.6.3, should at least run on Python 3.5
'''

import os
import sys
import json

sys.argv[1] = sys.argv[1].lower()

os.mkdir(sys.argv[1])
os.chdir(sys.argv[1])
os.system("npm init")
os.system("npm install --save electron")
os.system("npm install --save-dev electron-packager")

package = json.loads(open("package.json", "r").read())
package["scripts"]["start"] = "electron ."
package["scripts"]["package-mac"] = "electron-packager . --overwrite --platform=darwin --arch=x64 --icon=assets/icons/mac/icon.icns --prune=true --out=release-builds"
package["scripts"]["package-win"] = "electron-packager . " + sys.argv[1] + " --overwrite --asar=true --platform=win32 --arch=ia32 --prune=true --out=release-builds --version-string.CompanyName=CE --icon=assets/icons/win/icon.ico --version-string.FileDescription=CE --version-string.ProductName=\"" + sys.argv[1] + "\""
package["scripts"]["package-linux"] = "electron-packager . " + sys.argv[1] + " --overwrite --asar=true --platform=linux --arch=x64 --icon=assets/icons/png/1024x1024.png --prune=true --out=release-builds"

main_js_name = package["main"]

with open("package.json", "w") as f:
    f.write(json.dumps(package, indent=1))

print("npm init finished, creating starting files...")
print("preparing icon folders, place there your icons...")
os.makedirs("assets/icons/win")
os.makedirs("assets/icons/mac")
os.makedirs("assets/icons/png")
open("assets/icons/win/icon.ico.placehere", "w").close()
open("assets/icons/mac/icon.icns.placehere", "w").close()
open("assets/icons/png/1024x1024.png.placehere", "w").close()


print("creating basic main javascript file...")

index_js = """
const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;

// Listen for app to be ready
app.on('ready', function() {
    //Create new Window

    mainWindow = new BrowserWindow({});

    //load html file
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));
});

// Create menu template

const mainMenuTemplate = [
    {
        label: 'File'
    }
];
"""

print("creating basic hello world index.html file...")

with open(main_js_name, "w") as f:
    f.write(index_js)

index_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>[[]]</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
</head>
<body>
    <p>Hello World</p>
</body>
</html>
"""
index_html = index_html.replace("[[]]", sys.argv[1])
with open("index.html", "w") as f:
    f.write(index_html)
