row = 1  # 行号

while row <=9:
    col = 1  # 列号

    while col <= row:
        print("%d * %d = %d" % (col,row,col * row) ,end="\t")  # print自带换行，加一个end=""就不会换行,\t是指转义字符，垂直方向对齐

        col += 1
    
    print("")  # 换行

    row += 1
