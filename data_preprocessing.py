import numpy as np
import sklearn.preprocessing as pp
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import SplineTransformer

def impute_data(array):
    imputer = SimpleImputer(strategy="median")
    imputer = imputer.fit(array)
    result = imputer.transform(array)
    return result

def normalize_array(array, data_range):
    normalized = MinMaxScaler(feature_range=data_range)
    normalized_data = normalized.fit_transform(array)
    return normalized_data

def quantile_transform_array(array, quantiles, distribution, ignore_zero, sub_sample):
    x = QuantileTransformer(n_quantiles=quantiles, output_distribution=distribution, ignore_implicit_zeros=ignore_zero, subsample=sub_sample)
    result = x.fit_transform(array)
    return result

def power_transform_array(array, meth, standard, cop):
    power = PowerTransformer(method=meth, standardize=standard, copy=cop)
    return power.fit_transform(array)

def normalize_array_preprocessing(array, n):   
    return pp.normalize(array, norm=n)

def ordinal_encode_array(array):
    encode = pp.OrdinalEncoder(categories="auto") 
    encode = encode.fit(array)
    return encode.transform(array)

def onehot_encode_array(array):
    return OneHotEncoder(categories="auto").fit_transform(array)

def k_bins_discretize_array(array, b, strat):
    return KBinsDiscretizer(n_bins=b, strategy=strat).fit_transform(array)

def binarize_array(array, thr):
    return Binarizer(threshold=thr).fit_transform(array)

def polynomial_features_array(array, deg, bias):
    return pp.PolynomialFeatures(degree=deg, include_bias=bias).fit_transform(array)

def spline_transform_array(array, knot, degr):
    spline = SplineTransformer(n_knots=knot, degree=degr)
    return spline.fit_transform(array)



arr = np.array([[1, 2, np.nan], [3, np.nan, 5], [6, 7, 8]])

imputed_Data = impute_data(arr)

normalized_arr = normalize_array(imputed_Data, (0, 1))

quantile_transformed_arr = quantile_transform_array(imputed_Data, 10, 'uniform', False, 100000)

power_transformed_arr = power_transform_array(imputed_Data, 'yeo-johnson', False, True) 

normalized_arr_preprocessing = normalize_array_preprocessing(imputed_Data,'l2') 

ordinal_encoded_arr = ordinal_encode_array(imputed_Data) 

onehot_encoded_arr = onehot_encode_array(imputed_Data) 

k_bins_discretized_arr = k_bins_discretize_array(imputed_Data, 3, 'uniform') 

binarized_arr = binarize_array(imputed_Data, 0.5) 

polynomial_features_arr = polynomial_features_array(imputed_Data, 2, True)

spline_transformed_arr = spline_transform_array(imputed_Data,5, 3)



print(imputed_Data,'\n')
print(normalized_arr,'\n')
print(quantile_transformed_arr,'\n')
print(power_transformed_arr,'\n')
print(normalized_arr_preprocessing,'\n')
print(ordinal_encoded_arr,'\n')
print(onehot_encoded_arr,'\n')
print(k_bins_discretized_arr,'\n')
print(binarized_arr,'\n')
print(polynomial_features_arr,'\n') 
print(spline_transformed_arr,'\n')