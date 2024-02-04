from libkdv import kdv
import pandas as pd


def gen_kdv(filename='./hainan-sanya-taxi.csv'):
    ds = pd.read_csv('./hainan-sanya-taxi.csv')
    kdv_ds = kdv(ds, GPS = True, KDV_type='KDV', bandwidth=2000)
    df = kdv_ds.compute()
    
    med_v = gen_median(df)
    fin_v = gen_val(df)
    response = {
        "middle": med_v,
        "data": fin_v
    }
    return response


def gen_spa_kdv(par, body: list):
    ds = pd.DataFrame(body, columns = ["lon","lat"])
    kdv_ds = kdv(ds, KDV_type="KDV", GPS=True, bandwidth=par["bandwidthS"], row_pixels=par["rowP"], col_pixels=par["colP"], num_threads=par["nThreads"])
    df = kdv_ds.compute()

    med_v = gen_median(df)
    fin_v = gen_val(df)
    response = {
        "middle": med_v,
        "data": fin_v
    }
    return response

def gen_spa_stkdv(par, body: list):
    ds = pd.DataFrame(body, columns = ["lon","lat","t"])
    stkdv_ds = kdv(ds, KDV_type="STKDV", GPS=True, bandwidth=par["bandwidthS"], row_pixels=par["rowP"], col_pixels=par["colP"], bandwidth_t=par["bandwidthT"], t_pixels=par["tPixel"], num_threads=par["nThreads"])
    df = stkdv_ds.compute()

    med_v = gen_median(df)
    fin_v = gen_dict_val(df)
    response = {
        "middle": med_v,
        "data": fin_v,
    }
    print(fin_v.keys())
    return response


def gen_median(df):
    median = df.median()
    return [ median['lon'], median['lat']]

def gen_val(df):
    return df.values.tolist()

def gen_dict_val(df):
    results = {}
    grouped = df.groupby('t')
    
    for t, group in grouped:
        results[t] = [list(row) for row in group[['lon', 'lat', 'val']].values]
    
    return results