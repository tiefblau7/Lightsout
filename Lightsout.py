import copy
N, M = map(int, input("何行何列かを(行 列)の形で数字で入力: ").split())
pre_lights_list = []
for _ in range(N):
    pre_lights_list.append(list(input("ライトの点灯パターンを「.」（消灯）と「0」（点灯）で入力")))
result = N*M


#スイッチ
def switch(pos, lights_list):
    row = pos // M
    column = pos % M
    if lights_list[row][column] == '.':
        lights_list[row][column] = '0'
    else:
        lights_list[row][column] = '.'
    if row != 0:
        if lights_list[row-1][column] == '0':
            lights_list[row-1][column] = '.'
        else:
            lights_list[row-1][column] = '0'
    if row != N-1:
        if lights_list[row+1][column] == '0':
            lights_list[row+1][column] = '.'
        else:
            lights_list[row+1][column] = '0'
    if column != 0:
        if lights_list[row][column-1] == '0':
            lights_list[row][column-1] = '.'
        else:
            lights_list[row][column-1] = '0'
    if column != M-1:
        if lights_list[row][column+1] == '0':
            lights_list[row][column+1] = '.'
        else:
            lights_list[row][column+1] = '0'


def search(upper_row_pattern, lights_list):
    cur_result = 0
    on_off_pattern = ''
    #上端行のパターン変更
    for i in range(M):
        if i % M == 0:
            on_off_pattern += '\n'
        if upper_row_pattern[i] == 1:
            switch(i, lights_list)
            cur_result += 1
            on_off_pattern += '☆'
        else:
            on_off_pattern += '◯'

    #2行以降の押下
    for j in range(N*M):
        row = j // M
        column = j % M
        if M <= j:
            if j % M == 0:
                on_off_pattern += '\n'
            if lights_list[row-1][column] == '0':
                switch(j, lights_list)
                cur_result += 1
                on_off_pattern += '☆'
            else:
                on_off_pattern += '◯'
    return [cur_result, on_off_pattern]

#上端行の押下パターン
for i in range(2**M):
    lights_list = copy.deepcopy(pre_lights_list)
    pre_upper_row_pattern = list(bin(i).replace('0b', '').zfill(M))
    upper_row_pattern = [int(i) for i in pre_upper_row_pattern]
    cur_result, on_off_pattern = search(upper_row_pattern, lights_list)

    #最終行チェック
    flag = True
    for k in range(M):
        if lights_list[N-1][k] == '0':
            flag = False
    if flag:
        if cur_result <= result:
            result = cur_result
        print(on_off_pattern)
        print(f'押下回数は{cur_result}回です。')
print()
print(f'最小押下回数は{result}回です。')
#考察メモ
#結果の数は左右対称のとき、上下対称のときでそれぞれ1/2、左右対称かつ上下対称なら1/4になる？
#N*Nサイズのときのみ1/4の状況ができる。

'''
入力例
8 10
..........
..0.......
...0......
.....0....
..0.......
..........
..0.......
..........

☆☆☆☆◯◯◯☆☆◯
◯☆☆◯☆◯☆◯◯☆
◯☆◯☆☆◯☆◯◯☆
☆◯☆☆☆◯◯☆☆◯
☆☆◯◯☆◯◯◯◯◯
☆◯☆◯◯☆◯☆☆◯
◯☆☆☆◯☆◯◯◯☆
◯◯☆◯◯◯☆☆◯☆
押下回数は39回です。
'''
