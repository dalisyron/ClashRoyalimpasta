import time
import pygame
import sys
from pygame.locals import *

class InputEvent:
    def __init__(self, key, down):
        self.key = key
        self.down = down
        self.up = not down

class InputManager:
    def __init__(self):
        self.init_joystick()
        self.buttons = ['start', 'down', 'right', 'up', 'left', 'A']
        self.key_map = {
            K_UP : 'up',
            K_DOWN : 'down',
            K_LEFT : 'left',
            K_RIGHT : 'right',
            K_RETURN : 'start',
            K_a : 'A',
            K_b : 'B',
            K_x : 'X',
            K_y : 'Y',
            K_l : 'L',
            K_r : 'R'
        }
        self.keys_pressed = {}
        for button in self.buttons:
            self.keys_pressed[button] = False
        self.joystick_config = {}
        self.quit_attempt = False
    
    def is_pressed(self, button):
        return self.keys_pressed[button]
    def get_events(self):
        events = []
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.quit_attempt = True
            if event.type == KEYDOWN or event.type == KEYUP:
                key_pushed_down = event.type == KEYDOWN
                button = self.key_map.get(event.key)
                if button != None:
                    events.append(InputEvent(button, key_pushed_down))
                    self.keys_pressed[button] = key_pushed_down
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None:
                if config[0] == 'is_button':
                    pushed = self.joystick.get_button(config[1])
                    if pushed != self.keys_pressed[button]:
                        events.append(InputEvent(button, pushed))
                        self.keys_pressed[button] = pushed
                elif config[0] == 'is_hat':
                    status = self.joystick.get_hat(config[1])
                    if config[2] == 'x':
                        amount = status[0]
                    else:
                        amount = status[1]
                    pushed = amount == config[3]
                    if pushed != self.keys_pressed[button]:
                        events.append(InputEvent(button, pushed))
                        self.keys_pressed[button] = pushed
                elif config[0] == 'is_ball':
                    status = self.joystick.get_ball(config[1])
                    if config[2] == 'x':
                        amount = status[0]
                    else:
                        amount = status[1]
                    if config[3] == 1:
                        pushed = amount > 0.5
                    else:
                        pushed = amount < -0.5
                    if pushed != self.keys_pressed[button]:
                        events.append(InputEvent(button, pushed))
                        self.keys_pressed[button] = pushed
                elif config[0] == 'is_axis':
                    status = self.joystick.get_axis(config[1])
                    if config[2] == 1:
                        pushed = status > 0.5
                    else:
                        pushed = status < -0.5
                    if pushed != self.keys_pressed[button]:
                        events.append(InputEvent(button, pushed))
                        self.keys_pressed[button] = pushed
        return events        
    def configure_button(self, button):
        js = self.joystick
        for button_index in range(js.get_numbuttons()):
            button_pushed = js.get_button(button_index)
            if button_pushed and not self.is_button_used(button_index):
                self.joystick_config[button] = ('is_button', button_index)
                return True
        for hat_index in range(js.get_numhats()):
            hat_status = js.get_hat(hat_index)
            if hat_status[0] < -.5 and not self.is_hat_used(hat_index, 'x', -1):
                self.joystick_config[button] = ('is_hat', hat_index, 'x', -1)
                return True
            elif hat_status[0] > .5 and not self.is_hat_used(hat_index, 'x', 1):
                self.joystick_config[button] = ('is_hat', hat_index, 'x', 1)
                return True
            if hat_status[1] < -.5 and not self.is_hat_used(hat_index, 'y', -1):
                self.joystick_config[button] = ('is_hat', hat_index, 'y', -1)
                return True
            elif hat_status[1] > .5 and not self.is_hat_used(hat_index, 'y', 1):
                self.joystick_config[button] = ('is_hat', hat_index, 'y', 1)
                return True
        for ball_index in range(js.get_numballs()):
            ball_status = js.get_ball(ball_index)
            if ball_status[0] < -.5 and not self.is_ball_used(ball_index, 'x', -1):
                self.joystick_config[button] = ('is_ball', ball_index, 'x', -1)
                return True
            elif ball_status[0] > .5 and not self.is_ball_used(ball_index, 'x', 1):
                self.joystick_config[button] = ('is_ball', ball_index, 'x', 1)
                return True
            if ball_status[1] < -.5 and not self.is_ball_used(ball_index, 'y', -1):
                self.joystick_config[button] = ('is_ball', ball_index, 'y', -1)
                return True
            elif ball_status[1] > .5 and not self.is_ball_used(ball_index, 'y', 1):
                self.joystick_config[button] = ('is_ball', ball_index, 'y', 1)
                return True
        for axis_index in range(js.get_numaxes()):
            axis_status = js.get_axis(axis_index)
            if axis_status < -.5 and not self.is_axis_used(axis_index, -1):
                self.joystick_config[button] = ('is_axis', axis_index, -1)
                return True
            elif axis_status > .5 and not self.is_axis_used(axis_index, 1):
                self.joystick_config[button] = ('is_axis', axis_index, 1)
                return True
        return False
    def is_button_used(self, button_index):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_button' and config[1] == button_index:
                return True
        return False
    def is_hat_used(self, hat_index, axis, direction):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_hat':
                if config[1] == hat_index and config[2] == axis and config[3] == direction:
                    return True
        return False
    def is_ball_used(self, ball_index, axis, direction):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_ball':
                if config[1] == ball_index and config[2] == axis and config[3] == direction:
                    return True
        return False
    def is_axis_used(self, axis_index, direction):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_axis':
                if config[1] == axis_index and config[2] == direction:
                    return True
        return False
    def init_joystick(self):
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        self.joystick = joystick
        self.joystick_name = joystick.get_name()

class Player:
    def __init__(self):
        self.x = 320
        self.y = 240
        self.speed = 4
    def move_left(self):
        self.x -= self.speed
    def move_right(self):
        self.x += self.speed
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
flag = True
input_managerss = None

pygame.init()
num_joysticks = pygame.joystick.get_count()
if num_joysticks < 1:
    print("You didn't plug in a joystick. FORSHAME!")
    flag = False

if (flag):
    input_managerss = InputManager()

def main():
    if (not flag):
        return
    fps = 30
    print("Plug in a USB gamepad. Do it! Do it now! Press enter after you have done this.")
    wait_for_enter()
    screen = pygame.display.set_mode((640, 480))
    button_index = 0
    player = Player()
    while not input_managerss.quit_attempt:
        start = time.time()
        screen.fill((0,0,0))
        is_configured = button_index >= len(input_managerss.buttons)
        if not is_configured:
            success = configure_phase(screen, input_managerss.buttons[button_index], input_managerss)
            if success:
                button_index += 1
        else:
            pygame.display.quit()
            break
        pygame.display.flip()
        difference = start - time.time()
        delay = 1.0 / fps - difference
        if delay > 0:
            time.sleep(delay)

def configure_phase(screen, button, input_manager):
    input_manager.get_events() 
    success = input_manager.configure_button(button)
    write_text(screen, "Press the " + button + " button", 100, 100)
    return success

def getPressedKey(input_manager = input_managerss):
    for event in input_manager.get_events():
        if event.key == 'A' and event.down:
            pass # weeeeeeee 
        if event.key == 'X' and event.up:
            input_manager.quit_attempted = True
    if input_manager.is_pressed('left'):
        return 'left'
    elif input_manager.is_pressed('right'):
        return 'right'
    elif input_manager.is_pressed('up'):
        return 'up'
    elif input_manager.is_pressed('down'):
        return 'down'
    elif input_manager.is_pressed('A'):
        return 'A'
    else:
        return None

def wait_for_enter():
    try: input()
    except: pass
cached_text = {}
cached_font = None
def write_text(screen, text, x, y):
    global cached_text, cached_font
    image = cached_text.get(text)
    if image == None:
        if cached_font == None:
            cached_font = pygame.font.Font(pygame.font.get_default_font(), 12)
        image = cached_font.render(text, True, (255, 255, 255))
        cached_text[text] = image
    screen.blit(image, (x, y - image.get_height()))