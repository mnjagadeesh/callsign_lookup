This is a very small README. If you have questions shoot email to 
mnjagadeesh@gmail.com

* install pyQRZ using github https://github.com/zebpalmer/pyQRZ
[do not use pip. I submitted patch to git which is yet to push to
 pypi.python.org/pyQRZ]

* instll argparse using 
	# pip install -U argparse [if you do not have it]
* create an account with qrz.com. and store password in settings.py.
  [name can be changed]
* list out all the callsigns you want to list in a file as supplied
  in clist
* this script writes to csv file if supplied, open in excel and mine data
  OR prints output on console

* how to run it?
  $  python lookup_callsign.py -c settings.cfg -i clist -o out.csv

any suggestions to improve the scripts are welcome. Happy to receive email on
mnjagadeesh@gmail.com

==============================================================================
   
