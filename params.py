import numpy as np

dias_evaluacion = 120
dt=.01
periodo_evaluacion = np.arange(0,dias_evaluacion+dt,dt) # Mejora en resolución por github: friverap

alpha = 0.2
beta = 1.75
gamma = 0.5
parametros = alpha, beta, gamma

#Condiciones iniciales de la ZMG
JAL_Population = 8000000 
I_o = 32 / JAL_Population  # Tenemos 32 casos
E_o = (32*4)/ JAL_Population # Asumimos 4 expuestos por caso
S_o = (1) - (E_o+I_o) # El resto somos suceptibles
R_o = 0 # NO hay ningun recuperado

Condiciones_Iniciales = S_o,E_o,I_o,R_o