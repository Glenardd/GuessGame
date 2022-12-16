import random
import PySimpleGUI as sg

#theme
sg.theme('DarkBlue')

#layout of the GUI
layout = [
    [sg.Text('INPUT GUESSED NUMBER HERE:', key='-GUIDE_TEXT-')],
    [sg.Input(key='-ANSWER-', visible=True), sg.Text('...',visible=False ,key='-DISABLED_ANSWER_ELEMENT-')],
    [sg.Text('MESSAGE POPS HERE',visible=True ,key='-MESSAGE-')],
    [sg.Button('OK',visible=True, key='-SUBMIT-'), sg.Button('Retry', visible=False, key='-RETRY-')],
    [sg.Text('....',visible=True,key='-progress_msg-'),sg.ProgressBar(3, orientation='h', size=(24,15),visible=False ,key='-progress-')]
]

# windows mainloop gui
window = sg.Window('Guessing Game', layout)

# The input is only limited by three
counter = 0

#store congratulations string
congrats_msg = ''

#store lose string
lose_message = ''

#use this function to return message
def msg():
    global congrats_msg
    congrats_msg = 'You guessed it right!'
    return congrats_msg

# lose message
def lose_msg():
    global lose_message
    lose_message = "Sorry try again"
    return lose_message

# generates random integer
random_int = random.randint(1,10)

while True:

    event, values = window.read()
    # print(event)

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-SUBMIT-':
        val = values['-ANSWER-']
        if val == '':
            window['-MESSAGE-'].update('NO NUMBER IS INPUTTED')
            
            # #console print only if no input is found
            # print('EMPTY INPUT')

            # subtract so the progressbar wont show or add up
            counter-=1
        else:
            try:
                val_ = int(val)

                if val_ == random_int:
                    window['-MESSAGE-'].update(msg())
                    window['-RETRY-'].update(visible=True)
                    window['-SUBMIT-'].update(visible=False)
                    
                elif val_ < random_int:
                    window['-MESSAGE-'].update('Higher')
            
                elif val_ > random_int:
                    window['-MESSAGE-'].update('Lower')
            except:
                # subtract so the progressbar wont show or add up
                counter-=1
                window['-MESSAGE-'].update('NOT A NUMBER')

        # shows the picked random number
        # print('random number: {VAL}'.format(VAL=random_int))

    #will add as long the loop exist
    counter +=1
    window['-progress-'].update(counter)

    # console print only for showing counter 
    # print(counter)
    
    # progress bar will show up if counter has 1 value or more
    if counter >= 1:
        window['-progress-'].update(visible=True)
        window['-progress_msg-'].update(visible=False) 
    # three guesses are only allowed, so we limit the submissions
    if counter == 3:
        window['-RETRY-'].update(visible=True)
        window['-SUBMIT-'].update(visible=False)

        window['-MESSAGE-'].update(lose_msg())
        window['-ANSWER-'].update(visible=False)

        window['-DISABLED_ANSWER_ELEMENT-'].update(visible=True)

    #retry or restart
    if event == '-RETRY-':
        window['-progress-'].update(visible=False)
        window['-progress_msg-'].update(visible=True) 
        #counter will reset
        counter = 0
        
        # if retry key exist it will randomize, only if retry key exist
        # hence this will generate another random number
        random_int = random.randint(1,10)
        window['-RETRY-'].update(visible=False)
        window['-SUBMIT-'].update(visible=True)

        # back to zero progress bar if retry
        window['-progress-'].update(0)
        window['-MESSAGE-'].update('MESSAGE POPS HERE')
        window['-ANSWER-'].update(visible=True)
        window['-DISABLED_ANSWER_ELEMENT-'].update(visible=False)

        # print('back to zero')

        






