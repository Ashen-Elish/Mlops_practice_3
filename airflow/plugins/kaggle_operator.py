from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleOperator(BaseOperator):

    @apply_defaults
    def __init__(
        self,
        dataset,
        output,
        *args, **kwargs):
        super(KaggleOperator, self).__init__(*args, **kwargs)
        self.dataset = dataset
        self.output = output

    def execute(self, context):
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(self.dataset, path=self.output, unzip=True)
