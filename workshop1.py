quantity = int(input("จำนวนปืนที่รับมาขาย: "))
cost_price = int(input("ต้นทุนของปืนที่รับมา: "))
sell_price = int(input("ราคาที่นำไปขายต่อ: "))
team_member = int(input("จำนวนลูกน้องไปทำงาน: "))

print("ต้นทุนทั้งหมด:" , quantity * cost_price)
print("ราคาขายทั้งหมด:", quantity * sell_price)
print("กำไรต่อคน:", (quantity * sell_price) - (quantity * cost_price))
print("ส่วนแบ่งกำไรต่อคน:", (quantity * sell_price - quantity * cost_price)/team_member)
print("กำไรสุท"