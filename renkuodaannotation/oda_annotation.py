import json

from pathlib import Path
from renku.domain_model.project_context import project_context

from aqsconverters.io import ODA_ANNOTATION_DIR, COMMON_DIR
from renkuodaannotation.config import ENTITY_METADATA_AQS_DIR


class OdaAnnotation(object):
    def __init__(self, run):
        self.run = run

    @property
    def renku_oda_annotation_path(self):
        """Return a ``Path`` instance of Renku oda annotation folder."""
        return Path(project_context.metadata_path).joinpath(ODA_ANNOTATION_DIR).joinpath(COMMON_DIR)

    @property
    def oda_metadata_path(self):
        """Return a ``Path`` instance of Renku oda metadata folder."""
        return Path(project_context.metadata_path).joinpath(ENTITY_METADATA_AQS_DIR)

    def load_model(self, path):
        """Load AQS reference file."""
        if path and path.exists():
            return json.load(path.open())
        return {}
