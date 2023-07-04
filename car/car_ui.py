import time

class UI:
    def red_light(self):
        print("-" * 12)
        print("| \U0001F534 \U000026AB \U000026AB |  \033[31mREADY!\033[0m")
        print("-" * 12)
        time.sleep(2)

    def yellow_light(self):
        print("-" * 12)
        print("| \U000026AB \U0001F7E1 \U000026AB |  \033[93mSET!\033[0m")
        print("-" * 12)
        time.sleep(2)

    def green_light(self):
        print("-" * 12)
        print("| \U000026AB \U000026AB \U0001F7E2 |  \033[32mGO!\033[0m")
        print("-" * 12)
        time.sleep(2)

    def car_sfx(self):
        print()
        print("vrooom vrooomm .... " * 2 + " \U0001F695 \U0001F4A8")
        time.sleep(2)

    def roadway(self):
        print("\033[90m" + ("-" * 17 + "|")*2 + "-" * 17 + "\033[0m")
