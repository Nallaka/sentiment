import googleNewsScraper from "google-news-scraper";

console.log("hello");

// Start function
const start = async function() {
    const articles = await googleNewsScraper({
        searchTerm: "opiate in memphis",
        prettyURLs: false,
        queryVars: {
            hl:"en-US",
            gl:"US",
            ceid:"US:en"
        },
        timeframe: "5y",
        puppeteerArgs: []
    })

   console.log(articles)
}

start()