"""Tests to test the MacPyVer class."""

from datetime import datetime
from typing import Type

import pytest

from macpyver_core.macpyver import MacPyVer
from macpyver_core.model import Software
from macpyver_core.version_source import VersionSource


@pytest.mark.parametrize(
    'index, version, year, month, day',
    [
        (0, '2.1.1', 2023, 10, 26),
        (1, '2.1.0', 2023, 9, 16),
        (2, '1.1.1', 2022, 1, 20),
        (3, '1.1.1-dev', 2022, 1, 12),
    ]
)
def test_macpyver_class(
    software: Software,
    source: Type[VersionSource],
    index: int,
    version: str,
    year: int,
    month: int,
    day: int
) -> None:
    """Test the MacPyVer class.

    Test if we get the correct versions when the `version_source` is set to the
    `test_source`.

    Args:
        software: a test Software object.
        source: a test VersionSource object.
    """
    macpyver = MacPyVer(software=software, version_source=source)
    versions = macpyver.get_all_versions()

    # Tests
    version_object = versions[index]
    assert version_object.version == version
    if version_object.release_datetime:
        assert version_object.release_datetime.year == year
        assert version_object.release_datetime.month == month
        assert version_object.release_datetime.day == day
