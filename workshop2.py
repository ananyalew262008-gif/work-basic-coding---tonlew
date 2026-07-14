name = str(input("ชื่อ: "))
age = int(input("อายุ: "))
height = int(input("ส่วนสูง: "))
power = int(input("พลังงาน: "))
money = int(input("มีเงินกี่บาท: "))
if age >= 30 and height >= 190 and power == 10 and money >= 1000000:
    print("ยินดีด้วย คุณผ่านการคัดเลือก ตำแหน่งของคุณคือ รองหัวหน้ามาเฟียร์!")
elif age >= 20 and height >= 180 and power >= 8 and money >= 100000:
    print("ยินดีด้วย คุณผ่านการคัดเลือก ตำแหน่งของคุณคือ บอร์ดี้การ์ดส่วนตัวของหัวหน้า!")
elif age >= 18 and height >= 170 and power >= 6 and money >= 10000:
    print("ยินดีด้วย คุณผ่านการคัดเลือก ตำแหน่งของคุณคือ ขี้ข้า!")
else:
    print("คุณกากเกินไปสำหรับตองค์กรของเรา ไสหัวไป!")
