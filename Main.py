from Classification import Classification
import os
import time
import numpy as np
class Main:

    @staticmethod
    def main():
        array_data = {}
        path_data_uji = './Data/Data latih'
        array_kelas = []
        for root, dirs, files in os.walk(path_data_uji, topdown=False):
            for name in files:
                if name.endswith('.txt'):
                    get_root = root.split('/')
                    if (len(get_root) == 4):
                        array_kelas.append(get_root[3])
                        key = root.replace("./", "")
                        path_file = os.path.join(key, name)
                        data_docs = open(path_file, 'r', encoding="ISO-8859-1").read()
                        if key in array_data:
                            temp = array_data[key]
                            temp.append(data_docs)
                            array_data[key] = temp
                        else:
                            array_data[key] = [data_docs]
        array_document = [data for value in array_data.values() for data in value]
        path_data_uji = './Data/Data uji'
        print(len(array_document))

        array_data_testing = {}
        array_kelas_testing = []
        for root, dirs, files in os.walk(path_data_uji, topdown=False):
            for name in files:
                if name.endswith('.txt'):
                    get_root = root.split('/')
                    if (len(get_root) == 4):
                        array_kelas_testing.append(get_root[3])
                        key = root.replace("./", "")
                        path_file = os.path.join(key, name)
                        data_docs = open(path_file, 'r', encoding="ISO-8859-1").read()
                        if key in array_data_testing:
                            temp = array_data_testing[key]
                            temp.append(data_docs)
                            array_data_testing[key] = temp
                        else:
                            array_data_testing[key] = [data_docs]
        array_document_testing = [data for value in array_data_testing.values() for data in value]

        # document =['Sekarang saya sedang suka memasak. Masakan kesukaan saya sekarang adalah nasi goreng. Cara memasak nasi goreng adalah nasi digoreng','Ukuran nasi sangatlah kecil, namun saya selalu makan nasi','Nasi berasal dari beras yang ditanam di sawah. Sawah berukuran kecil hanya bisa ditanami sedikit beras','Mobil dan bus dapat mengangkut banyak penumpang. Namun, bus berukuran jauh lebih besar dari mobil, apalagi mobil-mobilan','Bus pada umumnya berukuran besar dan berpenumpang banyak, sehingga bus tidak bisa melewati pemukiman','mobil formula satu melaju kencang di dalam balapan, max verstapen memenangkan gp brazil kemarin, namun sayang ke 2 kuda merah terpaksa gagal finish karena bertberakan satus sama lain','piere gasly memenangkan ajang perlombaan balap yang digelar di brazil kemarin.Mobil yang dikendarainya melaju kencang, namun sayang ke 2 ferari gagal finish karena bertaberakan satu sama lain.mobil melaju cepat, licah gesti dan tak terkalahkan'],['terjadi kelangkaan beras di dalam Indonesia sehingga harus mengimpor beras dari thailand.Padahal lahan sawah di Indonesia banyak',' bus buatan scania sukses dipasar menjadi bus terbesar di jagat raya.Bus ini dapat dinaiki oleh banyak penumpan.Dan lebih besar dari pada mobil']
        # kelas =['A', 'A', 'C', 'B', 'B','D','D','C','B']
        # klasifikasi= Classification()
        # klasifikasi.train(array_document, array_kelas)
        # klasifikasi.testing(array_document_testing,array_kelas_testing)


start_time = time.time()
Main.main()
awal = ['health', 'health', 'health', 'health', 'health', 'health', 'food', 'food', 'food', 'food', 'food', 'food', 'finance', 'finance', 'finance', 'finance', 'finance', 'finance', 'inet', 'inet', 'inet', 'inet', 'inet', 'inet', 'sport', 'sport', 'sport', 'sport', 'sport', 'sport']
akhir = ['health', 'health', 'food', 'health', 'health', 'health', 'finance', 'finance', 'food', 'health', 'health', 'health', 'health', 'health', 'health', 'health', 'health', 'health', 'finance', 'health', 'health', 'finance', 'health', 'health', 'health', 'health', 'health', 'health', 'health', 'health']

count=0
for x in range(len(awal)):
    if awal[x] is akhir[x]:
       count+=1

print(len(awal))
print(count/len(awal)*100)

print("--- %s seconds ---" % (time.time() - start_time))

