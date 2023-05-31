import sys
sys.path.insert(1, '../src')
from model_world import get_world_file_path as getWorld




def test_get_world_path():
    assert getWorld("burger_pi.model") == "/home/davidgf/David/turtlebot3_ws/install/proy_jomdec_my_world/share/proy_jomdec_my_world/world/burger_pi.model"