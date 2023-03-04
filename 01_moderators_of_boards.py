import PyPtt
from shared import Bot, to_csv, to_file_path

ptt_bot = Bot()

f = open(to_file_path('01_moderators_of_boards.txt'), 'r', encoding='utf-8')

index = 1

output_rows = ['看板名稱,板主']

for board_name in f:
    board_name = board_name.replace('\n', '')
    print(f'正在查詢第{index}筆資料')

    try:
        board_info = ptt_bot.get_board_info(board=board_name)
    except PyPtt.exceptions.NoSuchBoard:
        print('[錯誤] 找不到看板: ' + board_name)
        continue
    
    if board_info is not None:
        board_infos = [
            board_name, #看板名稱
        ] + board_info[PyPtt.BoardField.moderators]
    
    output_rows.append(','.join(board_infos))

    index = index + 1

to_csv(output_rows, '01_moderators_of_boards.csv')
