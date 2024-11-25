#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  Joueur
#  Created by Ingenuity i/o on 2024/11/05
#

import sys
import ingescape as igs
from src.Joueur import Joueur

joueur = Joueur()

def attribute_callback(io_type, name, value_type, value, my_data):
    pass
    # add code here if needed
def demanderPioche_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.demanderPioche(sender_agent_name,sender_agent_uuid)

def jouerTour_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.jouerTour()

def finTour_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.finTour()
    
def input_carte_callback(io_type, name, value_type, value, my_data):
    print("Vous avez tiré",value.split("|")[0])  
    joueur.ajouterMain(value)

def rester_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.rester()

def donnerScore_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.donnerScore()

def reinitialiser_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    joueur.reinitialiser()
    
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

    igs.attribute_create("hand", igs.DATA_T, None)

    igs.output_create("action", igs.STRING_T, None)

    igs.output_create("score", igs.INTEGER_T, None)

    igs.input_create("carte",igs.STRING_T,None)
    igs.observe_input("carte",input_carte_callback,None)

    igs.observe_attribute("hand", attribute_callback, None)

    igs.service_init("demanderPioche", demanderPioche_callback, None)

    igs.service_init("jouerTour", jouerTour_callback, None)

    igs.service_init("finTour", finTour_callback, None)

    igs.service_init("rester", rester_callback, None)

    igs.service_init("donnerScore", donnerScore_callback, None)

    igs.service_init("reinitialiser", reinitialiser_callback,None)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()

