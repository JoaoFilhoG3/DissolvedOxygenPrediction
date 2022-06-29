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

#####
# Carregando entradas recebidas via método GET
#####
params = st.experimental_get_query_params()

#####
# Verificando se as entradas foram informadas
#####
if not ('temp' in params.keys()):
  st.json({
    'error': "Parâmetro 'temp' não informado!"
  })
elif not ('cond' in params.keys()):
  st.json({
    'error': "Parâmetro 'cond' não informado!"
  })
elif not ('sal' in params.keys()):
  st.json({
    'error': "Parâmetro 'sal' não informado!"
  })
elif not ('depth' in params.keys()):
  st.json({
    'error': "Parâmetro 'depth' não informado!"
  })
elif not ('ph' in params.keys()):
  st.json({
    'error': "Parâmetro 'ph' não informado!"
  })
elif not ('turbid' in params.keys()):
  st.json({
    'error': "Parâmetro 'turbid' não informado!"
  })
elif not ('chl' in params.keys()):
  st.json({
    'error': "Parâmetro 'chl' não informado!"
  })
elif not ('odo_sat' in params.keys()):
  st.json({
    'error': "Parâmetro 'odo_sat' não informado!"
  })
elif not ('data_hora' in params.keys()):
  st.json({
    'error': "Parâmetro 'data_hora' não informado!"
  })
else:
  #####
  # Executar modelo preditivo caso as entradas tenham sido informadas
  #####
  temp = params['temp'][0]
  cond = params['cond'][0]
  sal = params['sal'][0]
  depth = params['depth'][0]
  ph = params['ph'][0]
  turbid = params['turbid'][0]
  chl = params['chl'][0]
  odo_sat = params['odo_sat'][0]
  data_hora = params['data_hora'][0]

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
    'data_hora': data_hora
  })