import sys
input = sys.stdin.readline

n,m = map(int, input().split())
world_map = [[] for _ in range(n)] # 월드맵

"""
. 빈칸 / # 벽 / B 아이템 상자 / ^ 가시 함정 / & 몬스터 / M 보스몬스터
아이템상자 - W 무기 / A 갑옷 / O 장신구 
"""
turn_count = 0

player_info = {
    'LV':1,
    'MAX_HP':20, 
    'NOW_HP':20, 
    'ATT':2, 
    'DEF':2,
     'EXP':0
} # 플레이어 정보

player_item = {
    'sword': 0,
    'armor': 0,
    'HR': False,
    'RE': False, 
    'CO': False, 
    'EX': False, 
    'DX': False, 
    'HU': False, 
    'CU': False, 
    'item_count': 0
} # 아이템 정보 

monster_cnt = 0
monster_info = {}
item_cnt = 0
item_info = {}

for i in range(n):  #월드맵 입력받기
    line = list(input().rstrip())
    for j in range(m):
        if line[j] == '@':
            player_location = [i,j] # 플레이어 위치 
            line[j] = '.'
        if line[j] == '&':
            monster_cnt += 1
        if line[j] == 'B':
            item_cnt += 1
        world_map[i].append(line[j])

start_location = player_location[:]

player_move = list(input().rstrip())

for i in range(monster_cnt+1):
    r,c,s,w,a,h,e = input().rstrip().split() 
    r,c,w,a,h,e = map(int, (r,c,w,a,h,e))
    monster_info[(r-1,c-1)] = (s,w,a,h,e)# s 몬스터이름 / w 몬스터 공격력 / a 몬스터 방어력 / h 몬스터 체력 / e 경험치

for i in range(item_cnt):
    r,c,t,s = input().rstrip().split()
    r,c = map(int, (r,c))
    if t in ('W', 'A'):
        s = int(s)
        item_info[(r-1,c-1)] = (t,s)
    if t == 'O':
        item_info[(r-1,c-1)] = (t,s)

def monster():
    global player_location
    now_locate = (player_location[0], player_location[1])
    player_att = player_info['ATT']
    player_hp = player_info['NOW_HP']
    player_def = player_info['DEF']
    monster_att = monster_info[now_locate][1]
    monster_hp = monster_info[now_locate][3]
    monster_def = monster_info[now_locate][2]
    monster_death = False # 몬스터 처치여부
    first_attack = True
    while True: # 전투
        if first_attack and player_item['CO']: # CO 장신구 - 첫공격 데미지 2배
            first_attack = False
            if player_item['DX']: # DX 장신구 - CO와 함께 착용시 첫공격이 3배의 데미지
                monster_hp -= max(1, player_att*3 - monster_def)
            else:
                monster_hp -= max(1, player_att*2 - monster_def)
            if monster_hp <= 0:
                monster_death = True
                break
            player_hp -= max(1, monster_att - player_def)
            if player_hp <= 0:
                break
        else:
            monster_hp -= max(1, player_att - monster_def)
            if monster_hp <= 0:
                monster_death = True
                break
            player_hp -= max(1, monster_att - player_def)
            if player_hp <= 0:
                break
    player_info['NOW_HP'] = player_hp
    if monster_death: # 몬스터 처치
        if player_item['HR']: # HR 장신구 - 전투승리시 체력 3 회복
            player_info['NOW_HP'] = min(player_info['MAX_HP'], player_info['NOW_HP'] + 3)
        world_map[player_location[0]][player_location[1]] = '.'
        if player_item['EX']: # EX 장신구 - 얻는 경험치 1.2배 소수점 버림
            get_exp = int(monster_info[now_locate][4] * 1.2)
        else:
            get_exp = monster_info[now_locate][4] # 얻는 경험치 
        now_exp = player_info['EXP'] 
        now_lv = player_info['LV']
        if now_exp + get_exp >= now_lv*5: # 레벨업 조건
            player_info['LV'] += 1
            player_info['ATT'] += 2
            player_info['DEF'] += 2 
            player_info['MAX_HP'] += 5
            player_info['NOW_HP'] = player_info['MAX_HP']
            player_info['EXP'] = 0
        else:
            player_info['EXP'] += get_exp
        return 'continue'
    else: # 플레이어 사망
        if player_item['RE']: # RE 장신구 - 사망시 최대체력 부활, 첫 시작위치로 이동
            player_item['RE'] = False
            player_item['item_count'] -= 1
            world_map[player_location[0]][player_location[1]] = '&'
            player_location = start_location[:]
            player_info['NOW_HP'] = player_info['MAX_HP']
            return 'continue'
        else:
            world_map[player_location[0]][player_location[1]] = '&'
            game_end()
            print(f'YOU HAVE BEEN KILLED BY {monster_info[now_locate][0]}..')
            return 'gameover'

def item():
    world_map[player_location[0]][player_location[1]] = '.'
    now_locate = (player_location[0], player_location[1])
    type,s = item_info[now_locate]
    if type == 'W':
        player_info['ATT'] += s - player_item['sword']
        player_item['sword'] = s
    if type == 'A':
        player_info['DEF'] += s - player_item['armor']
        player_item['armor'] = s
    if type == 'O':
        if player_item['item_count'] < 4 and not player_item[s]:
            player_item[s] = True
            player_item['item_count'] += 1
        
def trap():
    global player_location
    now_hp = player_info['NOW_HP']
    if player_item['DX']:
        now_hp -= 1
    else:
        now_hp -= 5

    if now_hp <= 0:
        if player_item['RE']: # RE 장신구 - 사망시 최대체력 부활, 첫 시작위치로 이동
            player_item['RE'] = False
            player_item['item_count'] -= 1
            player_location = start_location[:]
            player_info['NOW_HP'] = player_info['MAX_HP']
            return 'continue'
        player_info['NOW_HP'] = 0
        game_end()
        print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
        return 'gameover'
    else:
        player_info['NOW_HP'] = now_hp
        return 'continue'

def boss():
    global player_location
    if player_item['HU']:
        player_info['NOW_HP'] = player_info['MAX_HP']
    now_locate = (player_location[0], player_location[1])
    player_att = player_info['ATT']
    player_hp = player_info['NOW_HP']
    player_def = player_info['DEF']
    monster_att = monster_info[now_locate][1]
    monster_hp = monster_info[now_locate][3]
    monster_def = monster_info[now_locate][2]
    monster_death = False # 몬스터 처치여부
    first_attack = True
    while True: # 전투
        if first_attack:
            first_attack = False
            if player_item['CO']: # CO 장신구 - 첫공격 데미지 2배
                if player_item['DX']: # DX 장신구 - CO와 함께 착용시 첫공격이 3배의 데미지
                    monster_hp -= max(1, player_att*3 - monster_def)
                else:
                    monster_hp -= max(1, player_att*2 - monster_def)
            else:
                monster_hp -= max(1, player_att - monster_def)

            if monster_hp <= 0:
                monster_death = True
                break
            player_hp -= max(1, monster_att - player_def)
            if player_hp <= 0:
                break
        else:
            monster_hp -= max(1, player_att - monster_def)
            if monster_hp <= 0:
                monster_death = True
                break
            player_hp -= max(1, monster_att - player_def)
            if player_hp <= 0:
                break
    player_info['NOW_HP'] = player_hp
    if monster_death:
        if player_item['HR']: # HR 장신구 - 전투승리시 체력 3 회복
            player_info['NOW_HP'] = min(player_info['MAX_HP'], player_info['NOW_HP'] + 3)
        world_map[player_location[0]][player_location[1]] = '.'
        if player_item['EX']: # EX 장신구 - 얻는 경험치 1.2배 소수점 버림
            get_exp = int(monster_info[now_locate][4] * 1.2)
        else:
            get_exp = monster_info[now_locate][4] # 얻는 경험치 
        now_exp = player_info['EXP'] 
        now_lv = player_info['LV']
        if now_exp + get_exp >= now_lv*5: # 레벨업 조건
            player_info['LV'] += 1
            player_info['ATT'] += 2
            player_info['DEF'] += 2 
            player_info['MAX_HP'] += 5
            player_info['NOW_HP'] = player_info['MAX_HP']
            player_info['EXP'] = 0
        else:
            player_info['EXP'] += get_exp
        game_end()
        print('YOU WIN!')
        return 'gameover'
    else:
        if player_item['RE']: # RE 장신구 - 사망시 최대체력 부활, 첫 시작위치로 이동
            player_item['RE'] = False
            player_item['item_count'] -= 1
            world_map[player_location[0]][player_location[1]] = 'M'
            player_location = start_location[:]
            player_info['NOW_HP'] = player_info['MAX_HP']
            return 'continue'
        game_end()
        print(f'YOU HAVE BEEN KILLED BY {monster_info[now_locate][0]}..')
        return 'gameover'

def game():
    global turn_count
    turn_count += 1
    nx,ny = player_location
    now = world_map[nx][ny]
    if now == '.':
        return 'continue'
    if now == '&':
        state = monster()
    if now == 'B':
        state = item()
    if now == 'M':
        state = boss()
    if now == '^':
        state = trap()
    return state

def game_end():
    print(f'Passed Turns : {turn_count}')
    print(f'LV : {player_info["LV"]}')
    print(f'HP : {player_info["NOW_HP"]}/{player_info["MAX_HP"]}')
    print(f'ATT : {player_info["ATT"]-player_item["sword"]}+{player_item["sword"]}')
    print(f'DEF : {player_info["DEF"]-player_item["armor"]}+{player_item["armor"]}')
    print(f'EXP : {player_info["EXP"]}/{player_info["LV"]*5}')


for move in player_move:
    nx,ny = player_location # nx 세로 ny 가로
    if move == 'R':
        x,y = nx, ny+1
    if move == 'L':
        x,y = nx, ny-1
    if move == 'U':
        x,y = nx-1, ny
    if move == 'D':
        x,y = nx+1, ny
    if 0 <= x < n and 0 <= y < m and world_map[x][y] != '#':
        player_location = [x,y]
    game_state = game()
    if game_state == 'continue':
        continue
    if game_state == 'gameover':
        break
else:
    game_end()
    print('Press any key to continue.')