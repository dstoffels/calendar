from constants import DAYS_OF_WEEK

class Calendar:
  def __init__(self):
    self.days_of_the_week = ''
    self.starting_day = ''
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
      self.days_of_the_week += day + self.three_spaces
    print(self.days_of_the_week)

  def display_dates(self):
    self.first_row = ''
    # for day in range (1,self.days_in_month + 1):
    #   row_one = day + self. three_spaces
    #   print()
    for cell in range(1,43):
      if cell < 10:
        cell = ' ' + str(cell)
    
        


      
    


  # def days_in_minth(  ):
    
  #       # #If the month is January, March, May, july, august, = 31
  #   # month = September, april, june, november = 30
  #   # month - february = 28      

  def input_month_and_year(self):
    pass

# Calendar().display_header()
Calendar().display_dates()