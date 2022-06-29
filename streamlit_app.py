import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from pycaret.regression import *

#####
# Carregando modelo preditivo previamente salvo em arquivo
#####
loaded_model = load_model('my_model')

#####
# Função responsável por submeter ao modelo preditivo os valores recebidos por parâmetros
#####
def realizar_predicao(loaded_model, temp, cond, sal, depth, ph, turbid, chl, odo_sat, data_hora):
  data_hora = pd.to_datetime(data_hora)

  dia_da_semana = [datetime.weekday(data_hora)][0]
  ano = [data_hora.year][0]
  mes = [data_hora.month][0]
  dia_do_mes = [data_hora.day][0]
  hora = [data_hora.hour][0]
  minutos = [data_hora.minute][0]
  semana = [data_hora.week][0]
  trimestre = [data_hora.quarter][0]

  col_names = ['temp_c','cond_us','sal_ppt','depth_m','pH ','turbid_ntu','chl_ug/l','odo_sat_%','dia_da_semana','ano','mes','dia_do_mes','hora','minutos','semana','trimestre']
  sample_values = [temp, cond, sal, depth, ph, turbid, chl, odo_sat, dia_da_semana, ano, mes, dia_do_mes, hora, minutos, semana, trimestre]

  d = dict(zip(col_names, sample_values))
  unseen_data = pd.DataFrame([d])

  predictions = predict_model(loaded_model, data=unseen_data)

  return predictions.head()['Label'][0]


coluna1, coluna2 = st.columns(2)

temp = coluna1.number_input('Temperatura', value= 34.49)
cond = coluna2.number_input('Condutividade', value= 84.0)
sal = coluna1.number_input('Salinidade', value= 0.04)
depth = coluna2.number_input('Profundidade', value= 0.404)
ph = coluna1.number_input('Acidez', value= 0.0)
turbid = coluna2.number_input('Turbidez', value= -28.6)
chl = coluna1.number_input('Clorofila', value= -0.57)
odo_sat = coluna2.number_input('Saturação de oxigênio dissolvido', value= 100.7)
data = coluna1.date_input('Data', value= datetime.strptime("2020-11-21", "%Y-%m-%d"))
hora = coluna2.time_input('Hora', value= datetime.strptime("12:21:00", "%H:%M:%S"))

data_hora = data.strftime("%Y-%m-%d") + " " + hora.strftime("%H:%M:%S")

if st.button('Calcular'):
    valor = realizar_predicao(
        loaded_model,
        temp = temp,
        cond = cond,
        sal = sal,
        depth = depth,
        ph = ph,
        turbid = turbid,
        chl = chl,
        odo_sat = odo_sat,
        data_hora = data_hora)

    st.warning('A previsão de oxigênio dissolvido é de: ' + valor)

    #st.json({
        #'temp': temp,
        #'cond': cond,
        #'sal': sal,
        #'depth': depth,
        #'ph': ph,
        #'turbid': turbid,
        #'chl': chl,
        #'odo_sat': odo_sat,
        #'data_hora': data_hora,
        #'result': valor
    #})

