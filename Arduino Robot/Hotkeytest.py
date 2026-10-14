import keyboard

def my_function():
    print("The 'w' key was pressed! Function executed.")

def StopFunc(event):
    # Only run the code if the released key name is 'w'
    if event.name == 'w':
        print("Stopped")

# Trigger 'my_function' instantly when 'w' is pressed
keyboard.add_hotkey('w', my_function)

# Pass the callback directly; keyboard will pass a KeyboardEvent to it
keyboard.on_release(StopFunc)

print("Program is running. Press 'w' to trigger the function.")
print("Press 'esc' to close the program.")

# Keep the script running in the background until you press Escape
keyboard.wait('esc')
