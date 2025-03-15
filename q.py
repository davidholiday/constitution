#!/usr/bin/env python3

import sys
import os
import csv
from random import randrange
from simple_term_menu import TerminalMenu


def parse_csv(csv_filename):
  with open(csv_filename) as csv_file:
    csv_data=csv.reader(csv_file, delimiter=',')
    return list(csv_data) 

  
def get_tag_index_map(parsed_csv):
  rv = {}
  for i in range(1, len(parsed_csv)):
    tag_str = parsed_csv[i][2]
    tags = tag_str.split(',')
    for tag in tags:
      if tag not in rv.keys():
        rv[tag] = []
      rv[tag].append(i)
  return rv 


def get_q_and_a(menu_entry_index, tag_index_map, parsed_csv):
  tag = list(tag_index_map.keys())[menu_entry_index]
  indexes = tag_index_map[tag]
  question_index = indexes[randrange(0, len(indexes))]
  return (parsed_csv[question_index][0], parsed_csv[question_index][1])
  

def main(csv_filename):
  parsed_csv = parse_csv(csv_filename)
  tag_index_map = get_tag_index_map(parsed_csv)
  options = []
  for k, v in tag_index_map.items():
    options.append(k + " (" + str(len(v)) + ' questions)')

  while True:
    terminal_menu = TerminalMenu(options, title="select constitution question type")
    menu_entry_index = terminal_menu.show()
    q_and_a = get_q_and_a(menu_entry_index, tag_index_map, parsed_csv)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(q_and_a[0])
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(q_and_a[1])
    input("Press Enter to continue...")

if __name__ == '__main__':
  if (len(sys.argv) < 2):
    print('missing csv filename argument')
    exit(8) 

  csv_filename = sys.argv[1]
  if os.path.exists(csv_filename) == False:
    print('csv filename argument points to file that does not exist')
    exit(8)

  main(csv_filename) 








