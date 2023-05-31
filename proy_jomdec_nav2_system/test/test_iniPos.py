import sys
sys.path.insert(1, '../proy_jomdec_nav2_system')
from initial_pose_pub import Publisher

import math


def test_getPosition():
    assert Publisher.position(Publisher, 1, 2, 87) == [1, 2, 87]
    assert Publisher.position(Publisher, -6, 50, 0) == [-6, 50, 0]