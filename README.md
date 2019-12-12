# Python BRfied

Why I create PyAtalhos? To avoid codes copy and paste. This are a many of code shortcuts  that I used many times.


## Date and time

* today
* now
* now_str
* this_month
* others_months


## Env

* env
* env_as_list
* env_as_list_of_maps
* env_as_bool
* env_from_json
* env_as_int


## Class manipulation

* instantiate_class

## Network sync

* get - Get HTTP and FTP content as decoded String 
* get_json - Get HTTP and FTP as JSON
* get_zip - Get HTTP and FTP as ZipFile
* get_zip_content - Get first (by default) HTTP and FTP file content in a ZipFile
* get_zip_csv_content - Get first (by default) HTTP and FTP file content in a ZipFile as iterable CSV (somma-separated values file)
* get_zip_fwf_content - Get first (by default) HTTP and FTP file content in a ZipFile as iterable FWF (fixed width file)


## Number

* percentage - Percentage of num2 of num1 width fixed precision (default 2)


## String 

* str2bool - Cast 'true', 'verdade', 'yes', 'sim', 't', 'v', 'y', 's', '1', 'false', 'falso', 'no', 'nao', 'não', 'f', 'n' and '0' to Boolean


## ZIP

* unzip_content - unzip the specified (first by default) file in a 'in memory' zip
* unzip_csv_content - unzip the specified (first by default) file in a 'in memory' zip, iterate that as a CSV (somma-separated values file) and return a list of dict of this content
* unzip_fwf_content - unzip the specified (first by default) file in a 'in memory' zip, iterate that as a FWF (fixed width file) and return a list of dict of this content


## LICENSE

The MIT License (MIT)

Copyright (c) 2015 kelsoncm

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

