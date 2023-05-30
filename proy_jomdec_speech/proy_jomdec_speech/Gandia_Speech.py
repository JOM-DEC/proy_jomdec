import rclpy
import sys
import time
import colored
import platform
import flet as ft
import configparser
from colored import stylize
from AI.AIManager import AIManager
from Audio.Algo import AudioManager
from Audio.SoundManager import SoundManager
from Logger.SimpleLogger import SimpleLogger
from Audio.VoiceOutputManager import VoiceOutputManager

import logging
import threading
import time

import flet as ft
import threading
import base64
 
   
from rclpy.node import Node
from std_msgs.msg import String

    
class RobotGandiaSpeechNode(Node):

    def __init__(self):
        super().__init__('proy_jomdec_speech')
        
        self.publisher_ = self.create_publisher(String, 'text_response', 10)
        
        timer_period = 0.5  # seconds
        
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.config_file = "Config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self.display_man = None
    
        self.l = SimpleLogger("DEBUG")
        
        if self.l is None:
            print("Exit...")
            exit()
            
        self.init_system()
        
    
    def cognibot(self):
        transcription = ""
        try:
            while True:
                if not self.audio_man.output_queue.empty():
                    transcription = self.audio_man.output_queue.get()
                #self.ai_man.handle_command(transcription)                                                                       
                
                if not self.ai_man.result_outputs.empty():
                    command = self.ai_man.result_outputs.get()              
                    self.voice_man.handle_command(command)
                else:
 
                    time.sleep(0.01)
                
        except KeyboardInterrupt:
            # AudioManager is the only module with a separate loop that needs
            # to stop in order to have a clean exit
            self.audio_man.stop()
            
    def init_system(self):
        self.sound_man = SoundManager(self.l, self.config_file)
        self.display_man = None
        self.audio_man = AudioManager(self.l, self.config_file, self.display_man, self.sound_man)
        self.ai_man = AIManager(self.l, self.config_file, self.display_man, self.sound_man)
        self.voice_man = VoiceOutputManager(self.l, self.config_file, self.display_man)
    
    
    def timer_callback(self):
        self.cognibot()
        msg = String()
        msg.data = 'Hello World'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    robot_gandia_speech = RobotGandiaSpeechNode()

    rclpy.spin(robot_gandia_speech)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_gandia_speech.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
        
