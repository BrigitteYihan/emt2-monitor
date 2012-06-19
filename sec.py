#!/lab/software/epd-7.0-1-rh5-x86/bin/python

from configobj import ConfigObj
# import sys
import argparse


def get_flags(filename, section):
  SEC = ConfigObj('%s' % filename)['%s' % section]
  flags = ""
  for key in SEC:
      value = SEC[key]
      flags += "-" + str(key + value) + "\t"
  return flags, SEC

def write_sec_to_ini(section, shotnum, section_name):
  shotstr = "%04d" % shotnum
  filename = 'report' + shotstr + '.INI'
  report = ConfigObj(filename)
  report[section_name] = {}
  for key in section:
    print "%s:%s" % ( key, section[key])
    report[section_name][key] = section[key]
  report.write() 

def write_to_ini( shotnum, sec, key, value):
  shotstr = "%04d" % shotnum
  filename = 'report' + shotstr + '.INI'
  report = ConfigObj(filename)
  if sec not in report:
    report[sec][key] = {}
  report[sec][key] = value
  report.write()
   

if __name__ == "__main__":
  parser = argparse.ArgumentParser('sec.py')
  parser.add_argument('FILE', action="store", type=str, help='filename')
  parser.add_argument('SEC', action="store", type=str, help='section')
  parser.add_argument('SHOT', action="store", type=int, help='shot number')
  parser.add_argument('DETUNE', action="store",type=str, help='detune')
  args = parser.parse_args()

  flagstring, section =  get_flags(args.FILE, args.SEC)
  write_sec_to_ini( section, args.SHOT, 'FLAGS') 
  write_to_ini( args.SHOT, 'FLAGS', 'd', args.DETUNE)
