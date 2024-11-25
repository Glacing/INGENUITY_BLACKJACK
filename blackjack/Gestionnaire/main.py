#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  Gestionnaire
#  Created by Ingenuity i/o on 2024/11/21
#

import sys
import ingescape as igs
from src.Gestionnaire import Gestionnaire

gestionnaire = Gestionnaire()

def service_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    pass
    # add code here if needed

def lancerPartie_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    gestionnaire.Lancerpartie()

def finTourJoueur_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    gestionnaire.finTourJoueur(sender_agent_name)

def defaiteJoueur_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    gestionnaire.defaiteJoueur(sender_agent_name)

def joueurRester_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    gestionnaire.joueurRester(sender_agent_name)

def input_scoreJ1_callback(io_type, name, value_type, value, my_data): 
    gestionnaire.setScoreJ1(value)

def input_scoreJ2_callback(io_type, name, value_type, value, my_data): 
    gestionnaire.setScoreJ2(value)

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

    igs.input_create("scoreJ1",igs.STRING_T,None)
    igs.observe_input("scoreJ1",input_scoreJ1_callback,None)

    igs.input_create("scoreJ2",igs.STRING_T,None)
    igs.observe_input("scoreJ2",input_scoreJ2_callback,None)

    igs.output_create("whiteboardOutput", igs.STRING_T, None)
    igs.output_create("whiteboardChat", igs.STRING_T, None)
    igs.output_create("whiteboardColor", igs.STRING_T, None)
    igs.output_create("clear", igs.IMPULSION_T, None)

    igs.service_init("lancerPartie", lancerPartie_callback, None)
    igs.service_init("donnerMain", service_callback, None)
    igs.service_init("finTourJoueur", finTourJoueur_callback,None)
    igs.service_init("defaiteJoueur", defaiteJoueur_callback,None)
    igs.service_init("joueurRester", joueurRester_callback,None)
    
    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()

