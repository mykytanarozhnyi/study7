from plane import Plane

plane_1 = Plane("Airbus","A320",2021,"300","destroyed")
plane_2 = Plane("Boeing","737MAX",2022,"340", "destroyed")
plane_3 = Plane("Antonov","AN225",1980,"10","destroyed")

plane_1.fly()
plane_1.stop()
plane_1.destroyed()

plane_2.fly()
plane_2.stop()
plane_2.destroyed()

plane_3.fly()
plane_3.stop()
plane_3.destroyed()

