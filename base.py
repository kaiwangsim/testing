# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:58:15 2020

@author: pc
"""

import pandas as pd
from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://wangkai:JIAyou@777@8.210.61.73:3306/mydb01")


sql_query = 'select * from table001'
# 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
df_read = pd.read_sql_query(sql_query, engine)
print(df_read)


