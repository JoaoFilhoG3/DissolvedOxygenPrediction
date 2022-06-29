import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
#from pycaret.regression import *

#loaded_model = load_model('my_model')

#def realizar_predicao(loaded_model, temp, cond, sal, depth, ph, turbid, chl, odo_sat, data_hora):
  #data_hora = pd.to_datetime(data_hora)
#
  #dia_da_semana = [datetime.weekday(data_hora)][0]
  #ano = [data_hora.year][0]
  #mes = [data_hora.month][0]
  #dia_do_mes = [data_hora.day][0]
  ##minutos = [data_hora.minute][0]
  #semana = [data_hora.week][0]
  #trimestre = [data_hora.quarter][0]
#
  #col_names = ['temp_c','cond_us','sal_ppt','depth_m','pH ','turbid_ntu','chl_ug/l','odo_sat_%','dia_da_semana','ano','mes','dia_do_mes','hora','minutos','semana','trimestre']
  #sample_values = [temp, cond, sal, depth, ph, turbid, chl, odo_sat, dia_da_semana, ano, mes, dia_do_mes, hora, minutos, semana, trimestre]
#
  #d = dict(zip(col_names, sample_values))
  #unseen_data = pd.DataFrame([d])
#
  #predictions = predict_model(loaded_model, data=unseen_data)
#
  #return predictions.head()['Label'][0]
  


#valor = realizar_predicao(
            #loaded_model,
            #temp = 34.49,
            #cond = 84.0,
            #sal = 0.04,
            #depth = 0.404,
            #ph = 0.0,
            #turbid = -28.6,
            #chl = -0.57,
            #odo_sat = 100.7,
            #data_hora = "2020-11-21 12:21:00")

params = st.experimental_get_query_params()

if 'oi' in params.keys():
  st.json({
    'predicao': params['oi'][0]
  })  