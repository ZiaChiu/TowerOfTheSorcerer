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


class _DatabaseError(BaseException):
    @contracts.contract
    def __init__(self, info):
        """
        Any errors in the SQL statement.
        :type info:str
        :param info:
        """
        super().__init__(info)

        self.info = info

    def __str__(self):
        return self.info


class Data:
    """
    This class is used to operate the database.
    """

    def __init__(self):
        self.__database = sqlite3.connect('data/data')
        self.__cursor = self.__database.cursor()

    @contracts.contract
    def data_query(self, sql, value=None):
        # example: self.data_query(sql="select * from hero")
        """
        This is a function to upload one sql statement to database.
        Sql should looks like
        '
        sql= f"select {row_name} from {table_name}"
        self.cursor.execute(sql)
        '

        :param sql:
        :param value:
        :return:
        :type sql:str
        """
        try:
            if value is None:
                self.__cursor.execute(sql)
                self.__database.commit()
            else:
                if "(" in sql:
                    if "?" in sql:
                        if ")" in sql:

                            self.__cursor.execute(sql, value)
                            self.__database.commit()
                        else:
                            raise _DatabaseError('wrong SQL statement')
                    else:
                        raise _DatabaseError('wrong SQL statement')
                else:
                    raise _DatabaseError('wrong SQL statement')
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)
        except contracts.ContractException:
            Log('wrong value format or value!!!', 'error', sys.exc_info()[2].tb_lineno)
        except _DatabaseError as db_error:
            Log(db_error.__str__(), 'error', sys.exc_info()[2].tb_lineno)

        Log('Query finished', 'info', sys._getframe().f_lineno)  # pylint: disable=W0212

    @contracts.contract
    def add_value(self, table_name: str, value_list: list):
        """
        :param table_name:
        :param value_list:
        :return:
        :type table_name: str
        :type value_list: list[N],N=tuple
        """
        try:
            pass
        except contracts.ContractException:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212
        check_sql = f'select * from {table_name}'
        data_value = self.__cursor.execute(check_sql)
        data_format = data_value.fetchone()
        row = '?'

        for index in range(len(data_format)):
            if index == 0:
                row += ',?,'
            elif index == (len(data_format) - 1):
                row += '?'
            elif index < (len(data_format) - 2):
                row += '?,'

        value_format = '(' + row + ')'

        try:
            for value in value_list:
                if len(value) != len(data_format):
                    raise _DatabaseError('wrong tuple length!!!')

            __sql = f'insert into {table_name} value {value_format}'
            self.__cursor.executemany(__sql, value_list)
            self.__database.commit()
            Log('Query finished', 'info', sys._getframe().f_lineno)  # pylint: disable=W0212

        except _DatabaseError as db_error:
            Log(db_error.__str__(), category='error', line=sys.exc_info()[2].tb_lineno)  # pylint: disable=W0212

        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

    @contracts.contract
    def update_all(self, table_name: str, value_list: list):
        # example:
        # db.update_all(table_name="hero", value_list=["'Zia'", 0, 1, 1000, 10, 10, 10, 10, 10, 10])
        """
        This is the function used to execute SQLite's update statement.

        :type table_name:str
        :type value_list:list[]
        """
        try:
            pass
        except contracts.ContractSyntaxError:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

        # Check if the table name exists.
        try:
            table = "'" + table_name + "'"
            tables = self.__cursor. \
                execute(f'SELECT count(*) FROM sqlite_master '
                        f'WHERE type="table" AND name = {table}').fetchone()
            self.__database.commit()
            if tables[0] == 0:
                Log(str(tables), 'debug', sys._getframe().f_lineno)  # pylint: disable=W0212
                raise _DatabaseError('table does not exist in db！！')
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212
        except _DatabaseError as db_error:
            Log(db_error.__str__(), 'error', sys.exc_info()[2].tb_lineno)  # pylint: disable=W0212

        rows = self.__cursor.execute(f"PRAGMA table_info([{table_name}])").fetchall()
        row_list = []
        for row in rows:
            row_list.append(row[1])

        # Check whether the length of the input list
        # is the same as the length of the list of the column name of the db.
        try:
            if len(value_list) != len(row_list):
                raise _DatabaseError("The length of value_list does not match the length of db！！！")
        except _DatabaseError:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

        value_dict = dict(zip(row_list, value_list))
        # update db
        try:
            for value in value_dict:
                sql = f'update {table_name} ' \
                      f'SET {value}={value_dict[value]} ' \
                      f'where {row_list[0]}={value_list[0]}'
                self.data_query(sql)
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

    @contracts.contract
    def update_row(self, table_name: str,
                   primary_id,
                   row_list: list,
                   value_list: list):
        # example:
        # db.update_row(table_name='hero',
        #               ID="'Zia'",
        #               row_list=['exp','gold'],
        #               value_list=[100,100])
        """
        This is the function used to execute SQLite's update statement.

        :param primary_id: the primary_key 's value of db's table.
        :type row_list:list[]
        :type table_name:str
        :type value_list:list[id]
        # value_list should looks like [,column1,column2...columnN]
        """

        # Intercepted the Contract Syntax Error from contracts package
        try:
            pass
        except contracts.ContractSyntaxError:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

        # Intercepted db Errors from SQLite3 database
        # Intercepted the _DatabaseError error
        # Check if the table name exists.
        try:
            table = "'" + table_name + "'"
            tables = self.__cursor. \
                execute(f'SELECT count(*) FROM sqlite_master '
                        f'WHERE type="table" AND name = {table}').fetchone()
            self.__database.commit()
            if tables[0] == 0:
                raise _DatabaseError('table does not exist in db！！')
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212
        except _DatabaseError as db_error:
            Log(db_error.__str__(), 'error', sys.exc_info()[2].tb_lineno)  # pylint: disable=W0212

        rows = self.__cursor.execute(f"PRAGMA table_info([{table_name}])").fetchone()

        try:
            if len(value_list) != len(row_list):
                raise _DatabaseError("The length of value_list does not match the length of db！！！")
        except _DatabaseError:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

        value_dict = dict(zip(row_list, value_list))

        # Intercepted db Errors from SQLite3 database
        # Intercepted the _DatabaseError error
        # update db
        try:
            for value in value_dict:
                sql = f'update {table_name} SET {value}={value_dict[value]} ' \
                      f'where {rows[1]}={primary_id}'
                self.data_query(sql)
        except sqlite3.Error:
            system = sys.exc_info()
            Log(str(system[0]) + str(system[1]), category='error', line=system[2].tb_lineno)  # pylint: disable=W0212

    def closing_db(self):
        """ Close the connection with the database"""
        self.__cursor.close()
        self.__database.close()
