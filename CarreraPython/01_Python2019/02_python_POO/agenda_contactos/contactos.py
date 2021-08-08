# -*- Coding: utf-8 -*-
import csv

class Contact:

  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email



class ContactBook:

  def __init__(self):
    self._contacts = []

  def add(self, name, phone, email):
    contact = Contact(name, phone, email)
    self._contacts.append(contact)
    self._save()

  def show_all(self ):
    for contact in self._contacts:
      self._print_contact(contact)

  def _print_contact(self, contact):
    print('====='*5)
    print(f'Nombre: {contact.name}')
    print(f'Celular: {contact.phone}')
    print(f'Email: {contact.email}')
    print('====='*5)

  def delete(self, name):

    for idx, contact in enumerate(self._contacts):
      if contact.name.lower() == name.lower():
        del self._contacts[idx]
        self._save()
        break

  def search(self, name):
    for contact in self._contacts:
      if contact.name.lower() == name.lower():
        self._print_contact(contact)
        break
    else:
      self._not_found()

  def _not_found(self):
    print('!!! No encontrado ¡¡¡')

  def _save(self):
    with open('save_contacts.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerow( ('name', 'phone','email'))

      for contact in self._contacts:
        writer.writerow((contact.name, contact.phone, contact.email ))



def main():
  contact_book = ContactBook() # instancia de la clase
  
  with open('save_contacts.csv', 'r') as f:
    reader = csv.reader(f)
    for idx, row in enumerate(reader):
      if idx == 0: # salta la primera linea del archivo
        continue

      contact_book.add(row[0], row[1], row[2])



  while True:
  
    command = str(input('''
  ¿Qué deseas hacer?

  [a] añadir contacto
  [d] editar contacto
  [b] buscar contacto
  [e] eliminar contacto
  [l] listar contactos
  [s] salir de agenda

  => '''))

    if command == 'a': # añadir

      name = str(input('Nombre: '))
      phone = str(input('Celular: '))
      email = str(input('Correo: '))
      contact_book.add(name, phone, email) # metodo

    elif command == 'd': # actualizar
        print('pensar como reutilizar el codigo de busqueda y añadir')
    
    elif command == 'b': # buscar
      name = str(input('Contacto a buscar: '))
      contact_book.search(name)

    elif command == 'e': # eliminar
       name = str(input('Contacto a eliminar: '))
       contact_book.delete(name) # metodo

    elif command == 'l': # listar
      contact_book.show_all() # metodo  

    elif command == 's': # salir
      print('salir de agenda')
      break
    else:
      print('comando invalido')



if __name__ == '__main__':
  print('''
  Bienvenido a la agenda telefónica''')
  main()
