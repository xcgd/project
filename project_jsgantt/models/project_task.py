from odoo import models, fields, api

from odoo.addons.project_jsgantt.models.project_planning import _TASK_ID_OFFSET


class ProjectTask(models.Model):
    _inherit = "project.task"

    planning_ids = fields.Many2many(
        comodel_name='project.planning',
        string="Planning Records",
        compute='_compute_planning_hierarchy',
        help="All planning records in the task hierarchy.",
        readonly=True,
    )

    def _compute_planning_hierarchy(self):
        for task in self:
            # Search for ProjectPlanning records where parent_id is the task's planning ID
            planning_records = self.env['project.planning'].search([
                ('parent_id', 'child_of', _TASK_ID_OFFSET + task.id)
            ])
            # Extract task_ids from these records (automatically unique)
            task.planning_ids = planning_records