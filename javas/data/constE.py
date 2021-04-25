"""
Names and positions of constellations
"""

db = """
Andromeda,And,0,40,+38
Monoceros,Mon,7,0,-3
Sagittarius,Sgr,19,0,-25
Delphinus,Del,20,40,+12
Indus,Ind,21,20,-58
Pisces,Psc,0,20,+10
Lepus,Lep,5,25,-20
Bootes,Boo,14,35,+30
Hydra,Hya,10,30,-20
Eridanus,Eri,3,50,-30
Taurus,Tau,4,30,+18
Canis Major,CMa,6,40,-24
Lupus,Lup,15,0,-40
Ursa Major,UMa,11,0,+58
Virgo,Vir,13,20,-2
Aries,Ari,2,30,+20
Orion,Ori,5,20,+3
Pictor,Pic,5,30,-52
Cassiopeia,Cas,1,0,+60
Dorado,Dor,5,0,-60
Cancer,Cnc,8,30,+20
Coma Berenices,Com,12,40,+23
Chamaeleon,Cha,10,40,-78
Corvus,Crv,12,20,-18
Corona Borealis,CrB,15,40,+30
Tucana,Tuc,23,45,-68
Auriga,Aur,6,0,+42
Camelopardalis,Cam,5,40,+70
Pavo,Pav,19,10,-65
Cetus,Cet,1,25,-12
Cepheus,Cep,22,0,+70
Centaurus,Cen,13,20,-47
Microscopium,Mic,20,50,-37
Canis Minor,CMi,7,30,+6
Equuleus,Equ,21,10,+6
Vulpecula,Vul,20,10,+6
Ursa Minor,UMi,15,40,+78
Leo Minor,LMi,10,20,+33
Crater,Crt,11,20,-15
Lyra,Lyr,18,45,+36
Circinus,Cir,14,50,-63
Ara,Ara,17,10,-55
Scorpius,Sco,16,30,-26
Triangulum,Tri,2,0,+32
Leo,Leo,10,30,+15
Norma,Nor,16,0,-50
Scutum,Sct,18,35,-10
Caelum,Cae,4,50,-38
Sculptor,Scl,0,30,-35
Grus,Gru,22,20,-47
Mensa,Men,5,40,-77
Libra,Lib,15,10,-14
Lacerta,Lac,22,25,+43
Horologium,Hor,3,20,-52
Volans,Vol,7,40,-69
Puppis,Pup,7,40,-32
Musca,Mus,12,30,-70
Cygnus,Cyg,20,30,+43
Octans,Oct,21,0,-87
Columba,Col,5,40,-34
Apus,Aps,16,0,-76
Gemini,Gem,7,0,+22
Pegasus,Peg,22,30,+17
Serpens,Ser,15,35,+10
Ophiuchus,Oph,17,10,-5
Hercules,Her,17,10,+27
Perseus,Per,3,20,+42
Vela,Vel,9,30,-45
Telescopium,Tel,19,0,-52
Phoenix,Phe,1,0,-48
Antlia,Ant,10,0,-35
Aquarius,Aqr,22,20,-13
Hydrus,Hyi,2,40,-70
Crux,Cru,12,20,-60
Piscis Austrinus,PsA,22,10,-60
Corona Australis,CrA,18,30,-41
Triangulum Australe,TrA,15,40,-65
Sagitta,Sge,19,40,+18
Capricornus,Cap,20,50,-20
Lynx,Lyn,7,50,+45
Pyxis,Pyx,8,50,-28
Draco,Dra,17,0,+60
Carina,Car,8,40,-62
Canes Venatici,Car,8,40,-62
Reticulum,Ret,3,50,-63
Fornax,For,2,30,-33
Sextans,Sex,10,10,-1
Aquila,Aql,19,30,+2
"""

for lines in db.strip().split('\n'):
    line = lines.split(',')
    name = str(line[0])
    h1 = int(line[2])
    m1 = int(line[3])
    ra = (h1 * 60 + m1)/4.
    dec = int(line[4])

    filed1 = ('%s' % name)
    filed3 = ('%s' % ra)
    filed4 = ('%s' % dec)
    prn = '\t"'+filed1+'":{Ra:'+filed3+',Dec:'+filed4+'},'
    print(prn)
