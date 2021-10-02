"""
Author : ZIA CHIU
EMAIL: admin@crazyziye.xyz
Website： www.crazyziye.top
license：GPL
Created DATE: 29/9/21 10:34 pm
"""
import sqlite3
import sys

import contracts

from log import Log


class Data:
    def __init__(self):
        self.data = sqlite3.connect('example.db')
        self.cursor = self.data.cursor()

    @contracts.contract
    def data_query_alone(self, sql, value=None):
        """
        This is a function to upload one sql statement to database.
        Sql can has 2 format which are
        'sql="select {} from {}".format(row_name,table_name)'

        :param sql:
        :param value:
        :return:
        :type sql:str
        :type value: list[N],N=tuple
        """
        try:
            if value is None:
                self.cursor.execute(sql)
                self.data.commit()
            else:
                self.cursor.execute(sql, value)
                self.data.commit()
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)
        except contracts.ContractException:
            Log('wrong value format or value!!!', 'error', sys.exc_info()[2].tb_lineno)
        except ValueError as v_error:
            Log(str(v_error), 'error', sys.exc_info()[2].tb_lineno)

        Log('Query finished', 'info', sys._getframe().f_lineno)  # pylint: disable=W0212

    @contracts.contract
    def data_query_batch(self, sql, value=None):
        """
        This is a function to upload many sql statements to database.
        :param sql:
        :param value:
        :return:
        :type sql:str
        :type value: list[N],N=tuple
        """
        #         Sql only should be
        #         'sql="'select (?) from (?)'",value=[(row_name,table_name)]'
        try:
            self.cursor.executemany(sql, value)

        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)
        except contracts.ContractException:
            Log('wrong value format or value!!!', 'error', sys.exc_info()[2].tb_lineno)
        except ValueError as v_error:
            Log(str(v_error), 'error', sys.exc_info()[2].tb_lineno)

        Log('Query finished', 'info', sys._getframe().f_lineno)  # pylint: disable=W0212

    @contracts.contract
    def add_data(self, table_name: str, data_list: tuple):
        """

        :param table_name:
        :param data_list:
        :return:
        :type table_name: str
        :type data_list: tuple(N),N=tuple
        """

        __sql = 'insert into "{}" values "{}"'.format(table_name, data_list)
        self.data_query_batch(__sql)

    def update_data(self, table_name: str, data_list: tuple):
        __sql = 'update '

    def closing_database(self):
        self.cursor.close()
        self.data.close()
