import sys
sys.path.append('dynpy')
from qrax import *
import glob

# In[5]:

def compute_rate(file):
    cart = read_efg_data(file)
    cart.rename(columns={'Unnamed: 0':'frame'},inplace=True)
    cart['time'] = cart['frame']*0.01015931
    cart['symbol']='Na'
    cart['label']=1
    cart['traj']=1
    cart['system']='Na'
    cart.head()
    spatial = cart_to_spatial(cart,pass_columns=['traj','system'])
    acfs = spatial.groupby('label',group_keys=True).apply(correlate, pass_columns=['traj','system','symbol','frame','time'])
    acfs.head()
    g = spectral_dens(acfs, cutoff=False, cutoff_tol=1e-3)
    rax = relaxation(g,'23Na')

    rax_numpy = rax.to_numpy()[0]
    return np.array([float(rax_numpy[1]),float(rax_numpy[2]),float(rax_numpy[3]) ])

#files = ['ml_efg_Na_guess_atomic_prop_density_kernel_poly_degree_1_ntrain_5.csv'] #glob.glob('*.csv')
# Na                  I                    Cs
ntrains = [[5,12,25,50,125,250],[4,12,24,49,124,249],[4,10,21,43,108,216]]
percentages = [1,2.5,5,10,25,50]
kernel = 'poly'
degree = 1
atoms = ['Na','I','Cs']
guesses = ['atomic','xtb']
props = ['overlap','density','ham']
diff = []
refs = []
mls = []
for k1, atom in enumerate(atoms):
    tmp1 = []
    file = f'csv_data/ref_{atom}.csv'
    rax_ref = compute_rate(file)
    print('************************************************')
    print('Reference rates:', rax_ref )
    for guess in guesses:
        tmp2 = []
        for prop in props:
            tmp3 = []
            for ntrain in ntrains[k1]:
                file = f'csv_data/ml_efg_{atom}_guess_{guess}_prop_{prop}_kernel_{kernel}_degree_{degree}_ntrain_{ntrain}.csv'
                print('======================')
                print(file)
                #cart = read_efg_data("../../Akimov-research/ml_efg_AGdensity_ntrain_250.csv")
                #cart = read_efg_data("ml_efg_AGdensity_ntrain_250.csv")
                rax = compute_rate(file)
                #rax_numpy = rax.to_numpy()
                print(rax)
                #tmp3.append(rax)
                tmp3.append(rax_ref)
                #tmp3.append(np.abs(rax-rax_ref)/(rax_ref))
            tmp2.append(tmp3)
        tmp1.append(tmp2)
    diff.append(tmp1)
diff = np.array(diff)
print(diff.shape)
#np.save(f'degree_{degree}.npy', diff)
#np.save(f'ml_relax_rates_degree_{degree}.npy', diff)
np.save(f'ref_relax_rates.npy', diff)

