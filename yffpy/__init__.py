__author__ = "Wren J. R. (uberfastman)"
__email__ = "wrenjr@yahoo.com"

import warnings

warnings.warn(
    "yffpy has been DEPRECATED and replaced by yfpy: https://pypi.org/project/yfpy/\n"
    "Please upgrade your project dependencies.",
    DeprecationWarning
)

from yfpy.data import Data
from yfpy.models import User, Game, League, Team, Standings, Manager, RosterAdds, TeamLogo, TeamPoints, \
    TeamStandings, OutcomeTotals, Streak, Settings, RosterPosition, StatCategories, StatModifiers, Stat, \
    StatPositionType, Bonus, Matchup, MatchupGrade, Player, ByeWeeks, Headshot, Name, PlayerPoints, PlayerStats, \
    SelectedPosition
from yfpy.query import YahooFantasySportsQuery
