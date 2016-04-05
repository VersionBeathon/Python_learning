# _*_ coding:utf-8 _*_
# database.py
import sys
import shelve


def store_person(db):

    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone number: ')

    db[pid] = person


def lookup_person(db):
    pid = raw_input('Enter ID number: ')
    field = raw_input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print field.capitalize() + ':', db[pid][field]


def print_help():
    print 'The available commands are: '
    print 'store :Stores information about a person'
    print 'lookup:looks up a person from ID number'
    print 'quit  :Save changes and exit'
    print '?     :Prints this message'


def enter_comand():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower().
    return cmd


def main():
    database = shelve.open('C:\\database.dat') # you want to change this name
    try:
        while True:
            cmd = enter command() 
            if cmd == 'strore':
                store_person(database)
            elif cmd == 'lookup'
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit'
                return
    finally:
        database.close()


if __name__ == '__main__':main()