# Models
import numpy as np

#----------------------------------------------------------------------------

# Normal-Metal Current
def current_NM(i, R_E, R_NM):
    '''
    Compute the normal-metal current.

    Input:
    -    i (float): Total Current
    -  R_E (float): Equivalent Resistance
    - R_NM (float): Normal-Metal Resistance

    Output:
    -    I (float): Current
    '''

    I = (R_E / R_NM) * i
    
    return I 

#----------------------------------------------------------------------------

# Interface-Superconductor Current
def current_IS(i, R_E, R_I, R_S):
    '''
    Compute the interface-superconductor current.

    Input:
    -    i (float): Total Current
    -  R_E (float): Equivalent Resistance
    -  R_I (float): Interface Resistance
    -  R_S (float): Superconductor Resistance

    Output:
    -    I (float): Current
    '''
    
    I = (R_E / (R_I + R_S)) * i     

    return I
    
#----------------------------------------------------------------------------

# Normal-Metal Resistance 
def resistance_NM(T, R0_NM, α_NM):
    '''
    Compute the normal-metal resistance as a function of temperature.

    Input: 
    -     T (float): Absolute Temperature
    - R0_NM (float): Normal-State Resistance
    -  α_NM (float): Linear Coefficient

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
    -    T (float): Absolute Temperature
    - R0_I (float): Normal-State Resistance
    - TC_I (float): Critical Temperature
    - ΔT_I (float): Superconducting Transition Width

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
    -    T (float): Absolute Temperature
    - R0_S (float): Normal-State Resistance
    - TC_S (float): Critical Temperature
    - ΔT_S (float): Superconducting Transition Width

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
    -    R (float): Equivalent Resistance
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
    - R0_NM (float): Normal-State Normal-Metal Resistance
    -  α_NM (float): Normal-Metal Linear Coefficient
    -  R0_I (float): Normal-State Interface Resistance
    -  TC_I (float): Interface Critical Temperature
    -  ΔT_I (float): Interface Superconducting Transition Width
    -  R0_S (float): Normal-State Superconductor Resistance
    -  TC_S (float): Superconductor Critical Temperature
    -  ΔT_S (float): Superconductor Superconducting Transition Width

    Output:
    -     R (float): Equivalent Resistance
    '''

    R_NM = resistance_NM(T, R0_NM, α_NM)
    R_I  = resistance_I(T, R0_I, TC_I, ΔT_I)
    R_S  = resistance_S(T, R0_S, TC_S, ΔT_S)
    R    = resistance_NMIS(R_NM, R_I, R_S)

    return R