from Preprocessing import Preprocessing
from Weighting import Weighting
from Classification import Classification

class Main:
    @staticmethod
    def main():

        document =[['Sekarang saya sedang suka memasak. Masakan kesukaan saya sekarang adalah nasi goreng. Cara memasak nasi goreng adalah nasi digoreng'],['Ukuran nasi sangatlah kecil, namun saya selalu makan nasi'],['Nasi berasal dari beras yang ditanam di sawah. Sawah berukuran kecil hanya bisa ditanami sedikit beras'],['Mobil dan bus dapat mengangkut banyak penumpang. Namun, bus berukuran jauh lebih besar dari mobil, apalagi mobil-mobilan'],['Bus pada umumnya berukuran besar dan berpenumpang banyak, sehingga bus tidak bisa melewati persawahan']]
        kelas =['A', 'A', 'B', 'B', 'C']
        klasifikasi= Classification()
        klasifikasi.train(document, kelas)
        new_docs='nasi goreng pedas'
        klasifikasi.testing(new_docs,'A')



Main.main()
