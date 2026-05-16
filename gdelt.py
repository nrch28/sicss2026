import os, time
from datetime import datetime
from gdeltdoc import GdeltDoc, Filters

months = [
    ("2024-01-01", "2024-01-31", "jan2024"),
    ("2024-02-01", "2024-02-28", "feb2024"),
    ("2024-03-01", "2024-03-31", "mar2024"),
    ("2024-04-01", "2024-04-30", "apr2024"),
    ("2024-05-01", "2024-05-31", "may2024"),
    ("2024-06-01", "2024-06-30", "jun2024"),
    ("2024-07-01", "2024-07-31", "jul2024"),
    ("2024-08-01", "2024-08-31", "aug2024"),
    ("2024-09-01", "2024-09-30", "sep2024"),
    ("2024-10-01", "2024-10-31", "oct2024"),
    ("2024-11-01", "2024-11-30", "nov2024"),
    ("2024-12-01", "2024-12-31", "dec2024")
]

for monthStart, monthEnd, monthName in months:
    try:
        filters = Filters(
            keyword="data center",
            country="US",
            start_date=monthStart,
            end_date=monthEnd,
            domain=[
                "reuters.com",
                "bloomberg.com",
                "wsj.com",
                "ft.com",
                "apnews.com",
                "cnbc.com",
                "cnn.com",
                "businesswire.com",
                "nytimes.com",
                "washingtonpost.com"
            ]
        )
        dataCenterArticles = GdeltDoc().article_search(filters)
        tone = GdeltDoc().timeline_search("timelinetone", filters)

        urlFile = f"data/{monthName}news.csv"
        toneFile = f"data/{monthName}tone.csv"

        dataCenterArticles.to_csv(urlFile)
        time.sleep(1200)

        tone.to_csv(toneFile)
        
    except Exception as e:
        print(f"Error for {monthName}: {type(e).__name__}, {e}")

    finally: 
        print(f"Waiting after making both requests for {monthName}.")
        print(f"\nCurrent time is {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(1200)