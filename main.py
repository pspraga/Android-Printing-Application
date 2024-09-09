import kivy
kivy.require('1.9.1')
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#Config.set('kivy','window_icon','icon.ico')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.utils import platform
from kivymd.toast import toast
import socket
from kivymd.uix.pickers import MDDatePicker
from configparser import ConfigParser
from os.path import join

class Function(Screen):
    def settings(self):
        sm.current="setting"
        pass


    def on_save1(self, instance, value, date_range):
        formated=value.strftime("%d-%m-%Y")
        self.ids.edate.text=str(formated)
     
        print(formated)
    def on_save2(self, instance, value, date_range):
        formated=value.strftime("%d-%m-%Y")
        self.ids.pdate.text=str(formated)
     
        print(formated)

    def on_cancel(self, instance, value):
        pass
    def show_date_picker1(self):
        date_dialog = MDDatePicker(primary_color="brown",
    accent_color="darkred",
    selector_color="red",
    text_toolbar_color="lightgrey",
    text_color="orange",
    text_current_color="white",
    text_button_color="lightgrey",
    input_field_background_color_normal="coral",)
        date_dialog.bind(on_save=self.on_save1, on_cancel=self.on_cancel)
        date_dialog.open()
    def show_date_picker2(self):
        date_dialog = MDDatePicker(primary_color="brown",
    accent_color="darkred",
    selector_color="red",
    text_toolbar_color="lightgrey",
    text_color="orange",
    text_current_color="white",
    text_button_color="lightgrey",
    input_field_background_color_normal="coral",)
        date_dialog.bind(on_save=self.on_save2, on_cancel=self.on_cancel)
        date_dialog.open()
   
        
        
    def viewimg(self,root):
        #self.stop(root)
        Window.close()
    def callback(self,root):
        pass
       
        
        
          
    def qrprint(self,root):
            cf=ConfigParser()
            """if platform=='android':
                from jnius import autoclass
                androidpath=autoclass('android.os.Environment')
                private=androidpath.getDataDirectory().getAbsolutePath()
                conf=join(private,'Config.ini')
            else:
                conf='Config.ini'"""
            conf='Config.ini'
            cf.read(conf)
            ipadd=cf.get("ip","ipadd")
        
            if self.ids.content.text=="" :
                toast("Please Enter Ip and Content to print.")
            else:
                try:
                    value=self.ids.content.text
                    pdate=self.ids.pdate.text
                    edate=self.ids.edate.text
                    print("button pressed")
                    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    host = ipadd
                    port = 9100
                    print(host)
                    
                    mysocket.connect((host, port))
                    print("connection success")#connecting to host
                    qr=f"""
                        ^XA
^PW799
^FO128,0^GFA,07680,07680,00060,:Z64:
eJzt2DuSnDAQBmBRBIQcgZtYRxM32CMZlwOHPsLiE5gqJ3JZVrv/bomHBpj1TG3ZAR3MsCM+gRq9WGOuuOKKK6644ooUdTDGDm8+vaWJDTHqRtNEY9xYnEHEH5YGU8WixJJHBVxuPX/zqVNxL0Q9Kpj4qM8/Ov3EJVuUO286/kJd62iIL8nW89FsadA74jvpUM6VsK1Ky/WOpiIubSmnoqLxYVtrw0iaem7R1P/McophNc97Filmu+T5xtrpjq3JHFnuV+d26VdrS6RNObQt7BKLHe7Z8E62umu7IzuqXXJVc3K4sArJRrWSK4cHdWOXZ9TyyR4jaGvxjBpkDs9lSrambd/oorFhY23uG530Q5Ia8DWpXfqkJeMiVK+W1KJPupyfcGDp2FJu44GtYEmyXloommb7m3xD39e2Luwr9S6qxVWk8iPbcHKcjExT2gY2nNiWjyxfc9cGlOY8/8afG9tJqnu5ttqBkm3RWNyVTHYUYL+urSP0kkFyDcuFOEvtaNjmfnVrUSks7VmpcrGx29ifGNFygZDtt7W1YbGO7cvK/kKvW9svbP1yz92Jldm+Qe/xO1aG2GLJFlbG0LSyPxYr/WW2lm1b2ho9dVL7me00941wbgNK/YHFk11ZKmzESre2lG2da06Wh3Pcs40ulC19wsVW46g/syS/71kZ++Op7fF7Wrq2tpNUnllGLu7ahnTWSxYT8J7VoQ+BX/IaKuk4tq9oqKV9K1PQsX1BCazZscjWYjFdr21Ep+VDO1s+vZ8tn94fWv5B7Md4a7FpPLNed4hEO5ZXG0xHs+V+Nm0sZqRl1eQi7rUmj6O7lo5sJ0vSiUWL0oJ3a4c71p3YUe/Zq+VbHEs7YDc2244TMM/PmLY5mx8OrJWhkjbShY219I00Xm5tpzvXHSvrUTRpgyKry7C1uLNKlw2jVwt/Zc2ulTU0rKwrbaN2yLaZrYxQn3Zlavu1xdQ9Gkn2bL3ZzDnJOtmaNPqukd5TKrUyfFGEruD8vM/pZSDyJ3ZVUbZOfJTfj6TSZLkIddlJTqp1iHT6yW9UXrZsfCTvZahWqhYqRfw3l8q+zkpT6vItahtEZ6XnQeUb3NujesqG+ycdRP2Ebcs9+NvD0eOW6PwJvqMdn7DDE7Z/wj5K9V8ID0b7eHOvuOKKK674t/EH8QOo1w==:4BE1
^FT74,139^A0N,34,33^FH\^FDMANGO MILK SHAKE^FS
^FT79,189^A0N,28,28^FH\^FDPRODUCTION DATE^FS
^FT79,249^A0N,28,28^FH\^FDEXPIRY DATE^FS
^FT79,317^A0N,28,28^FH\^FD{value}^FS
^FT79,381^A0N,28,28^FH\^FDBOX NO^FS
^FT327,189^A0N,28,28^FH\^FD:^FS
^FT327,249^A0N,28,48^FH\^FD:^FS
^FT327,381^A0N,28,28^FH\^FD:^FS
^FT364,189^A0N,28,28^FH\^FD{pdate}^FS
^FT364,249^A0N,28,28^FH\^FD{edate}^FS
^FT364,381^A0N,28,28^FH\^FD00005^FS
^FT559,323^BQN,2,5
^FH\^FDLA,MANGO MILK SHAKE,PRODUCTION DATE:{pdate},EXPIRY DATE:{edate},ERP.NO:{value},BOX NO:0005^FS
^PQ1,0,1,Y
^XZ



                         """
                    mysocket.send(qr.encode())#using bytes
                    toast("Printed Successfully!!!!!")
                    self.ids.content.text==""

                            

                    mysocket.close () 
                except Exception as e:
                    print(e)
                    toast("Not Connecting or Invalid IP Address")
                    self.ids.content.text==""
        
class Setting(Screen):
    def setip(self):
        cf=ConfigParser()
        cf.read("Config.ini")
        cf["ip"]["ipadd"]=self.ids.ipad.text
        with open('Config.ini', 'w') as configfile:    # save
            cf.write(configfile)
        sm.current="function"
    pass    
sm=ScreenManager()
class MyApp(MDApp):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Window.keboard_anim_args={"d":0.2,"t":"linear"}
        Window.softinput_mode="below_target"

    
    
    def build(self):
        Builder.load_file("design1.kv")
        
        if platform=="android":
            
            Window.maximize()
        else:
            Window.size=(460,720)
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="DeepOrange"
        sm.add_widget(Function(name='function'))
        sm.add_widget(Setting(name='setting'))
    
        
        
        
        
        return sm
if __name__=='__main__':
    MyApp().run()
