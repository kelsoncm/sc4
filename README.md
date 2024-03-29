# Shortcut functions for Python and Net (sc4)

Why I create sc4*?
To avoid code's copy and paste.
This are a many of code shortcuts  that I used many times.
And, because I wanna use the same function to HTTP(S) and FTP.

# sc4py 

## Date and time

* today - today date
* now - date and time of this moment
* now_str - date and time of this moment formatted as "%d-%m-%Y %H:%M:%S"
* this_month - this month (a integer from 1 to 12)
* others_months - a list of all monthts (a integer from 1 to 12), except this month


## Env

* env - the value of a environment variable as String
* env_as_list - the value of a environment variable as List, comma is the default separator
* env_as_list_of_maps - the value of a environment variable as List of Maps, comma is the default separator of maps
* env_as_bool - the value of a environment variable as Boolean
* env_as_int - the value of a environment variable as Integer
* env_from_json - the value of a environment variable Python structure (lists and maps) considering the env as JSON


## Class manipulation

* instantiate_class


## Number

* percentage - Percentage of num2 of num1 width fixed precision (default 2)


## String 

* str2bool - Cast 'true', 'verdade', 'yes', 'sim', 't', 'v', 'y', 's', '1', 'false', 'falso', 'no', 'nao', 'não', 'f', 'n' and '0' to Boolean


## ZIP

* unzip_content - unzip the specified (first by default) file in a 'in memory' zip
* unzip_csv_content - unzip the specified (first by default) file in a 'in memory' zip, iterate that as a CSV (somma-separated values file) and return a list of dict of this content



# sc4net

## Network sync

* get - Get HTTP and FTP content as decoded String 
* get_json - Get HTTP and FTP as JSON
* get_zip - Get HTTP and FTP as ZipFile
* get_zip_content - Get first (by default) HTTP and FTP file content in a ZipFile
* get_zip_csv_content - Get first (by default) HTTP and FTP file content in a ZipFile as iterable CSV (comma-separated values file)


## LICENSE

The MIT License (MIT)

Copyright (c) 2019 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

