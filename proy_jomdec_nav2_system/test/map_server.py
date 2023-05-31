import rospy
import rostest
import unittest

class TestMapServer(unittest.TestCase):
    def test_map_server_launch(self):
        # Iniciar el nodo de prueba
        rospy.init_node('test_map_server_node')

        # Esperar a que el nodo map_server se lance correctamente
        self.assertTrue(rospy.wait_for_service('/map_server/get_map', timeout=1.0))

if __name__ == '__main__':
    rostest.rosrun('proy_jomdec_nav2_system', 'test_map_server', TestMapServer)

