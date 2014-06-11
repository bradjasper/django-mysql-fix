import re
from django.db.backends.mysql.compiler import SQLCompiler as BaseSQLCompiler
from django.db.backends.mysql.compiler import SQLInsertCompiler, \
    SQLDeleteCompiler, SQLUpdateCompiler, SQLAggregateCompiler, \
    SQLDateCompiler, SQLDateTimeCompiler


import logging
log = logging.getLogger(__name__)

class SQLCompiler(BaseSQLCompiler):
    STRAIGHT_INNER = 'STRAIGHT_JOIN'
    
    def as_sql(self, *args, **kwargs):
        sql, args = super(SQLCompiler, self).as_sql(*args, **kwargs)

        # Hackiest thing ever. But Django doesn't allow an easy way to specify STRAIGHT_JOIN
        if "INNER JOIN `ticketbook_ticketgroup`" in sql:
            sql = re.sub(r"^SELECT", u"SELECT STRAIGHT_JOIN", sql)

        return (sql, args)













































































































