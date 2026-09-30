class controls:
  def __init__(self, location, output):
    self.fileLocation = location
    self.musicOutput = output

  nameWeight = 0.6
  artistWeight = 0.4
  weightNeeded = 0 # if totalweight less than this, raise warning
  searches = 5 # Amount of searches by video name