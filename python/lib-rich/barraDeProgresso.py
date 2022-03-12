from rich.progress import track
from time import sleep

for tarefa in track(range(10), 'processando...'):
    sleep(2)
