import subprocess
import os

# Переходим в нужную директорию
project_path = r"C:\Users\Александр\Desktop\project"
os.chdir(project_path)

try:
    # Инициализируем git репозиторий
    result = subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
    print("Git репозиторий успешно создан!")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Ошибка: {e}")
    print(f"Stderr: {e.stderr}")
except FileNotFoundError:
    print("Git не установлен на системе!")