from odoo import models, fields

from odoo.addons.project_jsgantt.models.project_planning import _TASK_ID_OFFSET
from odoo.addons.project_jsgantt.models.project_project import GANTT_COLOR_SELECTION


class ProjectTask(models.Model):
    _inherit = "project.task"

    planning_ids = fields.Many2many(
        comodel_name="project.planning",
        string="Planning Records",
        compute="_compute_planning_hierarchy",
        help="All planning records in the task hierarchy.",
        readonly=True,
    )

    gantt_color = fields.Selection(
        selection=GANTT_COLOR_SELECTION,
        default="purple",
        string="Gantt Color",
        help="Color used to display the task in the planning view",
    )

    def _compute_planning_hierarchy(self):
        for task in self:
            # Search for ProjectPlanning records where parent_id is the task's planning ID
            planning_records = self.env["project.planning"].search(
                [("parent_id", "child_of", _TASK_ID_OFFSET + task.id)]
            )
            # Extract task_ids from these records (automatically unique)
            task.planning_ids = planning_records
