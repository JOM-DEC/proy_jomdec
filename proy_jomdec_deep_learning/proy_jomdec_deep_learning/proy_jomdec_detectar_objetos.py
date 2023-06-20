import os
import cv2
import rclpy
import time
import sys
import getopt
import numpy as np
from rclpy.node import Node
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image
import boto3

class RobotGandiaDeepLearningNode(Node):
    def __init__(self):
        super().__init__('proy_jomdec_deep_learning')
        

        self.rekognition_client = boto3.client('rekognition', region_name='us-east-1')
        self.objetos_detectar = ['Bottle', 'Glass', 'Cup', 'dishes']  # Puedes agregar más etiquetas si es necesario
        
        self.subscription = self.create_subscription(Image, '/image', self.listener_callback, 10)
        self.subscription


        # Se utiliza para convertir entre ROS y OpenCV imágenes
        self.br = CvBridge()
        
        

        # Publisher    
        self.publisher_ = self.create_publisher(String, '/class_name', 10)
        self.fomo_image_publisher = self.create_publisher(Image, '/aws_image', 20)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        
        self.label_name = "---"

    def edgeImpulseModel(self, frame):
    
        # Convertir frame de OpenCV a formato de bytes
        _, img_encoded = cv2.imencode('.jpg', frame)
        image_bytes = img_encoded.tobytes()

        # Detectar objetos en el frame
        response = self.rekognition_client.detect_labels(
            Image={'Bytes': image_bytes},
            MinConfidence=85,  # Cambia este valor según tus necesidades
        )

        # Filtrar etiquetas de objetos a detectar
        objetos_detectados = [label['Name'] for label in response['Labels'] if label['Name'] in self.objetos_detectar]

        # Reiniciar la posición vertical del texto en cada frame
        text_x = 0
        text_y = 1

        try:
            if objetos_detectados:
                for objeto in objetos_detectados:
                    # Calcular la longitud de la palabra
                    palabra_longitud = len(objeto)

                    # Dibujar
                    cv2.putText(frame, objeto, (10 + text_y, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 2)

                    # Ajustar la posición vertical en función de la longitud de la palabra
                    text_y += 25 * palabra_longitud
            return frame, objeto

        except Exception as e:
            print("Ocurrió un error:", str(e))
    
    def listener_callback(self, data):
        """
        Función callback.
        """
        self.get_logger().info("Read Img..")
        current_frame = self.br.imgmsg_to_cv2(data)
        try:
            # Convertir mensaje de imagen ROS a imagen OpenCV
            img, self.label_name = self.edgeImpulseModel(current_frame)
            self.fomo_image_publisher.publish(self.br.cv2_to_imgmsg(img, encoding='bgr8'))
        except: 
            #Que publique la imagen en crudo
            self.fomo_image_publisher.publish(data)
            
            
    
    def timer_callback(self):
        msg = String()
        msg.data = self.label_name
        self.publisher_.publish(msg)


def main(args=None):

    
    rclpy.init(args=args)

    robot_gandia_deep_learning = RobotGandiaDeepLearningNode()

    rclpy.spin(robot_gandia_deep_learning)

    robot_gandia_deep_learning.destroy_node()

    rclpy.shutdown()
    


if __name__ == '__main__':
    main()
