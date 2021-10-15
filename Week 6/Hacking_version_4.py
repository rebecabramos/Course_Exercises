# Hacking version 4
# This is a graphical password guessing game that displays a
# list of possible computer passwords. the player is allowed
# 4 attempt to guess the password, when the player only has 1 try a lock message will appear.
# The game indicates whether the player guessed the password successfully or not.

from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')
    
# display header
line_x = 0
line_y = 0
pause_time = 0.3
string_height = window.get_font_height()

header = ['DEBUG MODE', '1 ATTEMPT(S) LEFT', '']
for header_line in header:
    # display header line
    window.draw_string(header_line, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height    
    
# display password list
#   create password list 
password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 
                 'SURVIVE', 'HEARING','HUNTING', 'REALIZE', 'NOTHING', 
                 'OVERLAP', 'FINDING', 'PUTTING', '']

for password_line in password_list:
    # display password list
    window.draw_string(password_line, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height

# prompt for guess
guess = window.input_string('ENTER PASSWORD >', 0, line_y)
       
# end game
#   clear window
window.clear()
    
#   create outcome
if guess == 'HUNTING':
    # create success
    outcome_line2 = 'EXITING DEBUG MODE'
    outcome_line3 = 'LOGIN SUCCESSFUL - WELCOME BACK'
    prompt = 'PRESS ENTER TO CONTINUE'
else:
    # create failure
    outcome_line2 = 'LOGIN FAILURE - TERMINAL LOCKED'
    outcome_line3 = 'PLEASE CONTACT AN ADMINISTRATOR'
    prompt = 'PRESS ENTER TO EXIT'
        
#   display outcome
#      display guess
#         compute x coordinate
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2

#         compute y coordinate
outcome_height = 7*string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

window.draw_string(guess, line_x, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height   
    
#      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height

#      display outcome line 2
#         compute x coordinate
x_space = window.get_width() - window.get_string_width(outcome_line2)
line_x = x_space // 2
window.draw_string(outcome_line2, line_x, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height   

#      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height

#      display outcome line 3
#         compute x coordinate
x_space = window.get_width() - window.get_string_width(outcome_line3)
line_x = x_space // 2
window.draw_string(outcome_line3, line_x, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height   
    
#      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(pause_time)
line_y = line_y + string_height

#   prompt for end
#      compute x coordinate
x_space = window.get_width() - window.get_string_width(prompt)
line_x = x_space // 2
window.input_string(prompt, line_x, line_y)

#   close window
window.close()