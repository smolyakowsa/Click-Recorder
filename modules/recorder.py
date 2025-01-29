import time
import os
from pynput import mouse, keyboard
import threading

class EventRecorder:
    def __init__(self):
        self.events = []  # Список для хранения событий
        self.last_event_time = time.time()  # Время последнего события
        self.is_recording = False  # Флаг для отслеживания состояния записи
        self.mouse_listener = None  # Слушатель событий мыши
        self.keyboard_listener = None  # Слушатель событий клавиатуры
        self.records_dir = "records"  # Папка для сохранения записей

        # Создаем папку records, если она не существует
        if not os.path.exists(self.records_dir):
            os.makedirs(self.records_dir)

    # Функция для записи событий мыши
    def on_click(self, x, y, button, pressed):
        if not self.is_recording:
            return

        current_time = time.time()
        time_interval = current_time - self.last_event_time
        self.last_event_time = current_time

        event = {
            'type': 'mouse',
            'x': x,
            'y': y,
            'button': str(button),
            'pressed': pressed,
            'time_interval': time_interval
        }
        self.events.append(event)
        print(f"Mouse click: {event}")

    # Функция для записи событий клавиатуры
    def on_press(self, key):
        if not self.is_recording:
            return

        current_time = time.time()
        time_interval = current_time - self.last_event_time
        self.last_event_time = current_time

        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        event = {
            'type': 'keyboard',
            'key': key_char,
            'pressed': True,
            'time_interval': time_interval
        }
        self.events.append(event)
        print(f"Key press: {event}")

        # Остановка записи по нажатию Esc
        if key == keyboard.Key.esc:
            self.stop_recording()

    def on_release(self, key):
        if not self.is_recording:
            return

        current_time = time.time()
        time_interval = current_time - self.last_event_time
        self.last_event_time = current_time

        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        event = {
            'type': 'keyboard',
            'key': key_char,
            'pressed': False,
            'time_interval': time_interval
        }
        self.events.append(event)
        print(f"Key release: {event}")

    # Запуск записи событий
    def start_recording(self):
        self.is_recording = True
        self.events = []  # Очищаем предыдущие события
        self.last_event_time = time.time()

        # Запуск слушателей в отдельных потоках
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

        self.mouse_listener.start()
        self.keyboard_listener.start()

    # Остановка записи событий
    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            if self.mouse_listener:
                self.mouse_listener.stop()
            if self.keyboard_listener:
                self.keyboard_listener.stop()
            self.save_events_to_file()
            print("Recording stopped and saved.")

    # Генерация уникального имени файла
    def _generate_unique_filename(self, base_name):
        counter = 1
        file_name = base_name
        while os.path.exists(os.path.join(self.records_dir, file_name)):
            file_name = f"{os.path.splitext(base_name)[0]}_{counter}.py"
            counter += 1
        return file_name

    # Сохранение событий в файл .py
    def save_events_to_file(self, filename='replay_script.py'):
        # Генерация уникального имени файла
        unique_filename = self._generate_unique_filename(filename)
        file_path = os.path.join(self.records_dir, unique_filename)

        with open(file_path, 'w') as f:
            # Добавляем импорт pyautogui
            f.write("import pyautogui\n")
            f.write("import time\n\n")

            # Записываем события
            for event in self.events:
                if event['type'] == 'mouse':
                    if event['pressed']:
                        f.write(f"time.sleep({event['time_interval']})\n")
                        f.write(f"pyautogui.mouseDown(x={event['x']}, y={event['y']}, button='{event['button'].split('.')[-1]}')\n")
                    else:
                        f.write(f"time.sleep({event['time_interval']})\n")
                        f.write(f"pyautogui.mouseUp(x={event['x']}, y={event['y']}, button='{event['button'].split('.')[-1]}')\n")
                elif event['type'] == 'keyboard':
                    if event['pressed']:
                        f.write(f"time.sleep({event['time_interval']})\n")
                        f.write(f"pyautogui.keyDown('{event['key']}')\n")
                    else:
                        f.write(f"time.sleep({event['time_interval']})\n")
                        f.write(f"pyautogui.keyUp('{event['key']}')\n")

        print(f"Events saved to {file_path}. You can now run this file as a script.")