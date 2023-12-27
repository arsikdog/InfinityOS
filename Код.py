import os
import sys
import time
import subprocess

# Функция для вывода приветственного сообщения
def welcome():
  print("🟦🟦🟦🟦")
  print("🟦.         🟦")
  print("🟦🟦🟦🟦🟦🟦🟦🟦")
  print("                    🟦.        🟦")
  print("                     🟦🟦 🟦🟦")
  print("Добро пожаловать в InfinityOS!")

# Функция для отображения меню
def menu():
  print("1. Запустить терминал")
  print("2. Выйти из системы")
  print("3. Об устройстве")
  print("4. Перезагрузка")
  print("5. Выбор раскладки клавиатуры")
  print("6. Выход из терминала")
  print("7. Настройка параметров системы")
  choice = input("Выберите пункт меню: ")
  return choice

# Функция для запуска терминала
def terminal():
  os.system("python -i")

# Функция для отображения информации об устройстве
def about_device():
  print("Информация об устройстве:")
  print("* Имя устройства:", os.uname().nodename)
  print("* Процессор:", os.uname().machine)
  print("* Операционная система:", os.uname().sysname)
  print("* Версия ядра:", os.uname().release)

# Функция для перезагрузки устройства
def reboot():
  os.system("sudo reboot")

# Функция для выбора раскладки клавиатуры
def choose_keyboard_layout():
  print("Доступные раскладки клавиатуры:")
  for layout in os.listdir("/usr/share/kbd/keymaps"):
    print("*", layout)
  layout = input("Выберите раскладку клавиатуры: ")
  os.system("sudo loadkeys /usr/share/kbd/keymaps/{}".format(layout))

# Функция для выхода из терминала без перезагрузки системы
def exit_terminal():
  os.system("exit")

# Функция для настройки параметров системы
def configure_system():
  print("Доступные параметры системы:")
  for option in os.listdir("/etc/systemd/system"):
    print("*", option)
  option = input("Выберите параметр системы: ")
  os.system("sudo systemctl edit {}".format(option))

# Основная функция
def main():
  welcome()
  while True:
    choice = menu()
    if choice == "1":
      terminal()
    elif choice == "2":
      sys.exit()
    elif choice == "3":
      about_device()
    elif choice == "4":
      reboot()
    elif choice == "5":
      choose_keyboard_layout()
    elif choice == "6":
      exit_terminal()
    elif choice == "7":
      configure_system()
    else:
      print("Неверный выбор!")

if __name__ == "__main__":
  main()
  