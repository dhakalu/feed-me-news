from feed.sources.nytimes import NYTimesSource

def main():
    ny_times_source = NYTimesSource()
    articles = ny_times_source.get_feed()
    for article in articles:
        print(article)

if __name__ == "__main__":
    main()
