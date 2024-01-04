"""PyTest fixtures and configuration."""
# pylint: disable=too-few-public-methods

from datetime import datetime
from typing import Type

import pytest

from macpyver_core.model import Software, Version
from macpyver_core.version_source import VersionSource


@pytest.fixture
def source() -> Type[VersionSource]:
    """Fixtre that creates a VersionSource class to test.

    Returns:
        A class of type VersionSource that can be used for unit testing.
    """

    class TestSource(VersionSource):
        """Test VersionSource for unit testing."""

        def get_all_versions(self) -> list[Version]:
            """Return test versions for test software.

            Returns:
                A list of test versions. These are not retrieved from the
                Internet but generated here.
            """
            return [
                Version(version='2.1.1', release_datetime=datetime(
                    year=2023, month=10, day=26
                )),
                Version(version='2.1.0', release_datetime=datetime(
                    year=2023, month=9, day=16
                )),
                Version(version='1.1.1', release_datetime=datetime(
                    year=2022, month=1, day=20
                )),
                Version(version='1.1.1-dev', release_datetime=datetime(
                    year=2022, month=1, day=12
                ))
            ]

    return TestSource


@pytest.fixture
def software() -> Software:
    """Fixture for a test Software object.

    Returns:
        A Software object to use in unit testing.
    """
    return Software(name='test_software')
