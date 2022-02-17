STARTUP_EVENT_KEYWORDS =            {
                                        'PRIORITY' :    [
                                                            'adventure',
                                                        ],
                                        'COMBINATION' : [
                                                            ['elevator','pitch'],
                                                            ['venture', 'pitch'],
                                                            ['venture','capital'],
                                                            ['venture','demo','day'],
                                                        ]

                                    }

STARTUP_NAMES =                      [
                                        'slack','telegraph',
                                    ]

STARTUP_LINK_PATTERNS =             [
                                        r'''(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))''',

                                    ]

DATE_PATTERNS_RE =                  [
                                        # r"(January|February|March|April|May|June|July|August|September|October|November|December)/s/d/d[,]/d/d/d/d",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]"
                                        r"[0-9][0-9][ ](?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9]",

                                        r"[0-9][0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",

                                        r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9]",
                                        r"[0-9]/[0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December),\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][ ](?:January|February|March|April|May|June|July|August|September|October|November|December)",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec).\s[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|SEPT.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec).\s[0-9]",
                                    ]

date_strf_pattern = '%m/%d/%Y'

DATE_PATTERNS =                     [
                                        ["%B %d, %Y"        ,date_strf_pattern],
                                        ["%m/%d/%Y"         ,date_strf_pattern],
                                        ["%B %d"            ,'%m/%d'],
                                        ["%Y-%m-%d"         ,date_strf_pattern],
                                        ["%b. %d, %Y"        ,date_strf_pattern],
                                        ["%b %d, %Y"        ,date_strf_pattern],
                                        ["%b %d"            ,'%m/%d'],
                                        ["%d %B, %Y"        ,date_strf_pattern],
                                        ["%d %B %Y"         ,date_strf_pattern],
                                        ["%dst %B %Y"         ,date_strf_pattern],
                                        ["%dnd %B %Y"         ,date_strf_pattern],
                                        ["%drd %B %Y"         ,date_strf_pattern],
                                        ["%dth %B %Y"         ,date_strf_pattern],
                                        ["%dst %b %Y"         ,date_strf_pattern],
                                        ["%dnd %b %Y"         ,date_strf_pattern],
                                        ["%drd %b %Y"         ,date_strf_pattern],
                                        ["%dth %b %Y"         ,date_strf_pattern],
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
                                        r"[0-9][0-9]:[0-9][0-9]\s[A-Za-z][A-Za-z][Tt]",
                                        r"[0-9]:[0-9][0-9]\s[A-Za-z][A-Za-z][Tt]",
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
                                        r"[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9][0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9][0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][A-Za-z][Tt]",
                                        r"[0-9][0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)[ ][A-Za-z][Tt]",
                                        r"[0-9][0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][.][0-9][0-9]\s(?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][.][0-9][0-9](?:a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.|am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn)",
                                        r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9]",
                                        r"[0-9][0-9]:[0-9][0-9]",
                                        r"[0-9]:[0-9][0-9]",
                                        r"[0-9][0-9][ ](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn|a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)",
                                        r"[0-9][ ](?:am|pm|AM|PM|Am|Pm|Nn|NN|nn|MN|Mn|mn|a.m.|p.m.|A.M.|P.M.|A.m.|P.m.|N.n.|N.N.|n.n.|M.N.|M.n.|m.n.)",

                                    ]

time_strf_pattern = '%I:%M:%S %p'

AM_PATTERNS =                       [
                                        "a.m.",
                                        "A.m.",
                                        "A.M.",
                                        "a.M.",
                                        "a.m",
                                        "A.m",
                                        "A.M",
                                        "a.M",
                                        "am.",
                                        "Am.",
                                        "AM.",
                                        "aM.",
                                    ]

PM_PATTERNS =                       [
                                        "p.m.",
                                        "P.m.",
                                        "P.M.",
                                        "p.M.",
                                        "p.m",
                                        "P.m",
                                        "P.M",
                                        "p.M",
                                        "pm.",
                                        "Pm.",
                                        "PM.",
                                        "pM.",
                                    ]

TIME_PATTERNS =                     [
                                        ["%I%p"         ,time_strf_pattern],
                                        ["%I %p"        ,time_strf_pattern],
                                        ["%I:%M %p"     ,time_strf_pattern],
                                        ["%I.%M %p"     ,time_strf_pattern],
                                        ["%I.%M%p"     ,time_strf_pattern],
                                        ["%I:%M%p"      ,time_strf_pattern],
                                        ["T%H:%M:%SZ"   ,time_strf_pattern],
                                        ["%H:%M"   ,time_strf_pattern],
                                        ["%I:%M"        , "'%I:%M:%S"],
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
