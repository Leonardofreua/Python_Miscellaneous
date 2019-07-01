#!/usr/bin/env python
# -*- coding: utf-8 -*-


from View import View


class ConsoleView(View):
    def show_item_list(self, item_type, item_list):
        print(item_type.upper() + ' LIST:')
        for item in item_list:
            print(item)
        print('')

    @staticmethod
    def capitalizer(string):
        return string[0].upper() + string[1:].lower()

    def show_item_information(self, item_type, item_name, item_info):
        print(item_type.upper() + ' INFORMATION:')
        printout = 'Name: %s' % item_name

        for key, value in item_info.items():
            printout += ', ' + self.capitalizer(str(key)) + ': ' + str(value)

        printout += '\n'
        print(printout)

    def item_not_found(self, item_type, item_name):
        print('That %s "%s" does not exist in the records' %
              (item_type, item_name))