from params import *

class Model(object):
  def __init__(self,name):
    self.name = name

  def SEIR(self,initial_conditions,params,t,theta=1):
    
    So,Eo,Io,Ro = initial_conditions
    S,E,I,R = [So],[Eo],[Io],[Ro]
    alpha,beta,gamma = params
    dt = t[1]-t[0]
    for _ in t[1:]:
      St = S[-1] - (theta*beta*S[-1]*I[-1])*dt
      Et = E[-1] + (theta*beta*S[-1]*I[-1] - alpha*E[-1])*dt
      It = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
      Rt = R[-1] + (gamma*I[-1])*dt
      S.append(St)
      E.append(Et)
      I.append(It)
      R.append(Rt)

    return S,E,I,R

# parametros 
params = parametros
initial_conditions = Condiciones_Iniciales
t = periodo_evaluacion

# setting up the model
seir = Model("SEIR")
seir_model = seir.SEIR(initial_conditions,params,t)

S,E,I,R = seir_model

model_results = {
'results':{
  'susceptible':S, 
  'exposed':E, 
  'infected':I,
  'recovered':R
  }
}



