import pandas as pd

# Step 1: Create a mapping from Exterior1st to average SalePrice (based on your data)
avg_price_by_exterior = {
    'ImStucc': 262000,
    'Stone': 258500,
    'CemntBd': 231691,
    'VinylSd': 213733,
    'BrkFace': 194573,
    'Plywood': 175942,
    'HdBoard': 163077,
    'Stucco': 162990,
    'WdShing': 150655,
    'Wd Sdng': 149842,
    'MetalSd': 149422,
    'AsbShng': 107386,
    'CBlock': 105000,
    'AsphShn': 100000,
    'BrkComm': 71000
}

# Step 2: Make the function
def categorize_exterior1st(materials):
    price = avg_price_by_exterior.get(materials, 0) # default zero if unknown

    if price >= 200000:
        return "Premium"
    elif 160000 <= price < 200000:
        return "High"

    elif 120000 <= price < 160000:
        return "Mid"
    else:
        return "Low"


# Step 1: Create a mapping from Neighborhood to average SalePrice (based on your data)
avg_price_by_neigh = {
    'NoRidge': 335295,
    'NridgHt': 316271,
    'StoneBr': 310499,
    'Timber': 242247,
    'Veenker': 238773,
    'Somerst': 225380,
    'ClearCr': 212565,
    'Crawfor': 210625,
    'CollgCr': 197966,
    'Blmngtn': 194871,
    'Gilbert': 192855,
    'NWAmes': 189050,
    'SawyerW': 186556,
    'Mitchel': 156270,
    'NAmes': 145847,
    'NPkVill': 142694,
    'SWISU': 142591,
    'Blueste': 137500,
    'Sawyer': 136793,
    'OldTown': 128225,
    'Edwards': 128220,
    'BrkSide': 124834,
    'BrDale': 104494,
    'IDOTRR': 100124,
    'MeadowV': 98576
}

def categorize_neighborhood(neigh):
    price = avg_price_by_neigh.get(neigh, 0)
    if price >= 250000:
        return 'Premium'
    elif 180000 <= price < 250000:
        return 'High'
    elif 130000 <= price < 180000:
        return 'Mid'
    else:
        return 'Low'

# Step 3:
avg_price_by_exterior2nd = {
    'Other': 319000,
    'ImStucc': 252070,
    'CmentBd': 230094,
    'VinylSd': 214432,
    'BrkFace': 195818,
    'Plywood': 168112,
    'HdBoard': 167662,
    'Wd Shng': 161329,
    'Stone': 158225,
    'Stucco': 155905,
    'MetalSd': 149803,
    'Wd Sdng': 148386,
    'AsphShn': 138000,
    'Brk Cmn': 126714,
    'AsbShng': 114061,
    'CBlock': 105000
}

def categorize_exterior2nd(mat):
    price = avg_price_by_exterior2nd.get(mat, 0)
    if price >= 200000:
        return 'Premium'
    elif 160000 <= price < 200000:
        return 'High'
    elif 120000 <= price < 160000:
        return 'Mid'
    else:
        return 'Low'

 