room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    for room in range(1, room_count + 1):
        rows = int(input("Nhập số hàng ghế : "))
        seats = int(input("Nhập số ghế : "))

        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        for row in range(rows):
            for seat in range(seats):
                print("*" , end = '')
            print()

#mọi hàng đều phải có số lượng dấu sao bằng nhau.
