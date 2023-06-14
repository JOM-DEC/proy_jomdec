***Proyecto Robótica (GTI\_3B\_TEAM\_01) Safe&Go 

***Documento Técnico Volumen 2*** 

**1  NTRODUCCIÓN** 

*El presente documento tiene como objetivo desarrollar un sistema innovador para un robot que será ubicado en un restaurante y tendrá la función de ayudar a los clientes a desechar sus residuos de manera responsable y efectiva. La idea central del proyecto es promover la cultura del reciclaje entre los clientes y contribuir activamente al cuidado del medio ambiente.* 

*El robot, diseñado para operar en un entorno de restaurante, se desplazará de manera autónoma a cada mesa del establecimiento, recolectando los residuos generados por los clientes. Además, brindará información clara y precisa sobre el tipo de residuo y el contenedor de reciclaje adecuado en el cual debe ser depositado.* 

*En este documento se describen las actividades clave que se llevarán a cabo en el proyecto, abordando aspectos tecnológicos, de diseño, programación y pruebas, con el fin de lograr el objetivo propuesto. Sirve como una referencia integral para el equipo de desarrollo y proporciona una visión general del enfoque y los resultados esperados.* 

1.1 **PROPÓSITO** 

*Este documento tiene como objetivo principal definir y detallar las etapas y actividades necesarias para lograr el objetivo del proyecto. Proporciona una guía clara para el equipo de desarrollo, estableciendo las tareas esenciales que deben llevarse a cabo en el proceso.* 

*Además, este documento cumple con el propósito de comunicar de manera efectiva el plan del proyecto a diversas partes interesadas. Al compartir esta información, como patrocinadores, clientes o equipos de gestión, se establecen expectativas claras en relación al alcance, los resultados esperados y los entregables del proyecto.* 

1.2 **ALCANCE** 

*Para alcanzar el objetivo del proyecto, se realizarán las siguientes actividades:* 

- *Análisis de tecnologías necesarias (entorno).* 
- *Estudio de técnicas SLAM y navegación en ROS para Turtlebot3.* 
- *Configuración y prueba de paquetes y librerías de Turtlebot3.* 
- *Programación e implementación de funcionalidades del robot.* 
- *Realización de pruebas y ensayos con usuarios.* 


**2  ELEMENTOS CLAVES (ENTORNO)** 

*En esta sección, se va describir de forma breve las herramientas clave que se usarán para el proyecto de Robótica. Donde se analizará las tecnologías clave, como SLAM, navegación y el entorno necesario para poder desarrollar el proyecto.*  

1.1 **TURTLEBOT3** 

*TurtleBot3 es un robot móvil de código abierto diseñado para la investigación, la educación y el desarrollo de aplicaciones robóticas. Desarrollado por ROBOTIS, TurtleBot3 se basa en el sistema operativo ROS (Robot Operating System) y ofrece una plataforma versátil y accesible para la experimentación y la implementación de robots autónomos.* 

*El TurtleBot3 está diseñado con un enfoque modular, lo que permite personalizar su configuración según las necesidades del proyecto. Cuenta con una amplia gama de sensores, como cámaras, láseres y sensores inerciales, que le permiten percibir y mapear su entorno.* 

*TurtleBot3 es ampliamente utilizado en entornos académicos y de investigación, así como en proyectos de robótica DIY (hazlo tú mismo) y desarrollo de prototipos. Su combinación de versatilidad, accesibilidad y capacidad de programación en ROS lo convierte en una opción popular para aquellos interesados en explorar el campo de la robótica móvil.* 

*El TurtleBot3 está equipado con las capacidades necesarias para realizar SLAM, lo que le permite construir un mapa del entorno mientras se desplaza de manera autónoma. Esto es fundamental para la navegación autónoma del robot, ya que puede reconocer y evitar obstáculos en tiempo real.* 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 005](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/c6ed19d8-cbf0-40fd-962a-b3cae0af4974)

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 006](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/3f8e0df2-3552-41ae-9a86-de80203c71d6)

1.2 **ROS** 

*ROS (Robot Operating System) es un framework y middleware de código abierto diseñado para el desarrollo de aplicaciones robóticas. Proporciona un conjunto de herramientas, bibliotecas y convenciones que simplifican la programación y comunicación entre componentes de un robot. ROS utiliza un modelo de comunicación basado en nodos, donde cada nodo es un proceso independiente que puede publicar, suscribirse o enviar servicios a otros nodos. Esto permite la colaboración y reutilización de software, promoviendo un enfoque modular en el diseño de sistemas robóticos. Con soporte para múltiples lenguajes de programación, ROS facilita el desarrollo de aplicaciones robóticas complejas y su integración con una amplia gama de hardware y sensores. Su naturaleza de código abierto ha generado una gran comunidad de usuarios y una extensa colección de paquetes y herramientas disponibles.* 

**1.  RQT** 

*Rqt es una herramienta que permite visualizar la información de los nodos y topics. Se empleará esta herramienta visual en el proyecto para asegurar que están conectados los nodos y topics correctamente.*  

*Consulte este enlace: [ https://wiki.ros.org/rqt*  ](https://wiki.ros.org/rqt)*

**2.1.1  RVIZ** 

*RViz es una herramienta de visualización 3D que forma parte de ROS (Robot Operating System). Es una interfaz gráfica que permite visualizar y analizar datos generados por robots o simulaciones en tiempo real. Ofrece también la visualización de mapas y trayectorias.*  

*RViz es una herramienta esencial en el desarrollo de nuestro proyecto y se empleará para visualizar mapas y simulaciones en tiempo real.*  

*Consulte este enlace:[ http://wiki.ros.org/rviz*  ](http://wiki.ros.org/rviz)*

1.3 **GAZEBO** 

*Gazebo es un simulador de robots de código abierto utilizado en el desarrollo y la simulación de sistemas robóticos. Proporciona un entorno de simulación en 3D donde se pueden modelar y simular robots, entornos y escenarios complejos.*  

*En este proyecto, se ha utilizado el modelo de la cafetería, ya que se asemejaba a nuestro enfoque.* 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 007](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/c77c9327-4755-43d9-9162-0f3e3decf062)

1.4 **ANGULAR** 

*Se ha desarrollado una interfaz web utilizando Angular para mejorar la interacción con el robot. Esta interfaz web permite visualizar el mapa generado por RViz y proporciona controles para controlar el robot de manera intuitiva. Además, hemos integrado una visualización en tiempo real de una imagen capturada por el robot.* 

1.5 **SLAM** 

*SLAM (Simultaneous Localization And Mapping) es una técnica de navegación utilizada por robots móviles para construir un mapa del entorno mientras se desplazan. A través de algoritmos y la información en tiempo real captada por los sensores del robot, como LIDAR, cámaras y odometría, el robot es capaz de determinar su posición y construir un mapa detallado del entorno a medida que se mueve.* 

**3  DESARROLLO Y PRUEBAS** 

*Una vez revisados los recursos tecnológicos clave utilizados en este proyecto, esta sección se enfoca en describir las diversas etapas que han sido parte del desarrollo de la funcionalidad implementada.* 

*El proceso se inició con la simulación del proyecto para luego trasladarlo a un entorno real. Para la simulación, se empleó el modelo de Gazebo de la cafetería. Posteriormente, en el entorno real, se construyó un ambiente similar y adecuado a nuestras necesidades.* 

1.6 **ESCANEO DEL ENTORNO SIMULADO**  

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 008](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/956cceb6-c39f-4869-b44a-dcde8102c2d3)

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 009](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/c7aee502-7a18-4939-8945-5b1a9f9a442e)

7. **ESCANEO DEL ENTORNO REAL** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 010](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/0c636f66-c5de-47fd-b7d4-967a9fac9473)

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 011](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/3cd5433b-4775-4bc6-ba1f-9548221b1959)

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 012](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/3f26483c-5ce3-4107-858c-cf2ada194b4e)

*Para escanear el entorno se ha empleado el método Cartographer y se ha empleado el programa de teleop\_keyboard para poder mover el robot.*  

***ros2 run turtlebot3\_teleop teleop\_keyboard*** 

*Por último para guardar el mapa se utiliza el ejecutable map\_server **ros2 run nav2\_map\_server map\_saver\_cli -f ~/my\_map*** 

**4  WEB** 

**4.1  INTERFAZ WEB** 

4.1.1 **Landing page (página principal)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 013](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/f5982fe3-8abe-4d78-988e-1447b0e05b11)

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 014](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/2e427ba9-0a98-47b8-9ccc-623fffef0046)


4.1.2 **Contact us (contáctanos)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 015](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/e2b95284-f8e1-49f7-8d4d-41288db54917)

4.1.3 **Sign in (iniciar sesion)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 016](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/d0f0f37c-77c1-45bf-b470-73157efc2509)

4.1.4 **Sign up (registrar)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 017](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/37a9235e-84a0-4b24-ab3a-6ca21872268d)

4.1.5 **Status page (página estado)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 018](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/52e7c7bf-aec3-400e-8d45-f3ca3d9346dc)

4.1.6 **Control page (página control)** 

![Aspose Words 5fdecf08-8866-425f-b65f-c1ad8f87c14f 025](https://github.com/JOM-DEC/proy_jomdec/assets/73239280/5c505111-1352-484d-95ff-f5c980d2b815)

**5  LIBRERIAS**  

*En esta sección se verán las bibliotecas que se han utilizado para interactuar con el robot y manejar la visualización.*  

5.1 **ROSLIB.MIN.JS** 

*Esta biblioteca interactua con el sistema de comunicación de ROS. Permite       establecer conexiones y enviar y recibir mensajes entre el cliente y el servidor de ROS.* 

5.2 **EVENTEMITTER2.MIN.JS** 

*Una biblioteca de JavaScript que implementa el patrón de diseño de publicación/suscripción.  Permite emitir eventos personalizados y suscribirse a ellos en diferentes partes de una aplicación, facilitando la comunicación y coordinación entre los componentes de un sistema de robótica.* 

5.3 **ROS2D.MIN.JS** 

*una biblioteca para la visualización de datos en 2D en aplicaciones basadas en ROS. Proporciona funciones para representar y manipular mapas, ocupación de rejillas (occupancy grids), líneas, puntos, texto y flechas.* 

5.4 **ANGULAR** *Se emplea*  

**6  ENLACES Y OTROS RECURSOS** 

*En esta sección se adjunta los enlaces para acceder a los repositorios de Web y ROS* 

**6.1  REPOSITORIOS**   

Ros >[ https://github.com/JOM-DEC/proy_jomdec/tree/sprint03 ](https://github.com/JOM-DEC/proy_jomdec/tree/sprint03) Web >[ https://github.com/JOM-DEC/Web_robotica ](https://github.com/JOM-DEC/Web_robotica)  

**7  CONCLUSIONES Y LINEAS DE MEJORA** 

- *Se ha conseguido implementar la funcionalidad del mapa y la cámara, pudiendo la cámara diferenciar algunos objetos. No obstante, para el siguiente sprint se quiere entrenar un modelo que adapte más clases y se tengan más casos.*  
- *Se ha conseguido el entorno de simulación. No obstante, se han tenido algunos problemas con el entorno real. Que se solucionarán para el siguiente sprint.*  

**CONTROL DEL DOCUMENTO** 

**Título:**  *Documento Técnico de Diseño*  **Volumen:**  *Vol. 1* 

**Fecha:**  *30 Enero 2023* 

**Autor:**  *Chenyi Jiang* 

**Referencia:**  *GTI\_3B\_TEAM\_01* 

**FIRMAS DEL DOCUMENTO** 



|**Naturaleza del  firmante** |**Nombre** |**Firma** |**Fecha** |**Rol** |
| :- | - | - | - | - |
|*Autor* |*Chenyi* ||*30/05/2023* |*Miembro del equipo* |
|*Autor* |*Jorge* ||*14/06/2023* |*Miembro del equipo* |

