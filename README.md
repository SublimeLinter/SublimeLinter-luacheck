SublimeLinter-luacheck
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-luacheck.svg)](https://travis-ci.org/SublimeLinter/SublimeLinter-luacheck)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [luacheck](http://luacheck.readthedocs.io).
It will be used with files that have the "Lua" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `luacheck` is installed on your system.
To install `luacheck`, follow the instructions at the [luacheck home page](http://luacheck.readthedocs.io).

Please make sure that the path to `luacheck` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Additional SublimeLinter-luacheck settings:

|Setting|Description|
|:------|:----------|
|ignore|Do not report warnings related to these variables|
|only|Only report warnings related to these variables|
|globals|Defined globals|
|limit|The maximum number of warnings|

The preferred method of configuring `luacheck` is via [.luacheckrc files](http://luacheck.readthedocs.io/en/stable/config.html)

