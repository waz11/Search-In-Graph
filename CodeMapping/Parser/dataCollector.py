
class dataCollector:

    def __init__(self, path):
        """
        Data Collector Constructor - adds google credentials.
        """
        cred_dir = dirname(dirname(__file__))
        # environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = join(cred_dir, 'CodeMapping/stackoverflowmap-03d45ecd6795.json')
        self.client = None
        self.dataset_ref = None

    def open_client(self):
        """
        open_client Function - connects to google big query dataset
        """
        self.client = bigquery.Client()
        self.dataset_ref = self.client.dataset("stackoverflow", project="bigquery-public-data")

    def get_dataset(self, query):
        """
        get_dataset Function - Enters a query to google big query dataset
        Return - dataframe that contains java related posts
        """
        safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=40 ** 10)
        questions_query_job = self.client.query(query, job_config=safe_config)
        questions_results = questions_query_job.to_dataframe()
        questions_results = questions_results[~questions_results.body.isin(['class'])]
        questions_results = questions_results[~questions_results.answers_body.isin(['class'])]
        questions_results.to_csv("question_result.csv")
        return questions_results
