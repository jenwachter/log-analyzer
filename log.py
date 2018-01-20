from datetime import datetime

class Log:
  def __init__(self, log):
    self.log = log

  def __repr__(self):
    return '{\n  ' + '\n  '.join([key + ': ' + self.formatValue(key) for key in self.log]) + '\n}'

  def __getattr__(self, attr):
    return self.log.get(attr)

  def formatValue(self, key):
    value = self.log.get(key)
    # if key is 'datetime':
    return value.__str__()
    # else:
    #   return value
