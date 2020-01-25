[![Build Status](https://travis-ci.org/StepanenkoArtem/python-project-lvl2.svg?branch=master)](https://travis-ci.org/StepanenkoArtem/python-project-lvl2)
[![Maintainability](https://api.codeclimate.com/v1/badges/d4f393a9ed1e0c24fc2d/maintainability)](https://codeclimate.com/github/StepanenkoArtem/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d4f393a9ed1e0c24fc2d/test_coverage)](https://codeclimate.com/github/StepanenkoArtem/python-project-lvl2/test_coverage)

**Description**

_gendiff_ is tool for generating file difference beetween two files. There are two file formats are supported: JSON, YAML. 

**Installation**

Use next 'pip' command to install from http;//test.pypi.org/

	pip install -i https://test.pypi.org/simple stepanenko-artem-gendiff

See asciinema below for more details
[![asciicast](https://asciinema.org/a/ojlj6fa3E09q2qkzDxB9Qhf8R.svg)](https://asciinema.org/a/ojlj6fa3E09q2qkzDxB9Qhf8R)
	

**Using**

Use 
	gendiff --help 

to get some more information about using gendiff


To get files difference run _gendiff_ with two mandatory parameters: path to first file and path to second file. Both absolute and relative path types are supported.
[![asciicast](https://asciinema.org/a/jVv1JuFoYNqWtgeDhnbWENupK.svg)](https://asciinema.org/a/jVv1JuFoYNqWtgeDhnbWENupK)

Runnin _gendiff_ for YAML files
[![asciicast](https://asciinema.org/a/ssJFLAQyrFeOW8bYWrdtyLTXH.svg)](https://asciinema.org/a/ssJFLAQyrFeOW8bYWrdtyLTXH)

By default _gendiff_ returns tree-like result. Removed lines marked by "-" and added lines marked by "+".
Modified lines displayed twice. Primary value which has been updated marked by "-"  and value which was added instead marked "+". 
Unchanged lines remains unmarked.

Task #6 asciinema
[![asciicast](https://asciinema.org/a/sdYRrXTUMLLcvEN2T0boiJEfX.svg)](https://asciinema.org/a/sdYRrXTUMLLcvEN2T0boiJEfX)

Task #7 asciinema
[![asciicast](https://asciinema.org/a/pbuGboKPDLT5B4LEBFYSuUuZL.svg)](https://asciinema.org/a/pbuGboKPDLT5B4LEBFYSuUuZL)

