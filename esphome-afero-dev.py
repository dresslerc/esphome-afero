esphome:
  name: seedesp32
  friendly_name: seedesp32

esp32:
  board: esp32-c6-devkitc-1
  framework:
    type: esp-idf

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "L7AsGLc+U1CG8jgn2JkDufr5FsCNpToLHN4NhJblI/U="

ota:
  - platform: esphome
    password: "bf607b7642e44e91d944714210e08235"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Seedesp32 Fallback Hotspot"
    password: "FZ93zPNX2Nmf"

web_server:
  port: 80

status_led:
  pin: GPIO15

remote_receiver:
  pin: 
    number: GPIO02
    inverted: false
  dump: all
  
  on_raw:
     then:
        - remote_transmitter.transmit_pronto:
            data: "0000 006D 0013 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0011 0003 0011 0003 000D 000F 0009 0003 0025 0003 0025 0003 0025 0003 0025 0003 0025 0003 0021 0007 0005 0003 0005 0003 0005 0003 0009 0180"

remote_transmitter:
  pin: 
    number: GPIO01
    inverted: true
  carrier_duty_percent: 100%

button:
  # Works - Requests current status from controller board (main)
  - platform: template
    name: "Request Controller Status"
    on_press:
      then:
        - remote_transmitter.transmit_pronto:
            data: "0000 006D 0009 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0025 0003 0005 0003 0011 0003 0009 0180"

  # Buttons below do not work
  - platform: template
    name: "Fan Up - Speed 1"
    on_press:
      then:
        - remote_transmitter.transmit_pronto:
            data: "0000 006D 0013 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0011 0003 0011 0003 000D 0003 0005 0003 000D 0003 0025 0003 0025 0003 0025 0003 0025 0003 0025 0003 0021 0007 0005 0003 0005 000F 0005 0180"

  - platform: template
    name: "Fan Up - Speed 5"
    on_press:
      then:
        - remote_transmitter.transmit_pronto:
            data: "0000 006D 0013 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0011 0003 0011 0003 000D 000F 0009 0003 0025 0003 0025 0003 0025 0003 0025 0003 0025 0003 0021 0007 0005 0003 0005 0003 0005 0003 0009 0180"

  - platform: template
    name: "Fan Up - Speed 9"
    on_press:
      then:
        - remote_transmitter.transmit_pronto:
            data: "0000 006D 0013 0000 0019 0003 0009 0003 0005 0003 001D 0003 0025 0003 0011 0003 0011 0003 000D 0003 0009 0007 0005 0003 0025 0003 0025 0003 0025 0003 0025 0003 0025 0003 0021 0007 0005 0003 0005 0007 0009 0180"
