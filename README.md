# digestauth-calc 

This tool is Calculate Program of Digest Authentication. 

## Description



## Version

`1.0.0`

## Features

- response calc 
- dictionary attk

## Requirement

- python v2.7

## Usage

```sh
+------------------------+
| Command Usage          |
+------------------------+
-v  : This Program Version
-h  : This help 

+A1 Calc Mode+
-a1 : Calculate A1 of Digest Authentication. 
      The needed parameter is <username>, <passwd>,
      <config-file-path>.

+A2 Calc Mode+
-a2 : Calculate A2 of Digest Authentication.
      The needed parameter is <URI>, <config-file-path>.

+Single Calc Mode+
-S  : Calculate response of Digest Authentication.
      The needed parameter is <username>, <passwd>,
      <URI>, <config-file-path>.

+Auto Calc Mode+
-A  : Calculate response of Digest Authentication
      with dictionary-file.
      The needed parameter is <dict-file-path>,
      <config-file-path>.

[A1 Calc Mode Usage]
$ python dcalc.py -a1 --user <username> --pass <passwd> -c <config-file-path>

[A2 Calc Mode Usage]
$ python dcalc.py -a2 --uri <URI> -c <config-file-path>

[Single Calc Mode Usage]
$ python dcalc.py -S --user <username> --pass <passwd> --uri <URI> -c <config-file-path>

[Auto Calc Mode Usage]
$ python dcalc.py -A -d <dict-file-path> -c <config-file-path>
```

## Installation

    $ git clone https://github.com/NPEMasa/digestauth-calc

## Author

[@RaspERMasa](https://twitter.com/RaspERMasa)

