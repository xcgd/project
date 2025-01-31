* Project names are English only, need to better support translatable jsonb fields.
* Extract date fields added by ``project_timeline`` into a separate module and use them in this one.
* Add jsgantt views onto project & task models, same as ``project_timeline`` (beware of action
  override conflicts, see <https://github.com/OCA/web/pull/3073>).
