class PetUI:
    """A class representing a user interface for displaying pet information in a bordered format."""
    def borders(self, text):

        border_length = 30 
        title = "Pet Identification"
        border = "+" + "-" * (border_length - 2) + "+" 
        
        header = "|" + title.center(border_length - 2) + "|"
        separator = "|" + "-" * (border_length - 2) + "|"

        name = "| Name: " + text[0].ljust(border_length - 9) + "|"
        type = "| Type: " + text[1].ljust(border_length - 9) + "|"
        age = "| Age: " + text[2].ljust(border_length - 8) + "|"

        print(border)
        print(header)
        print(separator)
        print(name)
        print(type)
        print(age)
        print(border)