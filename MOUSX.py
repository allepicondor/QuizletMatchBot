from pynput.mouse import Button, Controller
mouse = Controller()
while True:
    print(mouse.position)
    mouse.position = (20,76)
    