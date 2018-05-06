import pandas as pd
import matplotlib.pyplot as plt
import TISTNplot as tn

# data inlezen
df = pd.read_csv('data\\elementen_data.txt', sep=' ', header=1, names=['Z', 'm', 'N'], decimal=".")

# Bindingsenergie E per nucleon berekenen.
n = 1.008665  # massa neutron  [u]
H = 1.007825  # massa waterstof-1 [u]
df['E'] = (((df['Z']*H)+((df['N']-df['Z'])*n)+(df['m']*-1))*931.5)/df['N']

# standaard functie voor de correcte opmaak, let wel op juist gekozen significantie.
def correcte_opmaak():
    """
    Zorgt voor de correcte opmaak van de plot.
    """
    tn.PRECISION_X = 3
    tn.PRECISION_Y = 3
    tn.fix_axis(plt.gca())
    plt.tight_layout()
    plt.legend(loc=0)
    plt.grid()

# Maak de plot 
plt.clf() # clear frame (plot leeg maken, nu zijn alle voorgaande zeker weten weg uit het figuur)
plt.plot(df['Z'], df['E'], '.', color="#ff0000", ms=2)
plt.xlabel('Aantal nucleonen $A$ [-]',color='black')
plt.ylabel('Bindingsenergie per nucleon $E$ [MeV]',color='black')
correcte_opmaak()

# Slechts 1 data set dus legenda niet nodig.  Controleren met rapportage journaal?
plt.legend().remove()

# plot opslaan
plt.savefig('figuren\\bindingsenergie_per_nucleon.png', dpi=500, bbox_inches='tight')