#!/usr/bin/env python
# coding: utf-8

# In[106]:


import os
import shutil
import json

def create_folder(name):
    try:
        os.mkdir('C:\\Users\\Анастасия\\Desktop\\file_manager' + '\\' + name)
        os.chdir('C:\\Users\\Анастасия\\Desktop\\file_manager' + '\\' + name)
    except OSError:
        print ('Папка с таким именем уже есть') 


def delete_folder(name):
    try:
        try:
            os.rmdir(os.getcwd())
        except OSError:
            os.chdir('C:\\Users\\Анастасия\\Desktop\\file_manager')
            shutil.rmtree(os.getcwd() + '\\' + name)
    except FileNotFoundError:
        print('Папки с таким именем не существует')


def change_directory(new_directory = ''):
        try:
            os.chdir('C:\\Users\\Анастасия\\Desktop\\file_manager' + '\\' + new_directory)
        except FileNotFoundError:
            print('Такая папка не существует')


def create_file(name, text = None):
    with open(os.getcwd() + '\\' + name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)     
            
            
def add_text_to_file(name, text):
    try:
        with open(os.getcwd() + '\\' + name, mode='a', encoding='utf8') as f:
            f.write(text)
    except FileNotFoundError:
        print('Такого файла не существует')


def show_text_file(name):
    try:
        with open(os.getcwd() + '\\' + name, mode='r', encoding='utf8') as f:
            print(f.read())
    except FileNotFoundError:
        print('Такого файла не существует')


def delete_file(name):
    try:
        os.remove(os.getcwd() + '\\' + name)
    except FileNotFoundError:
        print('Такого файла не существует')
        
        
def copy_file(name_file, name_dir):
    try:
        shutil.copy(os.getcwd() + '\\' + name_file, 'C:\\Users\\Анастасия\\Desktop\\file_manager' + '\\' + name_dir)
    except FileNotFoundError:
        print('Папки или файла не существует')

        
def move_file(name_file, name_dir):
    try:
        os.replace(os.getcwd() + '\\' + name_file, 'C:\\Users\\Анастасия\\Desktop\\file_manager' + '\\' + name_dir + '\\' + name_file)
    except FileNotFoundError:
        print('Папки или файла не существует')
        
        
def rename_file(name, new_name):
    try:
        os.rename(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
    except FileNotFoundError:
        print('Такого файла не существует')

