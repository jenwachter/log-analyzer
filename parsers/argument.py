from datetime import datetime
import re
import sys

class ArgumentParser:
  """Parse command-line arguments

  Keyword arguments:
  label -- this match's label
  match -- the matched string
  """

  def __init__(self, arguments):
    self.arguments = arguments

  def parse(self):
    parsed = {}
    regex = re.compile('--([A-Za-z0-9]+)=(.*)')

    for argument in self.arguments:

      match = re.match(regex, argument).groups()
      key = match[0]
      value = match[1]
      method = 'parse__' + key

      try:
        parsed[key] = getattr(self, method)(value)
      except:
        print('Invalid option: \'{0}\''.format(key))
        sys.exit(1)

    return parsed


  def parse__daterange(self, value):
    dates = value.split(',')
    return [self.formatDate(date) for date in dates]

  def parse__ip(self, value):
    return value.split(',')

  def parse__url(self, value):
    return value

  def parse__useragent(self, value):
    return value

  def formatDate(self, value):
    return datetime.strptime(value.strip(), '%d/%b/%Y:%H:%M:%S %z')
