import unittest

import os
import uuid
from card_repository import CardRep, Card


class CardRepTests(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_cards.db"
        self.card_repository = CardRep(self.db_path)
        self.card_1 = Card(
            card_number="6100297465002704",
            expiration_date="07/25",
            cvv_code="378",
            issue_date="2023-11-09",
            owner_id=uuid.uuid4(),
            status_card="заблокирована"
        )
        self.card_2 = Card(
            card_number="5100297465002704",
            expiration_date="07/24",
            cvv_code="123",
            issue_date="2022-10-01",
            owner_id=uuid.uuid4(),
            status_card="активирована"
        )

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_save_and_get_card(self):
        self.card_repository.save(self.card_1)
        self.card_repository.save(self.card_2)

        retrieved_card_1 = self.card_repository.get(self.card_1.card_number)
        retrieved_card_2 = self.card_repository.get(self.card_2.card_number)

        self.assertIsNotNone(retrieved_card_1)
        self.assertEqual(retrieved_card_1.card_number, self.card_1.card_number)
        self.assertEqual(retrieved_card_1.expiration_date, self.card_1.expiration_date)
        self.assertEqual(retrieved_card_1.cvv_code, self.card_1.cvv_code)
        self.assertEqual(retrieved_card_1.issue_date, self.card_1.issue_date)
        self.assertEqual(retrieved_card_1.owner_id, self.card_1.owner_id)
        self.assertEqual(retrieved_card_1.status_card, self.card_1.status_card)

        self.assertIsNotNone(retrieved_card_2)
        self.assertEqual(retrieved_card_2.card_number, self.card_2.card_number)
        self.assertEqual(retrieved_card_2.expiration_date, self.card_2.expiration_date)
        self.assertEqual(retrieved_card_2.cvv_code, self.card_2.cvv_code)
        self.assertEqual(retrieved_card_2.issue_date, self.card_2.issue_date)
        self.assertEqual(retrieved_card_2.owner_id, self.card_2.owner_id)
        self.assertEqual(retrieved_card_2.status_card, self.card_2.status_card)

    def test_get_nonexistent_card(self):
        retrieved_card = self.card_repository.get("1234567890")
        self.assertIsNone(retrieved_card)


if __name__ == '__main__':
    unittest.main()
