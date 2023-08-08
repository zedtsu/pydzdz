import json
import uuid
from datetime import datetime

class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

def save(notes):
    with open('notes.json') as file:
        json.dump([note.__dict__ for note in notes], file, indent=4, separators=(',', ': '))

def read():
    try:
        with open('notes.json', 'r') as file:
            data = json.load(file)
            notes = [Note(**note) for note in data]
    except(json.decoder.JSONDecodeError, FileNotFoundError):
        notes = []
    return notes

def add():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст:')
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    id = str(uuid.uuid4())
    note = Note(id, title, body, date)
    notes.append(note)
    save(notes)

def edit():
    id = input('Введите айди заметки для редактирования: ')
    note = next((note for note in notes if note.id == id), None)
    if note:
        print(f'Редактирование заметки: {note.title}')
        title = input('Введите новый заголовок заметки: ')
        body = input('Введите новый текст заметки: ')
        date = input('Введите новую дата и время(пример: dd.mm.yyyy hh.mm.ss): ')
        if title:
            note.title = title
        if body:
            note.body = body
        if date:
            note.date = date
        save(notes)
    else:
        print('Не найдено заметки.')

def delete():
    id = input('Введите айди заметки для удаления: ')
    note = next((note for note in notes if note.id == id), None)
    if note:
        notes.remove(note)
        save(notes)
    else:
        print('Не найдено заметки.')

def printNotes():
    if notes:
        for note in notes:
            print(f'{note.id} {note.title} ({note.date}):n  {note.body}')
    else:
        print('Не найдено заметки.')

def main():
    global notes
    notes = read()
    flag = True
    while flag:
        print('1. Показать список заметок.')
        print('2. Добавить заметку.')
        print('3. Редактировать заметку.')
        print('4. Удалить заметку.')
        print('5. Выход.')
        choise = input('')
        if choise == 1:
            printNotes()
        elif choise == 2:
            add()
        elif choise == 3:
            edit()
        elif choise == 4:
            delete()
        elif choise == 5:
            flag = False
        else:
            print('Такого варианта нет.')