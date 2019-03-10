# Webshot

A python wrapper for the NodeJS module '[Pageres]'. I had tried a few different python screenshot modules and could not find one that 'just worked'.


Basic Usage
----
```python
from Modules.webshot import Webshot

urlArray =  ["https://github.com", "https://www.stackoverflow.com"]
screenshot = Webshot()
screenshot.configure("/path/to/nodejs/pageres")

for url in urlArray:
    screenshot.capture(url)
```

```python
from Modules.webshot import Webshot

urlArray = ["https://github.com", "https://www.stackoverflow.com"]
screenshot = Webshot()
screenshot.configure("/path/to/nodejs/pageres")
screenshot.capture(urlArray)
```

```python
from Modules.webshot import Webshot

urlArray = ["https://github.com", "https://www.stackoverflow.com"]
imageSizeArray = ["100x200","1920x1080"]
screenshot = Webshot()
screenshot.configure("/path/to/nodejs/pageres", size=imageSizeArray, crop=True, imageFormat="jpg")
screenshot.capture(urlArray)
```


Version
----

0.50

Requirements
-----------

Webshot has the following requirements:

* [NodeJS]
* [Pageres]


Preferred Installation
--------------
Use pip: 
```sh
pip install Webshot
```

Manual Installation
--------------
```sh
git clone https://github.com/rpunnett/Webshot.git
cd Webshot-<version>
python setup.py install
```


Portable NodeJS Instance
--------------

1. Get node binary (node.exe) from http://nodejs.org/download/
2. Create the folder where node will reside and move node.exe to it
3. Download the last zip version of npm from https://registry.npmjs.org/npm/-/npm-{version}.tgz.
4. Unpack the zip inside the node folder
5. Download the last tgz version of npm from http://nodejs.org/dist/npm
6. Open the tgz file and unpack only the file bin/npm (without extension) directly on the node folder.
7. Add the the node folder and the packages/bin folder to PATH
8. On a command prompt execute npm install -g npm to update npm to the latest version
9. *Git must be installed and in the system PATH*


Alternative Portable NodeJS Instance
--------------

https://sourceforge.net/projects/nodejsportable/
https://github.com/inexor-game-obsolete/platform/tree/master/bin/windows



Pageres Command Line Utility
--------------

[Pagres CLI]

```sh
npm install --global pageres-cli
```

License
----

MIT



[robert punnett]:https://github.com/rpunnett
[NodeJS]:https://nodejs.org/en/
[Pageres]:https://github.com/sindresorhus/pageres
[Pagres CLI]:https://github.com/sindresorhus/pageres-cli