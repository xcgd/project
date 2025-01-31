# Copyright 2025 XCG Consulting - Houzéfa Abbasbhay
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, tools


class ProjectPlanning(models.Model):
    _name = "project.planning"
    _description = "Project Planning"
    _auto = False

    project_id = fields.Many2one(comodel_name="project.project")
    task_id = fields.Many2one(comodel_name="project.task")

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name="project.planning")
    is_parent = fields.Boolean()
    is_expanded = fields.Boolean()
    resource_id = fields.Many2one(comodel_name="res.users")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    plan_start_date = fields.Date()
    plan_end_date = fields.Date()

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute(f"create view {self._table} as {self._get_sql_view_query()}")

    def _get_sql_view_query(self):
        query = f"""
        select
            project.id as id,
            project.create_date,
            project.create_uid,
            project.write_date,
            project.write_uid,
            project.id as project_id,
            null as task_id,
            project.name->>'en_US' as name,
            null as parent_id,
            true as is_parent,
            true as is_expanded,
            project.user_id as resource_id,
            project.date_start as start_date,
            project.date as end_date,
            project.date_start as plan_start_date,
            project.date as plan_end_date
        from project_project as project
        join project_task as task on task.project_id = project.id
        where project.active and task.active and not task.is_closed

        union all

        select
            {_TASK_ID_OFFSET} + task.id as id,
            task.create_date,
            task.create_uid,
            task.write_date,
            task.write_uid,
            task.project_id as project_id,
            task.id as task_id,
            task.name,
            (case when task.parent_id is null then task.project_id
             else {_TASK_ID_OFFSET} + task.parent_id end) as parent_id,
            (case when subtask is null then false else true end) as is_parent,
            true as is_expanded,
            tu_rel.user_id as resource_id,
            task.date_assign as start_date,
            greatest(task.date_assign, task.date_deadline) as end_date,
            task.create_date as plan_start_date,
            task.date_deadline as plan_end_date
        from project_task as task
        left join project_task_user_rel as tu_rel on tu_rel.task_id = task.id
        left join project_task as subtask on subtask.parent_id = task.id
        where task.active and not task.is_closed
        """
        return query


_TASK_ID_OFFSET = 1000000
