import time

from odoo import models


class FakeTestModel(models.Model):

    _name = "fake.test"
    _description = "Fake model to test JsonRequest"

    def name_search(self, name="", args=None, operator="ilike", limit=100):
        # here simulate time computations re-using name attribute with wait value
        time.sleep(float(name))
        return []
