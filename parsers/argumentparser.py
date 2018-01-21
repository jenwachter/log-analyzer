import re
from datetime import datetime

class ArgumentParser:
  """Parse command-line arguments

  Keyword arguments:
  label -- this match's label
  match -- the matched string
  """

  acceptedArguments = ['ip', 'daterange']

  def __init__(self, arguments):
    self.arguments = arguments

  def parse(self):
    parsed = {}
    regex = re.compile('--([A-Za-z0-9]+)=(.*)')

    for argument in self.arguments:

      match = re.match(regex, argument).groups()
      key = match[0]

      if key not in self.acceptedArguments:
        continue

      value = match[1]

      method = 'parse__' + key
      parsed[key] = getattr(self, method)(value)

    return parsed


  def parse__daterange(self, value):
    dates = value.split(',')
    return [self.formatDate(date) for date in dates]

  def parse__ip(self, value):
    return value.split(',')

  def parse__url(self, value):
    return value

  def formatDate(self, value):
    return datetime.strptime(value.strip(), '%d/%b/%Y:%H:%M:%S %z')
