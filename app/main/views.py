from app.press import sports_dong_a, tv_report, sports_seoul, sports_hangook, sports_world, joynews_inews, sbs, enews24, \
    isplus, newsen
from . import main


@main.route('/')
def index():
    return '<h1>Success</h1>'


@main.route('/crawl')
def crawl():
    # sports_dong_a.main()
    # tv_report.main()
    # sports_seoul.main()
    # sports_hangook.main()
    # sports_world.main()
    # joynews_inews.main()
    # sbs.main()
    # enews24.main()
    # isplus.main()
    newsen.main()
    return '<h1>Success - Crawling</h1>'