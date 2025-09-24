from display import Display
from scenes import SceneManager, StartScene
from wifi import connect_wifi

from utime import sleep


def main():
    wlan = connect_wifi("[Your SSID]", "[Your Password]")
    display = Display()
    manager = SceneManager(display)
    
    startScene = StartScene("Start")
    manager.set_scene(startScene)
    
    speed = 5
    
    while True:
        manager.render()
        dx, dy = 0, 0
        keys = display.listen()
        if 'X' in keys:
            dx -= speed
            dy -= speed
        if 'Y' in keys:
            dx += speed
            dy -= speed
        if 'A' in keys:
            dx -= speed
            dy += speed
        if 'B' in keys:
            dx += speed
            dy += speed
        manager.current_scene.move_camera(dx, dy)
        
        sleep(0.05)

if __name__ == "__main__":
    main()

