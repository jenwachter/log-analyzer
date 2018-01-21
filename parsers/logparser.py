import re
from datetime import datetime
from log import Log

class LogParser:

  def __init__(self, logs, options):
    self.logs = logs
    self.options = options
    self.regex = re.compile(self.pattern)

  def parse(self):
    """Based on the regular expression assigned to this parser, parse each
    log and map them to human-readable labels. Returns a generator object.

    Returns
    -------
    type
        Yields a list of logs
    """
    for line in self.logs:

      # see if this log matches the parser regex
      matches = re.match(self.regex, line)

      # continue to the next log if no match
      if matches is None:
        continue

      # parse log into a dictionary
      cleaned = Log({ self.matchmap[i]: self.cleanMatch(self.matchmap[i], match)
        for i, match in enumerate(matches.groups()) })

      # loop through the options passed in by the user to see
      # if this log should be included
      keep = True

      for option in self.options:
        method = 'filter__' + option
        keep = getattr(self, method)(cleaned)

        # if we don't need to keep this log, break out now
        if keep is False: break

      # log passed all the filters, yield it
      if keep: yield cleaned
      # if keep: yield line

  def cleanMatch(self, label, match):
    """Clean a matched string

    Parameters
    ----------
    label : string
        This match's label (i.e. `datetime`)
    match : string
        The matched string

    Returns
    -------
    type
        Description of returned object.
    """
    if label is 'datetime':
      return datetime.strptime(match, self.datetimeFormat)

    return match


  def filter__daterange(self, log):
    """Checks to see if the log's date is between the dates
    passed to the `daterange` option.

    Parameters
    ----------
    log : dictionary
        Current log being analyzed

    Returns
    -------
    type
        True if the log passes filter test
        False if the log does not pass the filter test
    """
    daterange = self.options.get('daterange')

    start = daterange[0]
    end = daterange[1]

    return start <= log.datetime <= end


  def filter__ip(self, log):
    ips = self.options.get('ip')
    return log.ip in ips
