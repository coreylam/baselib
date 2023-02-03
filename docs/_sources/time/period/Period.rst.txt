Period
**************************************************

.. py:currentmodule:: Period

时间段计算，用于获取某个时间段的起止时间（如1小时内，24小时内，7天内等），可用于监控等时间段查询方法，计算起止时间

.. code:: python

  from baselib.time.period import Period


获取 N 小时内时间段（起止时间）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: get_recent_hour(n, minutes_ago=0)

  获取近 N 个小时的起止时间

  :param int n: 必填，小时数
  :param int miinutes_ago: 选填，设置截止时间前移分钟数，默认为0（表示截止到当前时间），用于部分场景需要不统计近几分钟

  :rtype: datetime set
  :return: start_time, end_time, 表示起始时间和截止时间，均为 datetime 对象


ii. 调用案例
--------------------------------------------------

.. code-block:: python

    # 获取 1 小时内的时间段（从1小时之前，到当前时间）
    start_time, end_time = Period.get_recent_hour(1)

    # 获取 截止到 10 分钟前，1小时内的时间点（从1小时10分钟之前，到10分钟之前）
    start_time, end_time = Period.get_recent_hour(1, 10)

获取 N 分钟内时间段（起止时间）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: get_recent_minute(n, minutes_ago=0)

  获取近 N 分钟的起止时间

  :param int n: 必填，分钟数
  :param int miinutes_ago: 选填，设置截止时间前移分钟数，默认为0（表示截止到当前时间），用于部分场景需要不统计近几分钟

  :rtype: datetime set
  :return: start_time, end_time, 表示起始时间和截止时间，均为 datetime 对象

调用方式参考 ``get_recent_hour``

获取 N 天内时间段（起止时间）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: get_recent_day(n, minutes_ago=0)

  获取近 N 天的起止时间

  :param int n: 必填，天数
  :param int miinutes_ago: 选填，设置截止时间前移分钟数，默认为0（表示截止到当前时间），用于部分场景需要不统计近几分钟

  :rtype: datetime set
  :return: start_time, end_time, 表示起始时间和截止时间，均为 datetime 对象

调用方式参考 ``get_recent_hour``

获取当天的开始时间（0时0分0秒）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: get_day_begin(dt=None)

  获取指定日期那天的开始时间（0时0分0秒）

  :param datetime dt: 选填，指定日期，默认为None，即获取当天的开始时间

  :rtype: datetime
  :return: 当天的开始时间（0时0分0秒）

ii. 调用案例
--------------------------------------------------

.. code-block:: python

    start_time = Period.get_day_begion()

获取当天的结束时间（23时59分59秒）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: get_day_end(dt=None)

  获取指定日期那天的结束时间（23时59分59秒）

  :param datetime dt: 选填，指定日期，默认为None，即获取当天的结束时间

  :rtype: datetime
  :return: 当天的结束时间（23时59分59秒）

ii. 调用案例
--------------------------------------------------

.. code-block:: python

    end_time = Period.get_day_end()

获取当前时间
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: now()

  获取当前时间（等同于datetime.now()）

  :rtype: datetime
  :return: 获取当前时间（等同于datetime.now()）

ii. 调用案例
--------------------------------------------------

.. code-block:: python

    now = Period.now()

将时间转换为字符串（日期+时分秒）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: format_datetime(dt)

  将时间类型（datetime）转换为字符串

  :param datetime dt: 必填，指定日期

  :rtype: string
  :return: 日期对应的字符串，格式如： 2022-10-01 12:34:56

ii. 调用案例
--------------------------------------------------

.. code-block:: python

    now = datatime.datetime.now()
    now_string = Period.format_datetime(now)


将时间转换为字符串（日期+T+时分秒）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: format_t_datetime(dt)

  将时间类型（datetime）转换为字符串

  :param datetime dt: 必填，指定日期

  :rtype: string
  :return: 日期对应的字符串，格式如： 2022-10-01T12:34:56Z

调用方法参考 ``format_datetime``

将时间转换为字符串（日期）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: format_date(dt)

  将时间类型（datetime）转换为字符串

  :param datetime dt: 必填，指定日期

  :rtype: string
  :return: 日期对应的字符串，格式如： 2022-10-01

调用方法参考 ``format_datetime``

将时间转换为字符串（时分秒）
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: format_time(dt)

  将时间类型（datetime）转换为字符串

  :param datetime dt: 必填，指定日期

  :rtype: string
  :return: 日期对应的字符串，格式如： 12:34:56

调用方法参考 ``format_datetime``


将时间转化为时间戳
==================================================

i. 函数声明
--------------------------------------------------

.. py:function:: format_timestamp(dt)

  获取 dt 对应的时间戳， 用于部分产品的时间段计算（如审计）

  :param datetime dt: 必填，指定日期时间

  :rtype: int
  :return: 将 dt 对应时间转换成时间戳

调用方法参考 ``format_datetime``