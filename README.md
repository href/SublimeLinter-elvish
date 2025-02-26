This is a template. For "how to make a linter", please check [the HOWTO](HOWTO.md).

-----------------------------------------------------------------

SublimeLinter-contrib-elvish
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-elivsh.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-elivsh)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [elivsh](https://elv.sh). It will be used with files that have the "elvish" syntax.

Note that there is no proper linter yet for Elvish. This plugin simply calls elvish with '-compileonly', so the only
errors you see are compiler errors. Better than nothing though.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `elivsh` is installed on your system.

In order for `elivsh` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-elivsh settings:

|Setting|Description    |
|:------|:--------------|
|foo    |Something.     |
|bar    |Something else.|
