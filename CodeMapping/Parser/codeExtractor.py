
class codeExtractor:

    def __init__(self, dataset=None, path=None):
        """
        Code Extractor Constructor - Receives a dataset or path to a csv file and keeps the data as in Attribute.
        """
        if path is None:
            # self.data = dataset

            """splits the data frame into body and answers"""
            self.body_df = dataset[["title", "body", "tags", "post_id"]]
            self.answer_df = dataset[["title", "answers_body", "score"]]
            self.body_df = self.body_df.drop_duplicates(subset=['title'])
            self.body_mapping = {}
            self.answer_mapping = {}
        else:
            self.data = pd.read_csv(path)
        self.words = []
        self.all_text = []

    def extractCodes(self):
        """
        extractCodes Function - cleans the dataset by removing unnecessary tags like <p> and keeps <code> tags.
        Return - dictionary -> title : codes
        """
        # body_mapping = {}
        # answer_mapping = {}
        # index = 0
        # code_dict = pd.DataFrame(columns=['title', 'text', 'code'])

        """handle the posts"""
        tags = ""
        for index, df_row in self.body_df.iterrows():
            text, code = self.extract_code_text_to_dict(df_row['body'])

            if pd.notna(df_row['tags']):
                tags = df_row['tags'].split('|')  # extract the tags
            post_id = df_row["post_id"]

            body_dict = Body_Dict(text, code, tags, post_id )  # adds everything to the new dict
            self.body_mapping[df_row['title']] = body_dict
            self.answer_mapping[df_row['title']] = []  # prepare the title to the answer

        """handle the answers"""
        for index, df_row in self.answer_df.iterrows():
            try:
                text, code = self.extract_code_text_to_dict(df_row['answers_body'])
            except TypeError:
                continue
            body_dict = Post_Dict(text, code, df_row['score'])  # adds the comment score
            self.answer_mapping[df_row['title']].append(body_dict)

        return self.body_mapping, self.answer_mapping

    def extract_code_text_to_dict(self, post):
        """
        extract_code_text_to_dict Function - extract the code and the text from each post
        :param post:
        :return text, code after the data preprocess
        """
        text = ""
        code = []
        for curr_text in re.findall(r"<p>(.*?)</p>", post, flags=re.DOTALL):  # extract the text
            text += curr_text
            text = re.sub("<code>(.*?)</code>", '', text)
            text = text.replace('&gt;', '>')
            text = text.replace('&lt;', '<')
            text = text.replace('&amp;&amp;', '&&')
            text = text.replace('&amp;', '&')
            text = text.replace('&quot;', '"')
            # word_tokens = word_tokenize(text)

            # self.words += [w for w in word_tokens if not w in stop_words]
            self.all_text.append(text)
        row = re.sub('<p>.*?</p>', '', post)  # remove the text

        for curr_code in re.findall(r"<code>(.*?)</code>", row, flags=re.DOTALL):  # extract the code
            """handle html tags from crawler"""
            curr_code = curr_code.replace('&gt;', '>')
            curr_code = curr_code.replace('&lt;', '<')
            curr_code = curr_code.replace('&amp;&amp;', '&&')
            curr_code = curr_code.replace('&amp;', '&')
            curr_code = curr_code.replace('&quot;', '"')
            curr_code = curr_code.replace('[...]', '')  # TODO: TEST IF WORKING
            curr_code = curr_code.replace('...', '/** ...*/')

            code.append(curr_code)

        for index in range(len(code)):
            search_comments = re.findall("//(.*?)\n", code[index], flags=re.DOTALL)
            for comment in search_comments:
                if "/**" not in comment:
                    code[index] = code[index].replace("//" + comment, '/**' + comment + "*/")

        return text, code

