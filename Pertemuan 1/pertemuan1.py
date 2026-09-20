# products = [
#     {
#         "name": "Keyboard",
#         "price": 500000,
#         "stock": 10,
#         "category": "Aksesoris",
#         "brand": "Logitech"
#     },
#     {
#         "name": "Mouse",
#         "price": 300000,
#         "stock": 15,
#         "category": "Aksesoris",
#         "brand": "Logitech"
#     }
# ]

# print

class hero:
    jumlahhero = 0

    def __init__(self, nama, hp, attackPower):
        self.nama = nama
        self.hp = hp
        self.attackPower = attackPower

    def __str__(self):
        return f"Nama: {self.nama}, HP: {self.hp}, Attack Power: {self.attackPower}" 

    def infohero(self):
        return f"Nama: {self.nama}"

    @classmethod
    def tampilkan_jumlahhero(cls):
        return f"Jumlah Hero: {cls.jumlahhero}"
    
melissa = hero("Melissa", 100, 10)
print(melissa.infohero())
melissa.infohero()
hero.tampilkan_jumlahhero()