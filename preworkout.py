import pandas as pd
import streamlit as st
import openpyxl

st.set_page_config(page_title='Pre Workout Search Tool')
st.header('Pre Workout Search Tool')

###load data frame

excel_file = 'preworkout.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:P',
                   header=0)

#streamlit selection

caffeine_mg = df['Caffeine mg'].unique().tolist()
caffeine_selection_mg = st.slider('Caffeine mg:',
                               min_value= min(caffeine_mg),
                               max_value= max(caffeine_mg),
                               value=(min(caffeine_mg),max(caffeine_mg)))

citrulline_mg = df['Citrulline mg'].unique().tolist()
citrulline_selection_mg = st.slider('Citrulline mg:',
                                 min_value= min(citrulline_mg),
                                 max_value= max(citrulline_mg),
                                 value=(min(citrulline_mg),max(citrulline_mg)))

creatine_grams = df['Creatine grams'].unique().tolist()
creatine_selection_grams = st.slider('Creatine grams:',
                               min_value= min(creatine_grams),
                               max_value= max(creatine_grams),
                               value=(min(creatine_grams),max(creatine_grams)))

betaine_anhydrous_mg = df['Betaine Anhydrous mg'].unique().tolist()
betaine_anhydrous_selection_mg = st.slider('Betaine Anhydrous mg:',
                               min_value= min(betaine_anhydrous_mg),
                               max_value= max(betaine_anhydrous_mg),
                               value=(min(betaine_anhydrous_mg),max(betaine_anhydrous_mg)))

alpha_gpc_mg = df['Alpha GPC mg'].unique().tolist()
alpha_gpc_selection_mg = st.slider('Alpha GPC mg:',
                               min_value= min(alpha_gpc_mg),
                               max_value= max(alpha_gpc_mg),
                               value=(min(alpha_gpc_mg),max(alpha_gpc_mg)))

beta_alanine_mg = df['Beta-Alanine mg'].unique().tolist()
beta_alanine_selection_mg = st.slider('Beta-Alanine mg:',
                               min_value= min(beta_alanine_mg),
                               max_value= max(beta_alanine_mg),
                               value=(min(beta_alanine_mg),max(beta_alanine_mg)))

tyrosine_mg = df['L-Tyrosine mg'].unique().tolist()
tyrosine_selection_mg = st.slider('L-Tyrosine mg:',
                               min_value= min(tyrosine_mg),
                               max_value= max(tyrosine_mg),
                               value=(min(tyrosine_mg),max(tyrosine_mg)))

acetyl_tyrosine_mg = df['N-Acetyl-L-Tyrosine mg'].unique().tolist()
acetyl_tyrosine_selection_mg = st.slider('N-Acetyl-L-Tyrosine mg:',
                               min_value= min(acetyl_tyrosine_mg),
                               max_value= max(acetyl_tyrosine_mg),
                               value=(min(acetyl_tyrosine_mg),max(acetyl_tyrosine_mg)))

theanine_mg = df['L-Theanine mg'].unique().tolist()
theanine_selection_mg = st.slider('L-Theanine mg:',
                               min_value= min(theanine_mg),
                               max_value= max(theanine_mg),
                               value=(min(theanine_mg),max(theanine_mg)))
rhodiola_mg = df['Rhodiola mg'].unique().tolist()
rhodiola_selection_mg = st.slider('Rhodiola mg:',
                               min_value= min(rhodiola_mg),
                               max_value= max(rhodiola_mg),
                               value=(min(rhodiola_mg),max(rhodiola_mg)))

lions_mane_mg = df["Lion's Mane mg"].unique().tolist()
lions_mane_selection_mg = st.slider("Lion's Mane mg:",
                               min_value= min(lions_mane_mg),
                               max_value= max(lions_mane_mg),
                               value=(min(lions_mane_mg),max(lions_mane_mg)))

carbohydrates_grams = df["Carbohydrates grams"].unique().tolist()
carbohydrates_selection_grams = st.slider("Carbohydrates grams:",
                               min_value= min(carbohydrates_grams),
                               max_value= max(carbohydrates_grams),
                               value=(min(carbohydrates_grams),max(carbohydrates_grams)))

# filter dataframe based on selection

mask = df['Caffeine mg'].between(*caffeine_selection_mg) \
       & df['Citrulline mg'].between(*citrulline_selection_mg) \
       & df['Creatine grams'].between(*creatine_selection_grams) \
       & df['Betaine Anhydrous mg'].between(*betaine_anhydrous_selection_mg) \
       & df['Alpha GPC mg'].between(*alpha_gpc_selection_mg) \
       & df['Beta-Alanine mg'].between(*beta_alanine_selection_mg) \
       & df['L-Tyrosine mg'].between(*tyrosine_selection_mg) \
       & df['N-Acetyl-L-Tyrosine mg'].between(*acetyl_tyrosine_selection_mg) \
       & df['L-Theanine mg'].between(*theanine_selection_mg) \
       & df['Rhodiola mg'].between(*rhodiola_selection_mg) \
       & df["Lion's Mane mg"].between(*lions_mane_selection_mg) \
       & df["Carbohydrates grams"].between(*carbohydrates_selection_grams)


number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')




st.dataframe(df[mask])

