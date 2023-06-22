class Card:
    def __init__(self, card_number, expiration_date, cvv_code, issue_date, owner_id=None, status_card="new"):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv_code = cvv_code
        self.issue_date = issue_date
        self.owner_id = owner_id
        self.status_card = status_card

    def activate(self):
        if self.status_card == "new":
            self.status_card = "activated"
            return "Card activated."
        else:
            return "Card already activated."

    def block(self):
        if self.status_card == "activated":
            self.status_card = "blocked"
            return "Card blocked."
        else:
            return "Card cannot be blocked."

    def secure_data(self):
        return f"Secure data for Card {self.card_number}"
