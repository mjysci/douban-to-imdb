import os
import sys
import time
import csv

chunk_size = 1800

def split_csv():
    def write_chunk(part, lines):
        with open('movie_part_'+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header+"\n")
            f_out.writelines(lines)

    with open('movie.csv', 'r') as f:
        count = 0
        header = "Title,Rating,imdbID,WatchedDate"
        lines = []
        for line in f:
            count += 1
            try:
                lines.append(line.split('/')[1])
            except:
                lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)
            

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/movie.csv'):
        print('未能找到CSV文件，请先导出豆瓣评分，请参照：',
              'https://github.com/fisheepx/douban-to-imdb')
        sys.exit()
    split_csv()
