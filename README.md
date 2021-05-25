# Week 3 of 12
## Python
### Movie rating exercise with OOP


#### Tasks

* complete following the pseudo code:

```
# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.
```

Hint: Draw out what's communicating with what.

## Acceptance Criteria

* Program follow all business logic
* Program runs continuously, and exits on the word exit
* program does not break with integer or strings
* OOP implemented

### Film dictionary
```python
# Movie ratings
class Film_Ratings:
    def __init__(self):

        self.film_ratings = {
            'universal': 'Everyone can watch.',
            'pg': 'General viewing, but some scenes may be unsuitable for young children.',
            '12': 'Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.',
            '15': 'No one younger than 15 may see a 15 film in a cinema.',
            '18': 'No one younger than 18 may see an 18 film in a cinema.'

        }

rated_film = Film_Ratings()
```
### Calculating the film they want to watch
```python
from film_ratings import Film_Ratings


class Calc_Watchable_Ratings(Film_Ratings):
    def __init__(self):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()
        self.rating = ''

    def continue_rating(self):
        keep_calculating = input("Do you want to continue? Y/N:  ")  # collects value from user
        if keep_calculating.upper() == 'N':
            print('I hope this was informative!')
        else:
            calculate_rating.inputted_rating()

    def calc_rating(self):
        leave = True
        while leave:
            if self.rating == 'exit':  # if exit is inputted, then the loop ends
                print('Thank you for checking out the ratings')
                leave = False
            elif self.rating == 'u':
                print(calculate_rating.film_ratings['universal'])
                leave = False
            elif self.rating == 'pg':
                print(calculate_rating.film_ratings['pg'])
                leave = False
            elif self.rating == '12':
                print(calculate_rating.film_ratings['12'])
                leave = False
            elif self.rating == '15':
                print(calculate_rating.film_ratings['15'])
                leave = False
            elif self.rating == '18':
                print(calculate_rating.film_ratings['18'])
                leave = False
            else:
                print('Please enter a valid value')
        else:
            print('I hope you got your answer')
            calculate_rating.continue_rating()

    def inputted_rating(self):
        print(f'These are the available ratings:  {calculate_rating.film_ratings.keys()}')
        self.rating = input(
            'What rating would you like to learn about? Type exit to leave.  ')  # asks user for an input on film rating
        self.rating = self.rating.lower()  # sets the string case to lower
        calculate_rating.calc_rating()  # runs the select method


calculate_rating = Calc_Watchable_Ratings()
calculate_rating.inputted_rating()
```