#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  Pioche
#  Created by Ingenuity i/o on 2024/11/05
#

import sys
import ingescape as igs
from src.Pioche import Pioche

pio = Pioche()

def attribute_callback(io_type, name, value_type, value, my_data):
    pass
    # add code here if needed

def service_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    pass

def tirerCarte_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    

    carte = pio.Tirercarte(sender_agent_name,sender_agent_uuid)
    if(sender_agent_name=="J1"):
        igs.output_set_string("carteJ1",carte+"|J1")
        igs.output_set_string("carte","Joueur 1 a tiré " +carte)
    elif(sender_agent_name=="J2"):
        igs.output_set_string("carteJ2",carte+"|J2")
        igs.output_set_string("carte","Joueur 2 a tiré " +carte)
    
def reinitialiser_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    pio.reinitialiser()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: python3 main.py agent_name network_device port")
        devices = igs.net_devices_list()
        print("Please restart with one of these devices as network_device argument:")
        for device in devices:
            print(f" {device}")
        exit(0)

    igs.agent_set_name(sys.argv[1])
    igs.log_set_console(True)
    igs.log_set_file(True, None)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    igs.debug(f"Ingescape version: {igs.version()} (protocol v{igs.protocol()})")

    igs.attribute_create("cartes", igs.DATA_T, None)

    igs.output_create("carte", igs.STRING_T, None)
    igs.output_create("carteJ1", igs.STRING_T, None)
    igs.output_create("carteJ2", igs.STRING_T, None)

    igs.observe_attribute("cartes", attribute_callback, None)

    igs.service_init("tirerCarte", tirerCarte_callback, None)
    igs.service_init("donnerMain", service_callback, None)
    igs.service_init("reinitialiser", reinitialiser_callback, None)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()