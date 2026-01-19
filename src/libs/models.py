# Models
import numpy as np

#----------------------------------------------------------------------------

# Normal-Metal Current
def current_NM(i, R_NM, R_I, R_S):
    '''
    Compute the normal-metal current.

    Input:
    -    i (float): Total Current
    - R_NM (float): Normal-Metal Resistance
    -  R_I (float): Interface Resistance
    -  R_S (float): Superconductor Resistance

    Output:
    -    I (float): Current
    '''

    I = ((R_I + R_S) / (R_NM + R_I + R_S)) * i
    
    return I 

#----------------------------------------------------------------------------

# Interface-Superconductor Current
def current_IS(i, R_NM, R_I, R_S):
    '''
    Compute the interface-superconductor current.

    Input:
    -    i (float): Total Current
    - R_NM (float): Normal-Metal Resistance
    -  R_I (float): Interface Resistance
    -  R_S (float): Superconductor Resistance

    Output:
    -    I (float): Current
    '''
    
    I = (R_NM / (R_NM + R_I + R_S)) * i     

    return I
    
#----------------------------------------------------------------------------

# Normal-Metal Resistance 
def resistance_NM(T, R0_NM, α_NM):
    '''
    Compute the normal-metal resistance as a function of temperature.

    Input: 
    -     T (float): Temperature
    - R0_NM (float): Normal-Metal Resistance
    -  α_NM (float): Normal-Metal Linear Coefficient

    Output:
    -     R (float): Resistance
    '''
    
    R = R0_NM * (1.0 + α_NM * T)
    
    return R

#----------------------------------------------------------------------------

# Interface Resistance 
def resistance_I(T, R0_I, TC_I, ΔT_I):
    '''
    Compute the interface resistance as a function of temperature.

    Input: 
    -    T (float): Temperature
    - R0_I (float): Interface Resistance
    - TC_I (float): Interface Critical Temperature
    - ΔT_I (float): Interface Delta Temperature

    Output:
    -    R (float): Resistance
    '''
    
    R = 0.5 * R0_I * (1.0 + np.tanh((T - TC_I) / ΔT_I))
    
    return R

#----------------------------------------------------------------------------

# Superconductor Resistance 
def resistance_S(T, R0_S, TC_S, ΔT_S):
    '''
    Compute the superconductor resistance as a function of temperature.    

    Input: 
    -    T (float): Temperature
    - R0_S (float): Superconductor Resistance
    - TC_S (float): Superconductor Critical Temperature
    - ΔT_S (float): Superconductor Delta Temperature

    Output:
    -    R (float): Resistance
    '''
    
    R = 0.5 * R0_S * (1.0 + np.tanh((T - TC_S) / ΔT_S))

    return R

#----------------------------------------------------------------------------

# Normal-Metal-Interface-Superconductor Resistance 
def resistance_NMIS(R_NM, R_I, R_S):
    '''
    Compute the normal-metal-interface-superconductor equivalent resistance.

    Input:
    - R_NM (float): Normal-Metal Resistance
    -  R_I (float): Interface Resistance
    -  R_S (float): Superconductor Resistance

    Output:
    -     R (float): Equivalent Resistance
    '''

    R = (R_NM * (R_I + R_S)) / (R_NM + R_I + R_S)

    return R

#----------------------------------------------------------------------------

# Normal-Metal-Interface-Superconductor Resistance Fit
def resistance_NMIS_fit(T, R0_NM, α_NM, R0_I, TC_I, ΔT_I, R0_S, TC_S, ΔT_S):
    '''
    Read resistance_NMIS documentation. Function used for fitting.
    
    Input:
    -     T (float): Temperature
    - R0_NM (float): Normal-Metal Resistance
    -  α_NM (float): Normal-Metal Linear Coefficient
    -  R0_I (float): Interface Resistance
    -  TC_I (float): Interface Critical Temperature
    -  ΔT_I (float): Interface Delta Temperature
    -  R0_S (float): Superconductor Resistance
    -  TC_S (float): Superconductor Critical Temperature
    -  ΔT_S (float): Superconductor Delta Temperature

    Output:
    -     R (float): Equivalent Resistance
    '''

    R_NM = resistance_NM(T, R0_NM, α_NM)
    R_I  = resistance_I(T, R0_I, TC_I, ΔT_I)
    R_S  = resistance_S(T, R0_S, TC_S, ΔT_S)
    R    = resistance_NMIS(R_NM, R_I, R_S)

    return R