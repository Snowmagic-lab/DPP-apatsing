#อันนี้หาตำแหน่งของ King ก่อน

def checkmate(board):
    kingR = None #Roll ของ King
    kingC = None #Column ของ King

    rows = board.splitlines()#แยกแต่ละบรรทัด

    for r, row in enumerate(rows):#นับว่ามีกี่ row (เริ่มนับจาก 0 )
        for c, square in enumerate(row):#นับ column (เริ่มนับจาก 0 )
            if square == "K":
                kingR = r
                kingC = c


#เช็ค Pawn  x.x
#          .p.
#          ...

    pawnR = kingR + 1 #pawn ต้องอยู่ข้างล่างkingถึงจะกินได้
    if pawnR < len(rows): #กันตกขอบกระดาน
       for pawnC in (kingC - 1, kingC + 1):#ต้องอยู่ล่างซ้ายหรือล่างขวา
           if 0 <= pawnC < len(rows[pawnR]):#กันตกขอบกระดาน
              if rows[pawnR][pawnC] == "P":
                 print("Success")
                 return

#เช็ค Q กับ R

    straightD = [(-1,0), (1,0), (0,-1), (0,1)] #ขึ้น ลง ซ้าย ขวา

    for dr, dc in straightD: #หยิบมาทีละคู่
        #เริ่มจากช่องที่ติดกับ king ก่อนๆ
        r = kingR + dr
        c = kingC + dc

        while 0 <= r < len(rows) and 0 <= c < len(rows[r])  :#ใช้ while เพื่อตรวจไปเรื่อยๆ และกันตกกระดาน, len(rows) คือจำนวนแถว ส่วน len(rows[r]) คือจำนวนช่องในแถวนั้นๆ
              piece = rows[r][c]
              if piece in ("R", "Q"):#เช็ค R กับ Q
                 print("Success")
                 return

              if piece in ("P", "B", "K"): #เช็ค P B K ถ้เาปเ็นตัวเหล่านี้จะกินไม่ได้ ให้หยุด function whileนี้ แล้วกลับไปฟังค์ชั่น for เพื่อไปหาทิศต่อไป
                 break

              r += dr
              c += dc



     #หา Bishop กับ Queen ต่อ(แนวเฉียง)
    diagonalD = [(-1, -1), (-1, 1), (1, -1), (1, 1)]# เฉียงซ้าย เฉียงขวา ล่างซ้าย ล่างขวา

    for dr, dc in diagonalD:
        r = kingR + dr
        c = kingC + dc

        while 0 <= r < len(rows) and 0 <= c < len(rows[r]):
              piece = rows[r][c]

              if piece in ("B", "Q"):
                 print("Success")
                 return

              if piece in ("P", "R", "K"):
                 break
              
              
              r += dr
              c += dc
    print("Fail")