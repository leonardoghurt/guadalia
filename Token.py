from random import choice
import tokens
class Token:
    def __init__(self, token: str):
        self.token = token
        self.nexttokens = []
        tokens.tokens.append(self)
    def add_next_token(self, token: str):
        if token:
            self.nexttokens.append(token)
    def get_name(self):
        return self.token
    def get_new_token(self):
        if not self.nexttokens:
            return ""
        return choice(self.nexttokens)