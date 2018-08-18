"""
星座名、英名、略語、赤経、赤緯　（天文年鑑2018 p.298）
"""

db = """
アンドロメダ,Andromeda,And,0,40,+38
いっかくじゅう,Monoceros,Mon,7,0,-3
いて,Sagittarius,Sgr,19,0,-25
いるか,Delphinus,Del,20,40,+12
インディアン,Indus,Ind,21,20,-58
うお,Pisces,Psc,0,20,+10
うさぎ,Lepus,Lep,5,25,-20
うしかい,Bootes,Boo,14,35,+30
うみへび,Hydra,Hya,10,30,-20
エリダヌス,Eridanus,Eri,3,50,-30
おうし,Taurus,Tau,4,30,+18
おおいぬ,Canis Major,CMa,6,40,-24
おおかみ,Lupus,Lup,15,0,-40
おおぐま,Ursa Major,UMa,11,0,+58
おとめ,Virgo,Vir,13,20,-2
おひつじ,Aries,Ari,2,30,+20
オリオン,Orion,Ori,5,20,+3
がか,Pictor,Pic,5,30,-52
カシオペア,Cassiopeia,Cas,1,0,+60
かじき,Dorado,Dor,5,0,-60
かに,Cancer,Cnc,8,30,+20
かみのけ,Coma Berenices,Com,12,40,+23
カメレオン,Chamaeleon,Cha,10,40,-78
からす,Corvus,Crv,12,20,-18
かんむり,Corona Borealis,CrB,15,40,+30
きょしちょう,Tucana,Tuc,23,45,-68
ぎょしゃ,Auriga,Aur,6,0,+42
きりん,Camelopardalis,Cam,5,40,+70
くじゃく,Pavo,Pav,19,10,-65
くじら,Cetus,Cet,1,25,-12
ケフェウス,Cepheus,Cep,22,0,+70
ケンタウルス,Centaurus,Cen,13,20,-47
けんびきょう,Microscopium,Mic,20,50,-37
こいぬ,Canis Minor,CMi,7,30,+6
こうま,Equuleus,Equ,21,10,+6
こぎつね,Vulpecula,Vul,20,10,+6
こぐま,Ursa Minor,UMi,15,40,+78
こじし,Leo Minor,LMi,10,20,+33
コップ,Crater,Crt,11,20,-15
こと,Lyra,Lyr,18,45,+36
コンパス,Circinus,Cir,14,50,-63
さいだん,Ara,Ara,17,10,-55
さそり,Scorpius,Sco,16,30,-26
さんかく,Triangulum,Tri,2,0,+32
しし,Leo,Leo,10,30,+15
じょうぎ,Norma,Nor,16,0,-50
たて,Scutum,Sct,18,35,-10
ちょうこくぐ,Caelum,Cae,4,50,-38
ちょうこくしつ,Sculptor,Scl,0,30,-35
つる,Grus,Gru,22,20,-47
テーブルさん,Mensa,Men,5,40,-77
てんびん,Libra,Lib,15,10,-14
とかげ,Lacerta,Lac,22,25,+43
とけい,Horologium,Hor,3,20,-52
とびうお,Volans,Vol,7,40,-69
とも,Puppis,Pup,7,40,-32
はえ,Musca,Mus,12,30,-70
はくちょう,Cygnus,Cyg,20,30,+43
はちぶんぎ,Octans,Oct,21,0,-87
はと,Columba,Col,5,40,-34
ふうちょう,Apus,Aps,16,0,-76
ふたご,Gemini,Gem,7,0,+22
ペガスス,Pegasus,Peg,22,30,+17
へび,Serpens,Ser,15,35,+10
へびつかい,Ophiuchus,Oph,17,10,-5
ヘルクレス,Hercules,Her,17,10,+27
ペルセウス,Perseus,Per,3,20,+42
ほ,Vela,Vel,9,30,-45
ぼうえんきょう,Telescopium,Tel,19,0,-52
ほうおう,Phoenix,Phe,1,0,-48
ポンプ,Antlia,Ant,10,0,-35
みずがめ,Aquarius,Aqr,22,20,-13
みずへび,Hydrus,Hyi,2,40,-70
みなみじゅうじ,Crux,Cru,12,20,-60
みなみのうお,Piscis Austrinus,PsA,22,10,-60
みなみのかんむり,Corona Australis,CrA,18,30,-41
みなみのさんかく,Triangulum Australe,TrA,15,40,-65
や,Sagitta,Sge,19,40,+18
やぎ,Capricornus,Cap,20,50,-20
やまねこ,Lynx,Lyn,7,50,+45
らしんばん,Pyxis,Pyx,8,50,-28
りゅう,Draco,Dra,17,0,+60
りゅうこつ,Carina,Car,8,40,-62
りょうけん,Canes Venatici,Car,8,40,-62
レチクル,Reticulum,Ret,3,50,-63
ろ,Fornax,For,2,30,-33
ろくぶんぎ,Sextans,Sex,10,10,-1
わし,Aquila,Aql,19,30,+2
"""

constellations = {}

def build_constellations():
    global constellations
    import ephem
    for lines in db.strip().split('\n'):
        line = lines.split(',')
        namej = str(line[0])
        h1 = str(line[3])
        m1 = str(line[4])
        ra = ('%s:%s:00' % (h1, m1))

        h2 = str(line[5])
        dec = ('%s:00:00' % (h2))

        filed1 = ('%s,' % namej)
        filed2 = 'f|T,'
        filed3 = ('%s,' % ra)
        filed4 = ('%s,' % dec)
        filed5 = ','
        filed6 = '2000,'
        filed7 = '0'

        EADDB = filed1+filed2+filed3+filed4+filed5+filed6+filed7

        constellation = ephem.readdb(EADDB)
        constellations[constellation.name] = constellation

build_constellations()
del build_constellations

def constellation(name, *args, **kwargs):
    constellation = constellations[name].copy()
    if args or kwargs:
        constellation.compute(*args, **kwargs)
    return constellation

import math
import numpy as np
import ephem
#import planisfunc as plf

offset = 10

class const_namesJ:
    def __init__(self, observe, ax, zo):
    
        const = []
        for line in db.split('\n'):
            try:
                name = line.split(',')[0]
                constz = constellation(name)
                const.append(constz)

            except:
                None

        for i in range(len(const)):
            const[i].compute(observe)

        NAME = np.array([str(body.name) for body in const])
        RA   = np.array([float(body._ra) for body in const])
        DEC  = np.array([float(body._dec) for body in const])

        X = np.degrees(RA)
        Y = np.degrees(DEC)

        X -= offset
        Y -= offset

        for n in range(len(NAME)):
            ax.text(X[n], Y[n], NAME[n], color='white',
                    fontsize=10, alpha=0.6, zorder=zo)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from observe import *
    import sky

    fig, ax = plt.subplots()

    ax.set_aspect('equal')

    sf = sky.skyfield(obs, ax, zo=0, legend=True)
    cn = const_namesJ(obs, ax, zo=1)

    plt.xlim(- np.pi/2., np.pi/2.)
    plt.ylim(- np.pi/2., np.pi/2.)

    ax.axis('off')
    plt.show()

