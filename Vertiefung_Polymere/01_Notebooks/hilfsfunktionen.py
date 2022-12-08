import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_DSC_over_time(data, segment=[], temp=True):
    if type(segment) == int:
        segment = [segment]

    for i in segment:
        if i not in data.Segment.unique():
            print('Segment nicht in Daten enthalten')
            break

    if segment == []:
        segment = data.Segment.unique()

    fig, ax1 = plt.subplots(figsize=(12, 5))

    if temp:
        ax2 = ax1.twinx(
        )  # instantiate a second axes that shares the same x-axis

    for i in segment:
        data2 = data[data.Segment == i]
        ax1.plot(data2['Time/min'],
                 data2['DSC/(mW/mg)'],
                 label='Segment: ' + str(i))
        ax1.set_xlabel('Time/min')
        ax1.set_ylabel('DSC [mW/mg]')
        ax1.legend(loc=2)

        ax2.plot(data2['Time/min'], data2['Temp./C'], '--', color='red')

    ax2.set_ylabel('Temp [°C]', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    plt.show()
    
def plot_DSC_over_temp(data, segment=[]):
    if type(segment) == int:
        segment = [segment]

    for i in segment:
        if i not in data.Segment.unique():
            print('Segment nicht in Daten enthalten')
            break

    if segment == []:
        segment = data.Segment.unique()

    plt.figure(figsize=(12, 5))
    for i in segment:
        data2 = data[data.Segment == i]
        plt.plot(data2['Temp./C'],
                 data2['DSC/(mW/mg)'],
                 label='Segment: ' + str(i))
        plt.xlabel('Temp [°C]')
        plt.ylabel('DSC [mW/mg]')
        plt.legend(loc=2)
        
def calc_tg(data, segment='', bereich=[0.3, 1]):
    
    assert type(bereich) == list 
    assert bereich[0] >0 and bereich[0]<=bereich[1] and bereich[1]<=1, 'der erste Berichswert muss kleiner sein als der zweite und beide zwischen null und eins'
    assert type(segment) == int ,'geben Sie das Segment als int an'
    

    # Auswahl des Segments
    clipped_data = data[data.Segment == segment].reset_index(drop=True)
    
    #Ableitung
    dy = np.gradient(smooth(clipped_data['DSC/(mW/mg)']))
    
    #beschneiden des Vektors um den Anfangs und Endbereich zu löschen
    l = len(dy)
    i = np.argmin(dy[int(l * bereich[0]):int(l * bereich[1])]) + int(l * bereich[0])
    
    # Plot des Ergebnis
    plot_DSC_over_temp(data, segment)
    plt.plot(clipped_data.loc[i, 'Temp./C'],
             clipped_data.loc[i, 'DSC/(mW/mg)'],
             'r*', label='Segment: ' + str(i))
    plt.text(clipped_data.loc[i, 'Temp./C'] , clipped_data.loc[i, 'DSC/(mW/mg)']+0.05,
             'T_g = ' + str(round(clipped_data.loc[i, 'Temp./C'])))
    return round(clipped_data.loc[i, 'Temp./C'])

def calc_area(data, segment='', start_temp='', end_temp=''):
    
    # Auswahl des Segments
    clipped_data = data[data.Segment == segment].reset_index(drop=True)
    
    #Eingabenüberprüfung
    temp_min, temp_max = clipped_data['Temp./C'].min(), clipped_data['Temp./C'].max()
    assert type(start_temp+end_temp) == float or type(start_temp+end_temp) ==int, 'float oder int'
    assert start_temp >temp_min and start_temp<=end_temp and end_temp<=temp_max, 'der erste Berichswert muss kleiner sein als der zweite und beide zwischen {} und {}'.format(temp_min, temp_max)
    assert type(segment) == int ,'geben Sie das Segment als int an'
    
    
    temp = clipped_data['Temp./C']
    time = clipped_data['Time/min']
    dsc = clipped_data['DSC/(mW/mg)']
    plt.plot(temp, dsc, label='Signal')

    index_temp_min_t = np.argmin(np.abs(temp-start_temp))
    index_temp_max_t = np.argmin(np.abs(temp-end_temp))
    
    index_temp_min = min(index_temp_min_t, index_temp_max_t)
    index_temp_max = max(index_temp_min_t, index_temp_max_t)
    
    temp, dsc, time = temp[index_temp_min: index_temp_max].values, dsc[index_temp_min: index_temp_max].values, time[index_temp_min: index_temp_max].values

    baseline = np.linspace(dsc[0], dsc[-1], max(index_temp_max,index_temp_min)-min(index_temp_max,index_temp_min))
    plt.plot(temp, baseline, label = 'Baseline')
    plt.plot(temp[0], dsc[0], 'ro')
    plt.plot(temp[-1], dsc[-1], 'ro')
    plt.fill_between(temp, dsc, baseline, color='gainsboro', label='$\delta$H')
    area =(np.trapz(dsc-dsc.min(), x=time) - np.trapz(baseline-dsc.min(), x=time))*60
    plt.xlabel('Temp./C')
    plt.ylabel('DSC [mW/mg]')
    return area



    
def smooth(x, lookahead=21, window='flat'):
    """ Glaettung der Funktion

    Parameter
    __________
    y           ... Eingabevektor
    lookahead   ... Bereich [lookahead/2 ... Zahl ... l/2] aus dem der Mittelwerte gebildet wird
    window      ... Auswahl der Window-Function (flat, Savgol, hamming, bartlett, blackman, hanning, kaiser,...)
    pol_order   ... Polynomgrad der Aproximationsfunktion für den SavGol filter
    """

    # Korrektur der Eingaben
    if lookahead % 2 == 0:
        lookahead += 1

    aa = int(lookahead // 2)

    # Faltung des Vektors fuer Mittelwerte am Vektorrand
    s = np.r_[x[lookahead - 1:0:-1], x, x[-2:-lookahead - 1:-1]]

    # Auswahl des Mittelwertalgorythmus

    if window == 'flat':  # moving average
        w = np.ones(lookahead, 'd')
    else:
        w = eval('ws.' + window + '(lookahead)')

    # Bildung Mittelwerte
    y = np.convolve(w / w.sum(), s, mode='valid')

    # Beschneiden des Vektors
    y = y[aa:-aa]

    return y