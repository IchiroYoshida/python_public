# 年次毎の60分潮データ取得と保存
# 2019-06-22 Ichiro Yoshida

year = '2019'

import urllib.request
import jmadata as jma

for no in jma.No:
    n = int(no) - 1
    if year in jma.Year[n]:
        url = jma.url1 + jma.Symbol[n] + jma.url2

    with urllib.request.urlopen(url) as response:
        html_utf8 = response.read().decode('utf-8')
        response.close()

    parser = jma.JMAParser2()
    parser.feed(html_utf8)

    Speed = parser.list[0::3]
    Amp = parser.list[1::3]
    Deg = parser.list[2::3]

    file_name = './'+year+'/' + jma.Name[n] + '.TD3'
    f = open(file_name,'w')

    str = '{0:<},'.format(jma.Name[n])+\
          '{:>6},'.format(jma.Lat[n])+\
          '{:>6},'.format(jma.Lon[n])+\
          '{:>5}'.format(jma.MSL1[n])+'\n'
    f.write(str)

    for n in range(0,60, 2):
        str = '{:<4},'.format(jma.CompSymb[n])+\
              '{:>5},'.format(Amp[n])+\
              '{:>6},'.format(Deg[n])+\
              '      '+\
              '{:<4},'.format(jma.CompSymb[n+1])+\
              '{:>5},'.format(Amp[n+1])+\
              '{:>6}'.format(Deg[n+1])+'\n'
        f.write(str)
    f.close()
