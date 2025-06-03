from odoo import models, fields, api

GANTT_COLOR_SELECTION = [
    ("blue", "Blue"),
    ("red", "Red"),
    ("green", "Green"),
    ("yellow", "Yellow"),
    ("purple", "Purple"),
    ("pink", "Pink"),
]


class ProjectProject(models.Model):
    _inherit = "project.project"

    project_planning_ids = fields.Many2many(
        comodel_name="project.planning",
        string="Project Planning Records",
        compute="_compute_planning_ids",
        help="Planning records associated with tasks in this project",
    )

    gantt_color = fields.Selection(
        selection=GANTT_COLOR_SELECTION,
        default="blue",
        string="Gantt Color",
        help="Color used to display the project in the planning view",
    )

    @api.depends()
    def _compute_planning_ids(self):
        for project in self:
            # Search for ProjectPlanning records related to tasks in this project
            planning_records = self.env["project.planning"].search(
                [("parent_id", "child_of", project.id)]
            )
            # Set the planning records directly
            project.project_planning_ids = planning_records
