import requests
from bs4 import BeautifulSoup


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

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code==200:
        print(content.status_code)
        #soup = BeautifulSoup(content)
        #print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = '04 Agustus 2023'
        hasil['waktu'] = '18:48:38 WIB'
        hasil['magnitudo'] = 6.0
        hasil['lokasi'] = { 'ls':0.21, 'bt':125.03 }
        hasil['pusat'] = 'Pusat gempa berada di laut 117 km Tenggara Bolaang Mongondo Timur'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): III - IV Bone Bolango, III - IV Gorontalo, III Manado, III Tomohon, III Tondano, III Minahasa Utara, III Bolaang Mongondow Selatan, III Minahasa Tenggara, III Bolaang Mongondow Timur, III Kotamobagu, III Bitung, III Kab. Gorontalo, II-III Luwuk, II-III Kab. Gorontalo Utara, II-III Banggai Kepulauan, II Ampana'
        return hasil
    else:
        return None

def tamilkan_data(result):
    if result is None:
        print ("Tidak bisa menemukan gempa terkini")
        return
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print (f"waktu {result['waktu']}")
    print (f"magnitudo {result['magnitudo']}")
    print (f"lokasi: LS={result ['lokasi']['ls']}, BT={result ['lokasi']['bt']}")
    print (f"pusat {result['pusat']}")
    print (f"dirasakan {result['dirasakan']}")

#if __name__ == '__main__':
#    print('ini adalah package gempaterkini')
# kode yang paling kiri di jalankan. jika tidak di paling pinggir tidak dijalankan