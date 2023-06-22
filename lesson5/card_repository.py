import sqlite3
import uuid

from card import Card


class CardRep:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id TEXT PRIMARY KEY,
            card_number TEXT,
            expiration_date TEXT,
            cvv_code TEXT,
            issue_date TEXT,
            owner_id TEXT,
            status_card TEXT
        )
        ''')

        conn.commit()
        conn.close()

    def get(self, card_number: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cards WHERE card_number = ?", (card_number,))
        result = cursor.fetchone()

        conn.close()

        if result:
            card = Card(
                card_number=result[1],
                expiration_date=result[2],
                cvv_code=result[3],
                issue_date=result[4],
                owner_id=uuid.UUID(result[5]) if result[5] else None,
                status_card=result[6]
            )

            return card

        return None

    def save(self, card: Card):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO cards (id, card_number, expiration_date, cvv_code, issue_date, owner_id, status_card)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(uuid.uuid4()),
            card.card_number,
            card.expiration_date,
            card.cvv_code,
            card.issue_date,
            str(card.owner_id) if card.owner_id else None,
            card.status_card
        ))

        conn.commit()
        conn.close()


def main():
    card_repository = CardRep('cards.db')
    card_1 = Card(card_number="6100297465002704", expiration_date="07/25", cvv_code="378",
                  issue_date="2023-11-09", owner_id=uuid.uuid4(), status_card="blocked")

    card_repository.save(card_1)
    card = card_repository.get("6100297465002704")
    if card:
        print(f"Card number: {card.card_number}")
        print(f"Expiration date: {card.expiration_date}")
        print(f"CVV code: {card.cvv_code}")
        print(f"Issue date: {card.issue_date}")
        print(f"Owner ID: {card.owner_id}")
        print(f"Status: {card.status_card}")
    else:
        print("Card not found.")

    print(card_1.activate())
    print(card_1.block())


if __name__ == '__main__':
    main()
