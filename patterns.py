STARTUP_EVENT_KEYWORDS =            {
                                        'PRIORITY' :    [
                                                            'startup','start-up','demo-day'
                                                        ],
                                        'COMBINATION' : [
                                                            ['elevator','pitch'],
                                                            ['venture', 'pitch'],
                                                            ['venture','capital'],
                                                            ['venture','demo','day'],
                                                            ['tech','accelerator'],
                                                            ['pitch','accelerator'],
                                                            ['tech','accelerator'],
                                                            ['tech','competition'],
                                                        ],
                                        'WHOLE' : [
                                                    'venture','capital'
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
                                        r"[0-9][0-9](?:st|ST|nd|ND|rd|RD|th|TH)[ ](?:of|OF|Of|oF)[ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)",
                                        r"[0-9](?:st|ST|nd|ND|rd|RD|th|TH)[ ](?:of|OF|Of|oF)[ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]"
                                        r"[0-9][0-9][ ](?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][ ](?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9]",
                                        r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9]",

                                        r"[0-9][0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[,]\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[,]\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9](?:ST|ND|RD|TH|st|nd|rd|th)\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",

                                        r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9]-[0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9]",
                                        r"[0-9][0-9][0-9][0-9]-[0-9]-[0-9]",
                                        r"[0-9][0-9][.][ ](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|OKT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|OKT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Okt|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Okt.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|okt.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|okt|nov|dec)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][.][ ](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|OKT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|OKT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Okt|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Okt.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|okt.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|okt|nov|dec)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][.](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|OKT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|OKT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Okt|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Okt.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|okt.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|okt|nov|dec)[.][0-9][0-9][0-9][0-9]",
                                        r"[0-9][.](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|OKT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|OKT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Okt|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Okt.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|okt.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|okt|nov|dec)[.][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][,][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][ ][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[ ][0-9]",
                                        r"[0-9][0-9]/[0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9]/[0-9]/[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December),\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|January|February|March|April|May|June|July|August|September|October|November|December)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][ ](?:January|February|March|April|May|June|July|August|September|October|November|December)[ ][0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][ ](?:January|February|March|April|May|June|July|August|September|October|November|December)",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|sep|Sep.|sep.|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9][0-9][-][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|sep|Sep.|sep.|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9][-][0-9][0-9][0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9]",
                                        r"[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9]\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)\s[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9]\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)",
                                        r"[0-9]\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)",
                                        r"[0-9][0-9]/[0-9][0-9]",
                                        r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9]",
                                        r"[0-9][0-9]/[0-9]/[0-9][0-9]",
                                        r"[0-9]/[0-9][0-9]/[0-9][0-9]",
                                        r"[0-9]/[0-9]/[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9][0-9]",
                                        r"(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9]",
                                        r"[0-9][0-9](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9][0-9][0-9][0-9]",
                                        r"[0-9](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)[0-9][0-9][0-9][0-9]",
                                        r"[0-9][0-9](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)",
                                        r"[0-9](?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|JAN.|FEB.|MAR.|APR.|MAY.|JUN.|JUL.|AUG.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|OCT.|NOV.|DEC.|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec|Jan.|Feb.|Mar.|Apr.|May.|Jun.|Jul.|Aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|Oct.|Nov.|Dec.|jan.|feb.|mar.|apr.|may.|jun.|jul.|aug.|Sep|sep|Sep.|sep.|SEP|SEP.|Sept.|oct.|nov.|dec.|jan|feb|mar|apr|may|jun|jul|aug|sept|oct|nov|dec)",
                                        
                                    ]

date_strf_pattern = '%m/%d/%Y'

DATE_PATTERNS =                     [
                                        ["%B %d, %Y"        ,date_strf_pattern],
                                        ["%B %d %Y"        ,date_strf_pattern],
                                        ["%d. %B. %Y"        ,date_strf_pattern],
                                        ["%d %B. %Y"        ,date_strf_pattern],
                                        ["%d. %B %Y"        ,date_strf_pattern],
                                        ["%d %B %Y"        ,date_strf_pattern],
                                        ["%m/%d/%Y"         ,date_strf_pattern],
                                        ["%d/%m/%Y"         ,date_strf_pattern],
                                        ["%Y/%m/%d"         ,date_strf_pattern],
                                        ["%Y/%d/%m"         ,date_strf_pattern],
                                        ["%d/%m"         ,'%m/%d'],
                                        ["%m/%d"         ,'%m/%d'],
                                        ["%m.%d.%Y"         ,date_strf_pattern],
                                        ["%d.%m.%Y"         ,date_strf_pattern],
                                        ["%d.%B.%Y"         ,date_strf_pattern],
                                        ["%B.%d.%Y"         ,date_strf_pattern],
                                        ["%d.%b.%Y"         ,date_strf_pattern],
                                        ["%b.%d.%Y"         ,date_strf_pattern],
                                        ["%m.%d"         ,'%m/%d'],
                                        ["%B %d"            ,'%m/%d'],
                                        ["%Y-%m-%d"         ,date_strf_pattern],
                                        ["%m-%d-%Y"         ,date_strf_pattern],
                                        ["%d-%m-%Y"         ,date_strf_pattern],
                                        ["%b. %d, %Y"        ,date_strf_pattern],
                                        ["%b %d, %Y"        ,date_strf_pattern],
                                        ["%b. %d %Y"        ,date_strf_pattern],
                                        ["%d. %b., %Y"        ,date_strf_pattern],
                                        ["%d. %b. %Y"        ,date_strf_pattern],
                                        ["%d %b. %Y"        ,date_strf_pattern],
                                        ["%d. %b %Y"        ,date_strf_pattern],
                                        ["%d %b %Y"        ,date_strf_pattern],
                                        ["%b %d %Y"        ,date_strf_pattern],
                                        ["%d%b%Y"            ,date_strf_pattern],
                                        ["%b%d%Y"            ,date_strf_pattern],
                                        ["%b %d"            ,'%m/%d'],
                                        ["%d %b"            ,'%m/%d'],
                                        ["%d%b"            ,'%m/%d'],
                                        ["%b%d"            ,'%m/%d'],
                                        ["%d %B, %Y"        ,date_strf_pattern],
                                        ["%d %B %Y"         ,date_strf_pattern],
                                        ["%d %b %Y"        ,date_strf_pattern],
                                        ["%d. %b. %Y"         ,date_strf_pattern],
                                        ["%d. %b %Y"         ,date_strf_pattern],
                                        ["%d %B"            ,'%m/%d'],
                                        ["%dst of %B"            ,'%m/%d'],
                                        ["%dnd of %B"            ,'%m/%d'],
                                        ["%drd of %B"            ,'%m/%d'],
                                        ["%dth of %B"            ,'%m/%d'],
                                        ["%dst %B %Y"         ,date_strf_pattern],
                                        ["%dnd %B %Y"         ,date_strf_pattern],
                                        ["%drd %B %Y"         ,date_strf_pattern],
                                        ["%dth %B %Y"         ,date_strf_pattern],
                                        ["%dst %b %Y"         ,date_strf_pattern],
                                        ["%dnd %b %Y"         ,date_strf_pattern],
                                        ["%drd %b %Y"         ,date_strf_pattern],
                                        ["%dth %b %Y"         ,date_strf_pattern],
                                        ["%dst %B, %Y"         ,date_strf_pattern],
                                        ["%dnd %B, %Y"         ,date_strf_pattern],
                                        ["%drd %B, %Y"         ,date_strf_pattern],
                                        ["%dth %B, %Y"         ,date_strf_pattern],
                                        ["%dst %b, %Y"         ,date_strf_pattern],
                                        ["%dnd %b, %Y"         ,date_strf_pattern],
                                        ["%drd %b, %Y"         ,date_strf_pattern],
                                        ["%dth %b, %Y"         ,date_strf_pattern],
                                        ["%d.%m.%Y"         ,date_strf_pattern],
                                        ["%Y.%m.%d"         ,date_strf_pattern],
                                        ["%d/%m/%y"         ,date_strf_pattern],
                                        ["%m/%d/%y"         ,date_strf_pattern],
                                        ["%b-%d-%Y"         ,date_strf_pattern],
                                        ["%b%Y%d"         ,date_strf_pattern],
                                        ["%b0%y%d"         ,date_strf_pattern],
                                        ["%d %b %Y"         ,date_strf_pattern],
                                        ["%b-%d"         ,'%m/%d'],                                        
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
                                        ["%H:%M:%SZ"   ,time_strf_pattern],
                                        ["%H:%M:%S"   ,time_strf_pattern],
                                        ["%I:%M:%S"   ,time_strf_pattern],
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
                                        r"(?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)(?:[0-9]|\d|)(?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)(?:[0-9]|\d|)(?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)(?:[0-9]|\d|)(?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)(?:[0-9]|\d|)(?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[+().]|[-]|[ ]|\s|)(?:[+().]|[-]|[ ]|\s|)[0-9](?:[0-9]|\d|)(?:[0-9]|\d|)(?:[0-9]|\d|)(?:[0-9]|\d|)",
                                        # r"/^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d+)\)?)[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?$/i",
                                        # r"/^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$/gm",
                                        # r"^(\\+\\d{1,3}( )?)?((\\(\\d{1,3}\\))|\\d{1,3})[- .]?\\d{3,4}[- .]?\\d{4}$",
                                        r"^\+[0-9]{1,3}\.[0-9]{4,14}(?:x.+)?$",
                                        # r"^\+(?:[0-9]●?){6,14}[0-9]$",
                                        # r"/^(\+|\d)[0-9]{7,16}$/;",
                                        # r"^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$",
                                        # r"^(\+[1-9][0-9]*(\([0-9]*\)|-[0-9]*-))?[0]?[1-9][0-9\- ]*$",
                                        # UK NUMBERS
                                        # r"/^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$/"
                                        r"[+]\d\d\d\d\d\d\d\d\d\d\d\d",
                                        r"[+]\d\d\s\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\d\d\s\d\d\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d[(]\d[)]\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\s\d\d\d\s\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\d\d\s\d\d\d\d\s\d\d\d\d",
                                        r"[+]\d\d\s[(]\d[)]\s\d\d\d\d\s\d\d\d\d\d\d",
                                        # ITA NUMBERS
                                        # US NUMBERS
                                        # r"^([+]39)?((38[{8,9}|0])|(34[{7-9}|0])|(36[6|8|0])|(33[{3-9}|0])|(32[{8,9}]))([\d]{7})$",
                                        r"[()]\d\d\d[)]\s\d\d\d-\d\d\d\d",
                                        r"\d\d\d-\d\d\d-\d\d\d\d",
                                        r"\d\d\d.\d\d\d.\d\d\d\d",
                                        # r"\d\d\d.\d\d\d.\s{0,1}\D\D\D\D",
                                        # FRA NUMBERS
                                        # r"/^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$/",
                                        # NZL NUMBERS
                                        r"\d\d\d\s\d\d\d\d\d\d\d",
                                        r"\d\d\d\d\s\d\d\s\d\d\s\d\d",
                                        r"[+]\d\d\s\d\s\d\d\d\s\d\d\d\d",
                                        # IRL NUMBERS
                                        r"/d/d/d/d/s/d/d/s/d/d/s/d/d",
                                        r"[+]/d/d/d/s/d/s/d/d/d/s/d/d/d/d",
                                        r"/d/d/d/s/d/d/d/d/d/d/d",
                                        # CAN NUMBERS
                                        r"/d/d/d/s/d/d/d-/d/d/d/d",
                                        # AUS NUMBERS
                                        # r"/(^1300\d{6}$)|(^1800|1900|1902\d{6}$)|(^0[2|3|7|8]{1}[0-9]{8}$)|(^13\d{4}$)|(^04\d{2,3}\d{6}$)/",
                                        r"[+][0-9][0-9][ ][0-9][ ][0-9][0-9][0-9][0-9][ ][0-9][0-9][0-9][0-9]",
                                        r"[+][0-9][0-9][ ][0-9][ ][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
                                        # GER NUMBERS
                                        # r"/(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))/",
                                        # CHN NUMBERS
                                        # r"/^(?:(?:\d{3}-)?\d{8}|^(?:\d{4}-)?\d{7,8})(?:-\d+)?$/",
                                        # r"/^(?:(?:\+|00)86)?1(?:(?:3[\d])|(?:4[5-79])|(?:5[0-35-9])|(?:6[5-7])|(?:7[0-8])|(?:8[\d])|(?:9[189]))\d{8}$/",
                                        # IND NUMBERS
                                        # r"/((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}/",
                                        # BRA NUMBERS
                                        # r"/\(([0-9]{2}|0{1}((x|[0-9]){2}[0-9]{2}))\)\s*[0-9]{3,4}[- ]*[0-9]{4}/",
                                        # NLD NUMBERS
                                        # r"/(^\+[0-9]{2}|^\+[0-9]{2}\(0\)|^\(\+[0-9]{2}\)\(0\)|^00[0-9]{2}|^0)([0-9]{9}$|[0-9\-\s]{10}$)/",
                                        # SWEDEN NUMBERS
                                        # r"/^(([+]\d{2}[ ][1-9]\d{0,2}[ ])|([0]\d{1,3}[-]))((\d{2}([ ]\d{2}){2})|(\d{3}([ ]\d{3})*([ ]\d{2})+))$/",
                                    ]
