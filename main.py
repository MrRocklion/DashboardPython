import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from CustomWidgets.CustomSwitch import CSwitch
from CustomWidgets.CustomRounded import CircularProgress
from CustomWidgets.CustomIconButton import CIconButton
from CustomWidgets.CustomLine import PyLineEdit
from CustomWidgets.CustomButton import PyPushButton
#switchs
switchs = ["switch1","swtich2","switch3","switch4"]
etiquetas  = ["ACCION1","ACCION2","ACCION3","ACCION4"]
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.container = QFrame() #contenedor principal
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container {background-color: #222}")
        #creamos una rejilla para contener nuestros widgets
        self.grid = QGridLayout()
        #botones de la barra de tareas
        self.menuButton = CIconButton(

            icon_path="./assets/menu.svg",
            parent=None,
            app_parent=None,
            width=30,
            tooltip_text="hola",
            btn_id="btn1",
            icon_color="#00D6B4",
            icon_color_hover="#00D6B4",
            bg_color="transparent",
            bg_color_hover="transparent",

        )
        self.webButton = CIconButton(

            icon_path="./assets/web.svg",
            parent=None,
            app_parent=None,
            width=30,
            tooltip_text="hola",
            btn_id="btn1",
            icon_color="#00D6B4",
            icon_color_hover="#00D6B4",
            bg_color="transparent",
            bg_color_hover="transparent",

        )
        self.faceButton = CIconButton(

            icon_path="./assets/facebook.svg",
            parent=None,
            app_parent=None,
            width=30,
            tooltip_text="hola",
            btn_id="btn1",
            icon_color="#00D6B4",
            icon_color_hover="#00D6B4",
            bg_color="transparent",
            bg_color_hover="transparent",

        )
        self.settingButton = CIconButton(

            icon_path="./assets/settings.svg",
            parent=None,
            app_parent=None,
            width=30,
            tooltip_text="hola",
            btn_id="btn2",
            icon_color="#00D6B4",
            icon_color_hover="#00D6B4",
            bg_color="transparent",
            bg_color_hover="transparent",

        )
        #creamos un texto
        self.titulo = QLabel("DASHBOARD CON PYTHON")
        self.titulo.setObjectName("titulos")
        self.titulo.setStyleSheet("#titulos {color: white;font-size: 25px}")
        self.titleBar = QHBoxLayout()
        self.layout1 = QHBoxLayout()
        self.groupButtons = QHBoxLayout()
        self.layout1.addWidget(self.menuButton,Qt.AlignCenter)
        self.layout1.addWidget(self.titulo, Qt.AlignCenter)
        self.groupButtons.addWidget(self.faceButton,Qt.AlignCenter)
        self.groupButtons.addWidget(self.webButton,Qt.AlignCenter)
        self.groupButtons.addWidget(self.settingButton,Qt.AlignCenter)
        self.titleBar.addLayout(self.layout1,Qt.AlignCenter)
        self.titleBar.addLayout(self.groupButtons,Qt.AlignCenter)

        # creamos indicador rounded
        self.sensor = CircularProgress()
        self.sensor.set_value(75)
        self.sensor.setMinimumSize(self.sensor.width,self.sensor.height)
        self.sensor.progress_color = "#17A589"
        self.sensor.text_color = "#17A589"
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.sensor, Qt.AlignCenter, Qt.AlignCenter)

        # creamos indicador rounded2
        self.sensor2 = CircularProgress()
        self.sensor2.setMinimumSize(self.sensor.width,self.sensor.height)
        self.sensor2.set_value(12)
        self.sensor2.progress_color = "#17A589"
        self.sensor2.text_color = "#17A589"
        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.sensor2, Qt.AlignCenter, Qt.AlignCenter)

        # creamos indicador rounded3
        self.sensor3 = CircularProgress()
        self.sensor3.set_value(45)
        self.sensor3.progress_color = "#17A589"
        self.sensor3.text_color = "#17A589"
        self.sensor3.setMinimumSize(self.sensor.width,self.sensor.height)
        self.layout4 = QVBoxLayout()
        self.layout4.addWidget(self.sensor3, Qt.AlignCenter, Qt.AlignCenter)
        # creamos una tabla de switchs
        self.tabla = QGridLayout()
        self.switch1 = CSwitch(
            active_color="#17A589",
        )
        self.switch2 = CSwitch(active_color="#17A589",)
        self.switch3 = CSwitch(active_color="#17A589",)
        self.switch4 = CSwitch(active_color="#17A589",)
        #AGREGAMOS LOS RESPECTIVOS TEXTOS
        self.text1 = QLabel("Accion1")
        self.text1.setStyleSheet("color: white;font-size:15")
        self.text2 = QLabel("Accion1")
        self.text2.setStyleSheet("color: white; font-size:15")
        self.text3 = QLabel("Accion1")
        self.text3.setStyleSheet("color: white; font-size:15")
        self.text4 = QLabel("Accion1")
        self.text4.setStyleSheet("color: white; font-size:15")
        #Creamos un textfield
        self.campoEnviar = PyLineEdit(
            place_holder_text= "Ingresa un dato par enviar",
            context_color="#17A589",
            color="#FFF",
            width=160,
            radius=5
        )
        self.layout5 = QVBoxLayout()
        self.layout5.addWidget(self.campoEnviar)
        #creamos un boton para enviar
        self.layout6 = QVBoxLayout()
        self.sendButton = PyPushButton(
            text="SEND",
            radius=5,
            color="#17A589",
            bg_color_hover="#00D6B4",
            bg_color_pressed="#273746 ",
            width = 160
        )

        self.layout6.addWidget(self.sendButton)


        #incluimos dentro del respectivo grid

        self.tabla.addWidget(self.switch1,0,0,Qt.AlignCenter)
        self.tabla.addWidget(self.switch2, 1, 0, Qt.AlignCenter)
        self.tabla.addWidget(self.switch3, 2, 0, Qt.AlignCenter)
        self.tabla.addWidget(self.switch4, 3, 0, Qt.AlignCenter)
        self.tabla.addWidget(self.text1, 0, 1, Qt.AlignCenter)
        self.tabla.addWidget(self.text2, 1, 1, Qt.AlignCenter)
        self.tabla.addWidget(self.text3, 2, 1, Qt.AlignCenter)
        self.tabla.addWidget(self.text4, 3, 1, Qt.AlignCenter)
        self.tabla.setSpacing(30)
        #agregamos los widgets a la rejilla
        self.grid.addLayout(self.titleBar,0,0,1,5,Qt.AlignCenter)
        self.grid.addLayout(self.layout2,2,0, Qt.AlignCenter)
        self.grid.addLayout(self.layout3, 2,1, Qt.AlignCenter)
        self.grid.addLayout(self.layout4, 2, 3, Qt.AlignCenter)
        self.grid.addLayout(self.layout4, 2, 4, Qt.AlignCenter)
        self.grid.addLayout(self.tabla, 2, 4, Qt.AlignCenter)
        self.grid.addLayout(self.layout5,3,0,1,4,Qt.AlignCenter)
        self.grid.addLayout(self.layout6,3,4,Qt.AlignCenter)
        self.grid.setSpacing(30)
        #agregamos la rejilla al marco inicial
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
