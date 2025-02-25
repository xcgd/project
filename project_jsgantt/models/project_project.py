from odoo import models, fields, api
from odoo.addons.project_jsgantt.models.project_planning import _TASK_ID_OFFSET

class ProjectProject(models.Model):
    _inherit = "project.project"

    project_planning_ids = fields.Many2many(
        comodel_name='project.planning',
        string='Project Planning Records',
        compute='_compute_planning_ids',
        help="Planning records associated with tasks in this project"
    )

    @api.depends()
    def _compute_planning_ids(self):
        for project in self:
            # Search for ProjectPlanning records related to tasks in this project
            planning_records = self.env['project.planning'].search([
                ('parent_id', 'child_of', project.id)
            ])
            # Set the planning records directly
            project.project_planning_ids = planning_records