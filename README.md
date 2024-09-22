# Simple simulation of a first order Continuous Stirred Tank Reactor (CSTR)
- Includes response to various types of input concentation stimuli (step changes, ramp inputs, and sinusoidal inputs)
- Incorporation of PID controller to maintain exit concentration set point 
- Simulates the response of an MPC controller for a heat exchanger model
- Represents a first-order heat exchanger model using Euler's method for discrete-time simulation
- Uses heuristic Ziegler-Nichols tuning method for PID controller tuning

### Description of the System
A liquid stream of **A** enters the reactor at a volumetric flow rate **F** , decomposing in the reactor according to the irreversible chemical reaction (**A→B**), occuring at a rate of **r=k*C<sub>a</sub>**

The reactor is modeled with a time constant **𝜏** and a gain **K**. The purpose of the control system is to maintain the concentration of **B** leaving the reactor at a desired value despite variations in the inlet concentration **C<sub>a</sub><sub>0</sub>**

### Parameters
- **Volume (V)**: Set to 1.0 m³
- **Flow Rate (F)**: Set to 0.5 m³/s
- **Reaction Rate Constant (k)**: Set to 0.1 s<sup>-1<sup>
- **Set Point for Exit Concentration B**: Set to 0.8
  
### Reactor Formulas
V $\frac{dc}{dt}$ = F*C<sub>a</sub><sub>0</sub> - (F+kv)*C<sub>a</sub>

,and

𝜏 $\frac{dc}{dt}$ + C<sub>a</sub> = K*C<sub>a</sub><sub>0</sub> 

where:
- 𝜏 = $\frac{V}{F+kV}$
- K = $\frac{1}{kV/F}$

At steady state, $\frac{dc}{dt}$ = 0, so the equation becomes:
c= K*C<sub>a</sub><sub>0</sub>

<br>

#### Reference
Coughanower, D. R.; Koppel, L. B. *Process Systems Analysis and Control*; McGraw-Hill Chemical Engineering Series, McGraw-Hill Companies: New York, 1964; pp 123–124.
