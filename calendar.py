from constants import DAYS_OF_WEEK

class Calendar:
  def __init__(self):
    self.days_of_the_week = ''
    self.starting_day = ''
    self.days_in_month = 0
    self.month_name = 'January'
    self.year = 2022
    self.num_rows = 6
    self.num_col = 7
  
  def display_header(self):
    print(f'{self.month_name}, {self.year}')
    for day in DAYS_OF_WEEK:
      self.days_of_the_week += day + "   "
    print(self.days_of_the_week)

  def display_dates(self):
    pass

  def input_month_and_year(self):
    pass

Calendar().display_header()