#https://ikatakos.com/pot/programming/python/packages/simplekml

import simplekml
  
class PlotKml:
    # スタイルは適当に、simplekmlやKMLのドキュメントを見つつ好みに変更する
    # マーカーのスタイル１
    STYLE_I = simplekml.Style()
    STYLE_I.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png'
    STYLE_I.labelstyle.scale = 0.66
    STYLE_I.labelstyle.color = 'aaffffff'
    # マーカーのスタイル２
    STYLE_H = simplekml.Style()
    STYLE_H.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    STYLE_H.labelstyle.scale = 0.66
    STYLE_H.labelstyle.color = 'aaffffff'
    # ラインのスタイル
    STYLE_LS = simplekml.Style()
    STYLE_LS.linestyle.width = 3
 
 
    def __init__(self):
        self.kml = simplekml.Kml()
 
    def new(self):
        self.kml = simplekml.Kml()
 
    def draw_dots(self, lnglats, descriptions, style=None, linestring=True):
        """
        :param lnglats: [[lng, lat], [lng, lat], [], ...]
        :param descriptions: <name>属性に出力するタグ
        :param style: simplekml.Style のインスタンスまたはそのリスト
        :param linestring: 線が不要ならFalse
        """
        # descriptionsは、lnglatsと同じ要素数の文字列のリストで与える。
        #   対応する順番の文字列が、自動的に連番prefixを付与され、マーカーの横に添えられる
        # styleは、Noneなら全てデフォルト
        #   simplekml.Styleの（単独の）インスタンスの場合は全てそのスタイルに
        #   リストの場合はlnglatsと同じ要素数にする。対応する順番のマーカーがそのスタイルになる
 
        if descriptions is None:
            descriptions = [''] * len(lnglats)
        else:
            assert len(lnglats) == len(descriptions)
 
        if style is None:
            style = [self.STYLE_I] * len(lnglats)
        elif type(style) == simplekml.Style:
            style = [style] * len(lnglats)
        elif type(style) == list:
            assert len(lnglats) == len(style)
 
        for idx, (lnglat, description) in enumerate(zip(lnglats, descriptions)):
            pnt = self.kml.newpoint(name=str(idx) + ' ' + description, coords=[lnglat])
            pnt.style = style[idx]
 
        if linestring:
            ls = self.kml.newlinestring(name='LineString', coords=lnglats)
            ls.style = self.STYLE_LS
 
    def save(self, path):
        self.kml.save(path)
 
# --使い方--
pk = PlotKml()
pk.draw_dots([[124.3490, 24.5653], [124.3571, 24.5836]],       # lnglats
             ['2023/05/23 Start', '2023/05/23 End'])  # descriptions
pk.save('ika.kml')
 
#pk.new()  # リセット(これをしないと前のが残る。敢えて残すことも可)
#pk.draw_dots([[-112.35, 42.89], ...], style=PlotKml.STYLE_H)
#pk.save('out2.kml')
