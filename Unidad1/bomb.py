
####Codigo con el serial incorporado 



from microbit import display, button_a, button_b, pin_logo, sleep 
import music
from microbit import *

uart.init(baudrate=115200)
# Definiciones de botones
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = pin_logo

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
entered_code = []

def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Función para verificar si la clave ingresada coincide con la clave de desarme
def check_disarm_code():
    global entered_code
    disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'ARMED']
    return entered_code == disarm_code

def bomb_logic():
    global current_state, countdown_timer, entered_code

    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            uart.write('Tiempo aumentado en 1 segundo\n')
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            uart.write('Tiempo disminuido en 1 segundo\n')
            if countdown_timer > 10:
                countdown_timer -= 1                
            update_display()
        elif ARM_BTN.is_touched():
            uart.write('Bomba armada\n')
            current_state = BombStates.ARMED
            update_display()  
            
    elif current_state == BombStates.ARMED:
        if countdown_timer > 0:
            sleep(1000)
            countdown_timer -= 1
            uart.write('Tiempo restante: {}\n'.format(countdown_timer))
            update_display()
        if countdown_timer == 10:
            uart.write('Quedan 10 segundos\n')
        
        if ARM_BTN.is_touched():
            entered_code.append('ARMED')
            if len(entered_code) == 7:  
                if check_disarm_code():
                    uart.write('Bomba desarmada\n')
                    current_state = BombStates.DISARMED
                else:
                    uart.write('Código incorrecto. BOOMMM\n')
                    current_state = BombStates.EXPLODED
                sleep(500)
                update_display()
        elif countdown_timer == 0:
            current_state = BombStates.EXPLODED
            music.play(music.BA_DING)
            uart.write('BOOMMMMM!\n')
            update_display()  

    elif current_state == BombStates.EXPLODED:
        LED_COUNT.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

    elif current_state == BombStates.DISARMED:
        LED_COUNT.show("D")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

# Bucle principal
while True:
    bomb_logic()
