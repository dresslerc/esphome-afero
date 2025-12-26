# esphome-afero [![Made for ESPHome](https://img.shields.io/badge/Made_for-ESPHome-black?logo=esphome)](https://esphome.io)  [![Discord](https://img.shields.io/discord/1452835326845517938?logo=discord&logoColor=%23FFFFFF&label=Discord&labelColor=%235865F2&color=%2399AAB5)](https://discord.gg/26tnuHEZm7)

The goal of this project is to enable full local control of Afero/Hubspace devices by replacing the onboard wifi chip with an ESP32 running ESPhome for full local Home Assistant control.

## Testing Device

[Tager 52 in. Smart Indoor/Outdoor Matte Black with Whiskey Barrel Blades Ceiling Fan with Remote Powered by Hubspace](https://www.homedepot.com/p/Home-Decorators-Collection-Tager-52-in-Smart-Indoor-Outdoor-Matte-Black-with-Whiskey-Barrel-Blades-Ceiling-Fan-with-Remote-Powered-by-Hubspace-N383A-MBK-V8/322983364).

<img width="660" height="327" alt="image" src="https://github.com/user-attachments/assets/9f0efa76-8a13-4c45-9fb2-eade184deef4" />

## Receiver Unit
<img width="803" height="1168" alt="image" src="https://github.com/user-attachments/assets/54924b9a-38c1-4311-b8e2-4516c02f1ace" />

## Afero/HubSpace Chip:

Front

<img width="731" height="724" alt="image" src="https://github.com/user-attachments/assets/d103110a-3c96-4864-a218-b4dbf09a101d" />

Back

<img width="646" height="742" alt="image" src="https://github.com/user-attachments/assets/d145e7d8-3826-4721-b912-4064aa6265fb" />

## End Goal:

New Daughter board with ESP32 chip with full local control:
  
<img width="628" height="915" alt="image" src="https://github.com/user-attachments/assets/81a9ff2c-145e-4196-b627-49eab3627efb" />

## Discovery

### Afero Chip to Fan Board Sniffing:
I wanted to see what commands the Afero Wifi Chip sent to the Fan Board when controlling the fan through the HubSpace App.  I left the Afero Chip on the Fan Board and tapped in the RX/TX pins using an ESP32.  Then using the remote_receiver to sniff the commands.

<img width="705" height="850" alt="image" src="https://github.com/user-attachments/assets/7b4b3f58-b835-4d80-977d-674bf70f3441" />

It looks like the Afero Chip sends a "status request" to the Fan board every 1 second.  If I change the fan speed using the phyiscal remote, the Hubspace app updates pretty quick with the new set speed.  I assume this is where this "status request" comes in.

This is a response to the "status request" from the Fan Board:
- 0000 006D 0013 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0011 0003 0011 0003 000D 000F 0009 0003 0025 0003 0025 0003 0025 0003 0025 0003 0025 0003 0021 0007 0005 0003 0005 0003 0005 0003 0009 0180

If a response to the "status request" is not send, then the Afero Chip will not send any new commands from the app to the fan board.

### Afero Wifi Commands to Fan Board
Now that I knew the Afero Wifi chip sends a status request and expects a reply. I built the code below to simulate the "Fan Board" by responding with a payload that I sniffed from the Fan Board (Afero <-> ESP32):

https://github.com/dresslerc/esphome-afero/blob/main/esphome-afero-dev.py

Now when I used the Hubspace app to change the fan speed/mode, the Afero Wifi chip would send the commands found in this link:

https://github.com/dresslerc/esphome-afero/blob/main/fancommands.md

This is what their app looks like:

<img width="332" height="693" alt="image" src="https://github.com/user-attachments/assets/718b0fb6-638e-4fe0-9d46-2fdf4b284652" />

## Inspiration
I have 1 of these HubSpace Ceiling Fans from Home Depot.  I've been using Home Assistant extensively in my home for the last 5 years (since COVID) and want all devices I buy to have local control (no cloud dependencies).

I saw this project, but it requires the "cloud":

https://github.com/jdeath/Hubspace-Homeassistant

This is why I am attemping to reverse engineer the communication between the Afero Chip and the Fan Board.  I am by no means an expert on this topic; I am sure there are much more elegant ways of doing this... But baby steps :)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=dresslerc/esphome-afero&type=date&legend=top-left)](https://www.star-history.com/#dresslerc/esphome-afero&type=date&legend=top-left)


