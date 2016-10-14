# 6 oct 2016
import json
import requests # 3rd party package, use pip install requests jika nak install dalam python
d = {'ktn01': ('Kota Bahru', 'Bachok', 'Pasir Puteh', 'Tumpat', 'Pasir Mas', 'Tanah Merah', 'Machang', 'Kuala Krai',
               'Mukim Chiku', 'Chiku'),
     'ktn03': ('Jeli', 'Gua Musang', 'Mukim Galas', 'Galas', 'Bertam'),
     'phg01': 'Pulau Tioman',
     'phg02': ('Kuantan','Pekan', 'Rompin', 'Muadzam Shah'),
     'phg03': ('Maran', 'Chenor', 'Temerloh', 'Bera', 'Jerantut'),
     'phg04': ('Bentong', 'Raub', 'Kuala Lipis'),
     'phg05': ('Genting Sempah', 'Janda Baik', 'Bukit Tinggi'),
     'phg06': ('Bukit Fraser', 'Genting Highlands', 'Cameron Highlands'),
     'prk01': ('Tapah', 'Slim River', 'Tanjung Malim'),
     'prk02': ('Ipoh', 'Batu Gajah', 'Kampar', 'Sungai Siput', 'Kuala Kangsar'),
     'prk03': ('Pengkalan Hulu', 'Grid', 'Lenggong'),
     'prk04': ('Temenggung', 'Belum'),
     'prk05': ('Teluk Intan', 'Bagan Datoh', 'Kampung Gajah', 'Sri Iskandar', 'Beruas', 'Parit', 'Lumut', 'Setiawan', 'Pulau Pangkor'),
     'prk06': ('Selama' , 'Taiping' , 'Bagan Serai', 'Parit Buntar'),
     'prk07': 'Bukit Larut',
     'trg01': ('Kuala Terengganu', 'Marang'),
     'trg02': ('Besut', 'Setiu'),
     'trg03': 'Hulu Terengganu',
     'trg04': ('Kemaman', 'Dungun'),
     'jhr01': ('Pulau Aur', 'Pemanggil'),
     'jhr02': ('Kota Tinggi', 'Mersing', 'Johor Bahru'),
     'jhr03': ('Kluang', 'Pontian'),
     'jhr04': ('Batu Pahat', 'Muar', 'Segamat', 'Gemas'),
     'mlk01': ('Bandar Melaka', 'Melaka', 'Alor Gajah', 'Jasin', 'Masjid Tanah', 'Merlimau', 'Nyalas'),
     'ngs01': ('Jempol', 'Tampin'),
     'ngs02': ('Port Dickson', 'Seremban', 'Kuala Pilah', 'Jelebu', 'Rembau'),
     'pls01': ('Kangar', 'Perlis', 'Padang Besar', 'Arau'),
     'png01': ('Pulau Pinang', 'Penang'),
     'kdh01': ('Kota Setar', 'Kubang Pasu', 'Pokok Sena'),
     'kdh02': ('Pendang', 'Kuala Muda', 'Yan'),
     'kdh03': ('Padang Terap', 'Sik'),
     'kdh04': 'Baling',
     'kdh05': ('Kulim', 'Bandar Bahru'),
     'kdh06': 'Langkawi',
     'kdh07': 'Gunung Jerai',
     'sgr01': ('Hulu Langat', 'Sepang', 'Petaling', 'Petaling Jaya', 'Shah Alam', 'Rawang', 'Hulu Selangor', 'Gombak'),
     'sgr02': ('Sabak Bernam', 'Kuala Selangor', 'Klang', 'Kuala Langat'),
     'sgr03': 'Kuala Lumpur',
     'sgr04': 'Putrajaya',
     'wly02': 'Labuan'
     }
while True:
    s = input('Sila beri nama tempat tinggal anda:\n')
    tempoh = input('Anda mahu waktu solat untuk hari ini atau bulan ini{\'h\' untuk hari ini,'
                   'atau \'b\' untuk bulan ini}:\n')
    b = s.title()
    for k, v in d.items():
        for i in v:
            if b == i:
                key = k
        if b == v:
            key = k
    if tempoh == 'b' or tempoh == "'b'":
        bul = 'this_month'
        alamat = requests.get('http://api.kayrules.com/solatjakim/times/{}.json?zone={}&format=12-hour'.format(bul, key))
        solat = ('date', 'imsak', 'subuh', 'syuruk', 'zohor', 'asar', 'maghrib', 'isyak')
        data = alamat.json() # kita ambil maklumat dari web dan jadikan ia dict, method json digunakan sbb dict complex
                                # jika simple just guna alamat.text == jadi dict juga
        a = json.loads(json.dumps(data)) # kaedah ini sesuai jika dict nya agak complex, jika simple buang meth dumps
        for w in a['prayer_times']: # kita loop dlm val for key in a['prayer_times'] jadi w which is a dict type
            for asdf in solat: #kita loop tuple solat
                print(asdf, '==>', w[asdf])  # tetapkan bahawa kita just nak key from dict w same with tuple solat
    elif tempoh == 'h' or tempoh == "'h'":
        bul = 'today'
        alamat = requests.get('http://api.kayrules.com/solatjakim/times/{}.json?zone={}&format=12-hour'.format(bul, key))
        solat = ('date', 'imsak', 'subuh', 'syuruk', 'zohor', 'asar', 'maghrib', 'isyak')
        data = alamat.text
        a = json.loads(data)
        for q in solat:
            print(q, '==>', a['prayer_times'][q])

    order = input('Press \'q\' for exit or \'c\' to restart:\n')
    if order == 'c' or order == "'c'":
        continue
    elif order == 'q' or order == "'q'":
        quit()
