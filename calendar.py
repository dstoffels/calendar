from ctypes import WinDLL
from constants import DAYS_OF_WEEK, SAT, WED

class Calendar:
  def __init__(self):
    self.days_of_the_week = ''
    self.starting_day = SAT
    self.days_in_month = 31
    self.month_name = 'January'
    self.year = 2022
    self.num_rows = 6
    self.num_col = 7
    self.two_spaces = '  '
    self.three_spaces = '   '
  
  def display_header(self):
    print(f'{self.month_name}, {self.year}')
    for day in DAYS_OF_WEEK:
      self.days_of_the_week += day + self.two_spaces
    print(self.days_of_the_week)

  def display_dates(self):
    day = 1
    starting_col = DAYS_OF_WEEK.index(self.starting_day)
    start_counting = False  

    while day <= self.days_in_month:
      line_to_be_printed = ''
      col = 0
      while col < 7 and day <= self.days_in_month:
        if col >= starting_col: start_counting = True

        if start_counting:
          if day < 10: 
            line_to_be_printed += ' ' + str(day)
          else: 
            line_to_be_printed += str(day)
          day += 1
        else:
          line_to_be_printed += self.two_spaces

        line_to_be_printed += self.two_spaces
        col += 1
      print(line_to_be_printed)




  # def days_in_minth(  ):
    
  #       # #If the month is January, March, May, july, august, = 31
  #   # month = September, april, june, november = 30
  #   # month - february = 28      

  def input_month_and_year(self):
    pass

Calendar().display_header()
Calendar().display_dates()