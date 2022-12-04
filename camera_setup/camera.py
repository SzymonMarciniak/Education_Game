from kivy import Config
from kivy.app import App
from kivy.core.window import Window
# from iconfonts import iconfonts
from kivy.properties import ListProperty, ObjectProperty
import cv2
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import numpy as np
from kivy.clock import Clock
from multiprocessing import Process
import time
from kivy.core.window import Window
from kivy.config import Config


from kivy.uix.boxlayout import BoxLayout

global ch_time
ch_time = 3

Config.set('graphics','resizable', False)


class MainScreen(BoxLayout):
    available_cam_list = ListProperty(["0", "1", "2", "3", "4"])
    camera_view_parent = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.refresh_image, ch_time)
    
    def search_cameras(self):
        self.available_cam_list = CameraView.check_available_cameras()
    
    def choose_camera(self, choose):
        self.choose = choose
    
    def refresh_image(self, *args):
        t0 = time.time()
        img = cv2.imread("CurrentVideo.png")
        img = cv2.resize(img, [int(self.ids.my_cam.size[0]), int(self.ids.my_cam.size[1])], interpolation = cv2.INTER_AREA )
        buffer = img.tobytes()
        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.ids.my_cam.texture = texture
        print(self.ids.my_cam.size, img.shape[1], img.shape[0])
        t1 = time.time() 
        print("Time elapsed: ", t1 - t0)
    
    def save_and_exit(self):
        App.get_running_app().stop()

       
        
class CameraView(Image):   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    def check_available_cameras():
        cam_list = []
        for i in range(0, 4):
            cap = cv2.VideoCapture(i)
            if cap is None or not cap.isOpened():
                pass
            else:
                cam_list.append(str(i))
        return cam_list
    
    def cam_display(*args):
        print("0000")
        cap = cv2.VideoCapture(0)
        success, img= cap.read()
        img = np.array(img)
        img = np.rot90(img, 2)
        if success:
            print("3333333")
            cv2.imwrite("CurrentVideo.png",img)
    

class CameraSetup(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (1000, 750)

    def build(self):
        return MainScreen()


if __name__ == "__main__":
    cam = CameraView()
    p1 = Process(target=Clock.schedule_interval(cam.cam_display, ch_time))
    p1.start()
    
    p2 = Process(target=CameraSetup().run())
    p2.start()

    
    
   