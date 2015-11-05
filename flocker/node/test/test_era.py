# Copyright ClusterHQ Inc.  See LICENSE file for details.

"""
Tests for ``flocker.node._era``.
"""

from uuid import UUID
from unittest import skipUnless

from twisted.trial.unittest import SynchronousTestCase
from twisted.python.runtime import platform
from .._era import get_era


class EraTests(SynchronousTestCase):
    """
    Tests for ``get_era``
    """
    @skipUnless(platform.isLinux(), "Only possible on Linux.")
    def test_get_era(self):
        """
        The era is the current unique ``boot_id``.

        This rather duplicates the implementation, but can't do much
        better.
        """
        with open("/proc/sys/kernel/random/boot_id") as f:
            self.assertEqual(get_era(),
                             UUID(hex=f.read().strip()))
