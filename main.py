""""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 04 Agustus 2023
    Waktu: 18:48:38 WIB
    Magnitudo: 6.0
    Kedalaman: 10 km
    Lokasi: 0.21 LS - 125.03 BT
    Pusat gempak: Pusat gempa berada di laut 117 km Tenggara Bolaang Mongondo Timur
    Dirasakan (Skala MMI): III - IV Bone Bolango, III - IV Gorontalo, III Manado, III Tomohon, III Tondano, III Minahasa Utara, III Bolaang Mongondow Selatan, III Minahasa Tenggara, III Bolaang Mongondow Timur, III Kotamobagu, III Bitung, III Kab. Gorontalo, II-III Luwuk, II-III Kab. Gorontalo Utara, II-III Banggai Kepulauan, II Ampana
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '04 Agustus 2023'
    hasil['waktu'] = '18:48:38 WIB'
    hasil['magnitudo'] = 6.0
    hasil['lokasi'] = { 'ls':0.21, 'bt':125.03 }
    hasil['pusat'] = 'Pusat gempa berada di laut 117 km Tenggara Bolaang Mongondo Timur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III - IV Bone Bolango, III - IV Gorontalo, III Manado, III Tomohon, III Tondano, III Minahasa Utara, III Bolaang Mongondow Selatan, III Minahasa Tenggara, III Bolaang Mongondow Timur, III Kotamobagu, III Bitung, III Kab. Gorontalo, II-III Luwuk, II-III Kab. Gorontalo Utara, II-III Banggai Kepulauan, II Ampana'
    print(hasil)

    return hasil



def tamilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print (f"waktu {result['waktu']}")
    print (f"magnitudo {result['magnitudo']}")
    print (f"lokasi: LS={result ['lokasi']['ls']}, BT={result ['lokasi']['bt']}")
    print (f"pusat {result['pusat']}")
    print (f"dirasakan {result['dirasakan']}")


if __name__== '__main__':
    print('Aplikasi u tama')
    result=ekstraksi_data()
    tamilkan_data(result)