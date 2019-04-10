# Lightsout
## Lightsoutのソルバー

## Lightsoutとは
N*Mマスの形に並んだライトが不規則にいくつか点灯している。
ユーザーが触ったマス及び上下左右のマスのライトのON-OFFが入れ替わる。
【初期状態】
● ● ● ● ●
● ● ● ● ●
● ○ ● ● ●
● ● ○ ● ●
● ● ● ● ●

【真ん中を選択】
● ● ● ● ●
● ● ● ● ●
● ○ ★ ● ●
● ● ○ ● ●
● ● ● ● ●

【真ん中を押下後】
● ● ● ● ●
● ● ○ ● ●
● ● ○ ○ ●
● ● ● ● ●
● ● ● ● ●

この操作を繰り返し、点灯しているライトを全て消灯することが目的のパズルゲーム。
このソルバーはこのゲームを解く最短手数及び押下位置を表示する。

### 使い方
まずN行でM列であることを"N M"の形で入力する。
続いて盤面を「.」（点灯）と「0」（消灯）で入力する。
