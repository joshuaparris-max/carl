import copy
import unittest

from src.data_repository import DataRepository
from src.engine.validation import DataValidationError, DataValidator


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = DataRepository().load().__dict__
        self.validator = DataValidator()

    def test_current_data_is_valid(self):
        self.validator.validate_all(self.data)

    def test_character_missing_required_field_fails(self):
        data = copy.deepcopy(self.data)
        del data["characters"]["carl"]["resources"]
        with self.assertRaises(DataValidationError):
            self.validator.validate_all(data)

    def test_recipe_referencing_unknown_item_fails(self):
        data = copy.deepcopy(self.data)
        data["recipes"]["bad_recipe"] = {
            "id": "bad_recipe",
            "ingredients": ["missing_item"],
            "result": "crude_blast_charge",
        }
        with self.assertRaises(DataValidationError):
            self.validator.validate_all(data)

    def test_inconsistent_map_width_fails(self):
        data = copy.deepcopy(self.data)
        data["map_rows"][0] = "###"
        with self.assertRaises(DataValidationError):
            self.validator.validate_all(data)


if __name__ == "__main__":
    unittest.main()
