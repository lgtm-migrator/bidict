# Copyright 2009-2022 Joshua Bronson. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Test bidict metadata."""

import bidict


METADATA_ATTRS = """
__author__
__maintainer__
__copyright__
__email__
__description__
__keywords__
__license__
__status__
__url__
__version__
__project_urls__
""".split()


def test_metadata():
    """Ensure bidict has expected metadata attributes."""
    for i in METADATA_ATTRS:
        assert getattr(bidict, i)
