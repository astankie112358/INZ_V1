import nba_scraper.nba_scraper as nba
import nba_scraper.scrape_functions as sf
import nba_scraper.helper_functions as hf
import nba_api.stats.endpoints as api
from nba_api.stats.endpoints._base import Endpoint as end
#a=sf.get_date_games("2020-08-03","2020-08-05")
#print(nba.scrape_date_range("2020-08-03","2020-08-05"))
#print(a)
a=api.leaguegamefinder.LeagueIDNullable.nba.isnumeric().as_integer_ratio(

end.
