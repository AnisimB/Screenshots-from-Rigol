#! /usr/bin/env python3
import pyvisa
import keyboard
import time
from io import BytesIO
import win32clipboard
from PIL import Image

rigol_device = None

def send_to_clipboard(png_filename):
    image = Image.open(png_filename)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def make_screenshoot():
    if rigol_device == None:
        return
    buf = rigol_device.query_binary_values(':DISP:DATA? ON,0,BMP', datatype='B', chunk_size=1152054)
    #filename = "Rigol_{}.bmp".format(name.split("::")[3])
    filename = "Rigol.bmp"
    with open(filename, 'wb') as f:
        f.write(bytearray(buf))
        f.flush() 
    send_to_clipboard("Rigol.bmp")
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")

def app_exit():
    print("exit")
    exit()
    
def main():
    global rigol_device
    # Get list of connected Rigol devices
    rm = pyvisa.ResourceManager()
    exit_flag = False
    while True:
        for device_name in rm.list_resources():
            print("found device: " + device_name)
            device_id = ""
            try:
                device_id = rm.open_resource(device_name).query("*IDN?")
                #print(device_id)
            except pyvisa.VisaIOError:
                print("connect your Rigol oscilloscope via usb...")
                time.sleep(0.5)
            if device_id.lower().startswith("rigol"):
                rigol_device = rm.open_resource(device_name)
                #print(rigol_device)
                print("Rigol oscilloscope found! You can press Ctrl + Shift + F12 to paste screenshoot")
                exit_flag = True
                break
        if exit_flag:
            break
        

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit()
        
if __name__ == "__main__":
    keyboard.add_hotkey("ctrl+shift+f12", lambda: make_screenshoot())
    print("Rigol oscilloscope automatic screenshoot maker. Press Ctrl + C to exit")
    main()