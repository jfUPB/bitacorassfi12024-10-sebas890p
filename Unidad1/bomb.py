from microbit import display, button_a, button_b, pin_logo, sleep 
import music

# Definiciones de pines
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
disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'UP']
entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Función para manejar la lógica de la bomba 
def bomb_logic():
    global current_state, countdown_timer, entered_code

    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_touched():
            current_state = BombStates.ARMED
            entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]
            update_display()  
    elif current_state == BombStates.ARMED:
        if countdown_timer > 0:
            sleep(1000)
            countdown_timer -= 1
            update_display()

        if ARM_BTN.is_touched():
            entered_code.append('ARM')
            if len(entered_code) == 7:
                if entered_code == disarm_code:
                    current_state = BombStates.DISARMED
                else:
                    current_state = BombStates.EXPLODED
            sleep(500)  
            update_display()  
        elif countdown_timer == 0:
            current_state = BombStates.EXPLODED
            music.play(music.BA_DING)
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
