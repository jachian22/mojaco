import pandas as pd
import quandl as qd

#===============================================================================
# Utility
#===============================================================================

def get_data():
	df_fao = pd.read_csv('../data/FAO.csv', encoding='ISO-8859-1')
	'''
	Pulling from quandl:

	data = quandl.get(commodity_code, start_date="yyyy-mm-dd", end_date="yyyy-mm-dd")

	change sampling frequency with => collapse="monthly"
	'''
	return 'hi'

#===============================================================================
# Look up tables (lut)
#===============================================================================

# NOTE - Working on taxonomy for bringing in the quandl commodity pricing data

[
'barley_oda': 'oda/PBARL_usd',
'barley_worldbank': 'worldbank/WLD_BARLEY',
'corn_tfgrain': 'tfgrain/CORN',
'corn_cme': 'chris/cme_C1',
'corn_worldbank': 'worldbank/WLD_MAIZE',
'oats_cme': 'chris/cme_O1',
'rice_oda': 'oda/PRiceNPQ_usd',
'rice_cme': 'chris/cme_RR1',
'rice_tfgrain': 'tfgrain/SOYBEANS',
'soybean_cme': 'chris/cme_S1',
'soybean_cme': 'chris/cme_SM1',
'wheat_worldbank': 'worldbank/WLD_SOYBEAN_OIL',
'wheat_cme': 'chris/cme_BO1',
'wheat_oda': 'oda/PWHEAMT_usd',
'wheat_cme': 'chris/cme_W1',
'Dairy_cme': 'chris/cme_DA1',
'cattle_oda': 'oda/PBEEF_usd',
'cattle_cme': 'chris/cme_LC1',
'cattle_cme': 'chris/cme_FC1',
'cattle_oda': 'oda/PHIDE_usd',
'poulty_oda': 'oda/PPOULT_usd',
'pork_oda': 'oda/PPORK_usd',
'pork_cme': 'chris/cme_LN1',
'lamb_oda': 'oda/PLAMB_usd',
'lamb_wool_oda': 'oda/PWOOLC_usd',
'salmon_oda': 'oda/PSALM_usd',
'shrimp_oda': 'oda/PSHRI_usd',
'fishmeal_oda': 'oda/PFISH_usd',
'groundnuts_oda': 'oda/PGNUTS_usd',
'oranges_oda': 'oda/PORANG_usd',
'oranges_Juice_ice': 'chris/ice_OJ1',
'bananas_oda': 'oda/PBANSOP_usd',
'bananas_worldbank': 'worldbank/WLD_BANANA_US',
'oil_rapeseed_oda': 'oda/PROIL_usd',
'oil_sunflower_oda': 'oda/PSUNO_usd',
'oil_olive_oda': 'oda/POLVOIL_usd',
'oil_palm_oda': 'oda/PPOIL_usd',
'oil_palmkernal_worldbank': 'worldbank/WLD_PLMKRNL_OIL',
'oil_groundnut_worldbank': 'worldbank/WLD_GRNUT_OIL'
]

def main():
	pass

#===============================================================================

if __name__ == '__main__':
	main()