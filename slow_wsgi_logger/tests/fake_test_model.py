import time

from odoo import models


class FakeTestModel(models.Model):

    _name = "fake.test"
    _description = "Fake model to test JsonRequest"

    def name_search(self, wait="", args=None, operator="ilike", limit=100):
        # on parent model first param is name used to search in name_get value
        # here simulate time computations
        time.sleep(float(wait))
        return []
