# legal_knowledge.py - IPC Punishment Database
# Version: 2.0 - Fixed bail_provisions handling

"""
Indian Penal Code (IPC) Punishment Information
Updated as of January 2026
"""

IPC_PUNISHMENTS = {
    "murder": {
        "section": "IPC Section 302",
        "title": "Punishment for Murder",
        "definition": "Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.",
        "punishment": "Death penalty OR Life imprisonment + Fine",
        "key_points": [
            "Most serious offense under IPC",
            "Intention or knowledge to cause death",
            "Pre-meditation often considered for death penalty",
            "Death penalty reserved for 'rarest of rare' cases"
        ],
        "aggravating_factors": [
            "Brutal or heinous nature of crime",
            "Multiple murders",
            "Murder of child or helpless person",
            "Murder for ransom or during robbery",
            "Anti-national or anti-social nature"
        ],
        "supreme_court_guidelines": {
            "case": "Bachan Singh v. State of Punjab (1980) & Machhi Singh v. State of Punjab (1983)",
            "principle": "Death penalty only in rarest of rare cases",
            "test": "When alternative option is unquestionably foreclosed"
        },
        "related_sections": ["IPC 300 (Definition)", "IPC 304 (Culpable Homicide)"],
        "conviction_rate": "46.2% (NCRB 2025)",
        "average_sentence": "Life imprisonment (14-20 years actual)"
    },
    
    "culpable_homicide": {
        "section": "IPC Section 304",
        "title": "Punishment for Culpable Homicide Not Amounting to Murder",
        "definition": "Culpable homicide not amounting to murder",
        "punishment": {
            "Part 1": "Life imprisonment OR imprisonment up to 10 years + Fine (if act done with knowledge likely to cause death)",
            "Part 2": "Imprisonment up to 10 years OR Fine OR both (if act likely to cause death)"
        },
        "key_distinction": "Lacks pre-meditation or specific intent required for murder",
        "examples": [
            "Death caused in sudden fight (IPC 304 Part 1)",
            "Death caused by rash or negligent act (IPC 304A)",
            "Death during consent (IPC 304B - Dowry death)"
        ],
        "related_sections": ["IPC 299 (Definition)", "IPC 304A (Death by negligence)"]
    },
    
    "attempt_to_murder": {
        "section": "IPC Section 307",
        "title": "Attempt to Murder",
        "definition": "Whoever does any act with intention or knowledge and under circumstances that if he caused death would be guilty of murder",
        "punishment": "Imprisonment up to 10 years + Fine. If hurt caused: Imprisonment for life OR imprisonment up to 10 years + Fine (minimum 7 years if hurt)",
        "key_points": [
            "Requires intention or knowledge to kill",
            "Act must be proximate to causing death",
            "Failure to cause death due to circumstances beyond control",
            "More severe if actual hurt caused"
        ],
        "examples": [
            "Firing gunshot at someone (misses or non-fatal injury)",
            "Pushing someone from height (survives)",
            "Poisoning attempt (detected and treated)"
        ]
    },
    
    "murder_definition": {
        "section": "IPC Section 300",
        "title": "Definition of Murder",
        "definition": "Culpable homicide is murder if:",
        "conditions": [
            "Act done with intention of causing death",
            "Act done with intention of causing bodily injury likely to cause death",
            "Act done with knowledge that it is likely to cause death",
            "Intention to cause bodily injury sufficient in ordinary course to cause death"
        ],
        "exceptions": [
            "Grave and sudden provocation",
            "Private defense exceeding lawful limits",
            "Public servant exceeding lawful powers",
            "Sudden fight without pre-meditation",
            "Consent of person killed (above 18 years)"
        ]
    },
    
    "theft": {
        "section": "IPC Section 379",
        "title": "Punishment for Theft",
        "definition": "Whoever commits theft shall be punished with imprisonment of either description for a term which may extend to three years, or with fine, or with both.",
        "punishment": "Imprisonment up to 3 years OR Fine OR Both",
        "key_points": [
            "Bailable offense (can get bail as a matter of right)",
            "Cognizable offense (police can arrest without warrant)",
            "Triable by Magistrate",
            "Compoundable with permission of court"
        ],
        "bail_provisions": {
            "type": "Bailable",
            "explanation": "You have RIGHT to bail for simple theft under IPC 379",
            "conditions": [
                "Police can grant bail at station itself",
                "Court must grant bail if conditions met",
                "Surety bond may be required",
                "May need to surrender passport for valuable thefts"
            ],
            "amount": "Typically ₹5,000 - ₹50,000 depending on value stolen",
            "procedure": "Apply through lawyer or directly to police/court"
        },
        "aggravated_forms": [
            "IPC 380: Theft in dwelling house - Up to 7 years",
            "IPC 381: Theft by clerk/servant - Up to 7 years",
            "IPC 382: Theft after preparation for death/hurt - Up to 10 years"
        ],
        "related_sections": ["IPC 378 (Definition of theft)", "IPC 403 (Dishonest misappropriation)"],
        "conviction_rate": "28.4% (NCRB 2025)"
    },
    
    "robbery": {
        "section": "IPC Section 392",
        "title": "Punishment for Robbery",
        "definition": "Whoever commits robbery shall be punished with rigorous imprisonment for a term which may extend to ten years, and shall also be liable to fine.",
        "punishment": "Rigorous imprisonment up to 10 years + Fine",
        "key_points": [
            "Non-bailable offense (bail at court's discretion)",
            "Cognizable offense",
            "More serious than theft - involves force/threat",
            "If committed during daytime with deadly weapon: up to 14 years (IPC 397)"
        ],
        "bail_provisions": {
            "type": "Non-Bailable",
            "explanation": "Bail NOT automatic - must convince court",
            "conditions": [
                "Show you're not a flight risk",
                "Not likely to tamper with evidence",
                "Not likely to commit similar offense",
                "May require heavy surety"
            ],
            "factors_favoring_bail": [
                "First-time offender",
                "No violence involved",
                "Small value of property",
                "Willing to return stolen property",
                "Strong community ties"
            ]
        }
    },

    "rape": {
        "section": "IPC Section 376",
        "title": "Punishment for Rape",
        "definition": "Whoever commits rape shall be punished with rigorous imprisonment of either description for a term which shall not be less than ten years, but which may extend to imprisonment for life, and shall also be liable to fine.",
        "punishment": "Min 10 years to Life Imprisonment + Fine",
        "key_points": [
            "Non-bailable Offense",
            "Cognizable Offense (police must arrest)",
            "Tried in Sessions Court",
            "Victim identity must be protected (IPC 228A)",
            "Consent is a key defense but limited in scope"
        ],
        "aggravating_factors": [
            "Gang Rape (IPC 376D) - Min 20 years to Life",
            "Rape of minor (POCSO Act applies)",
            "Rape by person in authority (Police/Public Servant)",
            "Rape causing persistent vegetative state"
        ],
        "bail_provisions": {
            "type": "Non-Bailable",
            "explanation": "Very difficult to get bail. Triple test strictly applied.",
            "conditions": [
                "No contact with victim",
                "Prohibition on entering victim's locality",
                "Surrender of passport",
                "Regular police reporting"
            ]
        },
        "related_sections": ["IPC 375 (Definition)", "POCSO Act", "IPC 354 (Outraging Modesty)"],
        "conviction_rate": "27.4% (NCRB 2025)"
    },

    "cruelty_by_husband": {
        "section": "IPC Section 498A",
        "title": "Husband/Relative Subjecting Woman to Cruelty",
        "definition": "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "punishment": "Imprisonment up to 3 years + Fine",
        "key_points": [
            "Types of Cruelty: Physical or Mental",
            "Harassment for dowry included",
            "Cognizable offense if information given to police",
            "Non-bailable (can get bail from Court)"
        ],
        "bail_provisions": {
            "type": "Non-Bailable (but often granted)",
            "explanation": "Arnesh Kumar Guidelines (SC) apply - NO automatic arrest for offenses < 7 years punishment.",
            "conditions": [
                "Police must issue Notice of Appearance (CrPC 41A)",
                "Arrest only if specific reasons recorded",
                "Bail usually granted by Magistrate"
            ]
        },
        "supreme_court_guidelines": {
            "case": "Arnesh Kumar v. State of Bihar (2014)",
            "principle": "No automatic arrest under 498A",
            "test": "Checklist under CrPC 41(1)(b)(ii) must be filled"
        },
        "related_sections": ["Dowry Prohibition Act", "DV Act (Domestic Violence)"],
        "conviction_rate": "14% (High acquittal/settlement rate)"
    },

    "assault": {
        "section": "IPC Section 351/352",
        "title": "Punishment for Assault",
        "definition": "Whoever strikes illegally using force or makes a preparation to use force.",
        "punishment": "Imprisonment up to 3 months OR Fine up to ₹500 OR Both",
        "key_points": [
            "Bailable offense",
            "Non-cognizable (requires complaint to Magistrate)",
            "Compoundable (can settle)"
        ],
        "related_sections": ["IPC 323 (Voluntarily causing hurt)", "IPC 354 (Assault on woman)"]
    },

    
    "fraud": {
        "section": "IPC Section 420",
        "title": "Punishment for Cheating and Fraud",
        "definition": "Whoever cheats and thereby dishonestly induces the person deceived to deliver any property or to make, alter or destroy any valuable security, or anything which is signed or sealed, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.",
        "punishment": "Imprisonment up to 7 years + Fine (mandatory)",
        "key_points": [
            "More serious than simple cheating (IPC 417)",
            "Involves dishonest inducement to deliver property",
            "Cognizable offense (police can arrest without warrant)",
            "Non-bailable offense in many states (check local amendments)",
            "Triable by Magistrate"
        ],
        "elements": [
            "Deception or fraudulent act",
            "Dishonest inducement",
            "Victim delivers property or valuable security",
            "Accused gains wrongfully"
        ],
        "bail_provisions": {
            "type": "Non-Bailable (in most states)",
            "explanation": "IPC 420 is generally non-bailable, though some states have made it bailable for certain amounts",
            "conditions": [
                "Court discretion required for bail",
                "Must show you're not a flight risk",
                "Amount of fraud matters (smaller amounts may get bail easier)",
                "Willingness to return defrauded money helps",
                "Character and antecedents considered"
            ],
            "factors_favoring_bail": [
                "First-time offender",
                "Small amount involved",
                "No prior criminal record",
                "Willing to make restitution",
                "Strong community ties"
            ]
        },
        "examples": [
            "Fake investment schemes (Ponzi schemes)",
            "Credit card fraud",
            "Online scams and phishing",
            "Selling fake products as genuine",
            "Forgery and using forged documents",
            "Insurance fraud",
            "Employment scams"
        ],
        "related_sections": [
            "IPC 415 (Definition of cheating)",
            "IPC 417 (Punishment for cheating - up to 1 year)",
            "IPC 418 (Cheating with knowledge of wrongful loss)",
            "IPC 419 (Punishment for cheating by personation)",
            "IPC 463-471 (Forgery offenses)"
        ],
        "conviction_rate": "34.7% (NCRB 2025)",
        "note": "Compound fraud cases may involve multiple IPC sections and special laws like Prevention of Corruption Act, IT Act Section 66C/66D"
    },
    
    "bail_general": {
        "section": "CrPC Sections 436-439",
        "title": "Bail Provisions in India",
        "types": {
            "regular_bail": "Granted after arrest by police (CrPC 437/439)",
            "anticipatory_bail": "Granted BEFORE arrest (CrPC 438)",
            "interim_bail": "Temporary bail for short period"
        },
        "bailable_vs_nonbailable": {
            "bailable": {
                "definition": "Bail is a RIGHT - must be granted",
                "examples": "Simple theft (379), Simple hurt (323), Defamation (500)",
                "who_grants": "Police or Magistrate",
                "conditions": "Minimal - usually surety bond"
            },
            "non_bailable": {
                "definition": "Bail is at DISCRETION of court",
                "examples": "Murder (302), Rape (376), Robbery (392), Dowry death (304B)",
                "who_grants": "Only Court (not police)",
                "conditions": "Must satisfy triple test (see below)"
            }
        },
        "triple_test_for_bail": {
            "name": "Satender Kumar Antil v. CBI (2022) Supreme Court Guidelines",
            "factors": [
                "1. Severity of punishment if convicted",
                "2. Nature and gravity of accusation",
                "3. Reasonable apprehension of tampering with evidence",
                "4. Threat to witnesses",
                "5. Prima facie satisfaction of court",
                "6. Larger interest of public",
                "7. Character, behavior, means, position of accused",
                "8. Age and health of accused"
            ]
        },
        "bail_amount": {
            "petty_offense": "₹5,000 - ₹20,000",
            "moderate": "₹20,000 - ₹1,00,000",
            "serious": "₹1,00,000 - ₹10,00,000+",
            "note": "Depends on financial capacity of accused"
        }
    },
    
    "theft_bail": {
        "section": "IPC 379 + CrPC 436",
        "title": "Bail for Theft Cases",
        "summary": "GOOD NEWS: Theft is a BAILABLE offense - You have RIGHT to bail!",
        "bail_process": {
            "at_police_station": [
                "Police MUST grant bail for IPC 379",
                "Provide two sureties (people who guarantee you'll appear)",
                "Sign bail bond (promise to appear in court)",
                "Usually released within hours"
            ],
            "if_police_refuse": [
                "Go to nearest Magistrate court",
                "File bail application",
                "Court MUST grant bail (it's your right)",
                "Usually decided same day"
            ]
        },
        "bail_conditions": [
            "Appear in court on all dates",
            "Not leave city/country without permission",
            "Not intimidate witnesses",
            "Surrender passport (if valuable theft)",
            "Report to police station weekly (sometimes)"
        ],
        "bail_amount_typical": "₹10,000 - ₹50,000 (depends on value of theft)",
        "time_to_get_bail": "Same day to 3 days maximum",
        "what_if_bail_denied": "File revision petition in Sessions Court - but denial is rare for theft"
    },
    
    "kidnapping": {
        "section": "IPC Section 363",
        "title": "Punishment for Kidnapping",
        "definition": "Kidnapping any person from India or from lawful guardianship.",
        "punishment": "Imprisonment up to 7 years + Fine",
        "key_points": [
            "Section 363: Kidnapping from lawful guardianship",
            "Section 364: Kidnapping for ransom - Up to life imprisonment",
            "Section 366: Kidnapping woman to compel marriage - Up to 10 years",
            "Kidnapping minor (below 18) is more serious",
            "Cognizable and non-bailable offense"
        ],
        "bail_info": {
            "bailable": False,
            "bail_type": "Non-bailable - Court discretion required",
            "typical_grounds": "Long detention, weak evidence, minor involvement"
        },
        "related_sections": ["IPC 364 (For murder/ransom)", "IPC 366 (For marriage)", "IPC 367 (For grievous hurt)"]
    },
    
    "assault": {
        "section": "IPC Section 323",
        "title": "Punishment for Assault/Voluntarily Causing Hurt",
        "definition": "Whoever voluntarily causes hurt to any person shall be punished.",
        "punishment": "Imprisonment up to 1 year OR Fine up to ₹1,000 OR Both",
        "key_points": [
            "Section 323: Simple hurt - Up to 1 year",
            "Section 324: Hurt by dangerous weapon - Up to 3 years",
            "Section 325: Grievous hurt - Up to 7 years",
            "Section 326: Grievous hurt by dangerous weapon - Up to life imprisonment",
            "Simple assault under 323 is bailable"
        ],
        "bail_info": {
            "bailable": True,
            "bail_type": "Bailable - Right to bail for Section 323",
            "note": "Grievous hurt sections are non-bailable"
        },
        "related_sections": ["IPC 324", "IPC 325", "IPC 326", "IPC 351 (Assault definition)"]
    },
    
    "molestation": {
        "section": "IPC Section 354",
        "title": "Assault or Criminal Force to Woman with Intent to Outrage Her Modesty",
        "definition": "Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty.",
        "punishment": "Imprisonment from 1 to 5 years + Fine",
        "key_points": [
            "Non-bailable offense",
            "Cognizable offense (police can arrest without warrant)",
            "Triable by Magistrate First Class",
            "Specific to offenses against women",
            "Related sections cover stalking (354D), voyeurism (354C), disrobing (354B)"
        ],
        "bail_info": {
            "bailable": False,
            "bail_type": "Non-bailable - Court discretion",
            "note": "Must apply to court for bail"
        },
        "related_sections": ["IPC 354A (Sexual harassment)", "IPC 354B (Disrobing)", "IPC 354C (Voyeurism)", "IPC 354D (Stalking)"]
    },
    
    "defamation": {
        "section": "IPC Section 499-500",
        "title": "Punishment for Defamation",
        "definition": "Making or publishing any imputation concerning any person, intending to harm the reputation of such person.",
        "punishment": "Imprisonment up to 2 years OR Fine OR Both",
        "key_points": [
            "Section 499: Definition of defamation",
            "Section 500: Punishment for defamation",
            "Both written (libel) and spoken (slander) covered",
            "Truth is a defense if in public interest",
            "Bailable and compoundable offense"
        ],
        "bail_info": {
            "bailable": True,
            "bail_type": "Bailable - Right to bail",
            "note": "Can be settled/compounded with complainant's consent"
        },
        "exceptions": [
            "Truth for public good",
            "Opinion on public conduct of public servants",
            "Court proceedings reporting",
            "Merits of public performance",
            "Censure by person in authority"
        ]
    },
    
    "general_info": {
        "constitutional_protection": {
            "article_21": "Right to Life and Personal Liberty - No person shall be deprived of life except according to procedure established by law",
            "article_20": "Protection against ex-post-facto laws and double jeopardy"
        },
        "criminal_procedure": {
            "cognizable": "Police can arrest without warrant",
            "non_bailable": "Court discretion required for bail",
            "triable_by": "Court of Session (murder, IPC 302)"
        },
        "investigation": {
            "fir": "First Information Report must be filed",
            "investigation": "Police investigation under CrPC",
            "chargesheet": "Filed within 60-90 days",
            "trial": "Can take 2-5 years on average"
        }
    },

    "legal_concepts": {
        "law_vs_act": {
            "title": "Difference Between Law and Act",
            "definition": "While often used interchangeably, 'Act' and 'Law' have distinct legal meanings in the Indian legal system.",
            "key_differences": [
                "An ACT is a specific statute passed by Parliament or State Legislature (e.g., Indian Penal Code Act 1860, Companies Act 2013)",
                "LAW is a broader term encompassing Acts, Rules, Regulations, Ordinances, Judicial Precedents, and Constitutional provisions",
                "An Act becomes law after receiving Presidential/Governor's assent",
                "Rules and Regulations are made UNDER an Act to implement its provisions",
                "All Acts are laws, but not all laws are Acts"
            ],
            "examples": {
                "Acts": "Indian Penal Code 1860, Code of Criminal Procedure 1973, Companies Act 2013, Right to Information Act 2005",
                "Laws_not_Acts": "Constitutional provisions, Judicial precedents, Customary laws, Ordinances (temporary), Delegated legislation (Rules/Regulations)"
            },
            "hierarchy": [
                "1. Constitution of India (Supreme Law)",
                "2. Central Acts passed by Parliament",
                "3. State Acts passed by State Legislatures",
                "4. Ordinances (temporary, issued by President/Governor)",
                "5. Rules & Regulations (made under Acts)",
                "6. Judicial Precedents (interpretations by courts)"
            ],
            "key_points": [
                "An Act is a Bill that has been passed by both Houses of Parliament and received Presidential assent",
                "Law includes written law (statutes) and unwritten law (customs, precedents)",
                "Rules are subordinate legislation made by Executive under authority of an Act",
                "The term 'Code' refers to a comprehensive Act covering an entire subject (e.g., IPC, CrPC)"
            ]
        },
        "contract": {
            "title": "Indian Contract Act, 1872",
            "definition": "A contract is an agreement enforceable by law (Section 2h).",
            "key_elements": [
                "Offer and Acceptance",
                "Lawful Consideration",
                "Capacity to Contract (Age, Mind)",
                "Free Consent (No coercion/fraud)",
                "Lawful Object"
            ],
            "rights": [
                "Right to enforce contract",
                "Right to claim damages for breach",
                "Right to specific performance",
                "Right to injunction"
            ],
            "procedure_overview": [
                "1. Identify breach of contract",
                "2. Send legal notice to breaching party",
                "3. File civil suit in appropriate court",
                "4. Claim damages, specific performance, or injunction"
            ],
            "landmark_case": "Mohori Bibee v. Dharmodas Ghose (1903) - Contract with minor is void ab initio"
        },
        "constitution": {
            "title": "Constitution of India",
            "definition": "The supreme law of India, adopted on 26 Nov 1949 and enacted on 26 Jan 1950.",
            "key_elements": [
                "Longest written constitution in the world",
                "Sovereign, Socialist, Secular, Democratic Republic",
                "Fundamental Rights (Part III) - Justiciable, enforceable through courts",
                "Directive Principles (Part IV) - Non-justiciable, guiding principles for governance",
                "Fundamental Duties (Part IVA) - 11 duties of citizens",
                "22 Parts, 12 Schedules, 395 Articles (originally)"
            ],
            "rights": [
                "Right to Equality (Articles 14-18)",
                "Right to Freedom (Articles 19-22)",
                "Right against Exploitation (Articles 23-24)",
                "Right to Freedom of Religion (Articles 25-28)",
                "Cultural and Educational Rights (Articles 29-30)",
                "Right to Constitutional Remedies (Article 32)"
            ],
            "landmark_case": "Kesavananda Bharati v. State of Kerala (1973) - Basic Structure Doctrine"
        },
        "article_19": {
            "title": "Article 19: Right to Freedom",
            "definition": "Protection of certain rights regarding freedom of speech, etc.",
            "rights": [
                "19(1)(a): Speech and Expression",
                "19(1)(b): Assembly peaceably without arms",
                "19(1)(c): Form associations/unions",
                "19(1)(d): Move freely throughout India",
                "19(1)(e): Reside/settle in any part of India",
                "19(1)(g): Practice any profession/trade"
            ],
            "restrictions": "Detailed in Article 19(2) to 19(6) (e.g., sovereignty, public order, decency)"
        },
        "article_14": {
            "title": "Article 14: Equality Before Law",
            "definition": "The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.",
            "key_elements": [
                "Equality before Law (Negative Concept - No special privilege)",
                "Equal Protection of Laws (Positive Concept - Like treated alike)"
            ],
            "landmark_case": "E.P. Royappa v. State of Tamil Nadu (1974) - Arbitrariness is antithetical to equality."
        },
        "article_20": {
            "title": "Article 20: Protection in Respect of Conviction for Offences",
            "definition": "Provides three key protections to accused persons.",
            "rights": [
                "1. No Ex-post-facto Law (20(1)): Cannot be punished for act that was not offence when committed.",
                "2. No Double Jeopardy (20(2)): Cannot be prosecuted/punished twice for same offence.",
                "3. No Self-Incrimination (20(3)): Cannot be compelled to be witness against oneself."
            ]
        },
        "article_21": {
            "title": "Article 21: Protection of Life and Personal Liberty",
            "definition": "No person shall be deprived of his life or personal liberty except according to procedure established by law.",
            "scope": "Expanded by Supreme Court to include Right to Privacy, Dignity, Health, Education, etc.",
            "landmark_case": "Maneka Gandhi v. Union of India (1978) - Procedure must be 'just, fair and reasonable'"
        },
        "article_22": {
            "title": "Article 22: Protection Against Arrest and Detention",
            "definition": "Safeguards for persons who are arrested.",
            "rights": [
                "Right to be informed of grounds of arrest",
                "Right to consult legal practitioner",
                "Right to be produced before Magistrate within 24 hours"
            ],
            "exceptions": "Preventive Detention laws (e.g., NSA, UAPA)"
        },
        "article_23": {
            "title": "Right Against Exploitation (Articles 23 & 24)",
            "definition": "Prohibition of traffic in human beings and forced labour.",
            "rights": [
                "Article 23: Prohibition of traffic in human beings and forced labour.",
                "Article 24: Prohibition of employment of children in factories, etc."
            ],
            "key_elements": [
                "Begar (Forced labour without payment) is prohibited.",
                "Trafficking for immoral purposes is punishable."
            ],
            "statutes": ["Bonded Labour System (Abolition) Act, 1976", "Child Labour (Prohibition and Regulation) Act, 1986"]
        },
        "article_32": {
            "title": "Article 32: Right to Constitutional Remedies",
            "definition": "The 'Heart and Soul' of the Constitution (Dr. Ambedkar). Right to move Supreme Court for enforcement of Fundamental Rights.",
            "key_elements": [
                "Supreme Court can issue 5 types of writs for fundamental rights",
                "HABEAS CORPUS - Release from illegal detention",
                "MANDAMUS - Command to perform public duty",
                "PROHIBITION - Stop lower court proceedings",
                "CERTIORARI - Quash lower court order",
                "QUO WARRANTO - Challenge illegal public office occupation",
                "Article 32 is itself a fundamental right"
            ],
            "writs": [
                "Habeas Corpus (To have the body)",
                "Mandamus (We Command)",
                "Prohibition (To forbid)",
                "Certiorari (To be certified)",
                "Quo Warranto (By what authority)"
            ]
        },
        "case_kesavananda": {
            "title": "Kesavananda Bharati v. State of Kerala (1973)",
            "definition": "The most important case in Indian Constitutional History.",
            "key_elements": [
                "Established 'Basic Structure Doctrine'",
                "Parliament cannot alter basic features (Democracy, Secularism, etc.)",
                "Overruled Golaknath case judgment"
            ],
            "impact": "Saved Indian democracy from authoritarian amendments."
        },
        "fir": {
            "title": "First Information Report (FIR)",
            "definition": "Written document prepared by police when they receive information about commission of a cognizable offence.",
            "statutes": ["Section 154 of CrPC (Now BNSS Section 173)"],
            "procedure_overview": [
                "1. Go to police station having jurisdiction",
                "2. Narrate incident to Officer-in-Charge",
                "3. Verify written report and sign it",
                "4. Get free copy of FIR"
            ],
            "rights": [
                "Zero FIR: Can be filed in ANY police station",
                "e-FIR: Available in some states for theft/lost items"
            ]
        },
        "bail_procedure": {
            "title": "Bail Procedures",
            "definition": "Bail is the judicial release of an accused person from custody.",
            "statutes": ["Section 436 (Bailable)", "Section 437 (Non-bailable)", "Section 438 (Anticipatory)"],
            "procedure_overview": [
                "1. For Bailable Offence: Apply to Police/Court. Right to be released on furnishing surety.",
                "2. For Non-Bailable Offence: Apply to Magistrate/Session Court. Discretionary.",
                "3. Anticipatory Bail: Apply to Sessions Court/High Court BEFORE arrest."
            ],
            "documents_required": ["Bail Application", "Vakalatnama", "Surety Details (Aadhaar/Property papers)"]
        },
        "divorce": {
            "title": "Divorce Proceedings in India",
            "definition": "The legal dissolution of marriage governed by personal laws based on religion (e.g., Hindu Marriage Act 1955, Special Marriage Act 1954, Muslim Personal Law).",
            "statutes": ["Section 13, 13B of Hindu Marriage Act, 1955", "Section 27 of Special Marriage Act, 1954", "Divorce Act, 1869 (Christians)"],
            "types_of_divorce": {
                 "mutual_consent": "Both parties agree to separate. Fastest method (6-18 months).",
                 "contested": "Filed on specific grounds like cruelty, adultery, etc. Can take 3-5+ years."
            },
            "grounds": [
                "Cruelty (Mental or Physical)",
                "Adultery (Voluntary sexual intercourse with another person)",
                "Desertion (Continuous period of not less than 2 years)",
                "Conversion to another religion",
                "Unsoundness of mind / Mental Disorder",
                "Presumption of Death (Missing for 7+ years)"
            ],
            "documents_required": [
                "Marriage Certificate",
                "Address Proof of both parties",
                "Passport size photographs",
                "Evidence proving grounds (for contested divorce)",
                "Income tax returns (for alimony calculations)"
            ],
            "procedure_overview": [
                "1. Filing of Petition (Family Court)",
                "2. Service of Summons to other party",
                "3. Response/Counter-filing",
                "4. Trial & Evidence",
                "5. Arguments & Judgment",
                "6. Appeal (if any) to High Court"
            ],
            "expert_note": "In mutual consent divorce, a 'Cooling-off Period' of 6 months is mandatory but can be waived by the Supreme Court in exceptional cases (Amardeep Singh v. Harveen Kaur). Maintenance/Alimony is decided based on the husband's income and wife's financial status."
        },
        "property": {
            "title": "Property Disputes",
            "definition": "Disputes regarding ownership, possession, and transfer of property.",
            "key_laws": ["Transfer of Property Act, 1882", "Succession Acts", "RERA"],
            "types": ["Ancestral Property", "Self-Acquired Property", "Tenancy Disputes"],
            "key_elements": [
                "Title Deed verification is essential",
                "Encumbrance Certificate shows property is free from loans",
                "Mutation of property in revenue records"
            ]
        },
        "rti": {
            "title": "Right to Information Act, 2005",
            "definition": "Citizens' right to request information from public authorities, promoting transparency and accountability in government.",
            "statutes": ["Right to Information Act, 2005"],
            "procedure_overview": [
                "1. File RTI application with prescribed fee (₹10)",
                "2. First Appeal: If unsatisfied, appeal to First Appellate Authority within 30 days",
                "3. Second Appeal: Appeal to Central/State Information Commission within 90 days"
            ],
            "key_elements": [
                "Response must be provided within 30 days (48 hours for life/liberty matters)",
                "₹250 penalty per day for delay (max ₹25,000)",
                "Exemptions under Section 8 (national security, privacy, etc.)"
            ],
            "landmark_case": "CPIO Supreme Court v. Subhash Chandra Agarwal (2020) - CJI's office under RTI"
        },
        "consumer_protection": {
            "title": "Consumer Protection Act, 2019",
            "definition": "Law protecting consumers from unfair trade practices, defective goods, and deficient services.",
            "statutes": ["Consumer Protection Act, 2019", "Consumer Protection Rules, 2020"],
            "rights": [
                "Right to Safety",
                "Right to Information",
                "Right to Choice",
                "Right to be Heard",
                "Right to Redressal",
                "Right to Consumer Education"
            ],
            "procedure_overview": [
                "1. File complaint in Consumer Forum (District/State/National based on value)",
                "2. District: Up to ₹1 crore",
                "3. State Commission: ₹1 crore to ₹10 crore",
                "4. National Commission: Above ₹10 crore"
            ],
            "key_elements": [
                "E-filing available at edaakhil.nic.in",
                "No court fee required",
                "Complaint within 2 years of cause of action"
            ]
        },
        "cyber_crime": {
            "title": "Cyber Crimes under IT Act, 2000",
            "definition": "Criminal activities using computers, networks, or the internet.",
            "statutes": ["Information Technology Act, 2000 (Amended 2008)", "IPC Sections as applicable"],
            "key_elements": [
                "Section 66: Hacking - Up to 3 years + ₹5 lakh fine",
                "Section 66C: Identity theft - Up to 3 years + ₹1 lakh fine",
                "Section 66D: Cheating by personation - Up to 3 years + ₹1 lakh fine",
                "Section 67: Obscene content - Up to 5 years + ₹10 lakh fine",
                "Section 67A: Sexually explicit content - Up to 7 years",
                "Section 67B: Child pornography - Up to 7 years (first) / 10 years (repeat)"
            ],
            "procedure_overview": [
                "1. Report at cybercrime.gov.in (National Cyber Crime Portal)",
                "2. File FIR at nearest police station or Cyber Cell",
                "3. Preserve digital evidence (screenshots, emails, logs)"
            ],
            "expert_note": "Online fraud complaints can be filed within 'Golden Hour' (few hours of transaction) to freeze fraudulent accounts."
        },
        "dowry": {
            "title": "Dowry Prohibition Act, 1961",
            "definition": "Law prohibiting the giving, taking, or demanding of dowry in connection with marriage.",
            "statutes": ["Dowry Prohibition Act, 1961", "IPC Section 304B (Dowry Death)", "IPC Section 498A (Cruelty)"],
            "key_elements": [
                "Giving or taking dowry: Up to 5 years + ₹15,000 fine OR value of dowry",
                "Demanding dowry: 6 months to 2 years + ₹10,000 fine",
                "Dowry death (304B): 7 years to Life imprisonment",
                "Cruelty by husband or relatives (498A): Up to 3 years + fine"
            ],
            "landmark_case": "Satya v. Teja Singh (2009) - Wide interpretation of 'dowry' to include post-marriage demands"
        },
        "dowry_death": {
            "title": "Dowry Death (IPC Section 304B)",
            "definition": "Dowry death is when a woman dies within seven years of marriage under abnormal circumstances, and it is shown that she was subjected to cruelty or harassment for dowry.",
            "section": "IPC Section 304B",
            "key_elements": [
                "Section 304B: Dowry death provision under IPC",
                "Death within 7 years of marriage",
                "Death is caused by burns, bodily injury or abnormal circumstances",
                "Woman subjected to cruelty or harassment for dowry",
                "Section 498A: Cruelty by husband or relatives is linked offense",
                "Presumption under Section 113B Evidence Act: Court presumes husband/relatives caused death"
            ],
            "punishment": [
                "Minimum: 7 years imprisonment",
                "Maximum: Life imprisonment",
                "Offense is NON-BAILABLE, COGNIZABLE, NON-COMPOUNDABLE"
            ],
            "related_sections": [
                "Section 498A IPC: Cruelty by husband or relatives (up to 3 years)",
                "Section 113B Evidence Act: Presumption as to dowry death",
                "Section 304B IPC: Dowry death (7 years to life)",
                "Dowry Prohibition Act, 1961: Anti-dowry law"
            ],
            "cruelty_498A": "Section 498A punishes cruelty by husband or his relatives. Cruelty includes mental and physical harassment for dowry. Maximum punishment is 3 years imprisonment and fine.",
            "landmark_case": "Shanti v. State of Haryana (1991) - Supreme Court on dowry death presumption"
        },
        "pocso": {
            "title": "Protection of Children from Sexual Offences (POCSO) Act, 2012",
            "definition": "Special law to protect children below 18 years from sexual abuse and exploitation.",
            "statutes": ["POCSO Act, 2012 (Amended 2019)"],
            "key_elements": [
                "Penetrative sexual assault: Min 10 years to Life (20 years to death for below 12)",
                "Aggravated penetrative sexual assault: Min 20 years to Life/Death",
                "Sexual assault: 3 to 5 years + fine",
                "Mandatory reporting by everyone who has knowledge",
                "Child-friendly courts and procedures"
            ],
            "procedure_overview": [
                "1. Report to police/Special Juvenile Police Unit",
                "2. Medical examination within 24 hours",
                "3. Trial in Special Court within 1 year",
                "4. In-camera trial mandatory"
            ]
        },
        "writ": {
            "title": "Constitutional Writs",
            "definition": "Orders issued by High Courts (Article 226) or Supreme Court (Article 32) to enforce fundamental rights.",
            "writs": [
                "Habeas Corpus: 'To have the body' - Against unlawful detention",
                "Mandamus: 'We command' - To compel public official to perform duty",
                "Prohibition: To forbid lower court from exceeding jurisdiction",
                "Certiorari: To quash order of lower court",
                "Quo Warranto: 'By what authority' - Challenge to holding public office"
            ],
            "key_elements": [
                "Habeas Corpus is most valued (can't be suspended even in Emergency)",
                "Mandamus lies against public officials, not private persons",
                "Certiorari and Prohibition are judicial remedies"
            ],
            "landmark_case": "ADM Jabalpur v. Shivkant Shukla (1976) - Overruled; Habeas Corpus cannot be suspended"
        },
        "sedition": {
            "title": "Sedition - IPC Section 124A",
            "definition": "Bringing or attempting to bring hatred, contempt, or disaffection towards the Government.",
            "statutes": ["IPC Section 124A (Under review by Supreme Court)"],
            "key_elements": [
                "Punishment: Life imprisonment + Fine OR 3 years + Fine",
                "Non-bailable, Non-compoundable, Cognizable",
                "Supreme Court stayed sedition cases in 2022 (S.G. Vombatkere case)"
            ],
            "landmark_case": "Kedar Nath Singh v. State of Bihar (1962) - Sedition valid but only for incitement to violence"
        },
        "arbitration": {
            "title": "Arbitration and Conciliation Act, 1996",
            "definition": "Alternative dispute resolution mechanism for civil and commercial disputes outside courts.",
            "statutes": ["Arbitration and Conciliation Act, 1996 (Amended 2015, 2019, 2021)"],
            "key_elements": [
                "Arbitration award is final and binding",
                "Limited grounds for challenge under Section 34",
                "Time limit: Award within 12 months (extendable by 6 months)",
                "Emergency arbitration now recognized"
            ],
            "procedure_overview": [
                "1. Arbitration clause in contract or separate agreement",
                "2. Appointment of arbitrator(s)",
                "3. Hearing and Evidence",
                "4. Award and Enforcement"
            ]
        },
        "lok_adalat": {
            "title": "Lok Adalat (People's Court)",
            "definition": "Alternative dispute resolution forum for settling disputes amicably without court proceedings.",
            "statutes": ["Legal Services Authorities Act, 1987"],
            "key_elements": [
                "No court fee",
                "Decision (award) is final - No appeal",
                "Matters: Motor accident claims, matrimonial, labour, public utility services",
                "Permanent Lok Adalat for public utility services"
            ],
            "procedure_overview": [
                "1. Case pending in court or pre-litigation",
                "2. Referred to Lok Adalat with consent",
                "3. Compromise/Settlement reached",
                "4. Award passed by Presiding Officer"
            ]
        },
        "legal_aid": {
            "title": "Legal Services Authorities Act, 1987",
            "definition": "Law providing free legal services to weaker sections of society.",
            "statutes": ["Legal Services Authorities Act, 1987"],
            "key_elements": [
                "Free legal aid to SC/ST, women, children, disabled, victims",
                "NALSA (National), SLSA (State), DLSA (District) structure",
                "Lok Adalats for speedy settlement",
                "Legal awareness camps"
            ],
            "rights": [
                "Right to free legal aid under Article 39A",
                "Right to representation in court",
                "Right to legal advice",
                "Right to access Lok Adalat"
            ],
            "procedure_overview": [
                "1. Apply to DLSA/SLSA with proof of eligibility",
                "2. Committee examines application",
                "3. Legal aid counsel assigned",
                "4. Free representation in court"
            ],
            "expert_note": "Income limit for legal aid varies by state. Generally covers those earning below ₹3 lakh/year."
        },
        "pil": {
            "title": "Public Interest Litigation (PIL)",
            "definition": "Litigation filed in court of law for protection of public interest, not personal grievance.",
            "key_elements": [
                "Any citizen can file for public cause",
                "Filed in High Court or Supreme Court",
                "No court fee",
                "Relaxed locus standi rules"
            ],
            "landmark_case": "S.P. Gupta v. Union of India (1981) - Established PIL in India",
            "procedure_overview": [
                "1. Letter to Chief Justice or formal petition",
                "2. Court examines if genuine public interest",
                "3. Notice to respondents",
                "4. Hearing and directions/orders"
            ]
        },
        "defamation": {
            "title": "Defamation - IPC Sections 499-502",
            "definition": "Making or publishing false statements that damage a person's reputation.",
            "statutes": ["IPC Sections 499-502 (Criminal)", "Tort Law (Civil)"],
            "key_elements": [
                "Criminal Defamation (IPC 500): Up to 2 years + Fine",
                "Civil Defamation: Damages/Compensation",
                "Truth is an absolute defense",
                "10 exceptions under IPC 499 (fair comment, good faith, etc.)"
            ],
            "landmark_case": "Subramanian Swamy v. Union of India (2016) - Criminal defamation constitutional"
        },
        "contempt": {
            "title": "Contempt of Court",
            "definition": "Willful disobedience or disrespect towards court orders or authority.",
            "statutes": ["Contempt of Courts Act, 1971", "Article 129, 215 of Constitution"],
            "key_elements": [
                "Civil Contempt: Disobedience of court orders",
                "Criminal Contempt: Scandalizing court, interference with justice",
                "Punishment: Up to 6 months imprisonment + ₹2,000 fine",
                "Truth is a valid defense (2006 Amendment)"
            ],
            "landmark_case": "In Re: Prashant Bhushan (2020) - Tweets constituting contempt"
        },
        "maintenance": {
            "title": "Maintenance Rights",
            "definition": "Legal right to receive financial support from spouse, parents, or children.",
            "statutes": ["CrPC Section 125", "Hindu Adoption & Maintenance Act", "Muslim Women (Protection of Rights on Divorce) Act"],
            "key_elements": [
                "Wife, children, and parents entitled to maintenance",
                "Proceedings under CrPC 125 are civil in nature",
                "Quick remedy - summary proceedings",
                "Amount based on status, income, and needs"
            ],
            "landmark_case": "Rajnesh v. Neha (2020) - Guidelines on overlapping maintenance proceedings"
        },
        "article_44": {
            "title": "Article 44: Uniform Civil Code",
            "definition": "Directive Principle stating: 'The State shall endeavour to secure for citizens a uniform civil code throughout India.'",
            "key_elements": [
                "Currently NOT enforceable - Directive Principle",
                "Personal laws based on religion still prevail",
                "Goa is the only state with UCC",
                "Debate continues on implementation"
            ],
            "landmark_case": "Shah Bano case (1985) - Supreme Court recommended UCC"
        },
        "case_shah_bano": {
            "title": "Mohd. Ahmed Khan v. Shah Bano Begum (1985)",
            "definition": "Landmark case on maintenance rights of Muslim divorced women under CrPC Section 125.",
            "key_elements": [
                "Supreme Court awarded maintenance to Shah Bano under CrPC 125",
                "Sparked UCC debate",
                "Led to Muslim Women (Protection of Rights on Divorce) Act, 1986",
                "Later modified by Danial Latifi case (2001) - more protective interpretation"
            ],
            "impact": "Major constitutional and political landmark on personal laws"
        },
        "case_maneka_gandhi": {
            "title": "Maneka Gandhi v. Union of India (1978)",
            "definition": "Landmark case that expanded the scope of Article 21 (Right to Life and Personal Liberty).",
            "key_elements": [
                "Procedure established by law must be 'just, fair and reasonable'",
                "Articles 14, 19, 21 are interconnected",
                "Right to go abroad included in personal liberty",
                "Overruled A.K. Gopalan's narrow interpretation"
            ],
            "landmark_case": "Maneka Gandhi v. Union of India (1978)",
            "impact": "Transformed Article 21 into the most expansive fundamental right"
        },
        "case_bachan_singh": {
            "title": "Bachan Singh v. State of Punjab (1980)",
            "definition": "Death penalty upheld as constitutional but restricted to 'rarest of rare' cases.",
            "key_elements": [
                "Death penalty is constitutional under Article 21",
                "Must be imposed only in 'rarest of rare' cases",
                "Aggravating and mitigating circumstances must be balanced",
                "Followed by Machhi Singh guidelines (1983)"
            ],
            "impact": "Established judicial standards for imposing death penalty in India"
        },
        "case_adm_jabalpur": {
            "title": "ADM Jabalpur v. Shivkant Shukla (1976)",
            "definition": "Controversial Emergency-era case where Supreme Court held that Habeas Corpus could be suspended during Emergency.",
            "key_elements": [
                "During 1975 Emergency, fundamental rights suspended",
                "4-1 majority held citizens cannot approach courts during Emergency",
                "Justice H.R. Khanna's famous dissent upheld rule of law",
                "Overruled by 9-judge bench in K.S. Puttaswamy case (2017)"
            ],
            "landmark_case": "ADM Jabalpur v. Shivkant Shukla (1976) - Now overruled",
            "impact": "Considered darkest hour of Supreme Court; later acknowledged as wrong"
        },
        "case_arnesh_kumar": {
            "title": "Arnesh Kumar v. State of Bihar (2014)",
            "definition": "Supreme Court guidelines to prevent unnecessary arrests in IPC Section 498A cases.",
            "key_elements": [
                "No automatic arrest for offences punishable with < 7 years",
                "Police must issue Notice of Appearance under CrPC 41A first",
                "Arrest only after recording reasons as per CrPC 41(1)(b)(ii)",
                "Magistrate must verify compliance before remand"
            ],
            "impact": "Reduced misuse of Section 498A; landmark for protecting personal liberty"
        },
        "case_vishaka": {
            "title": "Vishaka v. State of Rajasthan (1997)",
            "definition": "Supreme Court laid down guidelines for prevention of sexual harassment at workplace.",
            "key_elements": [
                "Defined 'sexual harassment' at workplace",
                "Mandatory complaints committee in organizations",
                "Guidelines were law until POSH Act, 2013",
                "Based on CEDAW provisions"
            ],
            "impact": "Foundation for Sexual Harassment of Women at Workplace Act, 2013"
        },
        "case_triple_talaq": {
            "title": "Shayara Bano v. Union of India (2017)",
            "definition": "Supreme Court declared instant triple talaq (talaq-e-biddat) unconstitutional.",
            "key_elements": [
                "3-2 majority struck down instant triple talaq",
                "Violates Articles 14, 15, 21, 25",
                "Led to Muslim Women (Protection of Rights on Marriage) Act, 2019",
                "Triple talaq now punishable with 3 years imprisonment"
            ],
            "impact": "Major reform in Muslim personal law in India"
        },
        "case_privacy": {
            "title": "K.S. Puttaswamy v. Union of India (2017)",
            "definition": "9-judge bench unanimously held Right to Privacy is a fundamental right under Article 21.",
            "key_elements": [
                "Privacy is intrinsic to life and liberty under Article 21",
                "Overruled M.P. Sharma (1954) and Kharak Singh (1962)",
                "Covers informational privacy, bodily autonomy, decisional privacy",
                "Foundation for challenges to Aadhaar, data protection laws"
            ],
            "landmark_case": "K.S. Puttaswamy v. Union of India (2017)",
            "impact": "One of the most significant constitutional judgments of 21st century"
        },
        "case_sabarimala": {
            "title": "Indian Young Lawyers Association v. State of Kerala (2018)",
            "definition": "Sabarimala Temple case - Supreme Court allowed entry of women of menstruating age (10-50) into temple.",
            "key_elements": [
                "4-1 majority held exclusion violates Articles 14, 15, 25",
                "Religious practice cannot override constitutional morality",
                "Justice Indu Malhotra's dissent on faith vs law",
                "Review petitions pending before larger bench"
            ],
            "impact": "Major judgment on intersection of religion and constitutional rights"
        },
        "arrested_rights": {
            "title": "Rights of Arrested Person (Article 22 + D.K. Basu Guidelines)",
            "definition": "Under Article 22 of the Constitution and D.K. Basu guidelines, arrested persons have fundamental rights including right to lawyer, right to inform family, and right to be produced before Magistrate within 24 hours.",
            "section": "Article 22 Constitution, CrPC Section 50",
            "key_elements": [
                "RIGHT TO LAWYER: Can consult and be defended by lawyer of choice (Article 22(1))",
                "RIGHT TO FAMILY: Inform family/friend of arrest immediately",
                "24 HOURS MAGISTRATE: Must be produced before Magistrate within 24 hours (Article 22(2))",
                "Right to know grounds of arrest at time of arrest",
                "Right to BAIL in bailable offences",
                "Right to medical examination",
                "Right against self-incrimination (Article 20(3))"
            ],
            "what_to_do_if_arrested": [
                "Step 1: Remain calm, do NOT resist arrest",
                "Step 2: Ask for grounds of arrest in writing",
                "Step 3: Immediately inform family member/friend",
                "Step 4: Demand to meet your lawyer",
                "Step 5: Note names and badge numbers of arresting officers",
                "Step 6: If bailable offence, demand bail at police station",
                "Step 7: If tortured, inform Magistrate when produced in court"
            ],
            "dk_basu_guidelines": [
                "1. Arresting officer must wear visible identification",
                "2. Arrest memo with time, date, witness signature",
                "3. One witness from family/locality must attest",
                "4. Arrested person may inform friend/relative",
                "5. Entry in diary at place of detention",
                "6. Medical examination every 48 hours",
                "7. Copies of documents to family",
                "8. Information to Legal Aid Board"
            ],
            "landmark_case": "D.K. Basu v. State of West Bengal (1997) - 11 guidelines for arrest"
        },
        "cognizable_offence": {
            "title": "Cognizable and Non-Cognizable Offences",
            "definition": "Classification of offences based on police power to arrest without warrant.",
            "key_elements": [
                "Cognizable: Police can arrest without warrant, investigate without court permission",
                "Non-Cognizable: Police cannot arrest without warrant, need court permission to investigate",
                "First Schedule of CrPC lists all offences with classification",
                "Examples Cognizable: Murder, Rape, Robbery, Theft",
                "Examples Non-Cognizable: Assault, Defamation, Cheating below threshold"
            ],
            "procedure_overview": [
                "Cognizable: FIR registered, immediate investigation",
                "Non-Cognizable: NC Report, complaint to Magistrate required"
            ]
        },
        "chargesheet": {
            "title": "Chargesheet and Investigation",
            "definition": "Chargesheet (Police Report) is the final report filed by police after investigation under CrPC Section 173.",
            "key_elements": [
                "Must be filed within 60 days (90 days for serious offences)",
                "Contains evidence, witness statements, accused details",
                "If not filed in time, accused has right to statutory bail",
                "Magistrate takes cognizance and proceeds to trial"
            ],
            "procedure_overview": [
                "1. FIR registered",
                "2. Investigation by police",
                "3. Evidence and witness collection",
                "4. Chargesheet filed in court",
                "5. Trial begins"
            ]
        },
        "custody_duration": {
            "title": "Police Custody Duration",
            "definition": "Legal limits on how long police can keep a person in custody.",
            "key_elements": [
                "Must be produced before Magistrate within 24 hours (Article 22)",
                "Police custody (interrogation): Maximum 15 days total",
                "Judicial custody: Up to 60/90 days (based on offence severity)",
                "After max period without chargesheet: Statutory bail (default bail)"
            ],
            "procedure_overview": [
                "1. Arrest → 24 hours → Magistrate",
                "2. Remand to police custody (max 15 days total)",
                "3. Judicial custody in jail",
                "4. Chargesheet or release on statutory bail"
            ]
        },
        "bail_types": {
            "title": "Types of Bail in India",
            "definition": "Bail is release from custody on certain conditions pending trial.",
            "key_elements": [
                "Regular Bail (CrPC 437/439): After arrest",
                "Anticipatory Bail (CrPC 438): Before arrest",
                "Interim Bail: Temporary, pending full hearing",
                "Default/Statutory Bail (CrPC 167): If chargesheet not filed in time"
            ],
            "procedure_overview": [
                "1. File bail application with relevant court",
                "2. Court examines grounds (severity, flight risk, etc.)",
                "3. If granted, execute bail bond with sureties",
                "4. Comply with conditions (appearance, etc.)"
            ]
        },
        "theft_vs_robbery": {
            "title": "Difference Between Theft and Robbery",
            "definition": "Theft and Robbery are distinct offences under IPC with key differences in elements and punishment.",
            "key_elements": [
                "THEFT (IPC 379): Taking property without consent, NO force/threat used",
                "ROBBERY (IPC 392): Theft + Force/Fear/Threat used OR extortion with instant death fear",
                "Theft = Secret taking; Robbery = Violent taking",
                "Theft punishment: Up to 3 years (Bailable)",
                "Robbery punishment: Up to 10 years (Non-Bailable)",
                "Robbery becomes Dacoity when 5+ persons involved (IPC 395)"
            ],
            "procedure_overview": [
                "Theft is bailable - accused can get bail as right",
                "Robbery is non-bailable - bail at court's discretion",
                "Robbery is cognizable - police can arrest without warrant"
            ],
            "expert_note": "The key distinction is USE OF FORCE. If property is taken secretly = Theft. If force/intimidation is used = Robbery."
        },
        "bailable_vs_nonbailable": {
            "title": "Difference Between Bailable and Non-Bailable Offences",
            "definition": "Classification of offences based on the right to bail.",
            "key_elements": [
                "BAILABLE: Accused has RIGHT to bail - police/court MUST grant",
                "NON-BAILABLE: Bail is at court's DISCRETION - not automatic",
                "Bailable offences are generally less serious (theft, assault)",
                "Non-bailable offences are serious (murder, rape, robbery)",
                "First Schedule of CrPC lists classification of all offences"
            ],
            "procedure_overview": [
                "Bailable: Apply to police station officer or court",
                "Non-Bailable: Must apply to court with grounds",
                "Non-Bailable: Court considers flight risk, tampering, severity"
            ],
            "expert_note": "In non-bailable offences, bail is not impossible but harder to get. Court examines triple test: flight risk, tampering evidence, repeating offence."
        },
        "murder_vs_homicide": {
            "title": "Difference Between Murder and Culpable Homicide",
            "definition": "Both involve causing death, but differ in intention and punishment.",
            "key_elements": [
                "MURDER (IPC 302): Death caused with INTENTION to kill or knowledge of certainty of death",
                "CULPABLE HOMICIDE (IPC 304): Death caused with knowledge it's LIKELY to cause death (not certain)",
                "Murder = Higher degree of intention/knowledge",
                "Culpable Homicide = Lesser degree of intention",
                "Murder punishment: Death or Life imprisonment",
                "Culpable Homicide punishment: Up to 10 years or Life",
                "Section 300 Exception: Murder reduces to culpable homicide (provocation, private defence, etc.)"
            ],
            "expert_note": "Key test: Was death INTENDED or merely LIKELY? Intention = Murder; Likely = Culpable Homicide."
        },
        "article32_vs_226": {
            "title": "Difference Between Article 32 and Article 226",
            "definition": "Both provide for writ jurisdiction but with different scope and courts.",
            "key_elements": [
                "ARTICLE 32: Supreme Court writ jurisdiction",
                "ARTICLE 226: High Court writ jurisdiction",
                "Article 32: Only for Fundamental Rights - Narrower scope",
                "Article 226: Fundamental Rights + Any legal right - Wider scope",
                "Article 32: Itself a Fundamental Right (cannot be suspended except in Emergency)",
                "Article 226: Not a Fundamental Right (discretionary)",
                "Both can issue 5 types of writs",
                "Article 32 was called 'Heart and Soul' of Constitution by Dr. Ambedkar"
            ],
            "expert_note": "Article 226 is more commonly used as High Courts are more accessible. Article 32 is reserved for important constitutional matters."
        },
        "right_to_education": {
            "title": "Right to Education (Article 21A)",
            "definition": "The State shall provide free and compulsory education to all children of age 6-14 years.",
            "key_elements": [
                "Added by 86th Constitutional Amendment, 2002",
                "Made enforceable by RTE Act, 2009",
                "Free and compulsory education for ages 6-14",
                "25% reservation for EWS in private unaided schools",
                "No detention policy up to Class 8",
                "Neighborhood school norm"
            ],
            "landmark_case": "Society for Unaided Private Schools v. UOI (2012) - RTE applies to aided + unaided non-minority schools"
        },
        "constitution": {
            "title": "Indian Constitution - Fundamental Rights",
            "definition": "Part III of the Constitution contains Fundamental Rights (Articles 12-35).",
            "key_elements": [
                "Right to Equality (Articles 14-18)",
                "Right to Freedom (Articles 19-22)",
                "Right Against Exploitation (Articles 23-24)",
                "Right to Freedom of Religion (Articles 25-28)",
                "Cultural and Educational Rights (Articles 29-30)",
                "Right to Constitutional Remedies (Article 32)"
            ],
            "restrictions": "Fundamental Rights are not absolute. They can be restricted on reasonable grounds specified in the Constitution.",
            "expert_note": "Article 21 (Right to Life) has been given the widest interpretation by Supreme Court."
        },
        "post_fir_procedure": {
            "title": "What Happens After FIR is Filed",
            "definition": "The criminal investigation process that follows the registration of First Information Report.",
            "key_elements": [
                "1. Police investigation begins immediately",
                "2. IO (Investigating Officer) assigned to the case",
                "3. Evidence collection, witness statements recorded",
                "4. Accused may be arrested (if cognizable offence)",
                "5. Chargesheet must be filed within 60/90 days",
                "6. If chargesheet not filed, accused gets statutory bail"
            ],
            "procedure_overview": [
                "Step 1: FIR registered → Copy given to complainant free",
                "Step 2: Investigation by police → Evidence collection",
                "Step 3: Arrest of accused (if required)",
                "Step 4: Chargesheet/Final Report filed in court",
                "Step 5: Court takes cognizance → Trial begins"
            ],
            "expert_note": "You can track FIR status through the court's website or by visiting police station. Ask for case diary number."
        },
        "hacking": {
            "title": "Punishment for Hacking under IT Act",
            "definition": "Hacking is unauthorized access to computer system or network, punishable under Information Technology Act, 2000.",
            "section": "IT Act Section 66",
            "punishment": "Imprisonment up to 3 years + Fine up to ₹5 lakh",
            "key_elements": [
                "Section 66: Computer related offences - Up to 3 years + ₹5 lakh fine",
                "Section 66C: Identity theft using computer - Up to 3 years + ₹1 lakh fine",
                "Section 66D: Cheating by personation using computer - Up to 3 years + ₹1 lakh fine",
                "Section 43: Unauthorized access - Compensation up to ₹1 crore",
                "Cognizable and non-bailable for serious hacking"
            ],
            "procedure_overview": [
                "1. Report at cybercrime.gov.in",
                "2. File complaint at local Cyber Cell",
                "3. Preserve all digital evidence"
            ],
            "expert_note": "Ethical hacking (with permission) is legal. Only unauthorized access is punishable."
        },
        "default": {
            "title": "General Legal Query",
            "definition": "This is a general legal query.",
            "note": "In Lite Mode, specific case laws and deep retrieval are disabled. Please ask about Punishments, Bail, or basic Constitutional Articles."
        },
        
        # =============== ENHANCED PROCEDURES ===============
        "fir_filing": {
            "title": "How to File an FIR (Online and Offline)",
            "definition": "First Information Report (FIR) is the first step to initiate criminal proceedings for cognizable offences. FIR can be filed both ONLINE (e-FIR) and at police station.",
            "section": "CrPC Section 154",
            "key_elements": [
                "ZERO FIR: Can file FIR at ANY police station regardless of jurisdiction",
                "E-FIR / ONLINE FIR: Available online for theft/lost property in many states",
                "Police CANNOT refuse to register FIR for cognizable offence",
                "If refused: Complain to SP/Commissioner or file before Magistrate (CrPC 156(3))",
                "FREE COPY of FIR is your RIGHT under Section 154(2)"
            ],
            "step_by_step_procedure": [
                "Step 1: Go to police station having jurisdiction OR file online",
                "Step 2: Provide written complaint with facts of offence",
                "Step 3: Police writes information in FIR register",
                "Step 4: Read and verify FIR content before signing",
                "Step 5: Get FREE COPY of FIR (your legal right)",
                "Step 6: Note FIR number for future reference"
            ],
            "online_fir_process": [
                "Visit state police website (e.g., delhipolice.gov.in)",
                "Select 'e-FIR' or 'Online FIR' option",
                "Fill in details: incident, date, location, description",
                "Upload supporting documents if any",
                "Submit and note the acknowledgment number",
                "Available for: Theft, lost property, vehicle theft, mobile theft"
            ],
            "if_police_refuse": [
                "1. Get refusal in writing if possible",
                "2. Send complaint by registered post to SP",
                "3. File complaint before Magistrate under Section 156(3)",
                "4. File private complaint under Section 200 CrPC"
            ],
            "landmark_case": "Lalita Kumari v. State of UP (2014) - FIR mandatory for cognizable offence"
        },
        "anticipatory_bail": {
            "title": "Anticipatory Bail (CrPC Section 438)",
            "definition": "Bail granted BEFORE arrest in anticipation of arrest for non-bailable offence.",
            "statutes": ["CrPC Section 438", "BNSS Section 482"],
            "procedure_overview": [
                "1. File application in Sessions Court or High Court",
                "2. Application must state apprehension of arrest and grounds",
                "3. Court issues notice to prosecution/police",
                "4. Hearing conducted - Both sides present arguments",
                "5. If granted, accused protected from arrest",
                "6. Must comply with conditions (appearance, non-tampering)"
            ],
            "key_elements": [
                "Available only for non-bailable offences",
                "Not available for rape/acid attack (with exceptions)",
                "Can be granted by Sessions Court or High Court",
                "Interim protection often granted till final hearing",
                "Conditions: Join investigation, not leave country, etc."
            ],
            "landmark_case": "Sushila Aggarwal v. State (NCT of Delhi) (2020) - No time limit on anticipatory bail"
        },
        "arrest_procedure": {
            "title": "Arrest Procedure and Rights",
            "definition": "Legal process of taking a person into custody by police.",
            "statutes": ["CrPC Sections 41-60", "Article 22 of Constitution"],
            "procedure_overview": [
                "1. Police must have arrest warrant OR reasonable suspicion for cognizable offence",
                "2. Arrest memo MUST be prepared with time, date, place",
                "3. Arrestee MUST be informed of grounds of arrest",
                "4. One witness from family/locality required",
                "5. Produced before Magistrate within 24 HOURS",
                "6. Medical examination within 48 hours"
            ],
            "key_elements": [
                "Right to know grounds of arrest (Article 22)",
                "Right to consult lawyer of choice (Article 22)",
                "Right to inform family member (D.K. Basu guidelines)",
                "Right to medical examination",
                "Right against self-incrimination (Article 20(3))",
                "Woman cannot be arrested after sunset and before sunrise (except by female officer with Magistrate order)"
            ],
            "landmark_case": "D.K. Basu v. State of West Bengal (1997) - 11 mandatory guidelines for arrest"
        },
        "trial_procedure": {
            "title": "Criminal Trial Procedure in India",
            "definition": "The process by which criminal cases are heard and decided in court.",
            "statutes": ["CrPC Chapters XX-XXIV", "Indian Evidence Act"],
            "procedure_overview": [
                "1. COGNIZANCE: Court takes note of the case",
                "2. FRAMING OF CHARGES: Formal accusation read to accused",
                "3. PLEA: Accused pleads guilty or not guilty",
                "4. PROSECUTION EVIDENCE: Witnesses examined, documents produced",
                "5. STATEMENT OF ACCUSED: Accused gets chance to explain (Section 313)",
                "6. DEFENSE EVIDENCE: Accused presents witnesses/evidence",
                "7. ARGUMENTS: Both sides present final arguments",
                "8. JUDGMENT: Court delivers verdict - Acquittal or Conviction",
                "9. SENTENCING: If convicted, punishment decided"
            ],
            "key_elements": [
                "Burden of proof on prosecution - Beyond reasonable doubt",
                "Accused presumed innocent until proven guilty",
                "Right to cross-examine prosecution witnesses",
                "Right to present defense evidence",
                "Right to legal representation (free legal aid if needed)"
            ],
            "expert_note": "Criminal trials in India average 3-5 years. Fast track courts exist for certain offences."
        },
        "appeal_procedure": {
            "title": "Criminal Appeal Procedure",
            "definition": "Legal process to challenge a court judgment in a higher court.",
            "statutes": ["CrPC Sections 372-394", "Constitution Articles 132-136"],
            "procedure_overview": [
                "1. Obtain certified copy of judgment",
                "2. File appeal within limitation period (30-90 days)",
                "3. File memorandum of appeal with grounds",
                "4. Pay court fees (if applicable)",
                "5. Higher court admits appeal if grounds exist",
                "6. Hearing and fresh judgment"
            ],
            "key_elements": [
                "Sessions Court → High Court (First Appeal)",
                "High Court → Supreme Court (Second Appeal/SLP)",
                "Appeal against conviction: Always allowed",
                "Appeal against acquittal: Only by State with leave",
                "Revision: To examine legality, not re-appreciate evidence",
                "Review: Very limited grounds (error apparent on face)"
            ],
            "time_limits": {
                "sessions_to_hc": "30 days for appeal",
                "hc_to_sc": "90 days for SLP",
                "review": "30 days from judgment"
            }
        },
        "remand_custody": {
            "title": "Remand and Custody",
            "definition": "Judicial authorization to keep accused in custody during investigation.",
            "statutes": ["CrPC Section 167", "BNSS Section 187"],
            "procedure_overview": [
                "1. Accused produced before Magistrate within 24 hours",
                "2. Police request remand to police custody for investigation",
                "3. Magistrate can grant police custody up to 15 days (total)",
                "4. After police custody, judicial custody (in jail)",
                "5. Judicial custody: 60 days (minor offences) / 90 days (serious)",
                "6. If chargesheet not filed, statutory bail becomes right"
            ],
            "key_elements": [
                "Police custody MAX 15 days (for interrogation)",
                "Judicial custody: 60 days for offences up to 10 years",
                "Judicial custody: 90 days for offences above 10 years/life/death",
                "DEFAULT BAIL: If chargesheet not filed within time, release mandatory"
            ],
            "expert_note": "Police custody is for investigation. Once sent to judicial custody, accused cannot be brought back to police custody for same case."
        },
        
        # =============== ENHANCED CONSTITUTIONAL ARTICLES ===============
        "article_25": {
            "title": "Article 25: Freedom of Religion",
            "definition": "All persons are equally entitled to freedom of conscience and the right to freely profess, practice and propagate religion.",
            "key_elements": [
                "Freedom of conscience - Inner belief",
                "Right to profess - Declare faith openly",
                "Right to practice - Perform rituals, ceremonies",
                "Right to propagate - Spread one's religion (not convert by force)",
                "Subject to public order, morality, health",
                "Subject to other provisions of Part III"
            ],
            "restrictions": "State can regulate secular activities associated with religion; social welfare/reform legislation permitted",
            "landmark_case": "S.R. Bommai v. Union of India (1994) - Secularism is basic structure"
        },
        "article_226": {
            "title": "Article 226: Power of High Courts to Issue Writs",
            "definition": "High Courts have power to issue writs for enforcement of fundamental rights and 'any other purpose'.",
            "key_elements": [
                "Broader than Article 32 - Not limited to fundamental rights",
                "Can issue writs for 'any other purpose' (legal rights)",
                "Habeas Corpus, Mandamus, Certiorari, Prohibition, Quo Warranto",
                "Territorial jurisdiction must exist",
                "Discretionary remedy - Can be refused in exceptional circumstances"
            ],
            "vs_article_32": {
                "article_32": "Supreme Court only; Only for fundamental rights; Fundamental right itself",
                "article_226": "High Courts; Fundamental + Legal rights; Not a fundamental right"
            },
            "landmark_case": "L. Chandra Kumar v. UOI (1997) - Judicial review under 226 is basic structure"
        },
        "article_352": {
            "title": "Article 352: National Emergency",
            "definition": "President can proclaim Emergency if security of India or any part is threatened by war, external aggression, or armed rebellion.",
            "key_elements": [
                "Grounds: War, external aggression, armed rebellion",
                "Cabinet recommendation in writing required",
                "Parliamentary approval within 1 month",
                "Duration: 6 months at a time, can be extended",
                "Effects: Union gets expanded powers over states",
                "Articles 19 can be suspended; Article 20, 21 cannot be suspended"
            ],
            "landmark_case": "ADM Jabalpur v. Shivkant Shukla (1976) - Overruled; 44th Amendment protection"
        },
        "article_356": {
            "title": "Article 356: President's Rule in States",
            "definition": "If President is satisfied that government of a State cannot be carried on in accordance with Constitution, President's Rule can be imposed.",
            "key_elements": [
                "Report of Governor OR otherwise satisfied",
                "State Legislature dissolved or suspended",
                "State administration run by President through Governor",
                "Parliamentary approval within 2 months",
                "Maximum duration: 3 years (with conditions)",
                "Sarkaria Commission recommendations apply"
            ],
            "landmark_case": "S.R. Bommai v. UOI (1994) - Judicial review of President's Rule; floor test mandatory"
        },
        "article_370": {
            "title": "Article 370 - Special Status of Jammu & Kashmir (Abrogated)",
            "definition": "Article 370 granted special autonomous status to the state of Jammu and Kashmir, which was abrogated on August 5, 2019.",
            "key_elements": [
                "Granted special autonomous status to Jammu & Kashmir",
                "J&K had separate constitution and flag",
                "Only Article 1 and 370 applied directly",
                "Other constitutional provisions applied with President's order",
                "Permanent residents had special rights (Article 35A)",
                "ABROGATED on 5 August 2019 by Presidential Order"
            ],
            "historical_context": [
                "Part of Instrument of Accession negotiations (1947)",
                "Article 35A added in 1954 (Presidential Order)",
                "Allowed J&K to define 'permanent residents'",
                "Residents had exclusive rights to property, jobs, education"
            ],
            "abrogation_2019": [
                "Presidential Order under Article 370(1) on 5 Aug 2019",
                "Article 370 itself used to abrogate special status",
                "J&K reorganized into two Union Territories",
                "J&K (with legislature) and Ladakh (without legislature)",
                "Upheld by Supreme Court in December 2023"
            ],
            "landmark_case": "In Re: Article 370 (2023) - Supreme Court upheld abrogation as constitutional"
        },
        "case_indra_sawhney": {
            "title": "Indra Sawhney v. Union of India (1992) - Mandal Commission Case",
            "definition": "Landmark case upholding reservation for OBCs while setting 50% ceiling on total reservations.",
            "key_elements": [
                "Upheld 27% reservation for OBCs (Mandal Commission)",
                "50% ceiling on total reservations (including SC/ST/OBC)",
                "Introduced 'CREAMY LAYER' concept for OBCs",
                "Creamy layer excluded from OBC reservation benefits",
                "No reservation in promotions (later amended)",
                "Reservation based on backwardness, not religion"
            ],
            "fifty_percent_rule": [
                "Total reservations cannot exceed 50% normally",
                "Exception: Extraordinary situations (Tamil Nadu 69%)",
                "SC: 15%, ST: 7.5%, OBC: 27% = 49.5% Central",
                "States may have different percentages"
            ],
            "creamy_layer": [
                "OBCs with income above specified limit excluded",
                "Currently Rs. 8 lakh per annum",
                "Does not apply to SC/ST reservations",
                "Children of constitutional post holders excluded"
            ],
            "landmark_case": "Indra Sawhney v. Union of India (1992) - 9-judge bench"
        },
        "civil_vs_criminal": {
            "title": "Difference Between Civil Law and Criminal Law",
            "definition": "Civil law deals with private disputes between individuals seeking compensation, while criminal law deals with crimes against society punished by the State.",
            "key_differences": [
                "PURPOSE: Civil - Compensation/remedy; Criminal - Punishment/deterrence",
                "PARTIES: Civil - Plaintiff vs Defendant; Criminal - State vs Accused",
                "BURDEN: Civil - Preponderance of probability; Criminal - Beyond reasonable doubt",
                "OUTCOME: Civil - Damages/injunction; Criminal - Imprisonment/fine",
                "NATURE: Civil - Private wrong; Criminal - Public wrong against society"
            ],
            "civil_law": [
                "Disputes between private parties",
                "Contract disputes, property disputes, family matters",
                "Relief: Compensation, specific performance, injunction",
                "Filed in Civil Courts",
                "CPC (Civil Procedure Code) applies"
            ],
            "criminal_law": [
                "Crime against society/State",
                "Murder, theft, assault, fraud",
                "Punishment: Imprisonment, fine, death penalty",
                "Prosecution by State (Public Prosecutor)",
                "CrPC (Criminal Procedure Code) applies"
            ],
            "can_be_both": "Same act can be civil wrong AND criminal offence (e.g., defamation, assault)"
        },
        "parole_vs_furlough": {
            "title": "Difference Between Parole and Furlough",
            "definition": "Both are temporary release from prison, but parole is conditional release for specific reasons while furlough is routine release as a right.",
            "key_differences": [
                "PAROLE: Granted for specific emergent reason (death, marriage, illness)",
                "FURLOUGH: Routine temporary release - a RIGHT of prisoner",
                "PAROLE: Duration varies based on reason (usually 30 days max)",
                "FURLOUGH: Fixed duration (14-21 days typically)",
                "PAROLE: Not counted as sentence served",
                "FURLOUGH: Counted as part of sentence served"
            ],
            "parole": [
                "Conditional release for emergent/special reasons",
                "Death in family, serious illness, marriage",
                "Granted by Prison Authority/State Government",
                "Period NOT counted towards sentence",
                "Subject to conditions and surety"
            ],
            "furlough": [
                "Periodic temporary release as MATTER OF RIGHT",
                "Available after serving certain period",
                "Purpose: Maintain family/social ties",
                "Period COUNTED towards sentence",
                "Regular intervals (every 6 months to 2 years)"
            ],
            "common_conditions": [
                "Must not leave specified area",
                "Report to local police station",
                "Return on specified date",
                "Violation leads to arrest and added punishment"
            ]
        },
        "criminal_breach_of_trust": {
            "section": "IPC Section 406",
            "title": "Punishment for Criminal Breach of Trust",
            "definition": "Whoever, being entrusted with property, or with dominion over property, dishonestly misappropriates or converts to his own use that property, commits criminal breach of trust.",
            "punishment": "Imprisonment up to 3 years OR Fine OR Both",
            "key_elements": [
                "Section 405: Definition - Person entrusted with property",
                "Section 406: Punishment for criminal breach of trust - 3 years",
                "Section 407: By carrier/wharfinger - 7 years",
                "Section 408: By clerk/servant - 7 years",
                "Section 409: By public servant/banker/agent - 10 years/Life",
                "Dishonest misappropriation of entrusted property"
            ],
            "essential_elements": [
                "1. Property must be ENTRUSTED to accused",
                "2. Accused must have DOMINION over property",
                "3. DISHONEST misappropriation or conversion",
                "4. Violation of any direction of law or legal contract"
            ],
            "examples": [
                "Employee misappropriating company funds",
                "Agent retaining client's money",
                "Trustee using trust property for personal benefit",
                "Partner diverting partnership assets"
            ],
            "bail_info": {"bailable": True, "type": "Bailable for 406; Non-Bailable for 408/409"}
        },
        "writ_types": {
            "title": "Five Types of Writs Under Article 32 and 226",
            "definition": "The Constitution provides five types of writs for enforcement of fundamental rights through Supreme Court (Article 32) and High Courts (Article 226).",
            "writs": {
                "habeas_corpus": {
                    "meaning": "To have the body",
                    "purpose": "Against illegal detention/custody",
                    "issued_against": "Person detaining another illegally"
                },
                "mandamus": {
                    "meaning": "We command",
                    "purpose": "To direct public authority to perform duty",
                    "issued_against": "Public officials/bodies refusing to act"
                },
                "certiorari": {
                    "meaning": "To be certified",
                    "purpose": "To quash order of lower court/tribunal",
                    "issued_against": "Inferior courts/tribunals exceeding jurisdiction"
                },
                "prohibition": {
                    "meaning": "To forbid",
                    "purpose": "To prevent lower court from exceeding jurisdiction",
                    "issued_against": "Courts/tribunals before decision"
                },
                "quo_warranto": {
                    "meaning": "By what authority",
                    "purpose": "To challenge person holding public office illegally",
                    "issued_against": "Person usurping public office"
                }
            },
            "key_elements": [
                "HABEAS CORPUS: Release from illegal detention",
                "MANDAMUS: Compel public duty performance",
                "CERTIORARI: Quash judicial/quasi-judicial orders",
                "PROHIBITION: Stop proceedings without jurisdiction",
                "QUO WARRANTO: Challenge illegal occupation of office"
            ]
        },
        "article32_vs_226": {
            "title": "Difference Between Article 32 and Article 226",
            "definition": "Both articles provide writ jurisdiction, but Article 32 is for Supreme Court (Fundamental Rights only) while Article 226 is for High Court (broader scope).",
            "key_differences": [
                "COURT: Art 32 - Supreme Court; Art 226 - High Court",
                "SCOPE: Art 32 - Only Fundamental Rights; Art 226 - Any legal right",
                "NATURE: Art 32 - Fundamental Right itself; Art 226 - Discretionary power",
                "TERRITORY: Art 32 - Entire India; Art 226 - Within territorial jurisdiction",
                "WRITS: Both can issue all 5 writs"
            ],
            "article_32": [
                "Supreme Court's original jurisdiction",
                "Only for enforcement of FUNDAMENTAL RIGHTS",
                "Article 32 itself is a Fundamental Right",
                "Cannot be suspended except during Emergency",
                "Dr. B.R. Ambedkar called it 'Heart and Soul of Constitution'"
            ],
            "article_226": [
                "High Court's writ jurisdiction",
                "For enforcement of ANY legal right (not just fundamental)",
                "Discretionary power - can be refused",
                "Wider scope than Article 32",
                "Subject to territorial jurisdiction"
            ]
        },
        
        # =============== ENHANCED CRIMES ===============
        "dacoity": {
            "section": "IPC Section 395",
            "title": "Punishment for Dacoity",
            "definition": "When five or more persons conjointly commit or attempt to commit robbery, every such person is guilty of dacoity.",
            "punishment": "Rigorous imprisonment for life OR up to 10 years + Fine",
            "key_elements": [
                "Minimum 5 persons required",
                "All 5 need not be apprehended to prove dacoity",
                "Section 396: Dacoity with murder - Death or Life imprisonment",
                "Section 397: With deadly weapon - Minimum 7 years",
                "Non-bailable, Cognizable, Triable by Sessions"
            ],
            "bail_info": {"bailable": False, "type": "Non-Bailable"}
        },
        "extortion": {
            "section": "IPC Section 384",
            "title": "Punishment for Extortion",
            "definition": "Whoever intentionally puts any person in fear of injury to that person or another, and thereby dishonestly induces the person to deliver property or valuable security.",
            "punishment": "Imprisonment up to 3 years OR Fine OR Both",
            "key_elements": [
                "Section 383: Definition of extortion",
                "Section 384: Punishment for extortion",
                "Section 385: Putting in fear for extortion - 2 years",
                "Section 386: Extortion by putting in fear of death - 10 years",
                "Section 387: Putting in fear of death to commit extortion - 7 years"
            ],
            "bail_info": {"bailable": False, "type": "Non-Bailable for Section 386"}
        },
        "criminal_intimidation": {
            "section": "IPC Section 506",
            "title": "Punishment for Criminal Intimidation",
            "definition": "Threatening another with any injury to person, reputation or property with intent to cause alarm.",
            "punishment": "Imprisonment up to 2 years OR Fine OR Both; If threat to cause death/grievous hurt - 7 years",
            "key_elements": [
                "Section 503: Definition of criminal intimidation",
                "Section 506: Punishment - Part I (2 years) or Part II (7 years)",
                "Part I: Simple threat - Bailable",
                "Part II: Threat of death/grievous hurt - Non-Bailable",
                "Anonymous threats also covered"
            ],
            "bail_info": {"bailable": True, "type": "Bailable for Part I, Non-Bailable for Part II"}
        },
        "forgery": {
            "section": "IPC Section 465",
            "title": "Punishment for Forgery",
            "definition": "Making a false document or electronic record with intent to cause damage or support any claim.",
            "punishment": "Imprisonment up to 2 years OR Fine OR Both",
            "key_elements": [
                "Section 463: Definition of forgery",
                "Section 465: Punishment for forgery - 2 years",
                "Section 467: Forgery of valuable security - Up to life imprisonment",
                "Section 468: Forgery for cheating - 7 years",
                "Section 471: Using forged document as genuine"
            ],
            "bail_info": {"bailable": True, "type": "Bailable for Section 465, Non-Bailable for 467/468"}
        },
        "mischief": {
            "section": "IPC Section 426",
            "title": "Punishment for Mischief",
            "definition": "Whoever destroys or damages property with intent to cause wrongful loss or damage.",
            "punishment": "Imprisonment up to 3 months OR Fine OR Both",
            "key_elements": [
                "Section 425: Definition of mischief",
                "Section 426: Punishment - 3 months",
                "Section 427: Mischief causing damage ₹50+ - 2 years",
                "Section 435: Mischief by fire/explosive - 7 years",
                "Section 436: Mischief by fire to building - Life imprisonment"
            ],
            "bail_info": {"bailable": True, "type": "Bailable for simple mischief"}
        },
        "trespass": {
            "section": "IPC Section 447",
            "title": "Punishment for Criminal Trespass",
            "definition": "Whoever enters into or upon property in possession of another with intent to commit offence or intimidate.",
            "punishment": "Imprisonment up to 3 months OR Fine up to ₹500 OR Both",
            "key_elements": [
                "Section 441: Definition of criminal trespass",
                "Section 447: Punishment - 3 months",
                "Section 448: House-trespass - 1 year",
                "Section 449: House-trespass to commit offence punishable with death - Life imprisonment",
                "Section 452: House-trespass after preparation for hurt - 7 years"
            ],
            "bail_info": {"bailable": True, "type": "Bailable for simple trespass"}
        },
        
        # =============== ENHANCED WRITS ===============
        "habeas_corpus": {
            "title": "Writ of Habeas Corpus",
            "definition": "Latin for 'to have the body'. A writ directing a person detaining another to produce the detained person before court and show cause of detention.",
            "key_elements": [
                "Most powerful writ for personal liberty",
                "Against unlawful detention by State or private person",
                "Can be filed by detained person OR on their behalf",
                "Cannot be suspended even during Emergency (44th Amendment)",
                "Courts work even on holidays for habeas corpus"
            ],
            "procedure_overview": [
                "1. File petition in High Court or Supreme Court",
                "2. State grounds of illegal detention",
                "3. Court issues notice to detaining authority",
                "4. Detaining authority must justify detention",
                "5. If unjustified, person released immediately"
            ],
            "landmark_case": "Rudul Shah v. State of Bihar (1983) - Compensation for illegal detention"
        },
        "mandamus": {
            "title": "Writ of Mandamus",
            "definition": "Latin for 'we command'. A writ commanding a public official or body to perform a public duty.",
            "key_elements": [
                "Lies against public officials, government, statutory bodies",
                "Cannot be issued against private persons/bodies",
                "Cannot be issued against President or Governor",
                "Petitioner must have legal right to demand action",
                "Duty must be mandatory, not discretionary"
            ],
            "procedure_overview": [
                "1. Show legal right to demand performance of duty",
                "2. Show respondent has legal duty",
                "3. Show respondent failed to perform duty",
                "4. Court examines if duty is mandatory",
                "5. If yes, mandamus issued compelling performance"
            ],
            "landmark_case": "S.P. Gupta v. UOI (1981) - Mandamus for non-appointment of judges"
        },
        "certiorari": {
            "title": "Writ of Certiorari",
            "definition": "Latin for 'to be certified'. A writ to quash the order of a lower court or tribunal that has acted without or in excess of jurisdiction.",
            "key_elements": [
                "To quash order already passed",
                "Against judicial or quasi-judicial bodies",
                "Grounds: Lack of jurisdiction, error of law, violation of natural justice",
                "Cannot be used against private bodies",
                "Retrospective in nature - quashes past order"
            ],
            "procedure_overview": [
                "1. Challenge order of lower court/tribunal",
                "2. Show jurisdictional error or error of law",
                "3. Court examines if error exists",
                "4. If yes, order quashed (set aside)"
            ]
        },
        "prohibition": {
            "title": "Writ of Prohibition",
            "definition": "A writ to prohibit a lower court or tribunal from proceeding with a case beyond its jurisdiction.",
            "key_elements": [
                "Preventive in nature - stops proceedings",
                "Against judicial or quasi-judicial bodies only",
                "Issued when lower court acting without jurisdiction",
                "Must be filed before final order is passed",
                "Prospective in nature - prevents future action"
            ],
            "vs_certiorari": "Prohibition prevents; Certiorari quashes. Prohibition is before order; Certiorari is after order."
        },
        "quo_warranto": {
            "title": "Writ of Quo Warranto",
            "definition": "Latin for 'by what authority'. A writ to inquire into the legality of a person holding a public office.",
            "key_elements": [
                "Challenges right to hold public office",
                "Office must be public and substantive",
                "Office must be created by Constitution or statute",
                "Any person can file - no need for personal interest",
                "If successful, person removed from office"
            ],
            "procedure_overview": [
                "1. Any person files petition",
                "2. Challenge authority to hold public office",
                "3. Court examines qualifications/eligibility",
                "4. If holding illegally, declares office vacant"
            ],
            "landmark_case": "University of Mysore v. C.D. Govinda Rao (1965) - Quo warranto against illegal appointment"
        },
        
        # =============== MORE LANDMARK CASES ===============
        "case_shreya_singhal": {
            "title": "Shreya Singhal v. Union of India (2015)",
            "definition": "Supreme Court struck down Section 66A of IT Act as unconstitutional for violating free speech.",
            "key_elements": [
                "Section 66A was vague and overbroad",
                "Violated Article 19(1)(a) - Freedom of speech",
                "Terms like 'grossly offensive' too subjective",
                "Section 69A (blocking websites) upheld with safeguards",
                "Major victory for online free speech"
            ],
            "impact": "Landmark judgment protecting internet freedom in India"
        },
        "case_navtej_johar": {
            "title": "Navtej Singh Johar v. Union of India (2018)",
            "definition": "Supreme Court decriminalized consensual homosexual acts between adults by reading down Section 377 IPC.",
            "key_elements": [
                "Section 377 declared unconstitutional for consensual adult acts",
                "Violated Articles 14, 15, 19, 21",
                "LGBTQ+ community entitled to equal citizenship",
                "Criminalization of natural sexual orientation discriminatory",
                "5-judge constitution bench unanimous decision"
            ],
            "impact": "Historic judgment for LGBTQ+ rights in India"
        },
        "case_dk_basu": {
            "title": "D.K. Basu v. State of West Bengal (1997)",
            "definition": "Supreme Court laid down 11 mandatory requirements to be followed during arrest and detention to prevent custodial violence.",
            "key_elements": [
                "Arrest memo with date, time, place mandatory",
                "One witness from family/respectable person required",
                "Right to inform friend/relative of arrest",
                "Entry in diary at place of detention",
                "Medical examination every 48 hours",
                "Arrestee entitled to meet lawyer during interrogation"
            ],
            "impact": "Fundamental guidelines to prevent custodial torture and death"
        },
        
        # =============== CrPC SECTIONS (Enhanced) ===============
        "crpc_section_154": {
            "title": "CrPC Section 154 - First Information Report (FIR)",
            "definition": "Section 154 of CrPC deals with information relating to commission of cognizable offence and its recording.",
            "section": "CrPC Section 154",
            "key_elements": [
                "FIR is the first information given to police about a cognizable offence",
                "Must be reduced to writing and signed by the informant",
                "FREE COPY must be given to informant (Section 154(2))",
                "Officer in charge of police station must record FIR",
                "If refused, can send by post to SP or file before Magistrate (Section 156(3))",
                "Zero FIR can be filed at ANY police station"
            ],
            "procedure_overview": [
                "1. Visit police station having jurisdiction",
                "2. Give oral or written information about cognizable offence",
                "3. Police officer writes information in prescribed form",
                "4. Informant reads, verifies and signs FIR",
                "5. Get FREE copy of FIR immediately",
                "6. Investigation begins under Section 156"
            ],
            "important_points": [
                "FIR is NOT evidence but corroborative material",
                "Delay in FIR must be explained",
                "False FIR is punishable under IPC 182/211",
                "FIR can be quashed by High Court under Section 482"
            ],
            "landmark_case": "Lalita Kumari v. State of U.P. (2014) - FIR mandatory for cognizable offence"
        },
        "crpc_section_156": {
            "title": "CrPC Section 156 - Police Officer's Power to Investigate Cognizable Case",
            "definition": "Section 156 empowers police officers to investigate any cognizable case without order of Magistrate.",
            "section": "CrPC Section 156",
            "key_elements": [
                "Police can investigate cognizable offence without Magistrate's order",
                "Section 156(1): Power to investigate cognizable cases",
                "Section 156(3): Magistrate can order investigation if police refuse",
                "Investigation includes recording statements, collecting evidence",
                "IO (Investigating Officer) is appointed for the case"
            ],
            "procedure_overview": [
                "1. FIR registered under Section 154",
                "2. Investigation begins under Section 156(1)",
                "3. Police collect evidence, record statements (Section 161)",
                "4. If police refuse, file application under Section 156(3)",
                "5. Magistrate can direct police to investigate"
            ],
            "important_points": [
                "Section 156(3) is powerful remedy against police inaction",
                "Magistrate can order investigation even at pre-FIR stage",
                "Police must file action taken report after 156(3) order"
            ]
        },
        "crpc_section_161": {
            "title": "CrPC Section 161 - Examination of Witnesses by Police",
            "definition": "Section 161 empowers police officer to examine witnesses orally during investigation.",
            "section": "CrPC Section 161",
            "key_elements": [
                "Police can orally examine any person acquainted with facts",
                "Person is bound to answer truthfully (except self-incriminating questions)",
                "Statement recorded in writing by police",
                "Section 162: Statement to police NOT admissible as evidence",
                "Statement can only be used to contradict witness in trial"
            ],
            "procedure_overview": [
                "1. Police summons witness during investigation",
                "2. Witness examined orally by investigating officer",
                "3. Statement recorded in case diary",
                "4. Witness need not sign the statement",
                "5. Statement used only for contradiction, not as evidence"
            ],
            "important_points": [
                "Right against self-incrimination applies (Article 20(3))",
                "Woman witness to be examined at residence",
                "Statement to police is inadmissible under Section 162",
                "Only confession to Magistrate (Section 164) is admissible"
            ]
        },
        "crpc_section_41": {
            "title": "CrPC Section 41 - When Police May Arrest Without Warrant",
            "definition": "Section 41 specifies circumstances when police can arrest without warrant for cognizable offence.",
            "section": "CrPC Section 41",
            "key_elements": [
                "Arrest without warrant only for COGNIZABLE offences",
                "Section 41(1)(b)(ii): Must have REASON TO BELIEVE (not mere suspicion)",
                "Section 41A: Notice of Appearance for offences <7 years punishment",
                "Arrest memo mandatory with time, date, witness",
                "Conditions: Reasonable complaint, credible information, reasonable suspicion"
            ],
            "conditions_for_arrest": [
                "1. Committed cognizable offence in officer's presence",
                "2. Reasonable complaint or credible information received",
                "3. Reasonable suspicion of cognizable offence",
                "4. Person in possession of stolen property",
                "5. Person obstructing police officer",
                "6. Escapee from lawful custody"
            ],
            "arnesh_kumar_guidelines": [
                "No automatic arrest for offences punishable <7 years",
                "Notice of Appearance (Section 41A) must be issued first",
                "Arrest only after recording reasons",
                "Magistrate must verify compliance",
                "Applies to Section 498A cases"
            ],
            "landmark_case": "Arnesh Kumar v. State of Bihar (2014) - No automatic arrest for <7 years offences"
        },
        "crpc_section_125": {
            "title": "CrPC Section 125 - Maintenance of Wives, Children and Parents",
            "definition": "Section 125 provides for order of maintenance to be paid by a person to his wife, children and parents who are unable to maintain themselves.",
            "section": "CrPC Section 125",
            "key_elements": [
                "Wife: Unable to maintain herself, entitled to maintenance",
                "Children: Legitimate or illegitimate, minor children entitled",
                "Parents: Unable to maintain themselves, father/mother entitled",
                "Husband must have sufficient means to pay",
                "Maximum: ₹500/month per person initially, now increased by states",
                "Secular provision - applies to all religions including Muslims"
            ],
            "who_can_claim": [
                "Wife (including divorced wife who has not remarried)",
                "Minor children (legitimate or illegitimate)",
                "Major unmarried daughter (if unable to maintain)",
                "Major son (if minor or physically/mentally abnormal)",
                "Father and mother (if unable to maintain themselves)"
            ],
            "procedure": [
                "1. Application filed before Magistrate where wife/child/parent resides",
                "2. Notice issued to husband/father/son",
                "3. Both parties present evidence",
                "4. Magistrate examines means of husband and needs of claimant",
                "5. Order for maintenance passed",
                "6. Non-payment: Imprisonment up to 1 month or until paid"
            ],
            "landmark_case": "Shah Bano v. Union of India (1985) - Muslim divorced women entitled to maintenance under Section 125"
        },
        "crpc_section_482": {
            "title": "CrPC Section 482 - Inherent Powers of High Court",
            "definition": "Section 482 saves inherent power of High Court to make orders necessary to prevent abuse of process or secure ends of justice.",
            "section": "CrPC Section 482",
            "key_elements": [
                "HIGH COURT has inherent power to quash proceedings",
                "To prevent abuse of process of any court",
                "To secure the ends of justice",
                "Can quash FIR, criminal complaint, or chargesheet",
                "Used when charges are frivolous, vexatious, or prima facie no case",
                "Discretionary power - cannot be claimed as right"
            ],
            "grounds_for_quashing": [
                "Allegations even if taken as true do not constitute offence",
                "Proceedings are malicious prosecution",
                "Criminal proceedings based on civil dispute",
                "FIR based on false allegations by settled dispute",
                "No prima facie case made out",
                "Continuation of proceedings is abuse of process"
            ],
            "procedure": [
                "1. File petition under Section 482 in High Court",
                "2. Challenge FIR, chargesheet, or criminal proceedings",
                "3. Court examines if prima facie case exists",
                "4. If grounds made out, proceedings quashed",
                "5. Stay of arrest can be granted pending disposal"
            ],
            "limitations": [
                "Cannot be used to conduct mini-trial",
                "Facts must be taken as stated in FIR/complaint",
                "Not substitute for trial",
                "Rare in heinous offences like murder, rape"
            ],
            "landmark_case": "Bhajan Lal v. State of Haryana (1992) - 7 categories of cases where FIR can be quashed"
        },
        "crpc_section_173": {
            "title": "CrPC Section 173 - Report of Police Officer on Completion of Investigation",
            "definition": "Section 173 requires police to submit investigation report (chargesheet) to Magistrate upon completion of investigation.",
            "section": "CrPC Section 173",
            "key_elements": [
                "Police must complete investigation and file CHARGESHEET",
                "Report filed before Magistrate taking cognizance",
                "Chargesheet contains: Names of parties, nature of information, evidence",
                "If evidence insufficient: Closure report (FR) filed",
                "Magistrate may accept, reject, or direct further investigation",
                "Time limit: 60/90 days depending on offence severity"
            ],
            "contents_of_chargesheet": [
                "Names of parties and nature of offence",
                "Names of witnesses",
                "Whether any offence appears committed",
                "If committed, by whom",
                "Statement of accused under Section 313",
                "All documents and evidence collected"
            ],
            "types_of_reports": [
                "Chargesheet: When evidence sufficient for prosecution",
                "Final Report (Closure): When evidence insufficient",
                "Referred Report: Minor offences referred to panchayat",
                "Supplementary Chargesheet: Additional evidence after first chargesheet"
            ],
            "magistrate_powers": [
                "Take cognizance and issue process (summons/warrant)",
                "Accept closure report and close case",
                "Reject closure report and direct further investigation",
                "Add charges or drop charges based on evidence"
            ],
            "landmark_case": "State of Haryana v. Bhajan Lal (1992) - Procedures for investigation and chargesheet"
        },
        "crpc_section_167": {
            "title": "CrPC Section 167 - Procedure When Investigation Cannot Be Completed in 24 Hours",
            "definition": "Section 167 deals with remand of accused when investigation cannot be completed within 24 hours of arrest.",
            "section": "CrPC Section 167",
            "key_elements": [
                "Accused MUST be produced before Magistrate within 24 hours",
                "Police custody: Maximum 15 days (for interrogation)",
                "Judicial custody: 60 days (offences up to 10 years) / 90 days (above 10 years)",
                "DEFAULT BAIL: If chargesheet not filed in time, accused gets statutory bail",
                "Magistrate authorizes detention by remand order"
            ],
            "custody_periods": {
                "police_custody": "Maximum 15 days TOTAL (not continuous)",
                "judicial_custody_60_days": "Offences punishable up to 10 years imprisonment",
                "judicial_custody_90_days": "Offences punishable above 10 years, life, death"
            },
            "statutory_bail": [
                "If chargesheet not filed within 60/90 days, right to DEFAULT BAIL",
                "Also called STATUTORY BAIL or COMPULSIVE BAIL",
                "Court MUST release on bail - no discretion",
                "Indefeasible right - cannot be denied",
                "Once chargesheet filed, default bail right gone"
            ],
            "procedure_overview": [
                "1. Arrest → 24 hours → Produced before Magistrate",
                "2. Police request remand (custody) for investigation",
                "3. Magistrate grants police custody (max 15 days)",
                "4. After police custody, judicial custody (60/90 days)",
                "5. Chargesheet filed → Trial begins",
                "6. No chargesheet in time → Default bail"
            ],
            "landmark_case": "Sanjay Dutt v. State (1994) - Right to default bail is indefeasible"
        },
        
        # =============== EVIDENCE ACT ===============
        "evidence_act": {
            "title": "Indian Evidence Act, 1872 - Overview",
            "definition": "The Indian Evidence Act, 1872 is the primary law governing admissibility and relevancy of evidence in Indian courts.",
            "key_elements": [
                "Enacted in 1872, still in force (being replaced by Bharatiya Sakshya Adhiniyam 2023)",
                "Defines what evidence is admissible in court",
                "Covers relevancy, admissions, confessions, witnesses",
                "Applies to all judicial proceedings (civil and criminal)",
                "Part I: Relevancy (Sections 5-55)",
                "Part II: Proof (Sections 56-100)",
                "Part III: Witnesses (Sections 101-167)"
            ],
            "types_of_evidence": [
                "Oral Evidence: Statements made by witnesses in court",
                "Documentary Evidence: Documents and electronic records",
                "Direct Evidence: Directly proves fact (eyewitness)",
                "Circumstantial Evidence: Proves fact by inference",
                "Primary Evidence: Original document",
                "Secondary Evidence: Copy when original not available"
            ]
        },
        "burden_of_proof": {
            "title": "Burden of Proof (Evidence Act Section 101-104)",
            "definition": "Under the Evidence Act, the burden of proof means the obligation to prove a fact. Section 101 states: 'Whoever desires any court to give judgment as to any legal right or liability dependent on the existence of facts which he asserts, must prove that those facts exist.' In civil cases, the plaintiff bears the initial burden.",
            "section": "Evidence Act Section 101",
            "key_elements": [
                "Evidence Act governs all rules of burden of proof",
                "Section 101: Burden on person who asserts fact",
                "Section 102: Burden shifts based on pleadings",
                "Section 103: Burden of proof of particular fact",
                "Section 104: Burden on person desiring court to believe",
                "CIVIL: Plaintiff must prove case on preponderance of probability",
                "CRIMINAL: Prosecution must prove guilt beyond reasonable doubt"
            ],
            "who_proves": {
                "civil_case": "PLAINTIFF bears initial burden to prove claim under Evidence Act",
                "criminal_case": "PROSECUTION bears burden to prove guilt",
                "exceptions": "Burden on accused to prove insanity, intoxication, etc."
            },
            "standards": {
                "criminal": "Beyond reasonable doubt (highest standard)",
                "civil": "Preponderance of probability (balance of evidence)"
            },
            "plaintiff_burden": "In civil cases under the Evidence Act, the plaintiff who files the suit bears the burden to prove all essential facts of the claim. If plaintiff fails to discharge this burden, the suit is dismissed.",
            "presumption_of_innocence": "Accused is presumed innocent until proven guilty. Burden lies on prosecution to prove guilt beyond reasonable doubt. If prosecution fails, accused is entitled to acquittal."
        },
        "hearsay_evidence": {
            "title": "Hearsay Evidence (Section 60 - Evidence Act)",
            "definition": "Hearsay is second-hand evidence - what a witness heard from someone else rather than what they directly perceived. It is generally INADMISSIBLE under Section 60.",
            "section": "Evidence Act Section 60",
            "key_elements": [
                "Section 60: Oral evidence must be DIRECT evidence",
                "Hearsay is INADMISSIBLE in Indian courts",
                "Reason: Cannot cross-examine the original source",
                "Only DIRECT evidence of what witness saw/heard is admissible",
                "Exceptions: Dying declaration, res gestae, admissions"
            ],
            "inadmissibility_rule": [
                "Hearsay evidence is INADMISSIBLE under Section 60",
                "Section 60 requires oral evidence to be DIRECT",
                "What witness was TOLD by another is inadmissible",
                "Only what witness SAW or HEARD directly is admissible"
            ],
            "exceptions_to_hearsay": [
                "Dying Declaration (Section 32) - Statement of deceased",
                "Res Gestae (Section 6) - Statements contemporaneous with transaction",
                "Admissions and Confessions (Sections 17-31)",
                "Statements in public documents",
                "Expert opinion on published works"
            ],
            "rule": "What a witness SAW or HEARD directly is admissible. What someone TOLD them is hearsay and inadmissible."
        },
        "circumstantial_evidence": {
            "title": "Circumstantial Evidence (Indirect Evidence)",
            "definition": "Circumstantial or indirect evidence proves a fact by inference from other established facts, rather than by direct testimony or observation.",
            "key_elements": [
                "INDIRECT evidence - proves fact through chain of circumstances",
                "No direct eyewitness or confession available",
                "Must form COMPLETE CHAIN pointing only to guilt",
                "All circumstances must be proved beyond reasonable doubt",
                "Chain must exclude every hypothesis except guilt of accused",
                "Proof by INFERENCE from established facts"
            ],
            "chain_of_circumstances": [
                "Each link in chain must be proved",
                "Chain must form complete circle pointing to accused",
                "No break in chain of circumstances",
                "All circumstances together prove guilt by INFERENCE",
                "If chain is broken, benefit of doubt to accused"
            ],
            "legal_standards": [
                "Circumstances must be established conclusively",
                "Circumstances must point only to hypothesis of guilt",
                "All circumstances must form a complete chain",
                "Chain must exclude any reasonable hypothesis of innocence",
                "Motive alone is insufficient - need complete chain"
            ],
            "landmark_case": "Sharad Birdhichand Sarda v. State of Maharashtra (1984) - Five conditions for circumstantial evidence"
        },
        "expert_evidence": {
            "title": "Expert Evidence (Section 45 - Evidence Act)",
            "definition": "Section 45 of Evidence Act allows opinions of experts to be relevant on matters requiring special knowledge or skill.",
            "section": "Evidence Act Section 45",
            "key_elements": [
                "Section 45: Expert opinion on foreign law, science, art, handwriting",
                "Expert: Person with special knowledge gained by experience/study",
                "Areas: Foreign law, science, art, handwriting, fingerprints, DNA",
                "Expert OPINION is RELEVANT but not binding on court",
                "Court can accept or reject expert opinion",
                "Expert must be qualified and opinion must be reliable"
            ],
            "types_of_experts": [
                "Medical experts (cause of death, injury assessment)",
                "Forensic experts (fingerprints, DNA, ballistics)",
                "Handwriting experts (questioned documents)",
                "Cyber forensic experts (electronic evidence)",
                "Valuation experts (property valuation)"
            ],
            "weight_of_evidence": "Expert opinion is advisory. Court is final arbiter of fact and can disagree with expert if other evidence contradicts."
        },
        "presumption_of_innocence": {
            "title": "Presumption of Innocence",
            "definition": "Fundamental principle that accused is presumed innocent until proven guilty by prosecution beyond reasonable doubt.",
            "key_elements": [
                "Constitutional basis: Article 20(3) - Right against self-incrimination",
                "International: UDHR Article 11, ICCPR Article 14(2)",
                "Burden of proof on PROSECUTION, not accused",
                "Standard: BEYOND REASONABLE DOUBT",
                "If prosecution fails to prove, accused must be acquitted",
                "Benefit of doubt goes to accused"
            ],
            "legal_effect": [
                "Accused need not prove innocence",
                "Prosecution must prove every element of offence",
                "Doubt must be reasonable, not imaginary",
                "Acquittal if prosecution case has gaps",
                "Bail is rule, jail is exception (Supreme Court)"
            ],
            "landmark_case": "Kali Ram v. State of Himachal Pradesh (1973) - Prosecution must prove guilt, not accused prove innocence"
        },
        "dying_declaration": {
            "title": "Dying Declaration (Evidence Act Section 32)",
            "definition": "Statement made by a person as to the cause of death or circumstances of the transaction resulting in death, when the person is dead. Under Section 32 of the Indian Evidence Act.",
            "section": "Evidence Act Section 32(1)",
            "key_elements": [
                "Section 32 of Evidence Act - Statement of person who cannot be called as witness",
                "Statement by person who is dead about cause of death",
                "About cause of death OR circumstances of transaction causing death",
                "Declarant need not be under expectation of death (unlike English law)",
                "Can be oral, written, or by gestures",
                "Can be SOLE BASIS for conviction if reliable and voluntary",
                "Must be recorded by Magistrate preferably (but not mandatory)"
            ],
            "requirements": [
                "Declarant must be competent at time of statement",
                "Statement must relate to cause/circumstances of death",
                "Statement must be voluntary (not induced)",
                "Declarant must be in fit state to make statement",
                "Identity of accused must be clear"
            ],
            "sole_evidence_rule": [
                "YES - Dying declaration CAN BE SOLE EVIDENCE for conviction",
                "Supreme Court: Reliable dying declaration sufficient",
                "No corroboration needed if court satisfied of truthfulness",
                "But court must scrutinize carefully",
                "Multiple dying declarations: Prefer consistent one"
            ],
            "evidentiary_value": [
                "Can be sole basis for conviction if reliable",
                "Medical opinion on fitness to make statement is relevant",
                "Corroboration preferred but not mandatory",
                "If multiple dying declarations, consistent one preferred",
                "Court must scrutinize carefully if inconsistent"
            ],
            "landmark_case": "Laxman v. State of Maharashtra (2002) - Dying declaration can be sole basis for conviction"
        },
        "confession_evidence": {
            "title": "Confession to Police - Sections 25, 26, 27",
            "definition": "A confession is an admission of guilt by an accused person. Confession to police officer is INADMISSIBLE under Section 25 of Indian Evidence Act.",
            "section": "Evidence Act Sections 24-30",
            "key_elements": [
                "Section 24: Confession by inducement/threat/promise is irrelevant",
                "Section 25: Confession to POLICE OFFICER is INADMISSIBLE",
                "Section 26: Confession in police custody inadmissible (except Section 27)",
                "Section 27: Only discovery of facts from confession admissible",
                "Section 164 CrPC: Confession before MAGISTRATE is admissible"
            ],
            "section_25_rule": [
                "Confession to POLICE OFFICER is INADMISSIBLE",
                "Reason: Prevent torture and coercion by police",
                "No matter how voluntary, confession to police is excluded",
                "Police includes railway police, customs officers with police powers",
                "This is absolute rule - no exceptions"
            ],
            "what_is_admissible": [
                "Confession before Magistrate (Section 164 CrPC) - admissible",
                "Confession before court during trial - admissible",
                "Extra-judicial confession (to private person) - weak but admissible",
                "Discovery of facts from confession (Section 27) - admissible"
            ],
            "what_is_inadmissible": [
                "Confession to police officer - Section 25 - INADMISSIBLE",
                "Confession while in police custody - Section 26 - INADMISSIBLE",
                "Confession obtained by inducement/threat/promise - Section 24",
                "Confession in narco-analysis/polygraph/brain mapping"
            ],
            "landmark_case": "Selvi v. State of Karnataka (2010) - Narco-analysis results inadmissible"
        },
        "electronic_evidence": {
            "title": "Electronic Evidence (Section 65B)",
            "definition": "Section 65B lays down conditions for admissibility of electronic records as evidence.",
            "section": "Evidence Act Section 65B",
            "key_elements": [
                "Electronic record is admissible if conditions of 65B are met",
                "65B(4) certificate is MANDATORY for secondary electronic evidence",
                "Certificate must be signed by person in charge of device",
                "Must certify: Computer was regularly used, data was regularly fed, computer was operating properly",
                "Original electronic record doesn't need certificate"
            ],
            "requirements_for_65b_certificate": [
                "Identify the electronic record",
                "Describe the manner of production",
                "Give particulars of device used",
                "Certify compliance with conditions",
                "Signed by responsible person"
            ],
            "types_of_electronic_evidence": [
                "Emails and attachments",
                "CCTV footage",
                "Call records (CDR)",
                "WhatsApp/social media messages",
                "Bank transaction records",
                "Computer files and documents"
            ],
            "landmark_case": "Arjun Panditrao Khotkar v. Kailash Kushanrao (2020) - 65B certificate mandatory"
        },
        
        # =============== EDGE CASES ===============
        "juvenile_justice": {
            "title": "Juvenile Justice - Trial of Minors",
            "definition": "Children in conflict with law are dealt with under Juvenile Justice (Care and Protection of Children) Act, 2015.",
            "key_elements": [
                "Child: Person below 18 years of age",
                "JJB (Juvenile Justice Board): Special board for juvenile cases",
                "NOT tried in regular criminal courts",
                "Maximum period in special home: 3 years",
                "Exception: Children 16-18 for HEINOUS offences CAN be tried as adults",
                "Heinous offence: Minimum punishment 7+ years"
            ],
            "procedure": [
                "1. Apprehension (not arrest) by Special Juvenile Police Unit",
                "2. Produced before JJB within 24 hours",
                "3. Preliminary assessment by JJB",
                "4. If 16-18 and heinous: JJB assesses if to be tried as adult",
                "5. Inquiry completed within 4 months",
                "6. Rehabilitation, not punishment is focus"
            ],
            "can_minor_be_tried_as_adult": [
                "ONLY if child is 16-18 years old",
                "ONLY for heinous offence (min 7+ years punishment)",
                "JJB must conduct preliminary assessment",
                "JJB examines mental/physical capacity, circumstances",
                "If transferred to Children's Court, tried like adult",
                "But NO DEATH PENALTY or LIFE IMPRISONMENT"
            ],
            "landmark_case": "Nirbhaya case led to 2015 amendment allowing 16-18 trial as adults for heinous crimes"
        },
        "plea_bargaining": {
            "title": "Plea Bargaining (CrPC Chapter XXIA)",
            "definition": "Plea bargaining allows accused to plead guilty in exchange for lesser punishment, avoiding full trial.",
            "section": "CrPC Chapter XXIA (Sections 265A-265L)",
            "key_elements": [
                "Introduced in 2006 amendment to CrPC",
                "Accused voluntarily pleads guilty for lesser sentence",
                "Court awards minimum punishment or less",
                "Victim may receive compensation",
                "NOT available for: Death penalty, life imprisonment, 7+ years imprisonment",
                "NOT available for: Offences against women, children under 14"
            ],
            "procedure_overview": [
                "1. Accused files application for plea bargaining",
                "2. Court examines if voluntary (in camera)",
                "3. Notice to prosecution and victim",
                "4. Mutually satisfactory disposition worked out",
                "5. Court awards minimum sentence or below",
                "6. Victim may get compensation from accused"
            ],
            "benefits": [
                "Quick disposal of case",
                "Reduced sentence for accused",
                "Compensation for victim",
                "Reduced burden on courts",
                "Finality - no appeal against conviction"
            ],
            "excluded_offences": [
                "Offences punishable with death",
                "Offences punishable with life imprisonment",
                "Offences punishable with imprisonment above 7 years",
                "Offences affecting socio-economic conditions",
                "Offences against women",
                "Offences against children below 14"
            ]
        },
        "suicide_legality": {
            "title": "Is Suicide Illegal in India?",
            "definition": "Attempt to suicide was decriminalized by Mental Healthcare Act, 2017, which effectively nullified Section 309 IPC.",
            "key_elements": [
                "Section 309 IPC: Attempt to suicide - Up to 1 year imprisonment",
                "Mental Healthcare Act, 2017 Section 115: Presumes severe stress",
                "MHCA overrides Section 309 IPC",
                "Attempt to suicide now NOT punishable (effectively decriminalized)",
                "Person must receive care and rehabilitation, not prosecution",
                "Abetment to suicide (Section 306 IPC) is still criminal offence"
            ],
            "current_legal_position": [
                "Attempt to suicide is NOT a crime after MHCA 2017",
                "Person who attempts suicide shall not be punished",
                "Presumption of severe stress unless proved otherwise",
                "Government must provide care and rehabilitation",
                "Abetting/encouraging suicide is still criminal (Section 306)",
                "Dowry-related suicide abetment is Section 304B"
            ],
            "landmark_case": "P. Rathinam v. Union of India (1994) initially struck down 309, later reversed, finally MHCA 2017 settled issue"
        },
        "compoundable_offences": {
            "title": "Compoundable Offences",
            "definition": "Offences that can be settled between complainant and accused without trial, with or without court's permission.",
            "key_elements": [
                "Section 320 CrPC: Lists compoundable offences",
                "Two types: Without court permission / With court permission",
                "Victim and accused reach settlement",
                "Case closed, accused discharged",
                "Serious offences like murder, rape are NOT compoundable"
            ],
            "without_court_permission": [
                "Simple hurt (Section 323)",
                "Wrongful restraint (Section 341)",
                "Criminal trespass (Section 447)",
                "Defamation (Section 500)",
                "Insult provoking breach of peace (Section 504)"
            ],
            "with_court_permission": [
                "Voluntarily causing hurt by weapon (Section 324)",
                "Grievous hurt (Section 325)",
                "Theft (Section 379)",
                "Cheating (Section 417)",
                "Mischief (Section 426)"
            ],
            "non_compoundable": [
                "Murder, Rape, Dacoity, Robbery",
                "POCSO offences",
                "Offences against State",
                "Section 498A (Cruelty) - Generally not compoundable"
            ]
        },
        "hostile_witness": {
            "title": "Hostile Witness",
            "definition": "A witness who turns hostile by giving evidence contrary to the party who called them.",
            "key_elements": [
                "Witness changes statement from earlier recorded statement",
                "Party calling witness can seek court's permission to cross-examine",
                "Court declares witness 'hostile'",
                "Cross-examination allowed to discredit witness",
                "Earlier statement (Section 161) can be used to contradict",
                "Hostile witness testimony not automatically rejected"
            ],
            "procedure": [
                "1. Witness gives contradictory evidence",
                "2. Party seeks permission to treat witness as hostile",
                "3. Court examines and grants permission",
                "4. Cross-examination of own witness allowed",
                "5. Earlier statement put to witness",
                "6. Court evaluates credibility"
            ],
            "evidentiary_value": "Hostile witness testimony is not rejected outright. Court can rely on part of statement if corroborated by other evidence."
        },
        "narco_test": {
            "title": "Narco-Analysis, Polygraph, Brain Mapping",
            "definition": "Scientific interrogation techniques that cannot be conducted without accused's consent due to Article 20(3).",
            "key_elements": [
                "Narco-Analysis: Injecting 'truth serum' to extract information",
                "Polygraph: Lie detector test measuring physiological responses",
                "Brain Mapping (P300/BEOS): Measuring brain activity",
                "ALL require INFORMED CONSENT of accused",
                "Results are INADMISSIBLE as evidence if without consent",
                "Any information obtained is inadmissible under Article 20(3)"
            ],
            "legal_position": [
                "Violate Article 20(3) - Right against self-incrimination",
                "Cannot be compelled even by court order",
                "Voluntary consent with legal representation required",
                "Results not reliable scientific evidence",
                "Any discovery from involuntary test is inadmissible"
            ],
            "landmark_case": "Selvi v. State of Karnataka (2010) - All three tests require consent, results inadmissible without consent"
        },
        "blood_sample_examination": {
            "title": "Medical Examination and Blood Sample (Section 53 CrPC)",
            "definition": "Section 53 CrPC allows a registered medical practitioner to examine an accused person at the request of a police officer if there are reasonable grounds.",
            "section": "CrPC Section 53, 53A",
            "key_elements": [
                "Section 53: Medical examination of accused person",
                "Section 53A: Examination of person accused of rape",
                "Police can request medical examination including blood sample",
                "Must be conducted by registered medical practitioner",
                "DNA test can be ordered by court",
                "Accused CAN be compelled - this is NOT self-incrimination"
            ],
            "can_accused_be_compelled": [
                "YES - Accused CAN BE COMPELLED to give blood sample",
                "Blood/DNA is physical evidence, not testimonial",
                "Article 20(3) protects against TESTIMONIAL compulsion",
                "Physical evidence (blood, hair, DNA) is NOT protected",
                "Court can order blood sample for paternity, rape cases",
                "Refusal can lead to adverse inference"
            ],
            "consent_not_required": [
                "Unlike narco tests, blood sample doesn't need consent",
                "2005 Amendment added Section 53A for rape cases",
                "Reasonable force can be used if accused refuses",
                "Medical practitioner must ensure minimal harm"
            ],
            "landmark_case": "State of Bombay v. Kathi Kalu Oghad (1961) - Physical evidence not protected by Article 20(3)"
        },
        "insanity_defense": {
            "title": "Insanity Defense - Section 84 IPC",
            "definition": "Nothing is an offence which is done by a person who, at the time of doing it, by reason of unsoundness of mind, is incapable of knowing the nature of the act or that it is wrong or contrary to law.",
            "section": "IPC Section 84",
            "key_elements": [
                "Section 84 IPC: Act of a person of unsound mind",
                "Legal test of insanity: McNaughten Rules",
                "Must prove unsoundness of mind AT TIME of act",
                "Must prove incapacity to know nature of act",
                "OR incapacity to know it was wrong/contrary to law",
                "Burden of proving insanity is on ACCUSED"
            ],
            "mcnaughten_test": [
                "Accused must have mental disease at time of act",
                "Disease must cause defect of reason",
                "Must not know NATURE and QUALITY of act",
                "OR must not know act was WRONG or contrary to law",
                "Knowledge of wrongness judged by legal standards"
            ],
            "if_accused_mentally_ill": [
                "If proved insane: ACQUITTAL on ground of insanity",
                "Court may order detention in mental hospital",
                "Detention until fit to be released",
                "If unfit for trial: Trial suspended, treatment ordered",
                "Regular review of mental condition required"
            ],
            "burden_of_proof": [
                "Burden on ACCUSED to prove insanity",
                "Presumption of sanity exists",
                "Standard: Preponderance of probability",
                "Medical evidence crucial but not conclusive",
                "Court evaluates all circumstances"
            ],
            "landmark_case": "Hari Singh Gond v. State of MP (2008) - McNaughten Rules applied in India"
        },
        "judge_as_witness": {
            "title": "Judge as Witness - Competency Under Evidence Act",
            "definition": "Under the Indian Evidence Act, all persons are competent to testify as witnesses, including judges. However, there are restrictions on judges testifying about their own court proceedings.",
            "section": "Evidence Act Section 118, 121",
            "key_elements": [
                "Section 118: All persons are competent witnesses",
                "Section 121: No judge can be compelled to answer about conduct in court",
                "Judge CAN be witness on matters outside court proceedings",
                "Judge CANNOT be compelled to testify about own case proceedings",
                "Protection extends to conduct while acting judicially"
            ],
            "can_judge_be_witness": [
                "YES - Judge CAN BE a competent witness under Section 118",
                "Evidence Act considers all persons competent",
                "Judge can testify about facts seen/heard outside court",
                "Judge can give evidence in personal capacity"
            ],
            "what_judge_cannot_be_compelled_to_answer": [
                "Conduct of judge as judge in court proceedings (Section 121)",
                "Reasons for decisions in cases",
                "What happened in chambers/deliberations",
                "Matters protected by judicial privilege"
            ],
            "related": "Magistrate recording dying declaration can be witness to verify authenticity"
        },
        "emergency_fundamental_rights": {
            "title": "Fundamental Rights During Emergency",
            "definition": "During a National Emergency under Article 352, certain fundamental rights can be suspended. However, Article 20 and 21 CANNOT be suspended.",
            "section": "Article 352, 358, 359",
            "key_elements": [
                "Article 352: National Emergency proclamation",
                "Article 358: Suspension of Article 19 during emergency",
                "Article 359: Suspension of other rights by Presidential Order",
                "Article 20 and 21 can NEVER be suspended (44th Amendment)",
                "Only during emergency 'on ground of war or external aggression' for Art 19"
            ],
            "can_fundamental_rights_be_suspended": [
                "Article 19 freedoms: AUTOMATICALLY SUSPENDED during external emergency",
                "Other fundamental rights: CAN BE SUSPENDED by Presidential Order",
                "Article 20: CANNOT be suspended (protection against conviction)",
                "Article 21: CANNOT be suspended (right to life and liberty)",
                "44th Amendment made Article 20 and 21 non-suspendable"
            ],
            "historical_context": [
                "ADM Jabalpur case (1976): SC held rights suspended during emergency",
                "44th Amendment (1978): Protected Article 20 and 21 from suspension",
                "Internal disturbance no longer ground for Article 19 suspension"
            ],
            "landmark_case": "ADM Jabalpur v. Shivkant Shukla (1976) - Later effectively overruled by 44th Amendment"
        },
        "pardon_remission": {
            "title": "Difference Between Pardon, Reprieve, Remission, Commutation",
            "definition": "Presidential powers under Article 72 (Governor under Article 161) to grant mercy in criminal cases.",
            "key_elements": [
                "PARDON: Complete acquittal - Offence and conviction wiped out",
                "REPRIEVE: Temporary suspension of sentence (especially death penalty)",
                "REMISSION: Reducing sentence duration without changing nature",
                "COMMUTATION: Substituting lesser form of punishment",
                "RESPITE: Lesser sentence due to special reasons (pregnancy, illness)"
            ],
            "article_72_vs_161": {
                "article_72": "President - Court martial, Union law, death sentence",
                "article_161": "Governor - State law matters, cannot pardon death sentence"
            },
            "procedure": [
                "1. Convict or family files mercy petition",
                "2. Home Ministry examines petition",
                "3. President/Governor decides on advice of Council",
                "4. Decision is final but subject to judicial review",
                "5. Delay in deciding mercy can be ground for commutation"
            ],
            "landmark_case": "Shatrughan Chauhan v. Union of India (2014) - Inordinate delay in mercy petition can commute death to life"
        },
        "double_jeopardy": {
            "title": "Double Jeopardy - Article 20(2)",
            "definition": "No person shall be prosecuted and punished for the same offence more than once.",
            "key_elements": [
                "Article 20(2) of Constitution",
                "Protects against second prosecution for SAME OFFENCE",
                "Must have been prosecuted AND punished earlier",
                "Acquittal also protects against re-prosecution",
                "Different offences from same act can be prosecuted",
                "Departmental action alongside criminal action is allowed"
            ],
            "scope": [
                "Applies only to 'same offence'",
                "Previous prosecution must have been by 'court or tribunal'",
                "Departmental inquiry is not 'prosecution'",
                "Appeal by State against acquittal is allowed",
                "Retrial on appeal or revision is allowed"
            ],
            "landmark_case": "Maqbool Hussain v. State of Bombay (1953) - Customs proceeding is not 'prosecution'"
        },
        
        # =============== ADDITIONAL CONSTITUTIONAL ARTICLES ===============
        "article_15": {
            "title": "Article 15: Prohibition of Discrimination",
            "definition": "The State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth.",
            "key_elements": [
                "Prohibits discrimination by State (not private individuals for Art 15(1))",
                "Grounds: Religion, Race, Caste, Sex, Place of birth",
                "Article 15(2): No discrimination in access to public places",
                "Article 15(3): Special provisions for women and children allowed",
                "Article 15(4): Special provisions for SC/ST/backward classes allowed",
                "Article 15(5): Reservation in educational institutions"
            ],
            "vs_article_14": "Article 14 is general equality. Article 15 prohibits specific grounds of discrimination.",
            "landmark_case": "State of Madras v. Champakam Dorairajan (1951) - Communal reservation struck down"
        },
        "article_16": {
            "title": "Article 16: Equality of Opportunity in Public Employment",
            "definition": "There shall be equality of opportunity for all citizens in matters relating to employment or appointment to any office under the State.",
            "key_elements": [
                "Equality in public employment matters",
                "No discrimination on grounds of religion, race, caste, sex, descent, place of birth, residence",
                "Article 16(4): Reservation for backward classes",
                "Article 16(4A): Reservation in promotion for SC/ST",
                "Article 16(4B): Carry forward unfilled vacancies",
                "Reservation limit: 50% (Indra Sawhney case)"
            ],
            "important_points": [
                "Applies only to PUBLIC employment under State",
                "Residence requirement can be prescribed for some posts",
                "Backward class reservation must be based on data"
            ],
            "landmark_case": "Indra Sawhney v. Union of India (1992) - 50% ceiling, creamy layer, no reservation in promotion"
        },
        "article_17": {
            "title": "Article 17: Abolition of Untouchability",
            "definition": "'Untouchability' is abolished and its practice in any form is forbidden. The enforcement of any disability arising out of 'Untouchability' shall be an offence punishable in accordance with law.",
            "key_elements": [
                "Complete abolition of untouchability",
                "Practice of untouchability is a criminal offence",
                "Enforceable against State AND private individuals",
                "Protection of Civil Rights Act, 1955 (formerly Untouchability Offences Act)",
                "SC/ST Prevention of Atrocities Act, 1989",
                "Only Fundamental Right directly enforceable against private persons"
            ],
            "punishment": [
                "Prevention of Civil Rights Act: Up to 6 months + fine",
                "SC/ST Atrocities Act: More severe punishments",
                "Denying access to public places is punishable"
            ]
        },
        "article_24": {
            "title": "Article 24: Prohibition of Employment of Children",
            "definition": "No child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment.",
            "key_elements": [
                "Absolute prohibition for children below 14 years",
                "Covers: Factories, Mines, Hazardous employment",
                "Child Labour (Prohibition and Regulation) Act, 1986",
                "2016 Amendment: Complete ban on child labour below 14",
                "Adolescents (14-18): Prohibited in hazardous occupations",
                "Violation is criminal offence with imprisonment"
            ],
            "related_laws": [
                "Child Labour (Prohibition and Regulation) Act, 1986",
                "Factories Act, 1948",
                "Mines Act, 1952",
                "POCSO Act for child exploitation"
            ]
        },
        "article_29": {
            "title": "Article 29: Protection of Interests of Minorities",
            "definition": "Any section of citizens having a distinct language, script or culture have the right to conserve the same.",
            "key_elements": [
                "Right to conserve distinct language, script, culture",
                "Available to ANY section of citizens (not just religious minorities)",
                "Linguistic and cultural minorities protected",
                "Article 29(2): No denial of admission to educational institutions on grounds of religion, race, caste, language"
            ],
            "landmark_case": "T.M.A. Pai Foundation v. State of Karnataka (2002) - Minority status determined state-wise"
        },
        "article_30": {
            "title": "Article 30: Right of Minorities to Establish Educational Institutions",
            "definition": "All minorities, whether based on religion or language, shall have the right to establish and administer educational institutions of their choice.",
            "key_elements": [
                "Right to ESTABLISH educational institutions",
                "Right to ADMINISTER educational institutions",
                "Applies to religious AND linguistic minorities",
                "State can regulate but not destroy minority character",
                "Minorities can claim aid but State can impose conditions"
            ],
            "vs_article_29": "Article 29 is cultural protection. Article 30 is educational institution protection.",
            "landmark_case": "St. Stephen's College v. University of Delhi (1992) - Minority institutions can prefer their community"
        },
        "article_51a": {
            "title": "Article 51A: Fundamental Duties",
            "definition": "It shall be the duty of every citizen of India (11 duties added by 42nd Amendment, 1976).",
            "key_elements": [
                "Added by 42nd Amendment, 1976 (10 duties)",
                "11th duty added by 86th Amendment, 2002",
                "Not enforceable in court (non-justiciable)",
                "Meant to be moral obligations",
                "Can be considered in interpreting laws"
            ],
            "duties": [
                "1. Abide by Constitution, respect Flag and National Anthem",
                "2. Cherish noble ideals of freedom struggle",
                "3. Uphold sovereignty, unity and integrity of India",
                "4. Defend the country and render national service",
                "5. Promote harmony and brotherhood",
                "6. Preserve rich heritage of composite culture",
                "7. Protect natural environment",
                "8. Develop scientific temper and humanism",
                "9. Safeguard public property and abjure violence",
                "10. Strive for excellence in all spheres",
                "11. Provide education to children aged 6-14"
            ]
        },
        
        # =============== ADDITIONAL EVIDENCE ACT CONCEPTS ===============
        "best_evidence_rule": {
            "title": "Best Evidence Rule (Section 64)",
            "definition": "Primary evidence is required - documents must be proved by the original document, not copies, unless exceptions apply.",
            "section": "Evidence Act Sections 64-66",
            "key_elements": [
                "Section 64: Documents must be proved by PRIMARY (original) evidence",
                "Primary Evidence = Original document itself",
                "Secondary Evidence = Copies, oral accounts of contents",
                "Secondary evidence allowed only in specific situations",
                "Original document preferred over copies",
                "Rule ensures authenticity and prevents fabrication"
            ],
            "when_secondary_allowed": [
                "Original is in possession of adverse party (Section 65a)",
                "Original is lost or destroyed (Section 65c)",
                "Original cannot be moved (public records, tombstones) (Section 65d)",
                "Producing original would cause unreasonable delay (Section 65e)",
                "Original is voluminous document (Section 65f)",
                "Certified copies of public documents (Section 65e)"
            ],
            "practical_application": [
                "Sale deed: Produce original registered document",
                "Contract: Produce signed original agreement",
                "Will: Produce original will document",
                "Electronic record: Section 65B certificate needed for copies"
            ],
            "landmark_case": "H. Siddiqui v. A. Ramalingam (2011) - Best evidence rule and secondary evidence"
        },
        "wife_testimony_privilege": {
            "title": "Marital Communication Privilege (Section 122)",
            "definition": "No person who is or has been married shall be compelled to disclose any communication made to them during marriage by any person to whom they are or were married.",
            "section": "Evidence Act Section 122",
            "key_elements": [
                "Section 122: Communication during marriage is privileged",
                "Spouse CANNOT BE COMPELLED to disclose marital communications",
                "Privilege survives divorce (communication during marriage protected)",
                "Wife CAN testify against husband if she VOLUNTARILY chooses",
                "Privilege belongs to the communicating spouse",
                "Exception: Civil suits between spouses"
            ],
            "what_is_protected": [
                "Communication made DURING marriage",
                "Between husband and wife",
                "Includes oral, written, or gestural communication",
                "Intention must be confidential"
            ],
            "exceptions": [
                "Suit between married persons",
                "Criminal prosecution of one spouse by other",
                "If spouse is witness in proceeding for offence against other",
                "If communication relates to crime being committed",
                "Spouse can voluntarily waive privilege"
            ],
            "can_wife_testify": [
                "YES - Wife CAN testify against husband if she VOLUNTARILY chooses",
                "NO - Wife CANNOT BE COMPELLED to disclose marital communications",
                "Exception: Suit between spouses, prosecution of one by other"
            ],
            "related_sections": "Section 120: Spouse is competent witness"
        },
        "estoppel": {
            "title": "Estoppel (Section 115)",
            "definition": "When one person has, by declaration, act or omission, intentionally caused another person to believe a thing to be true and act upon such belief, neither he nor his representative shall be allowed to deny the truth of that thing.",
            "section": "Evidence Act Section 115",
            "key_elements": [
                "Section 115: Estoppel prevents denying earlier representation",
                "One person makes representation (by words, act, or omission)",
                "Another person believes and acts on that representation",
                "Representer CANNOT later deny the truth of representation",
                "Also called 'Rule against Blowing Hot and Cold'",
                "Based on equity - no person should benefit from their own wrong"
            ],
            "requirements": [
                "Representation by one party (express or implied)",
                "Representation of fact (not law or opinion)",
                "Belief by other party in that representation",
                "Action by other party based on that belief",
                "Resulting prejudice if denial allowed"
            ],
            "types_of_estoppel": [
                "Estoppel by Record: Previous court judgment binds parties",
                "Estoppel by Deed: Parties bound by recitals in deed",
                "Estoppel by Conduct: Prevented from denying conduct-based representations",
                "Promissory Estoppel: Promises inducing action are binding",
                "Estoppel by Negligence: Duty to speak but kept silent"
            ],
            "example": "If landlord accepts rent from tenant, cannot deny tenancy later",
            "landmark_case": "Motilal Padampat v. State of UP (1979) - Promissory estoppel against government"
        },
        "judicial_notice": {
            "title": "Judicial Notice (Sections 56 & 57)",
            "definition": "Facts of which the court will take notice without requiring proof. Court assumes certain facts are true without formal evidence.",
            "section": "Evidence Act Sections 56-57",
            "key_elements": [
                "Section 56: Facts judicially noticed need not be proved",
                "Section 57: Lists facts court SHALL take judicial notice of",
                "Court assumes certain notorious/established facts are true",
                "No formal proof required for judicially noticed facts",
                "Saves time by not proving obvious matters"
            ],
            "facts_judicially_noticed_section_57": [
                "All laws in force in India",
                "Course of proceedings in Parliament/State Legislature",
                "Accession of present monarch, Rajpramukh",
                "Seals of courts, public offices, official signatures",
                "Divisions of time, geographical divisions",
                "Territorial extent of State jurisdiction",
                "Commencement, continuance, termination of war",
                "Public fasts and holidays",
                "Ordinary course of nature",
                "Meaning of English words and legal terms"
            ],
            "examples": [
                "Sun rises in East - Ordinary course of nature",
                "Delhi is capital of India - Geographical fact",
                "Republic Day is January 26 - Public holiday",
                "Murder is punishable - All laws in force",
                "Meaning of 'murder' - English words"
            ],
            "practical_importance": [
                "Saves judicial time",
                "No need to prove obvious facts",
                "Court can refer to materials to refresh memory",
                "If court denies notice, fact must be proved normally"
            ]
        },
        "res_gestae": {
            "title": "Res Gestae (Section 6)",
            "definition": "Facts which are so connected with the fact in issue that they form part of the same transaction are admissible as Res Gestae. These are spontaneous statements made contemporaneously with the event.",
            "section": "Evidence Act Section 6",
            "key_elements": [
                "Section 6: Facts forming part of same transaction are relevant",
                "Latin: 'Things done' or 'things transacted'",
                "Exception to hearsay rule",
                "Statements must be CONTEMPORANEOUS (at same time)",
                "Must be SPONTANEOUS (not deliberate)",
                "Part of the same continuous transaction",
                "No time for concoction or fabrication"
            ],
            "requirements_for_admissibility": [
                "Statement made at or about time of act",
                "Statement and act are substantially contemporaneous",
                "Statement made by participant or spectator",
                "Statement is spontaneous and unreflecting",
                "No time for deliberation or fabrication"
            ],
            "examples": [
                "Victim screaming 'A stabbed me!' immediately after stabbing",
                "Eyewitness shouting identification of robber during robbery",
                "Dying person's immediate accusation of attacker",
                "Statements made in course of fight about cause"
            ],
            "difference_from_dying_declaration": [
                "Res Gestae: Statement during event (declarant may survive)",
                "Dying Declaration: Statement by person who dies later",
                "Res Gestae: Spontaneity is key requirement",
                "Dying Declaration: Expectation of death not required in India"
            ],
            "admissible_as_evidence": [
                "YES - Res Gestae statements ARE ADMISSIBLE",
                "Exception to hearsay rule due to spontaneity",
                "Reliability presumed due to no time for fabrication",
                "Can be sole basis for conviction if reliable"
            ],
            "landmark_case": "Rattan v. The Queen (1972) - Leading case on res gestae"
        },
        "burden_of_proof": {
            "title": "Burden of Proof (Section 101-106)",
            "definition": "The obligation to prove a fact lies on the party who asserts it. In criminal cases, prosecution must prove guilt beyond reasonable doubt.",
            "section": "Evidence Act Sections 101-106",
            "key_elements": [
                "Section 101: Burden on party who would fail without proving",
                "Section 102: Burden on party who desires court to believe",
                "Section 103: Burden of proof as to particular fact",
                "Section 105: Burden of proving exceptions on accused",
                "Section 106: Burden of proving fact especially within knowledge",
                "Criminal: Prosecution must prove beyond reasonable doubt",
                "Civil: Party asserting must prove on preponderance of probability"
            ],
            "in_criminal_cases": [
                "Prosecution bears burden of proving GUILT",
                "Standard: BEYOND REASONABLE DOUBT",
                "Accused presumed innocent until proven guilty",
                "Exception: If accused claims self-defense, burden on accused",
                "Exception: Facts especially within accused's knowledge",
                "Accused need not prove innocence"
            ],
            "in_civil_cases": [
                "Party who asserts must prove",
                "Standard: PREPONDERANCE OF PROBABILITY (51%)",
                "Balance of probabilities - more likely than not",
                "Plaintiff must prove case, then defendant responds"
            ],
            "section_105_exceptions": [
                "If accused claims insanity (Section 84 IPC)",
                "If accused claims private defense (Sections 96-106 IPC)",
                "If accused claims intoxication (Section 85 IPC)",
                "Accused must prove exception applies"
            ],
            "landmark_case": "Kali Ram v. State of HP (1973) - Prosecution must prove beyond reasonable doubt"
        },
        "hearsay_evidence": {
            "title": "Hearsay Evidence",
            "definition": "Hearsay is evidence not based on personal knowledge of witness but on what they heard from others. Generally INADMISSIBLE.",
            "section": "Evidence Act Section 60",
            "key_elements": [
                "Section 60: Oral evidence must be DIRECT",
                "Hearsay = What witness heard from someone else",
                "Generally INADMISSIBLE as evidence",
                "Reason: Cannot cross-examine original source",
                "Reason: Risk of distortion, fabrication",
                "Exception: If original declarant unavailable"
            ],
            "why_inadmissible": [
                "Cannot test truthfulness by cross-examination",
                "Cannot assess demeanor of original speaker",
                "Risk of misunderstanding, distortion",
                "Risk of fabrication or exaggeration",
                "Not reliable as direct evidence"
            ],
            "exceptions_to_hearsay": [
                "Dying Declaration (Section 32) - Statement by dead person",
                "Res Gestae (Section 6) - Contemporaneous statements",
                "Admission/Confession (Sections 17-31) - Statement against interest",
                "Public Documents (Section 74-76) - Official records",
                "Expert Reports (Section 45) - Based on specialized knowledge",
                "Previous Statement to refresh memory (Section 159)"
            ],
            "example": [
                "Witness says: 'A told me that B killed C' = HEARSAY (inadmissible)",
                "Witness says: 'I saw B kill C' = DIRECT EVIDENCE (admissible)",
                "Exception: If A is dead, A's statement may be admissible under Section 32"
            ],
            "landmark_case": "Subramaniam v. Public Prosecutor (1956) - Classic hearsay rule explanation"
        },
        "circumstantial_evidence": {
            "title": "Circumstantial Evidence",
            "definition": "Indirect evidence proving facts through inference. A chain of circumstances from which guilt can be inferred.",
            "section": "Not specifically defined in Evidence Act",
            "key_elements": [
                "Indirect proof - not eyewitness testimony",
                "Chain of circumstances leading to conclusion",
                "Each circumstance must be proved beyond reasonable doubt",
                "Chain must be complete - no missing links",
                "Circumstances must point only to guilt",
                "No reasonable hypothesis of innocence"
            ],
            "requirements_for_conviction": [
                "Circumstances must be proved, not assumed",
                "Circumstances must be consistent with guilt",
                "Circumstances must be inconsistent with innocence",
                "Chain must be complete and unbroken",
                "Hypothesis of guilt must be the only reasonable one",
                "No other reasonable explanation possible"
            ],
            "examples": [
                "Motive + Opportunity + Recovery of weapon = Circumstantial",
                "Last seen together + Enmity + Absconding = Circumstantial",
                "DNA match + Fingerprints + No alibi = Circumstantial"
            ],
            "difference_from_direct": [
                "Direct: Eyewitness testimony of actual crime",
                "Circumstantial: Inference from surrounding facts",
                "Both can be basis for conviction",
                "Circumstantial requires complete chain"
            ],
            "can_convict_on_circumstantial": [
                "YES - Conviction possible on circumstantial evidence ALONE",
                "But chain must be complete",
                "Must exclude reasonable hypothesis of innocence",
                "Strong circumstantial evidence can outweigh weak direct evidence"
            ],
            "landmark_case": "Sharad Birdichand Sarda v. State of Maharashtra (1984) - Five golden principles for circumstantial evidence"
        },
        "expert_evidence": {
            "title": "Expert Evidence (Section 45)",
            "definition": "Opinion of experts on foreign law, science, art, handwriting, or finger impressions is relevant and admissible.",
            "section": "Evidence Act Section 45",
            "key_elements": [
                "Section 45: Expert opinion is relevant fact",
                "Expert: Person with special knowledge, skill, or experience",
                "Areas: Foreign law, Science, Art, Handwriting, Fingerprints",
                "Opinion must be based on expert's specialized knowledge",
                "Expert must be qualified in the relevant field",
                "Court not bound by expert opinion - evaluates independently"
            ],
            "types_of_experts": [
                "Medical experts - Cause of death, injury analysis",
                "Forensic experts - DNA, fingerprints, ballistics",
                "Handwriting experts - Document examination",
                "Financial experts - Fraud, accounting matters",
                "IT experts - Cyber crimes, electronic evidence",
                "Psychiatrists - Mental condition of accused"
            ],
            "when_expert_evidence_admissible": [
                "Matters requiring specialized knowledge",
                "Scientific questions beyond ordinary knowledge",
                "Foreign law determination",
                "Handwriting or signature comparison",
                "Fingerprint identification",
                "Medical questions - injury, cause of death"
            ],
            "evidentiary_value": [
                "Expert opinion is advisory, not binding on court",
                "Court can accept, reject, or modify expert opinion",
                "Multiple expert opinions: Court decides weight",
                "Expert must give reasons for opinion",
                "Cross-examination of expert is important"
            ],
            "landmark_case": "State of HP v. Jai Lal (1999) - Court not bound by expert opinion"
        },
        # NEW ENHANCED PRACTICAL SCENARIOS
        "private_defense": {
            "title": "Right of Private Defense (Sections 96-106 IPC)",
            "definition": "IPC Sections 96-106 provide the right of private defense. Section 100 specifically allows causing death in self-defense when there is reasonable apprehension of death or grievous hurt.",
            "section": "IPC Sections 96-106, especially Section 100",
            "key_elements": [
                "Section 96: Nothing is an offence done in exercise of right of private defense",
                "Section 97: Right extends to defense of body and property",
                "Section 100: Right to cause DEATH in self-defense is allowed when:",
                "  - Assault causes reasonable apprehension of death",
                "  - Assault causes reasonable apprehension of grievous hurt",
                "  - Assault with intention of rape, kidnapping, or acid attack",
                "Force used must be PROPORTIONATE to threat",
                "Right is available only when State protection is not available"
            ],
            "conditions_for_section_100": [
                "1. Reasonable apprehension of DEATH to self",
                "2. Reasonable apprehension of GRIEVOUS HURT",
                "3. Assault with intention of committing rape",
                "4. Assault with intention of kidnapping or abduction",
                "5. Assault with intention of wrongful confinement",
                "6. Assault with intention of throwing acid"
            ],
            "important_limitations": [
                "Cannot exceed force needed to repel attack",
                "Must be proportionate - cannot kill for minor attack",
                "Right ceases when threat ceases",
                "Must prove reasonable apprehension (not imagination)",
                "Cannot be used for revenge or retaliation"
            ],
            "procedural_guidance": [
                "Step 1: If attacked, use only proportionate force",
                "Step 2: Document injuries immediately (medical report)",
                "Step 3: File FIR/complaint about attack you faced",
                "Step 4: If charged, claim private defense under Section 96-106",
                "Step 5: Burden of proof: Initially on prosecution; accused must show probability"
            ],
            "landmark_case": "Darshan Singh v. State of Punjab (2010) - Proportionality in self-defense"
        },
        "domestic_violence": {
            "title": "Remedies for Domestic Violence (DV Act 2005 + IPC 498A)",
            "definition": "Victims of domestic violence have both civil remedies under the Protection of Women from Domestic Violence Act, 2005 (DV Act) and criminal remedies under IPC Section 498A.",
            "section": "DV Act 2005, IPC Section 498A",
            "key_elements": [
                "Protection of Women from Domestic Violence Act, 2005 provides:",
                "  - Protection Order (stop violence immediately)",
                "  - Residence Order (right to live in shared household)",
                "  - Monetary Relief (maintenance, compensation)",
                "  - Custody Order (for children)",
                "IPC Section 498A provides criminal punishment for cruelty",
                "Punishment under 498A: Up to 3 years imprisonment + fine"
            ],
            "types_of_violence_covered": [
                "Physical abuse - beating, slapping, hitting",
                "Sexual abuse - forced sexual intercourse, marital rape",
                "Emotional/verbal abuse - humiliation, threats, insults",
                "Economic abuse - denying money, preventing employment",
                "Dowry harassment - demand for money/property"
            ],
            "step_by_step_guidance": [
                "Step 1: Approach Protection Officer (District Women & Child Development)",
                "Step 2: File complaint under DV Act for immediate protection order",
                "Step 3: Court will issue ex-parte protection order within 3 days",
                "Step 4: For criminal action, file FIR under Section 498A at police station",
                "Step 5: Seek shelter at Protection Home if needed",
                "Step 6: Apply for maintenance under DV Act Section 20"
            ],
            "where_to_get_help": [
                "National Women Helpline: 181 (24x7)",
                "Police: 100 or Women Police Helpline 1091",
                "National Commission for Women: www.ncw.nic.in",
                "District Protection Officer (DPO)",
                "Local NGOs and legal aid centers"
            ],
            "landmark_case": "S.R. Batra v. Taruna Batra (2007) - Right to residence"
        },
        "false_fir_remedies": {
            "title": "Remedies Against False FIR (Section 482 CrPC + Anticipatory Bail)",
            "definition": "If someone files a false FIR against you, you can seek quashing under Section 482 CrPC and apply for anticipatory bail under Section 438 CrPC to prevent arrest.",
            "section": "CrPC Sections 482, 438",
            "key_elements": [
                "Section 482 CrPC: High Court can QUASH FIR to prevent abuse of process",
                "Section 438 CrPC: Anticipatory Bail - protection from arrest",
                "Section 211 IPC: Filing false case is punishable (2 years)",
                "Can also file civil suit for damages for malicious prosecution",
                "Quashing grounds: No prima facie case, charges frivolous, abuse of process"
            ],
            "step_by_step_remedies": [
                "IMMEDIATE: Apply for Anticipatory Bail (Section 438)",
                "  - File before Sessions Court or High Court",
                "  - Argue: False allegations, no ground for arrest",
                "  - Court may grant protection from arrest",
                "QUASHING: File petition under Section 482 CrPC",
                "  - File in High Court",
                "  - Argue: FIR discloses no offence / abuse of process",
                "  - Court can quash FIR if satisfied",
                "COUNTER FIR: File complaint under Section 211 IPC",
                "  - For making false charge with intent to cause injury"
            ],
            "grounds_for_quashing": [
                "FIR does not disclose any cognizable offence",
                "Allegations are absurd and inherently improbable",
                "FIR filed with malicious intent to harass",
                "Settlement/compromise in compoundable matters",
                "Continuation of case would be abuse of process"
            ],
            "anticipatory_bail_procedure": [
                "1. Draft application showing apprehension of arrest",
                "2. File before Sessions Court (first instance)",
                "3. If rejected, appeal to High Court",
                "4. Attend all hearing dates religiously",
                "5. Don't tamper with evidence or influence witnesses"
            ],
            "landmark_case": "State of Haryana v. Bhajan Lal (1992) - Grounds for quashing FIR"
        },
        # PRACTICAL SCENARIOS - Situational legal guidance
        "arrest_without_warrant": {
            "title": "Police Arrest Without Warrant (Section 41 CrPC)",
            "definition": "Police can arrest without warrant under specific conditions laid down in Section 41 of the Code of Criminal Procedure.",
            "section": "CrPC Section 41",
            "key_elements": [
                "Section 41: Police can arrest without warrant in specific conditions",
                "Condition 1: Cognizable offence committed in officer's presence",
                "Condition 2: Reasonable complaint or credible information of cognizable offence",
                "Condition 3: Reasonable suspicion of cognizable offence",
                "Condition 4: Person has property suspected to be stolen",
                "Condition 5: Person obstructs police or is a deserter",
                "Police must record reasons for arrest"
            ],
            "conditions_for_arrest": [
                "Must be for COGNIZABLE offence (serious crimes)",
                "Must have reason to believe person committed offence",
                "Arrest should be necessary (not routine)",
                "Must comply with Section 41A: Notice of appearance for minor offences"
            ],
            "rights_when_arrested": [
                "Right to know grounds of arrest",
                "Right to inform family/friend",
                "Right to legal representation",
                "Right to be produced before magistrate within 24 hours"
            ],
            "landmark_case": "Arnesh Kumar v. State of Bihar (2014) - Guidelines on arrest"
        },
        "bail_in_murder": {
            "title": "Bail in Murder Case (Non-Bailable Offence)",
            "definition": "Murder is a non-bailable offence. Bail is at court's discretion and is granted only in exceptional circumstances.",
            "section": "CrPC Section 437 (bail in non-bailable)",
            "key_elements": [
                "Murder (Section 302 IPC) is NON-BAILABLE offence",
                "Bail is NOT a matter of right - it is court's DISCRETION",
                "Court considers: nature of accusation, severity of punishment",
                "Court considers: evidence against accused",
                "Court considers: flight risk, tampering with evidence",
                "Court considers: accused's antecedents and character"
            ],
            "discretion_of_court": [
                "Court has DISCRETION to grant or refuse bail",
                "Must consider reasonable grounds to believe guilt",
                "Must consider likelihood of absconding",
                "Must consider nature and gravity of offence",
                "May impose stringent conditions"
            ],
            "how_to_apply": [
                "1. File bail application before Sessions Court",
                "2. If rejected, appeal to High Court",
                "3. Argue exceptional circumstances",
                "4. Show lack of prima facie case",
                "5. Provide sureties and bonds"
            ],
            "landmark_case": "Sanjay Chandra v. CBI (2012) - Bail principles in serious offences"
        },
        "cheating_remedies": {
            "title": "Remedies When Cheated of Money (Section 420 IPC)",
            "definition": "If someone cheats you of money, you can file FIR under Section 420 IPC (cheating) at police station. You can also file a civil suit for money recovery.",
            "section": "IPC Section 420, 406",
            "key_elements": [
                "FILE FIR: Go to police station and file FIR under Section 420 IPC",
                "Section 420 IPC: Cheating and dishonestly inducing delivery of property",
                "Punishment: Up to 7 years imprisonment + fine",
                "Section 406: Criminal breach of trust (if property was entrusted)",
                "CIVIL SUIT: File civil suit for recovery of money",
                "Can pursue BOTH criminal and civil remedies simultaneously"
            ],
            "step_by_step_procedure": [
                "Step 1: Collect all evidence (receipts, messages, bank statements)",
                "Step 2: Go to police station having jurisdiction",
                "Step 3: FILE FIR in writing under Section 420 IPC",
                "Step 4: Get FIR copy (it's your RIGHT)",
                "Step 5: If police refuse FIR, file complaint before Magistrate (Section 156(3))",
                "Step 6: FILE CIVIL SUIT for money recovery in civil court",
                "Step 7: Apply for interim orders to freeze accused's assets"
            ],
            "required_evidence": [
                "Proof of transaction (receipts, bank statements, UPI records)",
                "Proof of false representation/promise made",
                "Proof of inducement and delivery of property/money",
                "Communication records (messages, emails, call records)"
            ],
            "criminal_vs_civil": [
                "CRIMINAL: FIR under Section 420 → Punishment for accused",
                "CIVIL: Civil suit → Recovery of your money + damages",
                "You can file BOTH simultaneously"
            ],
            "landmark_case": "Hridaya Ranjan v. State of Bihar (2003) - Elements of cheating"
        },
        "police_search": {
            "title": "Police Search Without Warrant (Section 100 CrPC)",
            "definition": "Police generally need warrant to search a house, but can search without warrant under Section 165 CrPC in urgent circumstances. Section 100 CrPC governs search procedures.",
            "section": "CrPC Sections 100, 165",
            "key_elements": [
                "Section 100: General procedure for search",
                "Section 165: Search by investigating officer",
                "Generally need WARRANT from Magistrate",
                "Exception: Urgent circumstances under Section 165",
                "Consent: If owner gives consent, no warrant needed",
                "Search must be in presence of two witnesses"
            ],
            "when_no_warrant_needed": [
                "Owner/occupier gives written CONSENT",
                "Urgent circumstances - evidence may be destroyed",
                "Police believe delay will defeat purpose",
                "Must record reasons in writing"
            ],
            "your_rights": [
                "Right to see search warrant",
                "Right to presence of independent witnesses",
                "Right to receive copy of seizure memo",
                "Right to refuse consent (if no warrant)",
                "Right to lodge complaint if illegal search"
            ],
            "landmark_case": "District Registrar v. Canara Bank (2005) - Search and seizure"
        },
        "right_to_silence": {
            "title": "Right to Remain Silent (Article 20(3))",
            "definition": "Under Article 20(3) of the Constitution, no person accused of any offence shall be compelled to be a witness against himself. This protects against self-incrimination.",
            "section": "Article 20(3) Constitution",
            "key_elements": [
                "Article 20(3): Protection against self-incrimination",
                "Right to remain silent during interrogation",
                "Cannot be compelled to give self-incriminating statement",
                "Applies only to ACCUSED person (not witnesses)",
                "Compelled testimony is inadmissible",
                "Right available at all stages - investigation and trial"
            ],
            "what_it_protects": [
                "Cannot be forced to confess",
                "Cannot be forced to answer incriminating questions",
                "Cannot be penalized for silence",
                "Silence cannot be used as evidence of guilt"
            ],
            "limitations": [
                "Can be compelled to give blood samples, fingerprints",
                "Can be compelled to participate in identification parade",
                "Applies only to testimonial compulsion"
            ],
            "landmark_case": "Nandini Satpathy v. P.L. Dani (1978) - Right to silence"
        },
        "drunk_driving": {
            "title": "Drunk Driving Punishment (Motor Vehicles Act Section 185)",
            "definition": "Under Section 185 of the Motor Vehicles Act, driving under influence of alcohol is punishable with imprisonment and fine.",
            "section": "Motor Vehicles Act Section 185",
            "key_elements": [
                "Section 185 Motor Vehicles Act: Drunk driving offence",
                "Blood alcohol level: Above 30 mg per 100 ml blood",
                "First offence: Up to 6 months imprisonment OR Rs. 10,000 fine OR both",
                "Second offence: Up to 2 years imprisonment OR Rs. 15,000 fine OR both",
                "Driving license suspension: Minimum 3 months"
            ],
            "test_and_detection": [
                "Breath analyzer test by police",
                "Blood test (more accurate)",
                "Refusal to test can lead to presumption of intoxication",
                "Police can stop vehicle for checking"
            ],
            "consequences": [
                "Criminal prosecution under Section 185",
                "License suspension or cancellation",
                "If accident: Additional charges under IPC",
                "If death: Charges under Section 304A IPC (negligent death)"
            ]
        },
        "cheque_bounce": {
            "title": "Cheque Bounce (Section 138 NI Act)",
            "definition": "Under Section 138 of the Negotiable Instruments Act (NI Act), dishonour of cheque for insufficient funds is a criminal offence punishable with imprisonment up to 2 years.",
            "section": "Section 138 NI Act (Negotiable Instruments Act)",
            "key_elements": [
                "Section 138 NI Act: Cheque dishonour is criminal offence",
                "Punishment: Up to 2 years imprisonment OR twice the cheque amount as fine OR both",
                "Must be for legally enforceable debt",
                "Cheque must be presented within validity period",
                "Legal notice must be sent within 30 days of dishonour",
                "Case must be filed within 30 days of notice expiry"
            ],
            "procedure_after_bounce": [
                "Step 1: Receive 'cheque return memo' from bank",
                "Step 2: Send legal notice within 30 days to drawer",
                "Step 3: Wait 15 days for payment",
                "Step 4: If not paid, file complaint under Section 138",
                "Step 5: File in court where cheque was presented"
            ],
            "requirements_for_prosecution": [
                "Cheque issued for legally enforceable debt",
                "Cheque presented within validity period",
                "Cheque returned unpaid",
                "Notice sent within 30 days of return",
                "Complaint filed within 30 days of notice period expiry"
            ],
            "landmark_case": "Dashrath Rupsingh Rathod v. State (2014) - Jurisdiction in cheque bounce"
        },
        "online_defamation": {
            "title": "Online Defamation (IT Act + IPC)",
            "definition": "Online defamation can be prosecuted under Section 499/500 IPC (defamation) along with Section 66A IT Act (now struck down) or Section 67 IT Act for obscene content.",
            "section": "IPC Section 499/500, IT Act Section 67",
            "key_elements": [
                "IPC Section 499: Definition of defamation",
                "IPC Section 500: Punishment - 2 years or fine or both",
                "IT Act applies for cyber defamation",
                "Can file case where content was published online",
                "Both criminal and civil remedies available"
            ],
            "how_to_file_case": [
                "Step 1: Take screenshots and preserve evidence",
                "Step 2: File complaint at local police station (cyber cell)",
                "Step 3: File complaint at www.cybercrime.gov.in",
                "Step 4: File private complaint before Magistrate",
                "Step 5: File civil suit for damages and injunction"
            ],
            "remedies_available": [
                "Criminal prosecution under IPC Section 500",
                "Civil suit for damages",
                "Injunction to remove content",
                "Compensation for mental harassment"
            ],
            "landmark_case": "Shreya Singhal v. Union of India (2015) - Section 66A struck down"
        },
        "trial_duration": {
            "title": "Duration of Criminal Trial",
            "definition": "Criminal trials in India typically take 3-7 years depending on complexity. The trial proceeds through various stages from cognizance to judgment.",
            "section": "CrPC Chapters XX-XXIV",
            "key_elements": [
                "Average trial time: 3-7 years (can be longer for complex cases)",
                "Stage 1: Filing of chargesheet (60-90 days investigation)",
                "Stage 2: Cognizance by court",
                "Stage 3: Framing of charges",
                "Stage 4: Prosecution evidence",
                "Stage 5: Statement of accused (Section 313)",
                "Stage 6: Defense evidence",
                "Stage 7: Arguments and judgment"
            ],
            "stages_of_trial": [
                "1. Chargesheet filed by police",
                "2. Court takes cognizance",
                "3. Charges framed (accused pleads guilty/not guilty)",
                "4. Prosecution witnesses examined",
                "5. Accused's statement recorded",
                "6. Defense witnesses examined",
                "7. Final arguments by both sides",
                "8. Judgment delivered"
            ],
            "time_estimates": [
                "Investigation: 60-90 days typically",
                "Chargesheet to cognizance: 1-3 months",
                "Prosecution evidence: 1-3 years",
                "Defense evidence: 6 months - 1 year",
                "Arguments to judgment: 2-6 months"
            ],
            "speedy_trial_right": "Right to speedy trial is part of Article 21. Delay can be ground for bail."
        },
        "bail_process": {
            "title": "Process of Getting Bail",
            "definition": "Bail is obtained by filing an application before the appropriate court, providing surety and personal bond, and complying with conditions imposed by court.",
            "section": "CrPC Sections 436-439",
            "key_elements": [
                "Step 1: File bail application before appropriate court",
                "Step 2: Court hears arguments from both sides",
                "Step 3: If granted, execute personal bond",
                "Step 4: Provide surety (guarantor) as required",
                "Step 5: Comply with conditions imposed"
            ],
            "how_to_apply": [
                "Bailable offence: Apply at police station OR court",
                "Non-bailable: Apply before Sessions Court",
                "Anticipatory bail: Apply before Sessions/High Court",
                "Regular bail: Apply before court trying the case"
            ],
            "requirements": [
                "Bail application with grounds for bail",
                "Personal bond (accused's promise to appear)",
                "Surety bond (guarantor's promise and property details)",
                "Identity proof of accused and surety",
                "Property documents of surety (if required)"
            ],
            "conditions_typically_imposed": [
                "Condition 1: Appear before court on all hearing dates",
                "Condition 2: Not leave jurisdiction without permission",
                "Condition 3: Not tamper with evidence or influence witnesses",
                "Condition 4: Surrender passport (in serious cases)",
                "Condition 5: Regular reporting to police station"
            ],
            "landmark_case": "State of Rajasthan v. Balchand (1977) - Bail is rule, jail is exception"
        },
        "custody_rights": {
            "title": "Rights During Police Custody (Section 167 CrPC)",
            "definition": "An arrested person has specific rights during police custody. Police custody is limited to 15 days maximum. You must be produced before Magistrate within 24 hours and have right to lawyer.",
            "section": "CrPC Section 167, Article 22",
            "key_elements": [
                "POLICE CUSTODY: Maximum 15 DAYS only (not more)",
                "JUDICIAL CUSTODY: 60 days (minor) or 90 days (serious) maximum",
                "Must be produced before Magistrate within 24 hours",
                "Right to inform family of arrest",
                "Right to consult and be defended by lawyer",
                "Protection from torture and cruel treatment",
                "If chargesheet not filed in time: RIGHT to DEFAULT BAIL"
            ],
            "custody_time_limits": [
                "Police custody: Maximum 15 DAYS (Section 167(2))",
                "After 15 days: Only judicial custody, no police custody",
                "Judicial custody: Maximum 60 days (offence < 10 years)",
                "Judicial custody: Maximum 90 days (offence ≥ 10 years / death)",
                "If chargesheet not filed: DEFAULT BAIL is RIGHT"
            ],
            "what_happens_during_custody": [
                "Police can interrogate (question) accused",
                "Lawyer can meet accused during interrogation",
                "Medical examination every 48 hours",
                "Must be produced before Magistrate for remand extension",
                "No torture/coercion allowed (Section 163 CrPC)"
            ],
            "your_rights": [
                "Right to know grounds of arrest",
                "Right to inform family/friend of arrest",
                "Right to meet lawyer during investigation",
                "Right to free legal aid if cannot afford",
                "Right to medical examination",
                "Right to complain to Magistrate if tortured"
            ],
            "landmark_case": "D.K. Basu v. State of West Bengal (1997) - Custodial rights guidelines"
        },
        "threat_remedies": {
            "title": "Remedies When Threatened (Section 506 IPC)",
            "definition": "Criminal intimidation (threatening someone) is punishable under Section 506 IPC. You should immediately file a police complaint at the nearest police station.",
            "section": "IPC Section 506",
            "key_elements": [
                "FILE POLICE COMPLAINT immediately at police station",
                "Section 506 IPC: Criminal intimidation (threatening)",
                "Punishment: Up to 2 years OR fine OR both",
                "If threat to cause death/grievous hurt: Up to 7 years",
                "Threat can be verbal, written, or through gestures",
                "This is a COGNIZABLE offence - police must register FIR"
            ],
            "immediate_steps": [
                "Step 1: File POLICE COMPLAINT at nearest police station",
                "Step 2: Police will register FIR under Section 506 IPC",
                "Step 3: Preserve all evidence of threats",
                "Step 4: If police refuse, file complaint with SP or Magistrate",
                "Step 5: Apply for protection order if threat is serious"
            ],
            "evidence_to_preserve": [
                "Record threatening calls (audio recording)",
                "Screenshot threatening messages/WhatsApp/emails",
                "Note witnesses who heard verbal threats",
                "Keep written threat letters safely",
                "Screenshot social media threats with timestamps"
            ],
            "additional_protection": [
                "Apply for protection order from court",
                "Request police protection at residence",
                "File for restraining order against accused",
                "Dial 100 immediately if threat is imminent"
            ],
            "landmark_case": "Manik Taneja v. State of Karnataka (2015) - Criminal intimidation"
        },
        "victim_rights": {
            "title": "Rights of Crime Victims",
            "definition": "Crime victims have rights to protection, compensation, and participation in criminal proceedings under various laws including CrPC and victim compensation schemes.",
            "section": "CrPC Section 357, 357A",
            "key_elements": [
                "Right to file FIR and get copy",
                "Right to legal representation",
                "Right to protection from accused",
                "Right to compensation under Section 357/357A CrPC",
                "Right to participate in proceedings"
            ],
            "compensation_rights": [
                "Section 357 CrPC: Court can order accused to pay compensation",
                "Section 357A: State victim compensation scheme",
                "Can claim compensation even if accused acquitted",
                "Each state has Victim Compensation Fund",
                "Compensation covers: Medical expenses, loss of earnings, rehabilitation"
            ],
            "protection_rights": [
                "Protection from threats by accused",
                "Right to give evidence in camera (private)",
                "Identity protection in certain cases (rape)",
                "Right to request transfer of case",
                "Protection under Witness Protection Scheme"
            ],
            "how_to_claim_compensation": [
                "Apply to District Legal Services Authority (DLSA)",
                "Apply to State Legal Services Authority (SLSA)",
                "Attach copy of FIR and relevant documents",
                "Medical bills and proof of expenses",
                "Court can also recommend compensation"
            ],
            "landmark_case": "Manohar Singh v. State (2015) - Victim compensation mandatory"
        }
    }
}

def get_punishment_info(crime_type: str) -> dict:
    """Get punishment information for a crime type"""
    return IPC_PUNISHMENTS.get(crime_type, IPC_PUNISHMENTS.get("general_info", {}))

def get_legal_concept(concept_key: str) -> dict:
    """Get info about a legal concept"""
    concepts = IPC_PUNISHMENTS.get("legal_concepts", {})
    return concepts.get(concept_key, concepts.get("default", {}))

def format_concept_answer(concept_key: str, info: dict) -> str:
    """Format a legal concept answer (not a crime/punishment)"""
    
    answer = f"""📚 **{info.get('title', concept_key.upper().replace('_', ' '))}**

**Definition**: {info.get('definition', 'N/A')}

"""
    
    # Handle section (for Evidence Act, IPC sections etc.)
    if 'section' in info:
        answer += f"**Section**: {info['section']}\n\n"
    
    # Handle key_differences (for law_vs_act etc.)
    if 'key_differences' in info:
        answer += "**Key Differences**:\n"
        for diff in info['key_differences']:
            answer += f"• {diff}\n"
        answer += "\n"
    
    # Handle hierarchy
    if 'hierarchy' in info:
        answer += "**Legal Hierarchy in India**:\n"
        for item in info['hierarchy']:
            answer += f"{item}\n"
        answer += "\n"
    
    # Handle examples as dict
    if 'examples' in info and isinstance(info['examples'], dict):
        answer += "**Examples**:\n"
        for category, examples in info['examples'].items():
            clean_category = category.replace('_', ' ').title()
            answer += f"• **{clean_category}**: {examples}\n"
        answer += "\n"
    
    # Handle key_points
    if 'key_points' in info:
        answer += "**Key Points**:\n"
        for point in info['key_points']:
            answer += f"• {point}\n"
        answer += "\n"
    
    # Handle key_elements
    if 'key_elements' in info:
        answer += "**Key Elements**:\n"
        for element in info['key_elements']:
            answer += f"• {element}\n"
        answer += "\n"
    
    # Handle step_by_step_procedure (enhanced practical guidance)
    if 'step_by_step_procedure' in info:
        answer += "**Step-by-Step Procedure**:\n"
        for step in info['step_by_step_procedure']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle step_by_step_guidance (for domestic violence etc.)
    if 'step_by_step_guidance' in info:
        answer += "**What To Do (Step-by-Step)**:\n"
        for step in info['step_by_step_guidance']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle step_by_step_remedies (for false FIR etc.)
    if 'step_by_step_remedies' in info:
        answer += "**Your Remedies (Step-by-Step)**:\n"
        for step in info['step_by_step_remedies']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle procedural_guidance (for self-defense etc.)
    if 'procedural_guidance' in info:
        answer += "**Procedural Guidance**:\n"
        for step in info['procedural_guidance']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle what_to_do_if_arrested
    if 'what_to_do_if_arrested' in info:
        answer += "**What To Do If Arrested**:\n"
        for step in info['what_to_do_if_arrested']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle immediate_steps
    if 'immediate_steps' in info:
        answer += "**Immediate Steps**:\n"
        for step in info['immediate_steps']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle conditions_for_section_100 (self-defense)
    if 'conditions_for_section_100' in info:
        answer += "**When Death in Self-Defense is Justified**:\n"
        for cond in info['conditions_for_section_100']:
            answer += f"• {cond}\n"
        answer += "\n"
    
    # Handle important_limitations
    if 'important_limitations' in info:
        answer += "**Important Limitations**:\n"
        for limit in info['important_limitations']:
            answer += f"• {limit}\n"
        answer += "\n"
    
    # Handle types_of_violence_covered (domestic violence)
    if 'types_of_violence_covered' in info:
        answer += "**Types of Violence Covered**:\n"
        for v_type in info['types_of_violence_covered']:
            answer += f"• {v_type}\n"
        answer += "\n"
    
    # Handle where_to_get_help
    if 'where_to_get_help' in info:
        answer += "**Where To Get Help**:\n"
        for help_item in info['where_to_get_help']:
            answer += f"• {help_item}\n"
        answer += "\n"
    
    # Handle grounds_for_quashing
    if 'grounds_for_quashing' in info:
        answer += "**Grounds for Quashing FIR**:\n"
        for ground in info['grounds_for_quashing']:
            answer += f"• {ground}\n"
        answer += "\n"
    
    # Handle anticipatory_bail_procedure
    if 'anticipatory_bail_procedure' in info:
        answer += "**Anticipatory Bail Procedure**:\n"
        for step in info['anticipatory_bail_procedure']:
            answer += f"{step}\n"
        answer += "\n"
    
    # Handle custody_time_limits
    if 'custody_time_limits' in info:
        answer += "**Custody Time Limits**:\n"
        for limit in info['custody_time_limits']:
            answer += f"• {limit}\n"
        answer += "\n"
    
    # Handle online_fir_process
    if 'online_fir_process' in info:
        answer += "**Online FIR Process**:\n"
        for step in info['online_fir_process']:
            answer += f"• {step}\n"
        answer += "\n"
    
    # Handle who_proves (for burden_of_proof)
    if 'who_proves' in info:
        answer += "**Who Bears the Burden**:\n"
        who = info['who_proves']
        if isinstance(who, dict):
            for case_type, description in who.items():
                clean_type = case_type.replace('_', ' ').title()
                answer += f"• **{clean_type}**: {description}\n"
        answer += "\n"
    
    # Handle plaintiff_burden (specific to burden of proof)
    if 'plaintiff_burden' in info:
        answer += f"**Plaintiff's Burden**: {info['plaintiff_burden']}\n\n"
    
    # Handle rights
    if 'rights' in info:
        answer += "**Rights**:\n"
        for right in info['rights']:
            answer += f"• {right}\n"
        answer += "\n"
    
    # Handle your_rights
    if 'your_rights' in info:
        answer += "**Your Rights**:\n"
        for right in info['your_rights']:
            answer += f"• {right}\n"
        answer += "\n"
    
    # Handle restrictions
    if 'restrictions' in info:
        answer += f"**Restrictions**: {info['restrictions']}\n\n"
    
    # Handle scope
    if 'scope' in info:
        answer += f"**Scope**: {info['scope']}\n\n"
    
    # Handle landmark_case
    if 'landmark_case' in info:
        answer += f"**Landmark Case**: {info['landmark_case']}\n\n"
    
    # Handle procedure_overview
    if 'procedure_overview' in info:
        answer += "**Procedure**:\n"
        for step in info['procedure_overview']:
            answer += f"{step}\n"
        answer += "\n"
    
    answer += "⚖️ **DISCLAIMER**: This is for educational purposes only. Consult a qualified lawyer for legal advice."
    
    return answer

def format_punishment_answer(crime_type: str = "murder") -> str:
    """Format a comprehensive educational answer about punishment"""
    
    try:
        info = IPC_PUNISHMENTS.get(crime_type, {})
        is_concept = False
        
        if not info:
            # Check in legal_concepts as well
            concepts = IPC_PUNISHMENTS.get("legal_concepts", {})
            info = concepts.get(crime_type, {})
            if info:
                is_concept = True
        
        if not info:
            # Default to general bail info if asking about bail
            if 'bail' in crime_type.lower():
                info = IPC_PUNISHMENTS.get("bail_general", {})
            else:
                crime_type = "murder"  # Default
                info = IPC_PUNISHMENTS["murder"]
        
        # Use concept formatter for legal concepts (no 'section' or 'punishment' field)
        if is_concept or ('section' not in info and 'punishment' not in info):
            return format_concept_answer(crime_type, info)
        
        answer = f"""📚 **LEGAL CONSEQUENCES: {info.get('title', 'UNKNOWN').upper()}**

**{info.get('section', 'N/A')}**

**Definition**: {info.get('definition', 'N/A')}

**Punishment**: {info.get('punishment', 'N/A')}

"""
        
        if 'key_points' in info:
            answer += "**Key Points**:\n"
            for point in info['key_points']:
                answer += f"• {point}\n"
            answer += "\n"
        
        if 'bail_provisions' in info:
            bail = info['bail_provisions']
            answer += f"**Bail Status**: {bail.get('type', 'N/A')}\n"
            if 'explanation' in bail:
                answer += f"• {bail['explanation']}\n\n"
            
            if 'conditions' in bail:
                answer += "**Bail Conditions**:\n"
                for condition in bail.get('conditions', []):
                    if isinstance(condition, str):
                        answer += f"• {condition}\n"
                answer += "\n"
            
            if 'amount' in bail:
                answer += f"**Typical Bail Amount**: {bail['amount']}\n\n"
        
        if 'bail_process' in info:
            answer += "**How to Get Bail**:\n"
            process = info['bail_process']
            if 'at_police_station' in process:
                answer += "\n**At Police Station**:\n"
                for step in process['at_police_station']:
                    answer += f"• {step}\n"
            if 'if_police_refuse' in process:
                answer += "\n**If Police Refuse**:\n"
                for step in process['if_police_refuse']:
                    answer += f"• {step}\n"
            answer += "\n"
        
        if 'bail_conditions' in info:
            answer += "**Bail Conditions You Must Follow**:\n"
            for condition in info['bail_conditions']:
                answer += f"• {condition}\n"
            answer += "\n"
        
        if 'summary' in info:
            answer += f"\n💡 **{info['summary']}**\n\n"
        
        if 'aggravating_factors' in info:
            answer += "**Aggravating Factors (May Lead to Death Penalty)**:\n"
            for factor in info['aggravating_factors']:
                answer += f"• {factor}\n"
            answer += "\n"
        
        if 'supreme_court_guidelines' in info:
            sc = info['supreme_court_guidelines']
            answer += f"**Supreme Court Guidelines**:\n"
            answer += f"• Case: {sc['case']}\n"
            answer += f"• Principle: {sc['principle']}\n"
            answer += f"• Test: {sc['test']}\n\n"
        
        if 'related_sections' in info:
            answer += f"**Related IPC Sections**: {', '.join(info['related_sections'])}\n\n"
        
        # Add constitutional protection safely
        if 'general_info' in IPC_PUNISHMENTS and 'constitutional_protection' in IPC_PUNISHMENTS['general_info']:
            const = IPC_PUNISHMENTS['general_info']['constitutional_protection']
            answer += "**Constitutional Protection**:\n"
            answer += f"• Article 21: {const.get('article_21', 'N/A')}\n"
            answer += f"• Article 20: {const.get('article_20', 'N/A')}\n\n"
        
        if 'conviction_rate' in info:
            answer += f"**Statistics** (NCRB 2025):\n"
            answer += f"• Conviction Rate: {info['conviction_rate']}\n"
            if 'average_sentence' in info:
                answer += f"• Average Sentence: {info['average_sentence']}\n"
            answer += "\n"
        
        if 'examples' in info:
            answer += "**Common Examples**:\n"
            for example in info['examples']:
                answer += f"• {example}\n"
            answer += "\n"
        
        answer += "⚖️ **DISCLAIMER**: This is for educational purposes only. Consult a qualified lawyer for legal advice.\n"
        answer += "🚨 **If you or someone you know is in danger, contact Police: 100 | Women's Helpline: 1091**"
        
        return answer
        
    except Exception as e:
        # Return error information for debugging
        import traceback
        return f"Error generating answer for '{crime_type}': {type(e).__name__}: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
