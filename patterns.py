STARTUP_EVENT_KEYWORDS =            [

                                    ]

STARTUP_LINK_PATTERNS =             [

                                    ]

DATE_PATTERNS =                     [

                                    ]

TIME_PATTERNS =                     [

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
                                        # +44 131 449 5111
                                    ]
