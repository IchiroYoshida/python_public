#!/usr/bin/perl
use strict;

my $filename = "hip_main.dat";
my $cnt = 0;
my ($c0, $c1, $c2, $c3) = (3.939654, -0.395361, 0.2082113, -0.0604097);

open(FILE, $filename) || die $!;
print "[";
while (my $line = <FILE>) {
  chomp $line;
  parseLine($line, $cnt++);
}
print "]";
close(FILE);

sub parseLine {
  my $line = shift;
  my $count = shift;

  my @h = split(/\s*\|\s*/, $line);

  my $id   = $h[1];
  my $Vmag = $h[5];
  my $RA   = $h[8];
  my $Dec  = $h[9];
  my $Parallax = $h[11];
  my $BV   = $h[37];

  if ($RA == "") {
    warn "Warning: RA is missing. This record will be skipped.";
    return 1;
  }
  if ($BV == "") {
    warn "Warning: B-V is missing, which is assumed to be 0.";
  }

  my $dist = plx2pc($Parallax);
  my $color = bv2rgb($BV);

  if ($count > 0) { print ","; }
  printf '{"ID":%d,"RA":%f,"Dec":%f,"Vmag":%0.2f,"dist":%f,"color":"%s"}',
         $id, $RA, $Dec, $Vmag, $dist, $color;
}

sub plx2pc {
  my $plx = shift;
  return ($plx == 0) ? 0 : (1000 / $plx);
}

sub bv2rgb {
  my $bv = shift;

  # Sekiguchi & Fukugita (2000)
  my $logT = $c0 + $c1*$bv + $c2*$bv*$bv + $c3*$bv*$bv*$bv;
  my $T = 10**$logT;

  # Planckian locus
  my ($x, $y);
  if ($T < 4000) {
    $x = -0.2661239e9 / ($T*$T*$T) - 0.2343580e6 / ($T*$T) + 0.8776956e3 / $T + 0.179910;
  } else {
    $x = -3.0258469e9 / ($T*$T*$T) + 2.1070379e6 / ($T*$T) + 0.2226347e3 / $T + 0.240390;
  }
  if ($T < 2222) {
    $y = -1.1063814 * $x*$x*$x - 1.34811020 * $x*$x + 2.18555832 * $x - 0.20219683;
  } elsif ($T < 4000) {
    $y = -0.9549476 * $x*$x*$x - 1.37418593 * $x*$x + 2.09137015 * $x - 0.16748867;
  } else {
    $y =  3.0817580 * $x*$x*$x - 5.87338670 * $x*$x + 3.75112997 * $x - 0.37001483;
  }

  my $Y = 1.0;
  my $X = $Y * $x / $y;
  my $Z = $Y * (1.0 - $x - $y) / $y;

  my $R = srgb( 3.2406 * $X - 1.5372 * $Y - 0.4986 * $Z);
  my $G = srgb(-0.9689 * $X + 1.8758 * $Y + 0.0415 * $Z);
  my $B = srgb( 0.0557 * $X - 0.2040 * $Y + 1.0570 * $Z);

  my $r = int(($R < 0 ? 0 : ($R > 1 ? 1 : $R)) * 255);
  my $g = int(($G < 0 ? 0 : ($G > 1 ? 1 : $G)) * 255);
  my $b = int(($B < 0 ? 0 : ($B > 1 ? 1 : $B)) * 255);

  return sprintf("0x%02x%02x%02x", $r, $g, $b);
}

sub srgb {
  my $c = shift;
  return ($c <= 0.0031308) ? 12.92 * $c : ((1 + 0.055) * $c**(1/2.4) - 0.055);
}

