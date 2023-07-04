class Formatter:
    """This class is responsible for formatting and printing out a given fan's properties"""
    
    def properties(self, fan):
        
        border_length = 40  # Length of the border
        
        fan_name = "Eureka Fan"  # Replace with the appropriate fan name

        # Top border line
        top_border = "╔" + "═" * (border_length - 2) + "╗"

        # Fan name line
        side_border1 = "║" + fan_name.center(border_length - 2) + "║"

        # Create the separator line
        separator = "╠" + "═" * (border_length - 2) + "╣"

        # Get the fan properties
        fan_deets1 = f"Speed: {fan.get_speed()}  |  Power On: {fan.get_on()}"
        fan_deets2 = f"Radius: {fan.get_radius()}  |  Color: {fan.get_color()}"
        side_border2 = "║" + fan_deets1.center(border_length - 2) + "║"
        side_border3 = "║" + fan_deets2.center(border_length - 2) + "║"

        # Create the bottom border line
        bottom_border = "╚" + "═" * (border_length - 2) + "╝"

        # Print the formatted output
        print(top_border)
        print(side_border1)
        print(separator)   
        print(side_border2)
        print(side_border3)
        print(bottom_border)
