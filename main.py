import sys
from scrapper import  scrap_website
from mcp_server import get_market_benchmarks, check_compliance_risks
from synthesizer import synthesize_insights
from pdf_generator import render_pdf_report



def main(topic):
    print("1 fetching news ...")
    articles = scrap_website(f"https://news.google.com/search?q={topic}")

    print("2 . getiing internal bechmark (mcp)")
    benchmark = get_market_benchmarks(topic)

    print("3 . checking compliance risks")
    compliance = check_compliance_risks(topic)

    print("4 . synthesizing insights")
    insights = synthesize_insights(topic, articles, benchmark, compliance)

    print("5 . generating pdf report")
    render_pdf_report(insights)

    print("Done !")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <topic>")
        sys.exit(1)

    topic = sys.argv[1]
    main(topic)