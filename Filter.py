numbers = [-2, -1, 0, 1, 2]
def extract_positive(numbers):
     positive_numbers = []
     for number in numbers:
         if number > 0: 
             positive_numbers.append(number)
     return positive_numbers
extract_positive(numbers)
