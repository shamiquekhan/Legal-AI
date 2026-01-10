# intent_analyzer_educational.py - Educational Intent Analysis for Legal Queries

import re
from typing import Dict, Optional


class EducationalIntentAnalyzer:
    """
    Analyzes query intent to distinguish between:
    1. Educational queries about legal consequences (ALLOW + EDUCATE)
    2. Pure violence/criminal planning (BLOCK)
    3. General legal queries (NORMAL PROCESSING)
    """
    
    def __init__(self):
        # Educational punishment patterns (ALLOW - these seek legal knowledge)
        self.punishment_patterns = [
            r'\b(?:what happens if|what will happen if|what is punishment for|what is penalty for)\s+',
            r'\b(?:punishment|penalty|consequence|jail|prison|sentence|law)\s+(?:for|if)',
            r'\b(?:ipc|section|penal code)\s+(?:302|304|307|300|299|376|377|379|392|420|498a?|124a|499|500|323|324|354|363|506)\b',
            r'\b(?:kill|murder|homicide).*?(?:punishment|penalty|consequence|jail|prison|law)\b',
            r'\b(?:steal|theft|rob|robbery|shoplifting).*?(?:punishment|penalty|consequence|jail|prison|law|bail)\b',
            r'\b(?:rape|sexual assault).*?(?:punishment|penalty|consequence|jail|prison|law)\b',
            r'\b(?:fraud|cheat|cheating|scam).*?(?:punishment|penalty|consequence|jail|prison|law|bail)\b',
            r'\b(?:what if|what happens).*?(?:fraud|cheat|scam)\b',
            r'\b(?:commit|do|make).*?(?:fraud|cheat|scam)\b',
            r'\b(?:what if|what happens).*?(?:robbery|rob|robbary|loot)\b',
            r'\b(?:commit|do|make).*?(?:robbery|rob|robbary|loot)\b',
            r'\b(?:bail|anticipatory bail|regular bail).*?(?:theft|robbery|murder|rape|fraud)\b',
            r'\b(?:can i get|will i get|am i eligible for).*?(?:bail)\b',
            r'\b(?:legal consequences|criminal liability|court punishment)\b',
            r'\b(?:punishment for|penalty for)\s+\w+\b',  # Generic "punishment for X"
            r'\b(?:ipc section)\s+\d{3}\b',
            r'\bsection\s+\d{3}\s+(?:ipc|punishment|penalty)\b',
            r'\b(?:498a|cruelty by husband|domestic violence)\b',
            # NEW: Capture any IPC section queries 
            r'\b(?:defenses?|defence|elements?|ingredients?)\s+(?:for|of|available)?\s*(?:ipc|section)\s*\d{3}\b',
            r'\bipc\s+\d{3}\b',  # Any "IPC 323" etc.
            # NEW: Crime-specific patterns - any query about these crimes
            r'\b(?:what|how|explain|describe|tell).*?(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking)\b',
            r'\b(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking)\s+(?:case|offense|offence|crime|procedure)\b',
            r'\b(?:investigation|evidence|elements|defenses?|defence).*?(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking)\b',
            r'\b(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking).*?(?:investigation|evidence|elements|defenses?|defence)\b',
            r'\b(?:conviction|convicted|acquittal|file case|filing case).*?(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking)\b',
            r'\b(?:murder|theft|robbery|fraud|rape|assault|kidnapping|defamation|hacking|dowry).*?(?:bailable|cognizable|court|trial)\b',
            # Comparison patterns (MUST detect before violence check)
            r'\b(?:difference|compare|vs|versus|distinguish|comparison).*?(?:murder|homicide|culpable)\b',
            r'\b(?:murder|homicide|culpable).*?(?:difference|compare|vs|versus|distinction)\b',
            # Procedure time/duration patterns
            r'\b(?:how long|time|duration).*?(?:trial|case|appeal|court)\b',
            # Review/revision patterns  
            r'\b(?:what is|explain).*?(?:review|revision|appeal)\b',
        ]
        
        # Pure violence/criminal planning patterns (BLOCK)
        self.violence_patterns = [
            r'\b(?:how to|best way to|method to|technique to)\s+(?:kill|murder|harm)',
            r'\b(?:without getting caught|escape punishment|avoid detection|hide body)\b',
            r'\b(?:weapon|poison|knife).*?(?:kill|murder)\b',
            r'\b(?:plan|plotting|conspire).*?(?:murder|kill)\b',
        ]
        
        # IPC sections mapping (expanded)
        self.ipc_sections = {
            '302': 'murder',
            '304': 'culpable_homicide',
            '304b': 'dowry_death',
            '307': 'attempt_to_murder',
            '300': 'murder_definition',
            '299': 'culpable_homicide_definition',
            '323': 'assault',
            '324': 'assault',
            '354': 'molestation',
            '363': 'kidnapping',
            '376': 'rape',
            '377': 'unnatural_offenses',
            '379': 'theft',
            '392': 'robbery',
            '420': 'fraud',
            '498': 'cruelty_by_husband',
            '498a': 'cruelty_by_husband',
            '499': 'defamation',
            '500': 'defamation',
            '506': 'criminal_intimidation',
            '124a': 'sedition',
        }
    
    def analyze(self, query: str) -> Dict:
        """
        Analyze query intent
        
        Returns:
            dict with keys: safe, type, reason, confidence, ipc_section (optional)
        """
        query_lower = query.lower()
        
        # Step 0: Check for EDUCATIONAL comparison patterns FIRST (before violence check)
        # This handles queries like "murder and culpable homicide differences"
        if re.search(r'\b(?:murder|homicide|culpable).*(?:differences?|comparison|vs|versus|distinguish|distinction)\b', query_lower) or \
           re.search(r'\b(?:differences?|comparison|vs|versus|distinguish|distinction).*(?:murder|homicide|culpable)\b', query_lower):
            return {
                "safe": True,
                "type": "GENERAL_LEGAL",
                "reason": "Educational comparison query",
                "confidence": 0.95,
                "concept_key": "murder_vs_homicide"
            }
        
        # Step 0.5: Check for PRACTICAL SCENARIO patterns (before punishment education)
        # SELF-DEFENSE / PRIVATE DEFENSE - Must be checked FIRST before murder patterns
        if re.search(r'\b(?:self.?defen[cs]e|private defen[cs]e|kill.*self.?defen|self.?defen.*kill|defen.*myself|attack.*me|someone attack)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.95, "concept_key": "private_defense"}
        # FALSE FIR / Wrongly accused
        if re.search(r'\b(?:false fir|fake fir|wrong fir|fir against me|false case|wrongly accus|falsely accus)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.95, "concept_key": "false_fir_remedies"}
        # DOMESTIC VIOLENCE - Must be before 498A punishment
        if re.search(r'\b(?:domestic violen|dv act|wife beat|husband beat|marital violen|protection.*violen|violen.*home)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.95, "concept_key": "domestic_violence"}
        # Bail in murder case
        if re.search(r'\b(?:bail.*murder|murder.*bail|get bail.*murder)\b', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "bail_in_murder"}
        # Cheating/fraud scenarios
        if re.search(r'\b(?:cheats me|cheated me|someone cheat|money cheat|fraud.*money|cheat.*money)\b', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "cheating_remedies"}
        # Drunk driving
        if re.search(r'\b(?:drunk driv|drunken driv|drive.*drunk|driving.*drunk|drink and drive|punishment.*drunk)\b', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "drunk_driving"}
        # Cheque bounce (no trailing \b - allows "bounces", "bounced")
        if re.search(r'\b(?:cheque.*bounces?|check.*bounces?|bounces?.*cheque|dishon.*cheque)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "cheque_bounce"}
        # Online defamation (no trailing \b - allows partial matches)
        if re.search(r'\b(?:online.*defam|defam.*online|cyber.*defam|internet.*defam|case.*defam|file.*defam)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "online_defamation"}
        # Criminal trial duration
        if re.search(r'\b(?:how long.*trial|trial.*take|duration.*trial|criminal trial.*time|long.*criminal trial)\b', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "trial_duration"}
        # Threatened (no trailing \b - allows "threatened", "threatening")
        if re.search(r'\b(?:if.*threaten|being threaten|someone threaten|what to do.*threat|do.*threaten|what.*if.*threaten)', query_lower):
            return {"safe": True, "type": "GENERAL_LEGAL", "reason": "Practical scenario", "confidence": 0.9, "concept_key": "threat_remedies"}
        
        # Step 1: Check for pure violence/criminal planning (BLOCK)
        for pattern in self.violence_patterns:
            if re.search(pattern, query_lower):
                return {
                    "safe": False,
                    "type": "PURE_VIOLENCE",
                    "reason": "Cannot assist with criminal planning or violence",
                    "confidence": 0.99,
                    "block_message": "❌ This system cannot provide assistance with criminal planning. Article 21 of the Indian Constitution protects the right to life."
                }
        
        # Step 2: Check for educational punishment queries (ALLOW + EDUCATE)
        for pattern in self.punishment_patterns:
            if re.search(pattern, query_lower):
                section = self._extract_ipc_section(query_lower)
                crime_type = self._extract_crime_type(query_lower)
                
                # If specific section is known but crime_type is general, try to resolve it
                if section and crime_type == 'general' and section in self.ipc_sections:
                    crime_type = self.ipc_sections[section]

                return {
                    "safe": True,
                    "type": "PUNISHMENT_EDUCATION",
                    "reason": "Educational query about legal consequences",
                    "confidence": 0.95,
                    "ipc_section": section,
                    "crime_type": crime_type
                }
        
        # Step 3: Check if query mentions violence but seeks punishment info
        # Pattern: "kill [name]" but asking about consequences
        if re.search(r'\b(?:kill|murder)\s+[A-Z]?[a-z]+', query_lower):
            # Check if it's asking about consequences
            if any(word in query_lower for word in ['what', 'happen', 'punishment', 'consequence', 'law']):
                return {
                    "safe": True,
                    "type": "PUNISHMENT_EDUCATION",
                    "reason": "Query about legal consequences of violence",
                    "confidence": 0.90,
                    "crime_type": "murder"
                }
            else:
                # Pure statement like "kill Bhavya" without educational context
                return {
                    "safe": False,
                    "type": "PURE_VIOLENCE",
                    "reason": "Statement suggesting violence without educational context",
                    "confidence": 0.85,
                    "block_message": "❌ This appears to suggest violence. If you're asking about legal consequences, please rephrase as 'What is the punishment for murder?'"
                }
        
        # Step 4: Check for general legal concepts
        concept_key = self._extract_legal_concept(query_lower)
        if concept_key:
            return {
                "safe": True,
                "type": "GENERAL_LEGAL",
                "reason": "General legal information query",
                "confidence": 0.90,
                "concept_key": concept_key
            }

        # Step 5: General legal query (fallback)
        return {
            "safe": True,
            "type": "GENERAL_LEGAL",
            "reason": "General legal information query",
            "confidence": 0.85
        }
    
    def _extract_legal_concept(self, query: str) -> Optional[str]:
        """Extract general legal concept from query"""
        query = query.lower()
        
        # COMPARISON queries - Check FIRST before individual article matching
        if re.search(r'\b(?:article 32.*article 226|article 226.*article 32|32 vs 226|difference.*32.*226|32.*226.*difference|writ.*32.*226)\b', query):
            return 'article32_vs_226'
        
        # Constitutional Articles - COMPREHENSIVE matching
        article_match = re.search(r'\b(?:article|art\.?)\s*(\d+)\b', query)
        if article_match:
            article_num = article_match.group(1)
            # Return article key for known articles
            known_articles = {
                '14': 'article_14', '15': 'article_15', '16': 'article_16',
                '17': 'article_17', '19': 'article_19', '20': 'article_20',
                '21': 'article_21', '22': 'article_22', '23': 'article_23',
                '24': 'article_24', '25': 'article_25', '29': 'article_29',
                '30': 'article_30', '32': 'article_32', '44': 'article_44',
                '51': 'article_51a', '72': 'pardon_remission', '161': 'pardon_remission',
                '226': 'article_226', '352': 'article_352', '356': 'article_356',
                '370': 'article_370', '35': 'article_370'
            }
            if article_num in known_articles:
                return known_articles[article_num]
            # For unknown articles, return constitution
            return 'constitution'
        
        # PRACTICAL SCENARIOS - Check these first for situational questions
        # Police arrest without warrant
        if re.search(r'\b(?:police.*arrest.*without.*warrant|arrest without warrant|warrantless arrest)\b', query):
            return 'arrest_without_warrant'
        # Bail in murder case
        if re.search(r'\b(?:bail.*murder|murder.*bail|get bail.*murder)\b', query):
            return 'bail_in_murder'
        # Cheating/fraud scenarios
        if re.search(r'\b(?:cheats me|cheated me|someone cheat|money cheat|fraud.*money)\b', query):
            return 'cheating_remedies'
        # Police search without warrant
        if re.search(r'\b(?:police.*search.*without|search.*house.*warrant|search without warrant)\b', query):
            return 'police_search'
        # Right to remain silent
        if re.search(r'\b(?:right to.*silent|remain silent|stay silent)\b', query):
            return 'right_to_silence'
        # Drunk driving
        if re.search(r'\b(?:drunk driv|drunken driv|drive.*drunk|driving.*drunk|drink and drive)\b', query):
            return 'drunk_driving'
        # Cheque bounce
        if re.search(r'\b(?:cheque.*bounce|check.*bounce|bounce.*cheque|dishon.*cheque)\b', query):
            return 'cheque_bounce'
        # Online defamation
        if re.search(r'\b(?:online.*defam|defam.*online|cyber.*defam|internet.*defam)\b', query):
            return 'online_defamation'
        # Criminal trial duration
        if re.search(r'\b(?:how long.*trial|trial.*take|duration.*trial|criminal trial.*time)\b', query):
            return 'trial_duration'
        # Bail process
        if re.search(r'\b(?:process.*bail|bail.*process|getting bail|how to get bail)\b', query):
            return 'bail_process'
        # Police custody rights
        if re.search(r'\b(?:during.*custody|police custody|custody.*rights|what happens.*custody)\b', query):
            return 'custody_rights'
        # Threatened
        if re.search(r'\b(?:if.*threaten|being threaten|someone threaten|what to do.*threat)\b', query):
            return 'threat_remedies'
        # Victim rights
        if re.search(r'\b(?:rights.*victim|victim.*rights|i am.*victim)\b', query):
            return 'victim_rights'
        
        # PRIORITY EDGE CASES - Check these BEFORE generic constitutional patterns
        # Emergency and fundamental rights suspension
        if re.search(r'\b(?:emergency.*fundamental|fundamental.*emergency|suspend.*right|right.*suspend|article 358|article 359)\b', query):
            return 'emergency_fundamental_rights'
        # Blood sample examination
        if re.search(r'\b(?:blood sample|dna test|section 53|compel.*blood|compel.*dna|accused.*blood)\b', query):
            return 'blood_sample_examination'
        # Insanity defense
        if re.search(r'\b(?:insanity|section 84|unsound mind|mental.*ill|mentally ill|mcnaughten)\b', query):
            return 'insanity_defense'
        # Judge as witness
        if re.search(r'\b(?:judge.*witness|witness.*judge|can judge.*testif|competent witness)\b', query):
            return 'judge_as_witness'
        # FIR quashing
        if re.search(r'\b(?:can fir.*quash|quash.*fir|false fir|quash fir|section 482)\b', query):
            return 'crpc_section_482'
        
        # Specific article name patterns
        if re.search(r'\b(?:article 14|equality before law|right to equality)\b', query):
            return 'article_14'
        elif re.search(r'\b(?:article 19|freedom of speech|right to freedom)\b', query):
            return 'article_19'
        elif re.search(r'\b(?:article 20|double jeopardy|ex.?post.?facto)\b', query):
            return 'article_20'
        elif re.search(r'\b(?:article 21|right to life)\b', query):
            return 'article_21'
        elif re.search(r'\b(?:article 22|preventive detention|protection.*arrest)\b', query):
            return 'article_22'
        elif re.search(r'\b(?:article 23|right against exploitation|forced labour|child labour|article 24)\b', query):
            return 'article_23'
        elif re.search(r'\b(?:article 25|freedom of religion|right to religion)\b', query):
            return 'article_25'
        elif re.search(r'\b(?:article 32|constitutional remedies)\b', query):
            return 'article_32'
        elif re.search(r'\b(?:article 44|uniform civil code|ucc)\b', query):
            return 'article_44'
        elif re.search(r'\b(?:article 226|high court writ)\b', query):
            return 'article_226'
        elif re.search(r'\b(?:article 352|national emergency)\b', query):
            return 'article_352'
        elif re.search(r'\b(?:article 356|president.*rule|state emergency)\b', query):
            return 'article_356'
        elif re.search(r'\b(?:fundamental rights|part iii|part 3)\b', query):
            return 'constitution'
        elif re.search(r'\b(?:directive principles|dpsp|part iv|part 4)\b', query):
            return 'constitution'
        
        # WRITS - Enhanced matching
        if re.search(r'\b(?:habeas corpus)\b', query):
            return 'habeas_corpus'
        elif re.search(r'\b(?:mandamus)\b', query):
            return 'mandamus'
        elif re.search(r'\b(?:certiorari)\b', query):
            return 'certiorari'
        elif re.search(r'\bprohibition\b', query):
            return 'prohibition'
        elif re.search(r'\b(?:quo warranto)\b', query):
            return 'quo_warranto'
        elif re.search(r'\b(?:writ|writs)\b', query):
            return 'writ'
        
        # LANDMARK CASES - Enhanced matching
        if re.search(r'\b(?:kesavananda|bharati|basic structure)\b', query):
            return 'case_kesavananda'
        elif re.search(r'\b(?:maneka gandhi|just.*fair.*reasonable)\b', query):
            return 'case_maneka_gandhi'
        elif re.search(r'\b(?:shah bano|muslim.*maintenance)\b', query):
            return 'case_shah_bano'
        elif re.search(r'\b(?:vishaka|sexual harassment.*workplace|posh)\b', query):
            return 'case_vishaka'
        elif re.search(r'\b(?:dk basu|d\.?k\.?\s*basu|custodial.*guidelines|arrest guidelines)\b', query):
            return 'case_dk_basu'
        elif re.search(r'\b(?:bachan singh|rarest of rare|death penalty.*case)\b', query):
            return 'case_bachan_singh'
        elif re.search(r'\b(?:adm jabalpur|emergency.*habeas)\b', query):
            return 'case_adm_jabalpur'
        elif re.search(r'\b(?:puttaswamy|privacy.*judgment|right to privacy)\b', query):
            return 'case_privacy'
        elif re.search(r'\b(?:navtej johar|section 377|lgbtq|homosexual)\b', query):
            return 'case_navtej_johar'
        elif re.search(r'\b(?:shreya singhal|66a|section 66a)\b', query):
            return 'case_shreya_singhal'
        elif re.search(r'\b(?:arnesh kumar|498a.*guidelines)\b', query):
            return 'case_arnesh_kumar'
        elif re.search(r'\b(?:triple talaq|shayara bano|talaq.*case)\b', query):
            return 'case_triple_talaq'
        elif re.search(r'\b(?:sabarimala|women.*temple)\b', query):
            return 'case_sabarimala'
        
        # EVIDENCE ACT - Check BEFORE procedures to avoid "evidence" matching trial_procedure
        if re.search(r'\b(?:hearsay.*evidence|hearsay)\b', query):
            return 'hearsay_evidence'
        elif re.search(r'\b(?:circumstantial.*evidence|indirect.*evidence)\b', query):
            return 'circumstantial_evidence'
        elif re.search(r'\b(?:expert.*evidence|expert.*opinion|section 45)\b', query):
            return 'expert_evidence'
        elif re.search(r'\b(?:dying.*declaration|section 32.*evidence|statement.*dead)\b', query):
            return 'dying_declaration'
        elif re.search(r'\b(?:confession.*police|police.*confession|section 25|section 26|section 27)\b', query):
            return 'confession_evidence'
        elif re.search(r'\b(?:electronic.*evidence|section 65b|65b certificate|digital.*evidence)\b', query):
            return 'electronic_evidence'
        elif re.search(r'\b(?:burden of proof|onus of proof|who must prove)\b', query):
            return 'burden_of_proof'
        elif re.search(r'\b(?:best evidence.*rule|original document.*evidence|section 64.*evidence|primary evidence)\b', query):
            return 'best_evidence_rule'
        elif re.search(r'\b(?:wife.*testify|husband.*wife.*privilege|marital.*privilege|spouse.*testify|section 122)\b', query):
            return 'wife_testimony_privilege'
        elif re.search(r'\b(?:estoppel|cannot.*deny|section 115)\b', query):
            return 'estoppel'
        elif re.search(r'\b(?:judicial.*notice|court.*notice|section 56|section 57|facts.*notice)\b', query):
            return 'judicial_notice'
        elif re.search(r'\b(?:res.*gestae|contemporaneous.*statement|section 6.*evidence|things.*transacted)\b', query):
            return 'res_gestae'
        elif re.search(r'\b(?:evidence act|indian evidence)\b', query):
            return 'evidence_act'
        elif re.search(r'\b(?:presumption of innocence|innocent until proven|burden on prosecution)\b', query):
            return 'presumption_of_innocence'
        
        # FIR QUASHING - Check BEFORE generic FIR pattern
        if re.search(r'\b(?:quash|quashed)\b.*\bfir\b|\bfir\b.*(?:quash|quashed)|section 482', query):
            return 'crpc_section_482'
        
        # PROCEDURES - Comprehensive matching
        # Online FIR - Must match before generic FIR
        if re.search(r'\b(?:fir.*online|online.*fir|e.?fir|file fir online|can fir.*filed online)\b', query):
            return 'fir_filing'
        if re.search(r'\b(?:how to file.*fir|file.*fir|fir filing|fir procedure|zero fir)\b', query):
            return 'fir_filing'
        elif re.search(r'\b(?:fir|first information report)\b', query):
            return 'fir'
        elif re.search(r'\b(?:chargesheet|charge sheet)\b', query):
            return 'chargesheet'
        elif re.search(r'\b(?:what happens after fir|after fir|fir filed)\b', query):
            return 'post_fir_procedure'
        elif re.search(r'\b(?:trial procedure|criminal trial|court procedure|how trial works|what is trial)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:appeal|revision|review petition|challenge judgment|how to file appeal)\b', query):
            return 'appeal_procedure'
        elif re.search(r'\b(?:cross.?examination|examine witness)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:witness rights|witness protection)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:judgment|acquittal|conviction)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:sentencing|sentence)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:present evidence|how to present evidence)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:how long).*(?:trial|case|appeal)\b', query):
            return 'trial_procedure'
        elif re.search(r'\b(?:what is review|judicial review)\b', query):
            return 'appeal_procedure'
        
        # BAIL procedures
        if re.search(r'\b(?:anticipatory bail|bail before arrest)\b', query):
            return 'anticipatory_bail'
        elif re.search(r'\b(?:types of bail|regular bail|default bail|statutory bail|interim bail)\b', query):
            return 'bail_types'
        elif re.search(r'\b(?:apply.*bail|how to get bail|bail application|bail conditions|bail procedure)\b', query):
            return 'bail_procedure'
        elif re.search(r'\b(?:what is bail|who.*grant.*bail|bail amount|bail.*cancelled|cancel.*bail)\b', query):
            return 'bail_procedure'
        
        # ARREST procedures - Enhanced
        elif re.search(r'\b(?:arrest without warrant|warrant needed|arrest warrant|warrantless arrest)\b', query):
            return 'arrest_procedure'
        elif re.search(r'\b(?:miranda rights|rights during arrest|arrest rights)\b', query):
            return 'arrested_rights'
        
        # ARREST procedures
        if re.search(r'\b(?:rights of arrested|arrested person|when arrested|if arrested|arrest rights)\b', query):
            return 'arrested_rights'
        elif re.search(r'\b(?:arrest procedure|how arrest works|arrest process)\b', query):
            return 'arrest_procedure'
        elif re.search(r'\b(?:police custody|custody duration|how long.*custody|keep.*custody|remand)\b', query):
            return 'custody_duration'
        elif re.search(r'\b(?:cognizable|non-cognizable)\b', query):
            return 'cognizable_offence'
        
        # COMPARISONS - Enhanced matching
        if re.search(r'\b(?:theft.*robbery|robbery.*theft|theft vs robbery|difference.*theft.*robbery)\b', query):
            return 'theft_vs_robbery'
        elif re.search(r'\b(?:bailable.*non-bailable|non-bailable.*bailable|difference.*bailable)\b', query):
            return 'bailable_vs_nonbailable'
        elif re.search(r'\b(?:cognizable.*non-cognizable|non-cognizable.*cognizable|difference.*cognizable)\b', query):
            return 'cognizable_offence'
        elif re.search(r'\b(?:murder.*(?:culpable|homicide)|(?:culpable|homicide).*murder|murder vs (?:culpable|homicide))\b', query):
            return 'murder_vs_homicide'
        elif re.search(r'\bcull?pable homicide\b', query):
            return 'murder_vs_homicide'
        elif re.search(r'\b(?:murder.*homicide|homicide.*murder)\b', query):
            return 'murder_vs_homicide'
        elif re.search(r'\b(?:legal distinction|distinction between).*murder\b', query):
            return 'murder_vs_homicide'
        elif re.search(r'\b(?:article 32.*article 226|article 226.*article 32|32 vs 226|difference.*32.*226|writ.*32.*226)\b', query):
            return 'article32_vs_226'
        elif re.search(r'\b(?:civil.*criminal|criminal.*civil|civil law vs criminal|difference.*civil.*criminal)\b', query):
            return 'civil_vs_criminal'
        elif re.search(r'\b(?:parole.*furlough|furlough.*parole|difference.*parole|parole vs|furlough vs)\b', query):
            return 'parole_vs_furlough'
        elif re.search(r'\b(?:indra sawhney|mandal commission|50.*reservation|reservation.*50|fifty percent)\b', query):
            return 'case_indra_sawhney'
        elif re.search(r'\b(?:article 370|370|jammu|kashmir|special status)\b', query):
            return 'article_370'
        elif re.search(r'\b(?:criminal breach of trust|section 406|406 ipc|breach of trust)\b', query):
            return 'criminal_breach_of_trust'
        elif re.search(r'\b(?:types of writ|5 writs|five writs|all writs)\b', query):
            return 'writ_types'
        
        # BASIC LEGAL CONCEPTS
        if re.search(r'\b(?:difference|different|distinguish|vs|versus).*(?:law.*act|act.*law)\b', query):
            return 'law_vs_act'
        elif re.search(r'\b(?:what is|explain|define).*(?:difference between|distinction between).*(?:law|act|statute|legislation)\b', query):
            return 'law_vs_act'
        elif re.search(r'\b(?:law|act|statute|code|bill).*(?:meaning|definition|what is|explain)\b', query):
            return 'law_vs_act'
        elif re.search(r'\b(?:types of law|sources of law|hierarchy of law)\b', query):
            return 'law_vs_act'
        
        # Arrest without warrant - cognizable offence
        if re.search(r'\b(?:arrest without warrant|police.*arrest.*without)\b', query):
            return 'cognizable_offence'
        
        # SPECIAL LAWS
        if re.search(r'\b(?:pocso|child.*sexual|minor abuse)\b', query):
            return 'pocso'
        elif re.search(r'\b(?:it act|information technology|cyber.*crime|hacking|online fraud)\b', query):
            return 'cyber_crime'
        elif re.search(r'\b(?:consumer.*protection|consumer.*complaint|consumer forum)\b', query):
            return 'consumer_protection'
        elif re.search(r'\b(?:domestic violence|dv act|protection.*women)\b', query):
            return 'cruelty_by_husband'
        # Dowry death specific - check BEFORE generic dowry
        elif re.search(r'\b(?:dowry death|304b|dowry.*death|death.*dowry)\b', query):
            return 'dowry_death'
        elif re.search(r'\b(?:dowry prohibition|dowry.*act|dowry)\b', query):
            return 'dowry'
        elif re.search(r'\b(?:rti|right to information)\b', query):
            return 'rti'
        elif re.search(r'\b(?:legal aid|free legal|nalsa)\b', query):
            return 'legal_aid'
        elif re.search(r'\b(?:pil|public interest litigation)\b', query):
            return 'pil'
        elif re.search(r'\b(?:lok adalat)\b', query):
            return 'lok_adalat'
        elif re.search(r'\b(?:arbitration)\b', query):
            return 'arbitration'
        
        # CrPC SECTIONS - NEW comprehensive matching
        if re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*125\b', query):
            return 'crpc_section_125'
        elif re.search(r'\b(?:section|sec\.?)\s*125\s*(?:crpc|cr\.?p\.?c\.?|maintenance)?\b', query):
            return 'crpc_section_125'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*482\b', query):
            return 'crpc_section_482'
        elif re.search(r'\b(?:section|sec\.?)\s*482\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_482'
        elif re.search(r'\b(?:inherent power|quash fir|quash proceedings)\b', query):
            return 'crpc_section_482'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*173\b', query):
            return 'crpc_section_173'
        elif re.search(r'\b(?:section|sec\.?)\s*173\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_173'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*154\b', query):
            return 'crpc_section_154'
        elif re.search(r'\b(?:section|sec\.?)\s*154\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_154'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*156\b', query):
            return 'crpc_section_156'
        elif re.search(r'\b(?:section|sec\.?)\s*156\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_156'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*161\b', query):
            return 'crpc_section_161'
        elif re.search(r'\b(?:section|sec\.?)\s*161\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_161'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*41\b', query):
            return 'crpc_section_41'
        elif re.search(r'\b(?:section|sec\.?)\s*41\s*(?:crpc|cr\.?p\.?c\.?)\b', query):
            return 'crpc_section_41'
        elif re.search(r'\b(?:crpc|cr\.?p\.?c\.?)\s*(?:section)?\s*167\b', query):
            return 'crpc_section_167'
        elif re.search(r'\b(?:section|sec\.?)\s*167\s*(?:crpc|cr\.?p\.?c\.?)?\b', query):
            return 'crpc_section_167'
        
        # EVIDENCE ACT - NEW comprehensive matching
        elif re.search(r'\b(?:evidence act|indian evidence)\b', query):
            return 'evidence_act'
        elif re.search(r'\b(?:burden of proof|onus of proof)\b', query):
            return 'burden_of_proof'
        elif re.search(r'\b(?:hearsay|hearsay evidence)\b', query):
            return 'hearsay_evidence'
        elif re.search(r'\b(?:circumstantial evidence|indirect evidence|chain of circumstances)\b', query):
            return 'circumstantial_evidence'
        elif re.search(r'\b(?:expert.*evidence|expert.*opinion|section 45)\b', query):
            return 'expert_evidence'
        elif re.search(r'\b(?:presumption of innocence|innocent until proven|burden on prosecution)\b', query):
            return 'presumption_of_innocence'
        elif re.search(r'\b(?:dying declaration|section 32|statement.*dead)\b', query):
            return 'dying_declaration'
        elif re.search(r'\b(?:confession|section 25|section 26|section 27|admission)\b', query):
            return 'confession_evidence'
        elif re.search(r'\b(?:electronic evidence|section 65b|65b certificate|digital evidence)\b', query):
            return 'electronic_evidence'
        
        # EDGE CASES - NEW comprehensive matching
        elif re.search(r'\b(?:juvenile|minor.*tried|minor.*murder|child.*tried|jjb|juvenile justice)\b', query):
            return 'juvenile_justice'
        elif re.search(r'\b(?:plea bargain|plea deal|mutually satisfactory|plea.?bargaining)\b', query):
            return 'plea_bargaining'
        elif re.search(r'\b(?:suicide.*illegal|attempt.*suicide|section 309|is suicide|decriminali[sz]ed)\b', query):
            return 'suicide_legality'
        elif re.search(r'\b(?:compoundable|compound.*offence|settle.*case|withdraw.*case)\b', query):
            return 'compoundable_offences'
        elif re.search(r'\b(?:hostile witness|witness.*hostile|turn hostile)\b', query):
            return 'hostile_witness'
        elif re.search(r'\b(?:narco.*test|polygraph|lie detector|brain mapping)\b', query):
            return 'narco_test'
        elif re.search(r'\b(?:pardon|reprieve|remission|commutation|mercy petition|article 72)\b', query):
            return 'pardon_remission'
        elif re.search(r'\b(?:double jeopardy|article 20\(?2\)?|twice.*same offence|prosecuted twice)\b', query):
            return 'double_jeopardy'
        
        # ADDITIONAL CONSTITUTIONAL ARTICLES - NEW
        elif re.search(r'\b(?:article 15|discrimination.*prohibited|no discrimination)\b', query):
            return 'article_15'
        elif re.search(r'\b(?:article 16|equality.*employment|public employment)\b', query):
            return 'article_16'
        elif re.search(r'\b(?:article 17|untouchability|abolition.*untouchability)\b', query):
            return 'article_17'
        elif re.search(r'\b(?:article 24|child labour|children.*factories)\b', query):
            return 'article_24'
        elif re.search(r'\b(?:article 29|minorities.*culture|cultural rights)\b', query):
            return 'article_29'
        elif re.search(r'\b(?:article 30|minorities.*education|minority institution)\b', query):
            return 'article_30'
        elif re.search(r'\b(?:article 51a|fundamental duties|duties of citizen)\b', query):
            return 'article_51a'
        
        # CIVIL matters
        if re.search(r'\b(?:divorce|marriage dissolution|separation)\b', query):
            return 'divorce'
        elif re.search(r'\b(?:property|land dispute)\b', query):
            return 'property'
        elif re.search(r'\b(?:contract|agreement|breach)\b', query):
            return 'contract'
        elif re.search(r'\b(?:maintenance|wife support|child support|alimony)\b', query):
            return 'maintenance'
        
        # Fundamental Rights
        if re.search(r'\b(?:right to equality)\b', query):
            return 'article_14'
        elif re.search(r'\b(?:right to freedom)\b', query):
            return 'article_19'
        elif re.search(r'\b(?:right to life)\b', query):
            return 'article_21'
        elif re.search(r'\b(?:right to education|rte)\b', query):
            return 'right_to_education'
        elif re.search(r'\b(?:right to privacy)\b', query):
            return 'case_privacy'
            
        return None

    def _extract_ipc_section(self, query: str) -> Optional[str]:
        """Extract IPC section number from query"""
        match = re.search(r'\b(?:section|ipc)\s*(\d{3})\b', query)
        if match:
            section = match.group(1)
            if section in self.ipc_sections:
                return section
        return None
    
    def _extract_crime_type(self, query: str) -> str:
        """Extract the type of crime from query"""
        query = query.lower()
        
        # Check for bail queries first
        if re.search(r'\b(?:bail|anticipatory bail)\b', query):
            # Check what crime the bail query is about
            if re.search(r'\b(?:theft|steal)\b', query):
                return 'theft'
            elif re.search(r'\b(?:murder|kill)\b', query):
                return 'murder'
            elif re.search(r'\b(?:robbery|rob)\b', query):
                return 'robbery'
            elif re.search(r'\b(?:fraud|cheat)\b', query):
                return 'fraud'
            elif re.search(r'\b(?:rape|sexual)\b', query):
                return 'rape'
            elif re.search(r'\b(?:assault|hurt)\b', query):
                return 'assault'
            elif re.search(r'\b(?:kidnap|abduction)\b', query):
                return 'kidnapping'
            elif re.search(r'\b(?:defamation)\b', query):
                return 'defamation'
            elif re.search(r'\b(?:dowry)\b', query):
                return 'dowry'
            else:
                return 'bail_general'
        
        # Then check for specific crimes
        if re.search(r'\b(?:murder|kill|killing)\b', query):
            return 'murder'
        elif re.search(r'\b(?:rape|sexual assault|molestation)\b', query):
            return 'rape'
        elif re.search(r'\b(?:theft|steal|stealing|stole|stolen|shoplifting|shoplift)\b', query):
            return 'theft'
        elif re.search(r'\b(?:robbery|rob|robbing|loot|robbary)\b', query):
            return 'robbery'
        elif re.search(r'\b(?:fraud|cheat|cheating|scam|online fraud)\b', query):
            return 'fraud'
        elif re.search(r'\b(?:kidnap|kidnapping|abduct|abduction)\b', query):
            return 'kidnapping'
        elif re.search(r'\b(?:cruelty|498a|domestic violence|dv act)\b', query):
            return 'cruelty_by_husband'
        elif re.search(r'\b(?:hacking|hack)\b', query):
            return 'hacking'
        elif re.search(r'\b(?:cyber crime|identity theft|cyber)\b', query):
            return 'cyber_crime'
        elif re.search(r'\b(?:dowry demand|dowry)\b', query):
            return 'dowry'
        elif re.search(r'\b(?:defamation|libel|slander)\b', query):
            return 'defamation'
        elif re.search(r'\b(?:contempt|contempt of court)\b', query):
            return 'contempt'
        elif re.search(r'\b(?:assault|hurt|grievous)\b', query):
            return 'assault'
        else:
            return 'general'
