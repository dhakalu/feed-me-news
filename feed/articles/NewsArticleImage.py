class NewsArticleImage:
    """
        Representation of an image
    """

    def __init__(self, url: str, credit: str, alt: str):
        self.url =url
        self.credit = credit
        self.alt = alt

    def __repr__(self) -> str:
        return f'''
            url: {self.url}
            credit: {self.credit}
            description: {self.alt}
        '''

    def __eq__(self, __o: object) -> bool:
        return self.url == __o.url and self.credit == __o.credit and self.alt == __o.alt
