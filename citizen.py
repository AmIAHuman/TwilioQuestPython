class Citizen:
  """Describes citizens of the City of Python"""
  greeting = "For the glory of Python!"
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
  def full_name(self):
    return self.first_name + " " + self.last_name