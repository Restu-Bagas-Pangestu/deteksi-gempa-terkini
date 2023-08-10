"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""
import gempa_terkini

if __name__== '__main__':
    print('Aplikasi utama')
    result=gempa_terkini.ekstraksi_data()
    gempa_terkini.tamilkan_data(result)

"""
    
"""