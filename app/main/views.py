from app.press import sports_dong_a, tv_report, sports_seoul
from . import main


@main.route('/')
def index():
    return '<marquee><h1>Success</h1></marquee>'


@main.route('/crawl')
def crawl():
    # sports_dong_a.main()
    # tv_report.main()
    sports_seoul.main()
    return '<marquee><h1>Success - Crawling</h1></marquee>'