Planning view based on projects & tasks displayed with the gantt view provided by
the `web_jsgantt <https://github.com/OCA/web/tree/16.0/web_jsgantt>`_ module.

Projects & tasks are displayed within the same hierarchy (projects > parent tasks > child tasks).

The datamodel is an SQL view maintained up-to-date by postgresql.
Depending on your needs, it may make sense to turn that view into a materialized one with scheduled
refreshes. Implementing this is outside the scope of this module; though take a look at
`bi_sql_editor <https://github.com/OCA/reporting-engine/tree/16.0/bi_sql_editor>`_ for inspiration.
