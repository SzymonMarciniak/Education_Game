from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty, StringProperty, NumericProperty
import cv2
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import numpy as np
from kivy.clock import Clock
from multiprocessing import Process
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

global refresh_time, cam_id, turn_off
refresh_time = 3
cam_id = None
turn_off = True
first_time = True
my_cam = None


class MainScreen(BoxLayout):
    available_cam_list = ListProperty(["0", "1", "2", "3", "4"])
    camera_view_parent = ObjectProperty()
    my_img = StringProperty("images/no_camera.jpg")
    left_val = NumericProperty(1)
    right_val = NumericProperty(1)
    top_val = NumericProperty(1)
    bottom_val = NumericProperty(2)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.procent_left_val = 0
        self.procent_right_val = 0
        self.procent_top_val = 0
        self.procent_bottom_val = 0
        
    def search_cameras(self):
        self.available_cam_list = CameraView.check_available_cameras()
    
    def choose_camera(self, choose):
        global turn_off, cam_id, first_time, my_cam
        cam_id = choose
        if first_time:
            cam = CameraView()
            p1 = Process(target=Clock.schedule_interval(cam.cam_display, refresh_time))
            Clock.schedule_interval(self.refresh_image, refresh_time)
            p1.start()
            my_cam = self.ids.my_cam
            first_time = not first_time

        if choose != "Turn off":
            turn_off = False
        else:
            turn_off = True
            
    def refresh_image(self, *args):
        if not turn_off:
            img = cv2.imread("CurrentVideo.png")
            img = cv2.resize(img, [int(self.ids.my_cam.size[0]), int(self.ids.my_cam.size[1])], interpolation = cv2.INTER_AREA )
            buffer = img.tobytes()
            texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.my_cam.texture = texture
        else: 
            my_cam.source = "images/no_camera.jpg"

    @staticmethod
    def calcualte_value(val):
        return 1 + int(val) / 100
    
    def print_values(self):
        print(f"Left: {self.procent_left_val}\nRight: {self.procent_right_val}\nTop: {self.procent_bottom_val}\nBottom: {self.procent_top_val}")
    
    def change_left_image_area(self, *args):
        self.left_val = self.calcualte_value(args[1])
        self.procent_left_val = (self.left_val - 1) * .45
        self.print_values()
        
    def change_right_image_area(self, *args):
        self.right_val = self.calcualte_value(100 - args[1])
        self.procent_right_val = (self.right_val - 1) * .45
        self.print_values()

    def change_top_image_area(self, *args):
        self.top_val = self.calcualte_value(args[1])
        self.procent_top_val = (self.top_val - 1) * .45
        self.print_values()
    
    def change_bottom_image_area(self, *args):
        self.bottom_val = self.calcualte_value(args[1])
        self.procent_bottom_val = (2 - self.bottom_val) * .45
        self.print_values()
        
    
    def save_and_exit(self):
        App.get_running_app().stop()

       
class CameraView(Image):   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    def check_available_cameras():
        cam_list = ["Turn off"]
        for i in range(0, 4):
            cap = cv2.VideoCapture(i)
            if cap is None or not cap.isOpened():
                pass
            else:
                cam_list.append(str(i))
        return cam_list
    
    def cam_display(self, *args):
        if not turn_off:
            cap = cv2.VideoCapture(int(cam_id))
            success, img= cap.read()
            img = np.array(img)
            img = np.rot90(img, 2)
            if success:
                cv2.imwrite("CurrentVideo.png",img)
        

class CameraSetup(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (1000, 750)

    def build(self):
        return MainScreen()


if __name__ == "__main__":
    p2 = Process(target=CameraSetup().run())
    p2.start()

    
    
   