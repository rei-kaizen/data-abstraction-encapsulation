class PetUI:
    """A class representing a user interface for displaying pet information in a bordered format."""
    def borders(self, text):

        border_length = 30 
        title = "Pet Identification \U0001F43E"
        border = "+" + "-" * (border_length - 2) + "+" 
        
        header = "|" + title.center(border_length - 3) + "|"
        separator = "|" + "-" * (border_length - 2) + "|"

        name = "|" + "\033[31m Name: \033[0m" + text[0].ljust(border_length - 9) + "|"
        type = "|" + "\033[31m Type: \033[0m" + text[1].ljust(border_length - 9) + "|"
        age = "|" + "\033[31m Age: \033[0m" + text[2].ljust(border_length - 8) + "|"

        print(border)
        print(header)
        print(separator)
        print(name)
        print(type)
        print(age)
        print(border)