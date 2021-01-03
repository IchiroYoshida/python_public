<?php
/** moonage.php
 * 月の満ち欠けを描く（PHP5以上）
 *
 * @copyright	(c)studio pahoo
 * @author		パパぱふぅ
 * @参考URL		http://www.pahoo.org/e-soul/webtech/phpgd/phpgd-17-01.shtm
 *
 * [コマンドライン・パラメータ]
 * moonage.php?age=月齢（0.0≦月齢≦30.0）
 * （例）moonage.php?age=12.8
*/
// 初期化処理 ================================================================
define('INTERNAL_ENCODING', 'UTF-8');
mb_internal_encoding(INTERNAL_ENCODING);
mb_regex_encoding(INTERNAL_ENCODING);
define('MYSELF', basename($_SERVER['SCRIPT_NAME']));
define('REFERENCE', 'http://www.pahoo.org/e-soul/webtech/phpgd/phpgd-17-01.shtm');

//プログラム・タイトル
define('TITLE', '月の満ち欠けを描く');

//リリース・フラグ（公開時にはTRUEにすること）
define('FLAG_RELEASE', FALSE);

//満月の画像
//　PNG形式限定
//　正方形で，領域いっぱいに真円の満月が描かれていること．
//　背景は透明であること．
define('FULLMOON', 'fullmoon.png');

//影の透明度（0～127）：0 は完全に不透明な状態。 127 は完全に透明な状態
define('ALPHA', 30);

//明部分を白色で塗るかどうか
define('MOON_BRIGHT', FALSE);

//画像を保存するフォルダ
define('SAVE_PATH', './');

//PHP5判定
if (! isphp5over()) {
	echo 'Error > Please let me run on PHP5 or more...';
	exit(1);
}

/**
 * 共通HTMLヘッダ
 * @global string $HtmlHeader
*/
$encode = INTERNAL_ENCODING;
$title = TITLE;
$HtmlHeader =<<< EOD
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="{$encode}">
<title>{$title}</title>
<meta name="author" content="studio pahoo" />
<meta name="copyright" content="studio pahoo" />
<meta name="ROBOTS" content="NOINDEX,NOFOLLOW" />
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
</head>

EOD;

/**
 * 共通HTMLフッタ
 * @global string $HtmlFooter
*/
$HtmlFooter =<<< EOD
</html>

EOD;

// サブルーチン ==============================================================
/**
 * エラー処理ハンドラ
*/
function myErrorHandler ($errno, $errmsg, $filename, $linenum, $vars) {
	echo "Sory, system error occured !";
	exit(1);
}
error_reporting(E_ALL);
if (FLAG_RELEASE)	$old_error_handler = set_error_handler('myErrorHandler');

/**
 * PHP5以上かどうか検査する
 * @return	bool TRUE：PHP5以上／FALSE:PHP5未満
*/
function isphp5over() {
	$version = explode('.', phpversion());

	return $version[0] >= 5 ? TRUE : FALSE;
}

/**
 * 指定したボタンが押されてきたかどうか
 * @param	string $btn  ボタン名
 * @return	bool TRUE＝押された／FALSE＝押されていない
*/
function isButton($btn) {
	if (isset($_GET[$btn]))		return TRUE;
	if (isset($_POST[$btn]))	return TRUE;
	return FALSE;
}

/**
 * 指定したパラメータを取り出す
 * @param	string $key  パラメータ名（省略不可）
 * @param	bool   $auto TRUE＝自動コード変換あり／FALSE＝なし（省略時：TRUE）
 * @param	mixed  $def  初期値（省略時：空文字）
 * @return	string パラメータ／NULL＝パラメータ無し
*/
function getParam($key, $auto=TRUE, $def='') {
	if (isset($_GET[$key]))			$param = $_GET[$key];
	else if (isset($_POST[$key]))	$param = $_POST[$key];
	else							$param = $def;
	if ($auto)	$param = mb_convert_encoding($param, INTERNAL_ENCODING, 'auto');
	return $param;
}

/**
 * 月の満ち欠けを描く
 * @param	double $age 月齢
 * @return	object GDリソース
*/
function draw_moonage($age) {
	if ($age < 0 || $age > 30)		$age = 0;

	//満月画像がなければ円を描画
	if (! file_exists(FULLMOON)) {
		$dd = 500;			//直径
		$rr = $dd / 2;		//半径
		$image = imagecreatetruecolor($dd, $dd);
		//背景透明化
		$bgcolor = imagecolorallocate($image, 0xFF, 0xFF, 0xFF);//背景色セット
		imagefill($image, 0, 0, $bgcolor);
		imagecolortransparent($image, $bgcolor);
		//円を描画
		$color = imagecolorallocate($image, 0xFF, 0xFF, 0x7F);
		imagefilledarc($image, $rr, $rr, $dd, $dd, 0, 360, $color, IMG_ARC_PIE);

	//満月画像の読み込み
	} else {
		if (($arr = getimagesize(FULLMOON)) == FALSE)	return FALSE;
		$dd = $arr[0];		//直径
		$rr = $dd / 2;		//半径
		//画像読み込み
		$image = imagecreatefrompng(FULLMOON);
	}

	//完全なアルファチャネル情報を保存するフラグをonにする
	imagesavealpha($image, TRUE);
	//カラー設定
	$black = imagecolorallocatealpha($image, 0x00, 0x00, 0x00, ALPHA);
	$white = imagecolorallocatealpha($image, 0xFF, 0xFF, 0xFF, ALPHA);

	//影を描く
	$x0 = $rr;
	$y0 = $rr;
	$th = $age / 14.765 * pi();
	for ($y = -$rr; $y <= 0; $y++) {
		$ac = acos($y / $rr);
		$x2 = $rr * sin($ac);				// 円周
		$x1 = $rr * cos($th) * sin($ac);	// 月の形
		if (($age > 0.5) && ($age < 29.5)) {
			if ($age < 15.0) {
				$x3 = $x0 + $x1;
				$x4 = $x0 + $x2;
				$x5 = $x0 - $x2;
				$y3 = $y0 + $y;
				$y4 = $y0 - $y;
			} else {
				$x3 = $x0 - $x1;
				$x4 = $x0 - $x2;
				$x5 = $x0 + $x2;
				$y3 = $y0 + $y;
				$y4 = $y0 - $y;
			}
			imageline($image, $x3, $y3, $x5, $y3, $black);
			if (MOON_BRIGHT)	imageline($image, $x3, $y3, $x4, $y3, $white);
			if ($y != 0) {
				imageline($image, $x3, $y4, $x5, $y4, $black);
				if (MOON_BRIGHT)	imageline($image, $x3, $y4, $x4, $y4, $white);
			}
		} else {
			$x3 = $x0 - $x2;
			$x4 = $x0 + $x2;
			$y3 = $y0 + $y;
			$y4 = $y0 - $y;
			imageline($image, $x3, $y3, $x4, $y3, $black);
			if ($y != 0) {
				imageline($image, $x3, $y4, $x4, $y4, $black);
			}
		}
	}
	return $image;
}

/**
 * 月の満ち欠けをサーバに保存する
 * @param	string $path 保存先フォルダ
 * @return	なし
*/
function save_moonage($path) {
	for ($age = 0; $age <= 30; $age++) {
		$image = draw_moonage($age);
		$fname = sprintf('%smoon_%02d.png', $path, $age);
		imagepng($image, $fname);
		imagedestroy($image);
	}
}

/**
 * HTML BODYを作成する
 * @param	double $age 月齢
 * @return	string HTML BODY
*/
function makeCommonBody($age) {
	$myself = MYSELF;
	$refere = REFERENCE;
	$title  = TITLE;
	$version = '<span style="font-size:small;">' . date('Y/m/d版', filemtime(__FILE__)) . '</span>';
	$body =<<< EOT
<body>
<h2>{$title} {$version}</h2>
<form name="myform" method="post" action="{$myself}" enctype="multipart/form-data">
月齢：
<input type="text" name="age" id="age" size="4" value="{$age}" />
<input type="submit" id="draw" name="draw" value="描画" />
<br />
<input type="submit" id="save" name="save" value="保存" />
</form>

<div style="border-style:solid; border-width:1px; margin:20px 0px 0px 0px; padding:5px; width:400px; font-size:small;">
<h3>使い方</h3>
<ol>
<li>［<span style="font-weight:bold;">月齢</span>］に描画したい月齢を入力し、［<span style="font-weight:bold;">描画</span>］ ボタンを押してください。月の満ち欠けが表示されます。</li>
<li>［<span style="font-weight:bold;">保存</span>］ ボタンを推すと、月の満ち欠けを画像ファイルとしてサーバに保存します。</li>
</ol>
※参考サイト：<a href="{$refere}">{$refere}</a>
</div>
</body>

EOT;
	return $body;
}

// メイン・プログラム ======================================================
$age = getParam('age', FALSE, 8);

//月の満ち欠けを描く
if (isButton('draw')) {
	$image = draw_moonage($age);
	//画像表示
	header('Content-Type: image/png');
	imagepng($image);
	//画像破棄
	imagedestroy($image);

//画像を保存する
} else if (isButton('save')) {
	save_moonage(SAVE_PATH);
	$HtmlBody = makeCommonBody($age);
	// 表示処理
	echo $HtmlHeader;
	echo $HtmlBody;
	echo $HtmlFooter;

//パラメータ入力
} else {
	$HtmlBody = makeCommonBody($age);
	// 表示処理
	echo $HtmlHeader;
	echo $HtmlBody;
	echo $HtmlFooter;
}

/*
** バージョンアップ履歴 ===================================================
 *
 * @version  1.1  2015/12/19
 * @version  1.0  2015/12/13
*/
?>
