# Copyright 2025 XCG Consulting - Houzéfa Abbasbhay
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project JSGantt",
    "summary": "Planning view based on projects & tasks displayed with JSGantt",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Services/Project",
    "website": "https://github.com/OCA/project",
    "author": "XCG Consulting, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["project", "web_jsgantt"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_planning_views.xml",
        "views/project_task_views.xml",
        "views/project_project_views.xml",
    ],
}
