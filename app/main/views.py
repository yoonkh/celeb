from app.models import Article
from app.press import sports_dong_a, tv_report, sports_seoul, sports_hangook, sports_world, joynews_inews, sbs, enews24, \
    isplus, newsen, mydaily, star_news, sports_khan, sports_chosun, sports_today, xports_news, mbc_sports_plus, \
    mk_sports, osen, spotv_news, ten_asia, tv_daily, heraldpop
from . import main


@main.route('/')
def index():
    return '<h1>Success</h1>'


@main.route('/crawl')
def crawl():
    # sports_dong_a.main() # 스포츠동아
    # tv_report.main() # TV리포트
    # sports_seoul.main() # 스포츠서울
    # sports_hangook.main() # 스포츠한국
    # sports_world.main() # 스포츠월드
    # joynews_inews.main() # 조이뉴스
    # sbs.main() # SBS연예스포츠
    # enews24.main() # enews24
    # isplus.main() # 일간스포츠
    # newsen.main() # 뉴스엔
    # mydaily.main() # 마이데일리
    # star_news.main() # 스타뉴스
    # sports_khan.main() # 스포츠경향
    # sports_chosun.main() # 스포츠조선
    # sports_today.main() # 스포츠투데이
    # xports_news.main() # 엑스포츠뉴스
    # mbc_sports_plus.main() # 엠스플뉴스
    # mk_sports.main() # MK스포츠
    # osen.main() # OSEN
    # spotv_news.main() # SPOTV뉴스
    # ten_asia.main() # 텐아시아
    # tv_daily.main() # 티브이데일리
    # heraldpop.main() # 헤럴드팝
    return '<h1>Success - Crawling</h1>'
