/*
 * tide.java
 * Created on 2002/01/16
 *
 * @author shintaro@umibozu
 *         mailto:umibozu@fish.plala.or.jp
 *         http://www7.plala.or.jp/umibozu/
 * @version 2.1
 * 表示を棒グラフに日数を次の土日２日表示に改変 ayuboke@yahoo.com
 * 日月出入り追加 2002/01/22　月齢桁他表示位置微修正2002/3/2
 * 港の切り替え表示に対応2002/3/26
 * tide.java verup2.1に対応修正2002/8/19
 * 閏年のバグ修正2004/8/2
 * 2007年の振替休日変更に対応（５月６日）2008/5/2
*/

import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class tide22 extends java.applet.Applet {
  //Image pic; /* 背景画像 */
  Image buf; /* ダブルバッファリング用 */
  Graphics dg; /* ダブルバッファリング用 */
  int err = 0; /* パラメータ読み込みエラー */
  int dialog = 0;
  int year, month, day;
  double itv = 20; /* 計算間隔 */
  double inc = 24 * 60 * 2 / itv + 2; /* 計算回数 */
  String portData[][] = new String[50][3];
  port pt = new port();

  public void init () {
    initComponents ();
    setSize(620, 380);
    setBackground(Color.lightGray);
    err = getParam(); /* パラメータ取得 */

    for(int i = 0; i < 2; i++)
     pt.ct[i] = new chancetable(); /* chancetableを初期化 */
    pt.tide(itv, inc, year, month, day); /* 潮時計算 */
    buf = createImage(620, 380); /* ダブルバッファリング準備 */
    dg = buf.getGraphics(); /* ダブルバッファリング準備 */
  }
  public void start() {
  }

  public void paint(Graphics g) {
    String[] weekday = {"日","月","火","水","木","金","土"};
    String[] tidename = {"大","中","小","長","若","中","大","中","小","長","若","中","大"};

      dg.setFont(new Font("Monospaced",Font.PLAIN,13));
	  dg.setColor(Color.lightGray);
      dg.fillRect(0, 0, 620, 380);
      dg.setColor(Color.black);
    /*if(pic != null) {
      dg.drawImage(pic, 0, 0, 600, 280, this);
    }*/

    if(err != 0) {
      dg.setColor(Color.red);
      dg.drawString("<param>タグを正しく読み取れませんでした.", 15, 20);
    } else {
      int x1, y1, x2 = 0, y2 = 0; /* グラフ座標 */
      //int x3 = 30, y3 = 220; /* テキスト用座標 */
      double sc; /* y軸のスケール */
      double cox = itv * 0.2 ;// 3.6; /* xの増分 */
     // double sunnie[] = new double[14];
      double moonnie[] = new double[2];
      double sunnie[] = new double[4];
      double sunak[] = new double[4];

      /* グラフのスケール調整 */
      if(pt.flood > 280) sc = 0.6;
      else if(pt.flood > 220) sc = 0.8;
      else if(pt.flood > 130) sc = 1.1;
      else if(pt.flood > 50) sc = 1.3;
      else sc = 4.0;

 	  int ghh = 0, ghd = 0;                /* ghh グラフ枠の最高　ghd グラフ枠の最低 */
	  if ( sc == 4 ) {ghh = 50;ghd = 30;}
	  if(sc == 1.3)  {ghh = 220;ghd = 30;};
	  if (sc == 1.1 )  {ghh = 270;ghd =30;};
	  if (sc == 0.8 ){ghh = 340;ghd =60;};
	  if (sc == 0.6 )  {ghh = 470;ghd =60;};
      int x0 = 30, y0 = 360 - (int)(ghd * sc); /* x,yの0点 表示の基準点を360に変更*/
	  dg.setColor(Color.white);  /* バックの白塗り */
	  dg.fillRect(x0,y0-(int)(ghh * sc),(int)(inc * cox)-8,(int)((ghh+ghd)*sc));
	  dg.fillRect( 30 , 12 , 290 , 15 );
	  
		/*バックの夜塗り*/
      for(int i = 0; i < 2; i++){
        sunak[i * 2] = sun_minute(pt.ct[i].sun_event[1])+ i*60*24;
        sunak[i * 2 + 1] = sun_minute(pt.ct[i].sun_event[5])+ i*60*24;
      }
      dg.setColor(new Color(0xddddde0));
	  dg.fillRect(x0,y0-(int)(ghh * sc),(int)(sunak[0]* cox / itv),(int)((ghh+ghd)*sc));
	  dg.fillRect(x0+(int)(sunak[1]* cox / itv),y0-(int)(ghh * sc),(int)(sunak[2]* cox / itv)-(int)(sunak[1]* cox / itv),(int)((ghh+ghd)*sc));
	  dg.fillRect(x0+(int)(sunak[3]* cox / itv),y0-(int)(ghh * sc),(int)(inc * cox)-(int)(sunak[3]* cox / itv)-8,(int)((ghh+ghd)*sc));

      /* 港データ表示 */
      dg.setColor(Color.black);
      dg.drawString(pt.name + " 緯度:" + pt.lat + " 経度:" + pt.lng +"   "+ year +"年", 40, 24);
      int x3 = x0 + (int)( 6 * 60 * cox / itv )+10, y3 = 63; /* テキスト用座標 */

      /* グラフ目盛数値表示 */
	  int jikan = 0;
	  for(int i = 0; i <= inc * cox; i += 2 * 60 * cox / itv){
		  dg.drawString("" + jikan, x0 +i-2 , 375 );
		  jikan +=2;
		  if(jikan == 24) jikan = 0;
	  }
	  if (ghh > 340){
		  dg.drawString("440", 4, y0 - (int)(440 * sc) + 5);
		  dg.drawString("400", 4, y0 - (int)(400 * sc) + 5);
		  dg.drawString("360", 4, y0 - (int)(360 * sc) + 5);

	  }
	  if (ghh > 270){
		  dg.drawString("320", 4, y0 - (int)(320 * sc) + 5);
		  dg.drawString("280", 4, y0 - (int)(280 * sc) + 5);
		  dg.drawString("-60", 4, y0 + (int)(60 * sc) + 5);

	  }
	  if (ghh > 220){
		dg.drawString("240", 4, y0 - (int)(240 * sc) + 5);
	  }
	  if (ghh > 50){
		dg.drawString("200", 4, y0 - (int)(200 * sc) + 5);
		dg.drawString("160", 4, y0 - (int)(160 * sc) + 5);
		dg.drawString("120", 4, y0 - (int)(120 * sc) + 5);
		dg.drawString("80" ,10, y0 - (int)(80 * sc) + 5);
	  }
      dg.drawString("40" ,10, y0 - (int)(40 * sc) + 5);
      dg.drawString("0"  ,15, y0  + 5);
      dg.drawString("-30", 4, y0 + (int)(30 * sc) + 5);
	  if (ghh == 50){
		dg.drawString("20", 4, y0 - (int)(20 * sc) + 5);
        dg.drawString("-20", 4, y0 + (int)(20 * sc) + 5);
	  }

	  dg.setColor(new Color(159, 159, 255));  /* グラフの罫線 */
      for(int i = 0; i <= inc * cox; i += 2 * 60 * cox / itv)
        dg.drawLine(x0 + i , y0 + (int)(ghd * sc), x0 + i, y0 - (int)(ghh * sc));
	  if (ghh == 50){
		  dg.drawLine(x0, y0 - (int)(30 * sc) , (int)(x0 + inc * cox)-8,y0 - (int)(30 * sc));
		  dg.drawLine(x0, y0 + (int)(30 * sc) , (int)(x0 + inc * cox)-8,y0 + (int)(30 * sc));
	  }
      dg.drawLine(x0, y0 + (int)(30 * sc) , (int)(x0 + inc * cox)-8, y0 + (int)(30 * sc));
      dg.drawLine(x0, y0 + (int)(20 * sc) , (int)(x0 + inc * cox)-8, y0 + (int)(20 * sc));
      dg.drawLine(x0, y0                  , (int)(x0 + inc * cox)-8, y0                 );
      dg.drawLine(x0, y0 - (int)(20 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(20 * sc));
      dg.drawLine(x0, y0 - (int)(40 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(40 * sc));
	  if (ghh > 50){
		dg.drawLine(x0, y0 - (int)(60 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(60 * sc));
		dg.drawLine(x0, y0 - (int)(80 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(80 * sc));
		dg.drawLine(x0, y0 - (int)(100 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(100 * sc));
		dg.drawLine(x0, y0 - (int)(120 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(120 * sc));
		dg.drawLine(x0, y0 - (int)(140 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(140 * sc));
		dg.drawLine(x0, y0 - (int)(160 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(160 * sc));
		dg.drawLine(x0, y0 - (int)(180 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(180 * sc));
		dg.drawLine(x0, y0 - (int)(200 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(200 * sc));
		dg.drawLine(x0, y0 - (int)(220 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(220 * sc));
	  }
	  if (ghh > 220){
		dg.drawLine(x0, y0 - (int)(240 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(240 * sc));
		dg.drawLine(x0, y0 - (int)(260 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(260 * sc));
	  }
	  if (ghh > 270){
		dg.drawLine(x0, y0 - (int)(280 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(280 * sc));
		dg.drawLine(x0, y0 - (int)(300 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(300 * sc));
		dg.drawLine(x0, y0 - (int)(320 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(320 * sc));
		dg.drawLine(x0, y0 - (int)(340 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(340 * sc));
		dg.drawLine(x0, y0 + (int)(60 * sc) , (int)(x0 + inc * cox)-8, y0 + (int)(60 * sc));

	  }
	  if (ghh > 340){
		dg.drawLine(x0, y0 - (int)(360 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(360 * sc));
		dg.drawLine(x0, y0 - (int)(380 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(380 * sc));
		dg.drawLine(x0, y0 - (int)(400 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(400 * sc));
		dg.drawLine(x0, y0 - (int)(420 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(420 * sc));
		dg.drawLine(x0, y0 - (int)(440 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(440 * sc));
		dg.drawLine(x0, y0 - (int)(460 * sc) , (int)(x0 + inc * cox)-8, y0 - (int)(460 * sc));
	  }

     
 	  dg.setColor(new Color(255,255,255));  /* 文字バックの白塗り */
	  dg.fillRect(x3-5,y3-12,160,75);
	  dg.fillRect(x3+(int)( 24 * 60 * cox / itv )-5,y3 -12,160,75);

      dg.setColor(Color.black);		/*市民薄明り表示*/
      for(int i = 0; i < 4; i++){
		  double sunakt = sunak[i];
		  sunakt = sunakt/60;
		  if(sunakt > 24){sunakt -= 24;}
        dg.drawString(""+ sun_print(sunakt),(int)(sunak[i]* cox / itv)-5,y0-(int)(ghh * sc)+10);
	  }

	/* for(int i = 0; i < 2; i++){
        //moonnie[i] = moon_minute(pt.ct[i].mmp) + i * 24 * 60;
        sunnie[i * 2] = sun_minute(pt.ct[i].sun_event[2]) + i * 24 * 60;
        sunnie[i * 2 + 1] = sun_minute(pt.ct[i].sun_event[4]) + i * 24 * 60;
      }*/

      /* グラフ表示 */
      for(int i = -2; i <= inc-2; i++) {
        if(i == 0) {
          x2 = x0;
          y2 = y0 - (int)(pt.tl[i + 2] * sc);
        }
        if(i > 0 && i < 24 * 60 * 7 / itv + 1) {
          x1 = x2;
          y1 = y2;
          x2 = (int)(x0 + i * cox);
          y2 = y0 - (int)(pt.tl[i + 2] * sc);
          dg.setColor(new Color(0,95,63));	/*棒グラフ表示 */
		  dg.drawRect(x1,y1-((y1-y2)/2),4,y0-y1+((y1-y2)/2)+(int)(ghd * sc));
		  dg.setColor(new Color(191,223,239));
		  dg.fillRect(x1+1,y1-((y1-y2)/2)+1,3,y0-y1+((y1-y2)/2)+(int)(ghd * sc)-1);
        }
      }
      for(int i = 0; i < 2; i++) {
      /* 月表示 */
		  int mwid = 25;
		  int xx0 = x3 + 15 + mwid*2; 
		  int yy0 = y3 - mwid * 2+20;
		  double wax = 0, wane = 0;
		  double Smd12 = pt.ct[i].Smd12;
		  if(0 <= Smd12 && Smd12 <180){
		  	  wax -= Math.cos(Smd12 * lib.dr);
		  	  wane = 1;
		  }else if(180 <= Smd12 && Smd12 <= 360){
		  	  wax =1;
		  	  wane -= Math.cos(Smd12 * lib.dr);
		  }
          //dg.setColor(new Color(0x000088));
          //dg.fillRect(xx0-mwid-2, yy0+mwid-2, mwid*2+4,mwid*2+4);
          dg.setColor(new Color(0xcccccc));
          dg.fillOval(xx0-mwid, yy0+mwid+1, mwid*2,mwid*2-1);
          dg.setColor(new Color(0xffff11));
		  for(int m = 0; m < mwid * 2; m++){
		  	  int arg = mwid - m;
		  	  int arg2 = mwid * mwid - arg * arg;
		  	  int xx1 = (int)(xx0 - Math.sqrt(arg2) * wax);
		  	  int xx2 = (int)(xx0 + Math.sqrt(arg2) * wane);
		  	  int yy = yy0 + mwid + m;
		  	  dg.drawLine(xx1, yy, xx2, yy);
		  }
        if(pt.ct[i].w == 0) dg.setColor(Color.red);
        else if(pt.ct[i].syuku == 1) dg.setColor(new Color(255,63,0));
        else if(pt.ct[i].w == 6) dg.setColor(Color.blue);
        else dg.setColor(Color.black);
      //dg.setFont(new Font("Monospaced",Font.PLAIN,14));
		dg.drawString(pt.ct[i].month + "月" + pt.ct[i].day + "日(" + weekday[pt.ct[i].w] + ")", x3 , y3);
        int age = (int)(pt.ct[i].age*10);
		int agel = age % 10;
		age = age / 10;
        //dg.drawString(tidename[tide(age)] + "潮(" + age + "."+ agel +")", x3 , y3 + 13);
        dg.drawString(tidename[tide(pt.ct[i].age)] + "潮(" + age + "."+ agel +")", x3 , y3 + 13);
        dg.drawString(" 日出 "+ sun_print(pt.ct[i].sun_event[2]),x3+78,y3+26);
        dg.drawString(" 日入 "+ sun_print(pt.ct[i].sun_event[4]),x3+78,y3+38);
        dg.drawString(" 月出 "+ pt.ct[i].hmo+":"+pt.ct[i].mmo,x3+78,y3+50);
        dg.drawString(" 月入 "+ pt.ct[i].hmi+":"+pt.ct[i].mmi,x3+78,y3+62);
        for(int j = 0; j < 8; j++) {
          if(pt.ct[i].hour[j] != 99)
            dg.drawString(dd(pt.ct[i].hour[j]) + ":" + dd(pt.ct[i].minute[j]) + pt.ct[i].leveld[j] + "cm", x3, y3 + 12 * j + 25);
		}
        x3 += (int)( 24 * 60 * cox / itv );
      }


	  dg.setColor(new Color(159, 159, 255));
      dg.drawLine(x0 + 1 , y0, (int)(x0 + inc * cox) - 9 , y0);
      dg.setColor(new Color(63, 63, 255));
      dg.drawLine(x0 + 1 , y0 - (int)(pt.level * sc), (int)(x0 + inc * cox) - 9 , y0 - (int)(pt.level * sc));
      //  grf.drawString("" + Math.round(level), 4, y0 - (int)(level * sc) + 5);
	  dg.setColor(new Color(255, 95, 95));
      dg.drawLine(x0 + 1 , y0 - (int)(pt.flood * sc), (int)(x0 + inc * cox) - 9 , y0 - (int)(pt.flood * sc));
      //  grf.drawString("" + Math.round(flood), 4, y0 - (int)(flood * sc) + 5);
      dg.drawLine(x0 + 1 , y0 - (int)(pt.ebb * sc), (int)(x0 + inc * cox) - 9 , y0 - (int)(pt.ebb * sc));
      // grf.drawString("" + Math.round(ebb), 4, y0 - (int)(ebb * sc) + 5);
     
    }
	g.drawImage(buf, 0, 0, this);
  }

  public void update(Graphics g){
    paint(g);
  }

  private void initComponents() {
    addMouseListener(new MouseAdapter() {
      public void mouseClicked(MouseEvent evt) {
        formMouseClicked(evt);
      }
    });
    setLayout(null);

    panel1 = new Panel();
    button1 = new Button("-28日");
    button2 = new Button("-7日");
    button3 = new Button("-1日");
    button4 = new Button("+1日");
    button5 = new Button("+7日");
    button6 = new Button("+28日");
    button7 = new Button("港変更");
    list1 = new List();


    button1.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(-28);
      }
    });
    add(button1);
    button1.setLocation(330, 0);
    button1.setSize(40, 18);

	button2.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(-7);
      }
    });
    add(button2);
    button2.setLocation(370, 0);
    button2.setSize(40, 18);
	
    button3.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(-1);
      }
    });
    add(button3);
    button3.setLocation(410, 0);
    button3.setSize(40, 18);
	
    button4.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(+1);
      }
    });
    add(button4);
    button4.setLocation(450, 0);
    button4.setSize(40, 18);
	
    button5.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(+7);
      }
    });
    add(button5);
    button5.setLocation(490, 0);
    button5.setSize(40, 18);
	
    button6.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
        changeDate(+28);
      }
    });
    add(button6);
    button6.setLocation(530, 0);
    button6.setSize(40, 18);
    
    button7.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent evt) {
    panel1.setBounds(400, 19, 220, 100);
      panel1.setVisible(true);
      dialog = 1;
      }
    });
    add(button7);
    button7.setLocation(570, 0);
    button7.setSize(50, 18);

	panel1.setLayout(null);
    panel1.setVisible(false);
    panel1.setBackground(new Color(212, 208, 200));
    add(panel1);

    list1.addItemListener(new ItemListener() {
      public void itemStateChanged(ItemEvent evt) {
        list1ItemStateChanged(evt);
      }
    });
    panel1.add(list1);
    list1.setBounds(2, 2, 216, 96);

  }

  private void formMouseClicked(MouseEvent evt) {
    if(dialog == 0) {
    	int msx = evt.getX();
    	int msy = evt.getY();
    	if(msy > 280){msy = 280;}
    	if(msx < 220){msx = 220;}
    	msx -= 220;
     panel1.setBounds(msx, msy, 220, 100);
   	
      panel1.setVisible(true);
      dialog = 1;
    } else {
      panel1.setVisible(false);
      dialog = 0;
    }
  }

  private void list1ItemStateChanged(ItemEvent evt) {
    List list = (java.awt.List)evt.getSource();
    int li = list.getSelectedIndex();
    err = pt.setParam(portData[li][0], portData[li][1], portData[li][2]);
    pt.tide(itv, inc, year, month, day);
    repaint();
    panel1.setVisible(false);
      dialog = 0;
  }

  void changeDate(int addDay) {
    Calendar cal = Calendar.getInstance();
    cal.set(Calendar.YEAR, year);
    cal.set(Calendar.MONTH, month - 1);
    cal.set(Calendar.DATE, day + addDay);
    year = cal.get(Calendar.YEAR);
    month = cal.get(Calendar.MONTH) + 1;
    day = cal.get(Calendar.DATE);
    pt.tide(itv, inc, year, month, day);
    repaint();
  }

  public void changeDateS(int yyy,int mmm,int ddd) {
    Calendar cal = Calendar.getInstance();
    cal.set(Calendar.YEAR, yyy);
    cal.set(Calendar.MONTH, mmm - 1);
    cal.set(Calendar.DATE, ddd);
    year = cal.get(Calendar.YEAR);
    month = cal.get(Calendar.MONTH) + 1;
    day = cal.get(Calendar.DATE);
    pt.tide(itv, inc, year, month, day);
    repaint();
  }

  public void changePort(String str0, String str1, String str2) {
    err = pt.setParam(str0, str1, str2);
    pt.tide(itv, inc, year, month, day);
    repaint();
  }

  String dd(int x) {
    if(x < 10) return "0" + x;
    else return "" + x;
  }

  int moon_minute(double x) {
    double h = lib.fix(x);
    double m = (x - h) * 60;
    return (int)(h * 60 + m);
  }

  String moon_print(double x) {
    double h = lib.fix(x);
    double m = (x - h) * 60;
    return dd((int)h) + ":" + dd((int)m);
  }

  int sun_minute(double x) {
    double h = Math.floor(x);
    double m = (x - h) * 60;
    return (int)(h * 60 + m);
  }

  String sun_print(double x) {
    double h = Math.floor(x);
    double m = (x - h) * 60;
    return dd((int)h) + ":" + dd((int)m);
  }

  /* パラメータを取得 */
  public int getParam() {

      Calendar cal = Calendar.getInstance(TimeZone.getTimeZone("JST"));
      cal.setTime(new Date());
      day = cal.get(Calendar.DATE);
		int w = cal.get(Calendar.DAY_OF_WEEK)-1;
		if(w < 6 && w > 0){int ww = 6 - w ;
						   cal.set(Calendar.DATE, day + ww);
	  }
     String str = getParameter("date"); /* 表示年月日を取得 */
    if(str != null) {
      int days = Integer.parseInt(str);
      cal.set(Calendar.DATE,day + days);
    }
     year = cal.get(Calendar.YEAR);
      month = cal.get(Calendar.MONTH) + 1;
      day = cal.get(Calendar.DATE);	
   //str = getParameter("pic"); /* 背景画像を取得 */
    //if(str != null) {
    //  pic = getImage(getDocumentBase(), str);
    //}
    //String str0 = getParameter("port"); /* 港データを取得 */
    //String str1 = getParameter("hr");
    //String str2 = getParameter("pl");
    //int err = pt.setParam(str0, str1, str2);
    int j = 0;
    for(int i = 0; i < 50; i++) {
      portData[j][0] = getParameter("port" + i); /* 港データを取得 */
      if(portData[j][0] == null)
        continue;
      portData[j][1] = getParameter("hr" + i);
      portData[j][2] = getParameter("pl" + i);
      StringTokenizer strST = new StringTokenizer(portData[j][0], ",");
      list1.add(strST.nextToken());
      j++;
    }
    int err = pt.setParam(portData[0][0], portData[0][1], portData[0][2]);
    return err;
  }


  int tide(double age) {
    int k = 0;
    if(age <= 1.5) k = 0;
    else if(age <= 5.5) k = 1; 
    else if(age <= 8.5) k = 2;
    else if(age <= 9.5) k = 3;
    else if(age <= 10.5) k = 4;
    else if(age <= 12.5) k = 5;
    else if(age <= 16.5) k = 6;
    else if(age <= 20.5) k = 7;
    else if(age <= 23.5) k = 8;
    else if(age <= 24.5) k = 9;
    else if(age <= 25.5) k = 10;
    else if(age <= 27.5) k = 11;
    else if(age <= 30.5) k = 12;
    return k;
  }

  private Panel panel1;
  private Label label1;
  private Button button1;
  private Button button2;
  private Button button3;
  private Button button4;
  private Button button5;
  private Button button6;
  private Button button7;
  private List list1;
}

/**********************************************************
 *
 * lagrange補完法 極点を求める
 *
 **********************************************************/

class lagrange {
  int k = 0;
  int[] sg = {0,0,0,0,0};
  double[] tt = {0,0,0,0,0};
  double[] tm = {0,0,0,0,0};
  double[] fx = {0,0,0,0,0};
  double[] df = {0,0,0,0,0};
  double lag1, lag2;

  int check(double t, double y) {
    double itv, fnn;
    k++;
    tm[1] = tm[2];
    tm[2] = tm[3];
    tm[3] = tm[4];
    tm[4] = t;
    fx[1] = fx[2];
    fx[2] = fx[3];
    fx[3] = fx[4];
    fx[4] = y;
    df[1] = df[2];
    df[2] = df[3];
    df[3] = fx[4] - fx[3];
    sg[1] = sg[2];
    sg[2] = sg[3];
    sg[3] = lib.sgn(df[3]);
    if(k > 3 && sg[1] != sg[2]) {
      itv = tm[4] - tm[3];
      tt[1] = tm[1] + itv / 2;
      tt[2] = tm[2] + itv / 2;
      tt[3] = tm[3] + itv / 2;
      fnn = (0 - df[1]) / (df[2] - df[1]);
      lag1 = (1 - fnn) * (2 - fnn) * tt[1] / 2 + fnn * (2 - fnn) * tt[2] - (1 - fnn) * fnn * tt[3] / 2;
      if(lag1 > 0) {
        fnn = (lag1 - tm[2]) / (tm[3] -tm[2]);
        lag2 = (1 - fnn) * (2 - fnn) * fx[2] / 2 + fnn * (2 - fnn) * fx[3] - (1 - fnn) * fnn * fx[4] / 2;
        return 1;
      } else return 0;
    } else return 0;
  }
}

/**********************************************************
 *
 *  class chancetable 潮時表
 *
 **********************************************************/

class chancetable {
  int year;
  int month;
  int day;
  int w;
  int hour[] = new int[8];
  int minute[] = new int[8];
  int level[] = new int[8];
  String leveld[] = new String[8];
  double sun_event[] = new double[7];
  double age;
  double M_O;     //出MJD
  double M_S;     //南中
  double M_I;     //入
  double L_O;     //出LST
  double L_S;     //南中
  double L_I;     //入
  int add_cnt1,add_cnt3,sub_cnt1,sub_cnt3;
  double dt0;
  double dt0n;
  double z;
  String hso,mso,hsi,msi;
  String hmo,mmo,hmi,mmi;
  double Smd12;

  int syuku;
  int syukuchec;

  void setDate(int y, int m, int d, double zt,double lat, double lng) {
    year = y;
    month = m;
    day = d;
    w = weekday(y, m, d);
    z = serial(year, month, day);
    moon(z, zt, lat, lng);
    sun(z, zt, lat, lng);
    SunR(z, lat, lng);
    syuku(y, m, d);
  }

  int weekday(int y, int m, int d) {
    Calendar cal = Calendar.getInstance();
    cal.set(Calendar.YEAR, y);
    cal.set(Calendar.MONTH, m - 1);
    cal.set(Calendar.DATE, d);
    return cal.get(Calendar.DAY_OF_WEEK) - 1;
  }


  int syuku(int y, int m, int d) {
    Calendar cal = Calendar.getInstance();
    cal.set(Calendar.YEAR, y);
    cal.set(Calendar.MONTH, m - 1);
    cal.set(Calendar.DATE, d);
    syukuchec(y, m, d);
	if((cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY) && (syuku == 0)){syukuchec(y,m,d-1);}
	return syuku;}
	int syukuchec(int y, int m, int d){
		syuku = 0;
	    Calendar cal = Calendar.getInstance();
	    cal.set(Calendar.YEAR, y);
	    cal.set(Calendar.MONTH, m - 1);
	    cal.set(Calendar.DATE, d);
		switch(m){
		case 1:
				if(d == 1){syuku = 1;}
				else if((cal.get(Calendar.DAY_OF_WEEK_IN_MONTH) == 2) && (cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY)){syuku = 1;}
			break;
		case 2:
				if(d == 11){syuku = 1;}
			break;
		case 3:
			int hbun = (int)(20.8431 + (0.242194 * (y-1980)) - (int)((y-1980)/4));
				if(d == hbun){syuku = 1;}
			break;
		case 4:
				if(d == 29){syuku = 1;}
			break;
		case 5:
				if(d == 3){syuku = 1;}
				else if(d == 4){syuku = 1;}
				else if(d == 5){syuku = 1;}
				else if(d == 6){
					if(cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY){syuku = 1;}
					else if(cal.get(Calendar.DAY_OF_WEEK)==Calendar.TUESDAY){syuku = 1;}
					else if(cal.get(Calendar.DAY_OF_WEEK)==Calendar.WEDNESDAY){syuku = 1;}
				}
			break;
		case 7:
				if((cal.get(Calendar.DAY_OF_WEEK_IN_MONTH) == 3) && (cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY)){syuku = 1;}
			break;
		case 9:
			hbun = (int)(23.2488 + (0.242194 * (y-1980)) - (int)((y-1980)/4));
				if(d == hbun){syuku = 1;}
				else if(d == (hbun-1) && cal.get(Calendar.DAY_OF_WEEK)==Calendar.TUESDAY){syuku = 1;}
				else if((cal.get(Calendar.DAY_OF_WEEK_IN_MONTH) == 3) && (cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY)){syuku = 1;}
			break;
		case 10:
				if((cal.get(Calendar.DAY_OF_WEEK_IN_MONTH) == 2) && (cal.get(Calendar.DAY_OF_WEEK)==Calendar.MONDAY)){syuku = 1;}
			break;
		case 11:
				if(d == 3){syuku = 1;}
				else if(d == 23){syuku = 1;}
			break;
		case 12:
				if(d == 23){syuku = 1;}
			break;
		}
		return syuku;
  }





  double fnc(double b, double t, double c) {
    double arg = b * t + c;
    arg -= Math.floor(arg / 360) * 360;
    return Math.cos(arg * lib.dr);
  }

  double lat_moon(double x) {
    double bt;
    bt = 5.1281 * fnc(483202.019, x, 3.273);
    bt += 0.2806 * fnc(960400.89, x, 138.24);
    bt += 0.2777 * fnc(6003.15, x, 48.31);
    bt += 0.1733 * fnc(407332.2 , x, 52.43);
    return bt;
  }

  double long_moon(double x) {
    double lm = 218.316;
    double arg= 481267.8809 * x;
    arg -= Math.floor(arg / 360) * 360;
    lm += arg - 0.00133 * x * x;
    lm += 6.2888 * fnc(477198.868, x, 44.963);
    lm += 1.274 * fnc(413335.35, x, 10.74);
    lm += 0.6583 * fnc(890534.22, x, 145.7);
    lm += 0.2136 * fnc(954397.74, x, 179.93);
    lm += 0.1851 * fnc(35999.05, x, 87.53);
    lm += 0.1144 * fnc(966404.0, x, 276.5);
    lm += 0.0588 * fnc(63863.5, x, 124.2);
    lm += 0.0571 * fnc(377336.3, x, 13.2);
    lm += 0.0533 * fnc(1367733.1, x, 280.7);
    lm += 0.0458 * fnc(854535.2, x, 148.2);
    lm += 0.0409 * fnc(441199.8, x, 47.4);
    lm += 0.0347 * fnc(445267.1, x, 27.9);
    lm += 0.0304 * fnc(513197.9, x, 222.5);
    return lib.rnd36(lm);
  }

  double long_sun(double x) {
    double g = lib.rnd36(36000.77 * x) + 357.53; 
    return lib.rnd36(g - (77.06 - 1.91 * Math.sin(g * lib.dr)));
  }

  void moon(double z, double zt, double lat, double lng) {
    //double tu, t, tg, lm, bt, sp, hp, sd, p, u, v, w, ra, dc, lha, hr;
    double td12 = z + (180 - zt) / 360;
    double ls12 = long_sun(td12 / 36525);
    double lm12 = long_moon(td12 / 36525);
   /* mmp = moon_meripass(z, zt, lng);
    mmp = (mmp + zt) / 15;
    if(mmp > 24)
      mmp = 99;*/
    Smd12 = lm12 - ls12;
    if(Smd12 < 0) Smd12 += 360;
    double td = td12 - 29.5305 * Smd12 / 360;
    td = moonage(3, td, 0);
    age = td12 - td;
  }

  /*double moon_meripass(double z, double zt, double lng) {
    int flg = 0, j = 0;
    double dt = 360;
    double tu = 165 - lng, tu2 = 0;
    double t, tg, lm, bt, p, u, v, ra, lha, lst = 0, mp = 0;
    while(flg < 2) {
      j = 0;
      dt = 360;
      while(Math.abs(dt) > 0.1) {
        j++;
        t = (z + tu / 360) / 36525;
        tg = lib.rnd36(100.4604 + 36000.7695 * t + 360 * (tu / 360));
        lm = long_moon(t);
        bt = lat_moon(t);
        p = 23.43928 - 0.01300417 * t;
        u = Math.cos(bt * lib.dr) * Math.cos(lm * lib.dr);
        v = Math.cos(bt * lib.dr) * Math.sin(lm * lib.dr) * Math.cos(p * lib.dr) - Math.sin(bt * lib.dr) * Math.sin(p * lib.dr);
        ra = lib.rnd36(Math.atan2(v, u) * lib.rd);
        lha = lib.rnd18(tg - ra + lng);
        tu -= lha;
        lst = tu + zt;
        dt = tu - tu2;
        tu2 = tu;
      }
      mp = tu;
      if( flg == 0 && lst < 0) {
        tu += 360;
        flg = 1;
      } else
        flg = 2;
    }
    //return  mp - (0.1);
    return  mp;
  }*/

  double moonage(int inc, double td, double smd) {
    double lm, ls;
    for(int i = 1; i < inc; i++) {
      lm = long_moon(td / 36525);
      ls = long_sun(td / 36525);
      td -= 29.5305 * lib.rnd18(lm - ls - smd) / 360;
    }
    return td;
  }

  double riseset(double x, double lat, double dc) {
    double arg = (Math.sin(x * lib.dr) - Math.sin(lat * lib.dr) * Math.sin(dc * lib.dr)) / Math.cos(lat * lib.dr) / Math.cos(dc * lib.dr);
    if(arg < -1 || 1 < arg)
      return 360;
    else
      return Math.acos(arg) * lib.rd;
  }

  void sun(double z, double zt, double lat, double lng) {
    sun_event[3] = sun_meripass(z, lng);
    double tu = sun_event[3];
    sun_event[0] = sun_eventtime(-18, -1, tu, z, lat, lng);
    if(sun_event[0] != 360)
      tu = sun_event[0];
    sun_event[1] = sun_eventtime(-6, -1, tu, z, lat, lng);
    if(sun_event[1] != 360)
      tu = sun_event[1];
    sun_event[2] = sun_eventtime(-54.2 / 60, -1, tu, z, lat, lng);
    tu = sun_event[3];
    sun_event[6] = sun_eventtime(-18, 1, tu, z, lat, lng);
    if(sun_event[6] != 360)
      tu = sun_event[6];
    sun_event[5] = sun_eventtime(-6, 1, tu, z, lat, lng);
    if(sun_event[5] != 360)
      tu = sun_event[5];
    sun_event[4] = sun_eventtime(-54.2 / 60, 1, tu, z, lat, lng);
    for(int i = 0; i < 7; i++) {
      if(sun_event[i] != 360.0 )
        sun_event[i] = (sun_event[i] + zt) / 15;
    }
  }

  double sun_eventtime(double als, double sg, double tu, double z, double lat, double lng) {
    double u, v, w, ra, dc, tg, lha;
    double hr, lst;
    for(int i = 1; i < 3; i++) {
      u = Math.cos(long_sun((z + tu / 360) / 36525) * lib.dr);
      v = Math.sin(long_sun((z + tu / 360) / 36525) * lib.dr) * Math.cos(23.44 * lib.dr);
      w = Math.sin(long_sun((z + tu / 360) / 36525) * lib.dr) * Math.sin(23.44 * lib.dr);
      ra = lib.rnd36(Math.atan2(v, u) * lib.rd);
      dc = Math.atan(w / Math.sqrt(u * u + v * v)) * lib.rd;
      tg = lib.rnd36(100.4604 + 36000.7695 * (z + tu / 360) / 36525 + 360 * (tu / 360));
      lha = lib.rnd36(tg - ra) + lng;
      if(lha > 180)
        lha -= 360;
      if(lha < -180)
        lha += 360;
      hr = riseset(als, lat, dc);
      if(hr == 360)
        return 360;
      tu = hr * sg + tu - lha;
      lst = tu + lng;
      if(lst < 0 || 360 < lst)
        return 0;
    }
    return tu;
  }

  double sun_meripass(double z, double lng) {
    double u, v, w, ra, tg, lha;
    double tu = 180 - lng;
    for(int i = 1; i < 3; i++) {
      u = Math.cos(long_sun((z + tu / 360) / 36525) * lib.dr);
      v = Math.sin(long_sun((z + tu / 360) / 36525) * lib.dr) * Math.cos(23.44 * lib.dr);
      w = Math.sin(long_sun((z + tu / 360) / 36525) * lib.dr) * Math.sin(23.44 * lib.dr);
      ra = lib.rnd36(Math.atan2(v, u) * lib.rd);
      tg = lib.rnd36(100.4604 + 36000.7695 * (z + tu / 360) / 36525 + 360 * (tu / 360));
      lha = lib.rnd36(tg - ra) + lng;
      if(lha > 180)
        lha -= 360;
      if(lha < -180)
        lha += 360;
      tu -= lha;
    }
    return tu;
  }

  /* 2000年1月1日を第1日とする通日 */
  double serial(int year, int month, int day) {
    if(month < 3) {
      year--;
      month += 12;
    }
    double a = lib.fix(year / 100);
    int b = (int)(2 - a + lib.fix(a / 4));
    double c = lib.fix(365.25 * year);
    double z = lib.fix(30.6001 * (month + 1)) + b + c + day;
    z -= 730550.5; 
    return z;
  }
  

  /*日の出日の入り時間計算*/
  //void SunR(int yy, int mm, int dd, double lat, double lng){
  void SunR(double z, double lat, double lng){
	double mjd0;
	double mjd0n;
	double mjd12;
	double dt12;
	double m_out,m_in;
	mjd0 = z + 51544.125;
	dt0 = (0.671262 + 1.002737909 * (mjd0 - 40000) + lng/360);
	mjd0n = mjd0 + 1.0;
	dt0n = (0.671262 + 1.002737909 * (mjd0n - 40000) + lng/360);
	mjd12 = mjd0 + 0.5;
	dt12 = (0.671262 + 1.002737909 * (mjd12 - 40000) + lng/360);
	
	

	/*月の出入り計算*/
	add_cnt1 = 0;
	add_cnt3 = 0;
	sub_cnt1 = 0;
	sub_cnt3 = 0;
	MoonPS(1,mjd12,dt12,lat,lng);
	double dt = (0.671262 + 1.002737909 * (M_S - 40000) + lng/360);
	MoonPS(0,M_S,dt,lat,lng);
	double mjd_out = M_O;
	double mjd_in = M_I;
	dt = (0.671262 + 1.002737909 * (mjd_out - 40000) + lng/360);
	MoonPS(1,mjd_out,dt,lat,lng);
	double m_out1 = M_O;
	dt = (0.671262 + 1.002737909 * (M_O - 40000) + lng/360);
	MoonPS(1,M_O,dt,lat,lng);
	double m_out2= M_O;
	if (m_out1 > m_out2) {
	if ((m_out1 - m_out2) > 0.7) {
			m_out = -1;
			} else {m_out = m_out2;}
		} else {
		if ((m_out2 - m_out1) > 0.7) {
			m_out = -1;} else {m_out = m_out2;}
		}
	dt = (0.671262 + 1.002737909 * (mjd_in - 40000) + lng/360);
	MoonPS(3,mjd_in,dt,lat,lng);
	double m_in1 = M_I;
	dt = (0.671262 + 1.002737909 * (M_I - 40000) + lng/360);
	MoonPS(3,M_I,dt,lat,lng);
	double m_in2 = M_I;
	if (m_in1 > m_in2) {
		if ((m_in1 - m_in2) > 0.7) {
		m_in = -1;
		} else {
		m_in = m_in2;
		}
	} else {
		if ((m_in2 - m_in1) > 0.7) {
			m_in = -1;
			} else {
			m_in = m_in2;
			}
			}
		if (m_out > 0) {
			dt = (0.671262 + 1.002737909 * (m_out - 40000) + lng/360);
			MoonPS(1,m_out,dt,lat,lng);
			m_out = M_O;
		}
		if (m_in > 0) {
			dt = (0.671262 + 1.002737909 * (m_in - 40000) + lng/360);
			MoonPS(3,m_in,dt,lat,lng);
			m_in = M_I;
		}
	double tout = (m_out - Math.floor(m_out)) + 0.375;
	if (tout >=1) {tout = tout - 1;}
	if (m_out >= mjd0 && m_out < (mjd0 + 1) ) {
		int thmo = (int)(Math.floor(tout * 24));
		int tmmo = (int)(Math.round((tout * 24 - thmo)*60));
		if (tmmo == 60) {tmmo = 0;thmo = thmo + 1;
			if (thmo == 24) {thmo = 23;tmmo = 59;}
			}
		if (thmo < 10) {hmo = "0" + thmo;}else{hmo = "" + thmo;}
		if (tmmo < 10) {mmo = "0" + tmmo;}else{mmo = "" + tmmo;}
	}else{hmo ="--"; mmo = "--";}
	
	double tin = (m_in - Math.floor(m_in)) + 0.375;
	if (tin >=1) {tin = tin - 1;}
	if (m_in >= mjd0 && m_in < (mjd0 + 1) ) {
		int thmi = (int)(Math.floor(tin * 24));
		int tmmi = (int)(Math.round((tin * 24 - thmi)*60));
		if (tmmi == 60) {tmmi = 0;thmi = thmi + 1;
			if (thmi == 24) {thmi = 23;tmmi = 59;}
		}
		if (thmi < 10) {hmi = "0" + thmi;}else{hmi = "" + thmi;}
		if (tmmi < 10) {mmi = "0" + tmmi;}else{mmi = "" + tmmi;}
	}else{hmi ="--"; mmi = "--";}
  }
  
  
  double CalcEpsilon(double mjd){   /*黄道傾斜角*/
	double t, e;
	t = (mjd - 51544.5 + 0.00074074) / 36525.0;
	e = 23.4393 - 0.0130 * t + 0.0026 * Math.cos((1934 * t + 235) * lib.dr);
	return e;
  }
  
  /*月の出南中入り時刻計算*/
  void MoonPS(int mode, double mjd, double dt,double lat, double lng){
  	double y = CalcLambda(mjd);
  	double b = CalcBeta(mjd);
  	double e = CalcEpsilon(mjd);
  	double rb = b / lib.rd;
  	double ry = y / lib.rd;
  	double re = e / lib.rd;
  	double xs = Math.cos(rb)*Math.sin(ry)*Math.sin(re) + Math.sin(rb)*Math.cos(re);
  	double d  = Math.asin(xs);
  	double c = Math.cos(rb) * Math.cos(ry);
  	double s = Math.cos(rb)*Math.sin(ry)*Math.cos(re) - Math.sin(rb)* Math.sin(re);
  	double a = Math.atan(s/c);
  	if (c < 0) {a = a + lib.pi;};
  	if (a < 0) {a = a + lib.pi * 2;};
  	double ri = lat * lib.dr;
  	double ct = - Math.tan(ri)*Math.tan(d);
  	ct = ct + Math.cos(89.61667*lib.dr)/(Math.cos(ri) * Math.cos(d));
  	double t = Math.acos(ct);
  	L_O = (a - t)/(2*lib.pi);
  	L_S = a/(2*lib.pi);
  	L_I = (a + t)/(2*lib.pi);
  	double dti = Math.floor(dt);
  	if (mode == 1) {  /* 出の補正*/
  		if ((dti + L_O) < dt0 && sub_cnt1 == 0) {
  		dti = dti + 1;
  		add_cnt1 = add_cnt1 + 1;
  		} else if ((dti + L_O) > (dt0n) && add_cnt1 == 0) {
  		dti = dti - 1;
  		sub_cnt1 = sub_cnt1 + 1;}
  	} else if (mode == 2) {  /*南中の補正*/
  		if ((dti + L_S) < dt0) {
  		dti = dti + 1;
  		} else if ((dti + L_S) > (dt0n)) {
  		dti = dti - 1;}
  	} else if (mode == 3) {   /*入の時刻計算の時の補正*/
  		if (L_I > 1) {
  		L_I = L_I - 1;}
  		if ((dti + L_I) < dt0 && sub_cnt3 == 0) {
  		dti = dti + 1;
  		add_cnt3 = add_cnt3 + 1;
  		} else if ((dti + L_I) > (dt0n) && add_cnt3 == 0) {
  		dti = dti - 1;
  		sub_cnt3 = sub_cnt3 + 1;}
  	}    /*地方恒星時からMJDへの逆算*/
  	M_O = 40000 + (dti + L_O -0.671262 - lng/360)/1.002737909;
  	M_S = 40000 + (dti + L_S -0.671262 - lng/360)/1.002737909;
  	M_I = 40000 + (dti + L_I -0.671262 - lng/360)/1.002737909;
  }
  
  double CalcLambda(double mjd){   /*月視黄径*/
	double t, y;
	t = (mjd - 51544.5 + 0.00074074) / 36525.0;  // δT:64秒固定
	y = 218.3166 + 481267.8811 * t - 0.0015 * t * t;
	y += 6.2888 * Math.cos((477198.868 * t + 44.963) * lib.dr);
	y += 1.274 * Math.cos((413335.35 * t + 10.74) * lib.dr);
	y += 0.6583 * Math.cos((890534.22 * t + 145.70) * lib.dr);
	y += 0.2136 * Math.cos((954397.74 * t + 179.93) * lib.dr);
	y += 0.1851 * Math.cos((35999.05 * t + 87.53) * lib.dr);
	y += 0.1144 * Math.cos((966404.0 * t + 276.5) * lib.dr);
	y += 0.0588 * Math.cos((63863.5 * t + 124.2) * lib.dr);
	y += 0.0571 * Math.cos((377336.3 * t + 13.2) * lib.dr);
	y += 0.0533 * Math.cos((1367733.1 * t + 280.7) * lib.dr);
	y += 0.0458 * Math.cos((854535.2 * t + 148.2) * lib.dr);
	y += 0.0409 * Math.cos((441199.8 * t + 47.4) * lib.dr);
	y += 0.0347 * Math.cos((445267.1 * t + 27.9) * lib.dr);
	y += 0.0304 * Math.cos((513197.9 * t + 222.5) * lib.dr);
	y += 0.0154 * Math.cos((75870 * t + 41) * lib.dr);
	y += 0.0125 * Math.cos((1443603 * t + 52) * lib.dr);
	y += 0.011 * Math.cos((489205 * t + 142) * lib.dr);
	y += 0.0107 * Math.cos((1303870 * t + 246) * lib.dr);
	y += 0.01 * Math.cos((1431597 * t + 315) * lib.dr);
	y += 0.0085 * Math.cos((826671 * t + 111) * lib.dr);
	y += 0.0079 * Math.cos((449334 * t + 188) * lib.dr);
	y += 0.0068 * Math.cos((926533 * t + 323) * lib.dr);
	y += 0.0052 * Math.cos((31932 * t + 107) * lib.dr);
	y += 0.005 * Math.cos((481266 * t + 205) * lib.dr);
	y = y % 360.0;
	if (y < 0) {y += 360.0;}
	return y;
	}
	
  double CalcBeta(double mjd){   /*月視黄緯*/
	double t,b;
	t = (mjd - 51544.5 + 0.00074074) / 36525.0;  // δt:64秒固定
	b = 5.1281 * Math.cos((483202.019 * t + 3.273) * lib.dr);
	b += 0.2806 * Math.cos((960400.89 * t + 138.24) * lib.dr);
	b += 0.2777 * Math.cos((6003.15 * t + 48.31) * lib.dr);
	b += 0.1733 * Math.cos((407332.20 * t + 52.43) * lib.dr);
	b += 0.0554 * Math.cos((896537.4 * t + 104.0) * lib.dr);
	b += 0.0463 * Math.cos((69866.7 * t + 82.5) * lib.dr);
	b += 0.0326 * Math.cos((1373736.2 * t + 239.0) * lib.dr);
	b += 0.0172 * Math.cos((1437599.8 * t + 273.2) * lib.dr);
	b += 0.0093 * Math.cos((884531 * t + 187) * lib.dr);
	b += 0.0088 * Math.cos((471196 * t + 87) * lib.dr);
	b += 0.0082 * Math.cos((371333 * t + 55) * lib.dr);
	return b;
	}
}

/**********************************************************
 *
 *  class port
 *
 **********************************************************/

class port {
  String name; /* 港 */
  //int year, month, day;
  double zt; /* zone time */
  double lat, lng; /* 緯度 経度 */
  double level, flood, ebb; /* 平均 満潮 干潮の水面高 */
  double hr[] = new double[40]; /* 調和定数 */
  double pl[] = new double[40]; /* 調和定数 */
  double tl[] = new double[285]; /* 潮位 */
  chancetable ct[] = new chancetable[7];

  int setParam(String str0, String str1, String str2) {
    Double buff;
    try {
      StringTokenizer strST = new StringTokenizer(str0, ",");
      name = strST.nextToken();
      buff = Double.valueOf(strST.nextToken());
      lat = buff.doubleValue();  
      buff = Double.valueOf(strST.nextToken());
      lng = buff.doubleValue();  
      buff = Double.valueOf(strST.nextToken());
      level = buff.doubleValue();  
      zt = Math.floor((lng + 7.5) / 15) * 15;
      if(nippon(lat, lng) == 1) zt = 135; 		strST = new StringTokenizer(str1, ",");
      for(int i = 0; i < 40; i++) {
        buff = Double.valueOf(strST.nextToken());
        hr[i] = buff.doubleValue();  
      }
      strST = new StringTokenizer(str2, ",");
      for(int i = 0; i < 40; i++) {
        buff = Double.valueOf(strST.nextToken());
        pl[i] = buff.doubleValue();  
      }
      flood = level + hr[24];
      ebb = level - hr[24];
      return 0;
    } catch (Exception e) {
      return 1;
    }
  }

  void tide(double itv, double inc, int year, int month, int day) {
    lagrange lag = new lagrange();
    int[] m = {31,31,28,31,30,31,30,31,31,30,31,30,31}; /* 各月の日数 */
    Calendar fcal = Calendar.getInstance();
    fcal.set(Calendar.YEAR, year);
    fcal.set(Calendar.MONTH, 2);
    fcal.set(Calendar.DATE, 0);
    int fdate = fcal.get(Calendar.DATE);
    m[2] = fdate;
    int[] nc = {0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,6,6}; /* 分潮の波数 */
    double[] ags = {0.0410686,0.0821373,0.5443747,1.0158958,1.0980331,13.3986609,13.4715145,13.9430356,14.0251729,14.4920521,14.9178647,14.9589314,15.0000000,15.0410686,15.0821353,15.1232059,15.5854433,16.0569644,16.1391017,27.8953548,27.9682084,28.4397295,28.5125831,28.9019669,28.9841042,29.4556253,29.5284789,29.9589333,30.0000000,30.0410667,30.0821373,31.0158958,42.9271398,43.4761563,44.0251729,45.0410686,57.9682084,58.9841042,86.9523127,87.9682084}; /* 分潮の角速度 */
    double vl[] = new double[40]; /* 天文引数 */
    double f[] = new double[40]; /* 天文因数 */
    double v[] = new double[40];
    double u[] = new double[40];
    double f0[] = new double[10];
    double u0[] = new double[10];

    /* 潮汐計算用通日 tz */
    int tz = serial(month, day, m) + (int)lib.fix((year + 3) / 4) - 500;

    /* 太陽・月の軌道要素 s, h, p, n */
    double ty = year - 2000;
    double s = lib.rnd36(211.728 + lib.rnd36(129.38471 * ty) + lib.rnd36(13.176396 * tz));
    double h = lib.rnd36(279.974 + lib.rnd36(-0.23871 * ty) + lib.rnd36(0.985647 * tz));
    double p = lib.rnd36(83.298 + lib.rnd36(40.66229 * ty) + lib.rnd36(0.111404 * tz));
    double n = lib.rnd36(125.071 + lib.rnd36(-19.32812 * ty) + lib.rnd36(-0.052954 * tz));

    /* 天文引数を求める */
    v[0] = h;
    v[1] = 2 * h;
    v[2] = s - p;
    v[3] = 2 * s - 2 * h;
    v[4] = 2 * s;
    v[5] = -3 * s + h + p + 270;
    v[6] = -3 * s + 3 * h - p + 270;
    v[7] = -2 * s + h + 270;
    v[8] = -2 * s + 3 * h - 270;
    v[9] = -s + h + 90;
    v[10] = -2 * h + 192;
    v[11] = -h + 270;
    v[12] = 180;
    v[13] = h + 90;
    v[14] = 2 * h + 168;
    v[15] = 3 * h + 90;
    v[16] = s + h - p +  90;
    v[17] = 2 * s - h - 270;
    v[18] = 2 * s + h + 90;
    v[19] = -4 * s + 2 * h + 2 * p;
    v[20] = -4 * s + 4 * h;
    v[21] = -3 * s + 2 * h + p;
    v[22] = -3 * s + 4 * h - p;
    v[23] = -2 * s + 180;
    v[24] = -2 * s + 2 * h;
    v[25] = -s + p + 180;
    v[26] = -s + 2 * h - p + 180;
    v[27] = -h + 282;
    v[28] = 0;
    v[29] = h + 258;
    v[30] = 2 * h;
    v[31] = 2 * s - 2 * h;
    v[32] = -4 * s + 3 * h + 270;
    v[33] = -3 * s + 3 * h + 180;
    v[34] = -2 * s + 3 * h + 90;
    v[35] = h + 90;
    v[36] = -4 * s + 4 * h;
    v[37] = -2 * s + 2 * h;
    v[38] = -6 * s + 6 * h;
    v[39] = -4 * s + 4 * h;

    double n1 = Math.sin(n * lib.dr);
    double n2 = Math.sin(lib.rnd36(n * 2) * lib.dr);
    double n3 = Math.sin(lib.rnd36(n * 3) * lib.dr);
    u0[0] = 0;
    u0[1] = -23.74 * n1 + 2.68 * n2 - 0.38 * n3;
    u0[2] = 10.80 * n1 - 1.34 * n2 + 0.19 * n3;
    u0[3] = -8.86 * n1 + 0.68 * n2 - 0.07 * n3;
    u0[4] = -12.94 * n1 + 1.34 * n2 - 0.19 * n3;
    u0[5] = -36.68 * n1 + 4.02 * n2 - 0.57 * n3;
    u0[6] = -2.14 * n1;
    u0[7] = -17.74 * n1 + 0.68 * n2 - 0.04 * n3;
    double cu = 1 - 0.2505 * Math.cos(p * 2 * lib.dr) - 0.1102 * Math.cos((p * 2 - n) * lib.dr) - 0.0156 * Math.cos((p * 2 - n * 2) * lib.dr) - 0.0370 * Math.cos(n * lib.dr);
    double su = -0.2505 * Math.sin(p * 2 * lib.dr) - 0.1102 * Math.sin((p * 2 - n) * lib.dr) - 0.0156 * Math.sin((p * 2 - n * 2) * lib.dr) - 0.0370 * Math.sin(n * lib.dr);
    u0[8] = Math.atan2(su, cu) * lib.rd;
    cu = 2 * Math.cos(p * lib.dr) + 0.4 * Math.cos((p - n) * lib.dr);
    su = Math.sin(p * lib.dr) + 0.2 * Math.cos((p - n) * lib.dr);
    u0[9] = Math.atan2(su, cu) * lib.rd;

    u[0] = 0;
    u[1] = 0;
    u[2] = 0;
    u[3] = -u0[6];
    u[4] = u0[1];
    u[5] = u0[2];
    u[6] = u0[2];
    u[7] = u0[2];
    u[8] = u0[6];
    u[9] = u0[9];
    u[10] = 0;
    u[11] = 0;
    u[12] = 0;
    u[13] = u0[3];
    u[14] = 0;
    u[15] = 0;
    u[16] = u0[4];
    u[17] = -u0[2];
    u[18] = u0[5];
    u[19] = u0[6];
    u[20] = u0[6];
    u[21] = u0[6];
    u[22] = u0[6];
    u[23] = u0[2];
    u[24] = u0[6];
    u[25] = u0[6];
    u[26] = u0[8];
    u[27] = 0;
    u[28] = 0;
    u[29] = 0;
    u[30] = u0[7];
    u[31] = -u0[6];
    u[32] = u0[6] + u0[2];
    u[33] = u0[6] * 1.5;
    u[34] = u0[6] + u0[3];
    u[35] = u0[3];
    u[36] = u0[6] * 2;
    u[37] = u0[6];
    u[38] = u0[6] * 3;
    u[39] = u0[6] * 2;

    for(int i = 0; i < 40 ; i++) {
      v[i] = lib.rnd36(v[i] + u[i]);
      vl[i] = lib.rnd36(v[i] + lng * nc[i] - ags[i] * zt / 15);
    }

    /* 天文因数 f */
    n1 = Math.cos(n * lib.dr);
    n2 = Math.cos(lib.rnd36(n * 2) * lib.dr);
    n3 = Math.cos(lib.rnd36(n * 3) * lib.dr);
    f0[0] = 1.0000 - 0.1300 * n1 + 0.0013 * n2;
    f0[1] = 1.0429 + 0.4135 * n1 - 0.0040 * n2;
    f0[2] = 1.0089 + 0.1871 * n1 - 0.0147 * n2 + 0.0014 * n3;
    f0[3] = 1.0060 + 0.1150 * n1 - 0.0088 * n2 + 0.0006 * n3;
    f0[4] = 1.0129 + 0.1676 * n1 - 0.0170 * n2 + 0.0016 * n3;
    f0[5] = 1.1027 + 0.6504 * n1 + 0.0317 * n2 - 0.0014 * n3;
    f0[6] = 1.0004 - 0.0373 * n1 + 0.0002 * n2;
    f0[7] = 1.0241 + 0.2863 * n1 + 0.0083 * n2 - 0.0015 * n3;
    cu = 1 - 0.2505 * Math.cos(p * 2 * lib.dr) - 0.1102 * Math.cos((p * 2 - n) * lib.dr) - 0.0156 * Math.cos((p * 2 - n * 2) * lib.dr) - 0.0370 * Math.cos(n * lib.dr);
    su = -0.2505 * Math.sin(p * 2 * lib.dr) - 0.1102 * Math.sin((p * 2 - n) * lib.dr) - 0.0156 * Math.sin((p * 2 - n * 2) * lib.dr) - 0.0370 * Math.sin(n * lib.dr);
    double arg = Math.atan2(su, cu) * lib.rd;
    f0[8] = su / Math.sin(arg * lib.dr);
    cu = 2 * Math.cos(p * lib.dr) + 0.4 * Math.cos((p - n) * lib.dr);
    su = Math.sin(p * lib.dr) + 0.2 * Math.cos((p - n) * lib.dr);
    arg = Math.atan2(su, cu) * lib.rd;
    f0[9] = cu / Math.cos(arg * lib.dr);

    f[0] = 1;
    f[1] = 1;
    f[2] = f0[0];
    f[3] = f0[6];
    f[4] = f0[1];
    f[5] = f0[2];
    f[6] = f0[2];
    f[7] = f0[2];
    f[8] = f0[6];
    f[9] = f0[9];
    f[10] = 1;
    f[11] = 1;
    f[12] = 1;
    f[13] = f0[3];
    f[14] = 1;
    f[15] = 1;
    f[16] = f0[4];
    f[17] = f0[2];
    f[18] = f0[5];
    f[19] = f0[6];
    f[20] = f0[6];
    f[21] = f0[6];
    f[22] = f0[6];
    f[23] = f0[2];
    f[24] = f0[6];
    f[25] = f0[6];
    f[26] = f0[8];
    f[27] = 1;
    f[28] = 1;
    f[29] = 1;
    f[30] = f0[7];
    f[31] = f0[6];
    f[32] = f0[6] * f0[2];
    f[33] = Math.pow(f0[6], 1.5);
    f[34] = f0[6] * f0[3];
    f[35] = f0[3];
    f[36] = Math.pow(f0[6], 2);
    f[37] = f0[6];
    f[38] = Math.pow(f0[6], 3);
    f[39] = Math.pow(f0[6], 2);

    Calendar cal = Calendar.getInstance();
    for(int i = 0; i < 2; i++) {
      cal.set(Calendar.YEAR, year);
      cal.set(Calendar.MONTH, month - 1);
      cal.set(Calendar.DATE, day + i);
      int yy = cal.get(Calendar.YEAR);
      int mm = cal.get(Calendar.MONTH) + 1;
      int dd = cal.get(Calendar.DATE);
      ct[i].setDate(yy, mm, dd, zt, lat, lng);
    }

    lag.k = 0;
    int dcnt = 0;
    int cnt = 0;

    for(int i = 0; i <= inc + 2; i++) {
      tl[i] = level;
      for(int j = 0; j < 40; j++) {
        tl[i] += f[j] * hr[j] * Math.cos((vl[j] + ags[j] * (i - 2) / (60 / itv) - pl[j]) * lib.dr);
      }
      if(lag.check(itv * (i - 2), tl[i]) == 1) {
        double dd = Math.floor(lag.lag1 / 60 / 24);
        if(dcnt < dd) {
          for(int j = cnt; j < 8; j++) {
            ct[dcnt].hour[j] = 99;
          }
          dcnt++;
          cnt = 0;
        }
        if(dcnt < 2) {
          if(cnt < 8) {
            ct[dcnt].hour[cnt] = (int)Math.floor(lag.lag1 / 60) - dcnt * 24;
            ct[dcnt].minute[cnt] = (int)(lag.lag1 - (ct[dcnt].hour[cnt] + dcnt * 24) * 60);
            //ct[dcnt].level[cnt] = (int)lag.lag2;
            if((int)lag.lag2 < -100){ct[dcnt].leveld[cnt] = "" + (int)lag.lag2;}
            	else if((int)lag.lag2 < -10){ct[dcnt].leveld[cnt] = " " + (int)lag.lag2;}
            	else if((int)lag.lag2 < -0){ct[dcnt].leveld[cnt] = "  " + (int)lag.lag2;}
            	else if((int)lag.lag2 < 10){ct[dcnt].leveld[cnt] = "   " + (int)lag.lag2;}
            	else if((int)lag.lag2 < 100){ct[dcnt].leveld[cnt] = "  " + (int)lag.lag2;}
            	else{ct[dcnt].leveld[cnt] = " " + (int)lag.lag2;}
          }
          cnt++;
        }
      }
    }
    if(dcnt < 2) {
      for(int j = cnt; j < 8; j++) {
        ct[dcnt].hour[j] = 99;
      }
    }
  }

  /* 年初からの経過日数 */
  int serial(int month, int day, int m[]) {
    int d = 0;
    for(int i = 1; i < month; i++) d += m[i];
    d += day - 1;
    return d;
  }
  
   int nippon (double lat, double lng){ 
    int nip = 0; 
    if(lat > 24) { 
      if(122 <= lng && lng < 128 && lat < 32) nip = 1; 
      if(128 <= lng && lng < 131 && lat < 35) nip = 1; 
      if(131 <= lng && lng < 138 && lat < 38) nip = 1; 
      if(138 <= lng && lng < 148 && lat < 46) nip = 1; 
    } 
    return nip; 
  }

}

/**********************************************************
 *
 *  class lib
 *
 **********************************************************/

class lib {
  static double dr = 0.0174532925199433; /* degree to radian */
  static double rd = 57.29577951308232; /* radian to degree */
  static double pi = 3.14159265358979;

  static double fix(double x) {
    if(x >= 0) return Math.floor(Math.abs(x));
    else return -Math.floor(Math.abs(x));
  }

  static double rnd36(double x) {
    return x - Math.floor(x / 360) * 360;
  }

  static double rnd18(double x) {
    return x - lib.fix((x + lib.sgn(x) * 180) / 360) * 360;
  }

  static int sgn(double x) {
    if(x < 0) return -1;
    else if(x > 0) return 1;
    else return 0;
  }
}

