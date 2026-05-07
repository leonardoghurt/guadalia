from datetime import datetime


class Debug:
    def __init__(self, message: str):
        self.message = message
        self.print_message()

    def print_message(self):
        current_datetime = datetime.now().astimezone()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        print(f"{formatted_datetime} - {self.message}")
