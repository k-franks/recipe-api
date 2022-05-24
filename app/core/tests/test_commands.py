""" Test custom command"""


from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycop2gError


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTest(SimpleTestCase):
    """Test command"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready."""
        patched_check.return_value = True

        call_command("wait_for_db")

        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_not_ready(self, patch_sleep, patched_check):
        """test waiting for db when getting Operror"""
        patched_check.side_effect = (
            [Psycop2gError] * 2 + [OperationalError] * 3 + [True]
        )

        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
