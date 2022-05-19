# Напишите программу, удаляющую из текста все слова, содержащие "абв".
my_str = 'Напишите программу, удалабвяющую из текста все слова, содеабвржащие'
my_str = my_str.split()
result = [world for world in my_str if (world.find('абв') == -1)]
print(" ".join(result))
