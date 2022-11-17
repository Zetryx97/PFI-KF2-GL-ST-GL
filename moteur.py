#Gabriel Lessard - Samy Tétrault
#PFI KF2

import gpio
from time import sleep

class Moteur :
    def __init__(self):
        self.moteur_avg = gpio.DigitalOutputDevice(6) #roue avant gauche
        self.moteur_arg = gpio.DigitalOutputDevice(5) #roue arrière gauche

        self.moteur_avd = gpio.DigitalOutputDevice(15) #roue avant droite
        self.moteur_ard = gpio.DigitalOutputDevice(14) #roue arrière droite

        self.control_moteur_g = gpio.PWMOutputDevice(13) #permet d'allumer ou d'éteindre les 2 moteurs de gauche
        self.control_moteur_d = gpio.PWMOutputDevice(18) #permet d'allumer ou d'éteindre les 2 moteur de droite
    
    def avancer(self,speed):
        self.moteur_avg.on()
        self.moteur_arg.off()
        self.control_moteur_g.on()
        self.moteur_avd.on()
        self.moteur_ard.off()
        self.control_moteur_d.on()

        self.control_moteur_g.value = speed
        self.control_moteur_d.value = speed

    def reculer(self,speed):
        self.moteur_avg.off()
        self.moteur_arg.on()
        self.control_moteur_g.on()
        self.moteur_avd.off()
        self.moteur_ard.on()
        self.control_moteur_d.on()

        self.control_moteur_g.value = speed
        self.control_moteur_d.value = speed

    def tourner_droite(self,speed):
        self.moteur_avg.on()
        self.moteur_arg.off()
        self.control_moteur_g.on()
        self.moteur_avd.off()
        self.moteur_ard.on()
        self.control_moteur_d.on()

        self.control_moteur_g.value = speed
        self.control_moteur_d.value = speed

    def tourner_gauche(self,speed):
        self.moteur_avg.off()
        self.moteur_arg.on()
        self.control_moteur_g.on()
        self.moteur_avd.on()
        self.moteur_ard.off()
        self.control_moteur_d.on()

        self.control_moteur_g.value = speed
        self.control_moteur_d.value = speed

    def freiner(self):
        self.moteur_avg.on()
        self.moteur_arg.on()
        self.control_moteur_g.on()
        self.moteur_avd.on()
        self.moteur_ard.on()
        self.control_moteur_d.on()

    def arreter(self):
        self.moteur_avg.off()
        self.moteur_arg.off()
        self.control_moteur_g.off()
        self.moteur_avd.off()
        self.moteur_ard.off()
        self.control_moteur_d.off()