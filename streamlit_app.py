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

temp = coluna1.number_input('Temperatura')
cond = coluna2.number_input('Condutividade')
sal = coluna1.number_input('Salinidade')
depth = coluna2.number_input('Profundidade')
ph = coluna1.number_input('Acidez')
turbid = coluna2.number_input('Turbidez')
chl = coluna1.number_input('Clorofila')
odo_sat = coluna2.number_input('Saturação de oxigênio dissolvido')
data = coluna1.date_input('Data')
hora = coluna2.time_input('Hora')

st.button("Oi")
data_hora = data+" "+hora



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
st.json({
  'temp': temp,
  'cond': cond,
  'sal': sal,
  'depth': depth,
  'ph': ph,
  'turbid': turbid,
  'chl': chl,
  'odo_sat': odo_sat,
  'data_hora': data_hora,
  'result': valor
})