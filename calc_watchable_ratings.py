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