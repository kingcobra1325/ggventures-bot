STARTUP_EVENT_KEYWORDS =            [

                                    ]

STARTUP_LINK_PATTERNS =             [

                                    ]

DATE_PATTERNS_RE =                  [
                                        # r"(January|February|March|April|May|June|July|August|September|October|November|December)/s/d/d[,]/d/d/d/d",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][0-9]",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9]",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9]",
                                        r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9]",
                                        r"[0-9]/[0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December),\s[0-9][0-9][0-9][0-9]",
                                    ]

date_strf_pattern = '%m/%d/%Y'

DATE_PATTERNS =                     [
                                        ["%B %d, %Y",date_strf_pattern],
                                        ["%m/%d/%Y",date_strf_pattern],
                                        ["%B %d",'%m/%d'],
                                        ["%Y-%m-%d",date_strf_pattern],
                                        ["%b %d, %Y",date_strf_pattern],
                                        ["%b %d",'%m/%d'],
                                        ["%d %B, %Y",date_strf_pattern],
                                    ]

TIME_PATTERNS_RE =                  [
                                        r"(?:Noon|noon|NOON|Midnight|midnight|MIDNIGHT)",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][(][A-Za-z][A-Za-z][Tt][)]",
                                        r"[0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][(][A-Za-z][A-Za-z][Tt][)]",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][(][A-Za-z][Tt][)]",
                                        r"[0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][(][A-Za-z][Tt][)]",
                                        r"T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9]:[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9]:[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9]:[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)[ ][A-Za-z][Tt]",
                                        r"[0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)[ ][A-Za-z][Tt]",
                                        r"[0-9][0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)",
                                        r"[0-9]:[0-9][0-9]\s(?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9]:[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)",
                                        r"[0-9]:[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9]:[0-9][0-9]",
                                        r"[0-9]:[0-9][0-9]",
                                        r"[0-9][ ](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn|a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)",

                                    ]

time_strf_pattern = '%I:%M:%S %p'

TIME_PATTERNS =                     [
                                        ["%I%p",time_strf_pattern],
                                        ["%I %p",time_strf_pattern],
                                        ["%I:%M %p",time_strf_pattern],
                                        ["%I:%M", "'%I:%M:%S"],
                                        ["%I:%M%p",time_strf_pattern],
                                        ["T%H:%M:%SZ",time_strf_pattern],
                                    ]

TZ_PATTERNS =                       [
                                        r'[ ][A-Za-z][A-Za-z][Tt]',
                                        r"[ ][A-Za-z][Tt]",
                                        r"[ ][(][A-Za-z][Tt][)]",
                                        r"[ ][(][A-Za-z][A-Za-z][Tt][)]",

                                    ]


TZ_EXCLUDE =                        [
                                        ' unt',
                                    ]

EMAIL_PATTERNS =                    [
                                        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
                                        r"^\S+@\S+\.\S+$",
                                        # r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                                    ]

PHONE_NUMBER_PATTERNS =             [
                                        # UK NUMBERS
                                        r"[+]\d\d\d\d\d\d\d\d\d\d\d\d",
                                        r"[+]\d\d\s\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\d\d\s\d\d\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d[(]\d[)]\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\s\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\s\d\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\s\d\d\d\d\s\d\d\d\d\d\d",
                                        # US NUMBERS
                                        r"[()]\d\d\d[)]\s\d\d\d-\d\d\d\d",
                                        r"\d\d\d-\d\d\d-\d\d\d\d",
                                        r"\d\d\d.\d\d\d.\d\d\d\d",
                                        # r"\d\d\d.\d\d\d.\s{0,1}\D\D\D\D",
                                        # NZL NUMBERS
                                        r"\d\d\d\s\d\d\d\d\d\d\d",
                                        r"\d\d\d\d\s\d\d\s\d\d\s\d\d",
                                        r"[+]\d\d\s\d\s\d\d\d\s\d\d\d\d",
                                        # IRL NUMBERS
                                        r"/d/d/d/d/s/d/d/s/d/d/s/d/d",
                                        r"[+]/d/d/d/s/d/s/d/d/d/s/d/d/d/d",
                                        r"/d/d/d/s/d/d/d/d/d/d/d"
                                        # CAN NUMBERS
                                        r"/d/d/d/s/d/d/d-/d/d/d/d",
                                        # AUS NUMBERS
                                        r"[+][0-9][0-9][ ][0-9][ ][0-9][0-9][0-9][0-9][ ][0-9][0-9][0-9][0-9]",
                                        r"[+][0-9][0-9][ ][0-9][ ][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
                                    ]
