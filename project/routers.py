omop_apps = ["omop"]
ontology_apps = ["icd_converter", "umls"]


class CustomDatabaseRouter:

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label in omop_apps:
            return "omop"
        if model._meta.app_label in ontology_apps:
            return "ontologies"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label in omop_apps:
            return "patient_data"
        if model._meta.app_label in ontology_apps:
            return "ontologies"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        If not set, migrations will create duplicate tables in all databases.
        """
        if app_label in omop_apps:
            return db == "patient_data"
        if app_label in ontology_apps:
            return db == "ontologies"
        return db == "default"
