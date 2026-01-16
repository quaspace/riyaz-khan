# The Profile of X - Personalized Data Layer
# Contains the Pillar Synthesis, Shadow Archive, and Sunday Dreams

class ProfileOfX:
    """
    The Personalized Data Layer (The Profile of X)
    
    A. The Pillar synthesis (The Identity)
    - The Polymath: Mastery of NEET (Biology/Chemistry), UPSC (Governance), and Physics (Laws of Reality).
    - The Innovator: Founder of Quaspace. Execution-focused, AI/Space-centric.
    - The Ethical Leader: Islamic Ethics framework. Power must serve humanity.
    
    B. The Shadow Archive (Failure Modes)
    - The Polymath's Trap: Breadth without depth. Learning without "encoding."
    - The Dreamer's Delay: Conceptualizing Quaspace without building the MVP.
    - Ethical Drift: Pursuing power or knowledge without the "Moral Anchor."
    
    C. The Sunday Dreams (The Deliverables)
    - Rank Dominance: Global respect through NEET/Olympiad results.
    - Institutional Entry: MIT, Oxford, Cambridge, Harvard, or Stanford.
    - Sovereignty: Quaspace as a dominant entity in AI and Space technology.
    """
    
    def __init__(self):
        # A. The Pillar Synthesis (The Identity)
        self.identity_pillars = {
            "polymath": {
                "description": "Mastery of NEET (Biology/Chemistry), UPSC (Governance), and Physics (Laws of Reality)",
                "current_status": 0,  # Scale 0-10
                "progress_notes": [],
                "focus_areas": ["NEET_Biology", "NEET_Chemistry", "UPSC_Governance", "Physics_Fundamentals"]
            },
            "innovator": {
                "description": "Founder of Quaspace. Execution-focused, AI/Space-centric",
                "current_status": 0,  # Scale 0-10
                "progress_notes": [],
                "focus_areas": ["Quaspace_MVP", "AI_Development", "Space_Tech", "Business_Strategy"]
            },
            "ethical_leader": {
                "description": "Islamic Ethics framework. Power must serve humanity",
                "current_status": 0,  # Scale 0-10
                "progress_notes": [],
                "focus_areas": ["Islamic_Ethics", "Leadership_Principles", "Moral_Decision_Making", "Service_to_Humanity"]
            }
        }
        
        # B. The Shadow Archive (Failure Modes)
        self.shadow_archive = {
            "polymath_trap": {
                "active": False,
                "description": "Breadth without depth. Learning without 'encoding.'",
                "warning_threshold": 0.7,  # If focus spread too thin
                "last_triggered": None
            },
            "dreamer_delay": {
                "active": False,
                "description": "Conceptualizing Quaspace without building the MVP.",
                "warning_threshold": 0,  # If no actual progress made
                "last_triggered": None
            },
            "ethical_drift": {
                "active": False,
                "description": "Pursuing power or knowledge without the 'Moral Anchor.'",
                "warning_threshold": 0.3,  # If ethics neglected
                "last_triggered": None
            }
        }
        
        # C. The Sunday Dreams (The Deliverables)
        self.sunday_dreams = {
            "rank_dominance": {
                "goal": "Global respect through NEET/Olympiad results",
                "milestones": [
                    {"target": "NEET_Top_100", "achieved": False, "deadline": "2026-05-01"},
                    {"target": "International_Olympiad_Participation", "achieved": False, "deadline": "2025-12-31"}
                ],
                "current_progress": 0.0
            },
            "institutional_entry": {
                "goal": "MIT, Oxford, Cambridge, Harvard, or Stanford",
                "milestones": [
                    {"target": "Application_Submitted", "achieved": False, "deadline": "2025-09-01"},
                    {"target": "Standardized_Test_Target", "achieved": False, "deadline": "2025-12-31"},
                    {"target": "Research_Publication", "achieved": False, "deadline": "2025-08-01"}
                ],
                "current_progress": 0.0
            },
            "sovereignty": {
                "goal": "Quaspace as a dominant entity in AI and Space technology",
                "milestones": [
                    {"target": "Quaspace_MVP_Completed", "achieved": False, "deadline": "2025-06-01"},
                    {"target": "First_Customer_Acquired", "achieved": False, "deadline": "2025-12-01"},
                    {"target": "Series_A_Funding", "achieved": False, "deadline": "2026-03-01"}
                ],
                "current_progress": 0.0
            }
        }
        
        # Track overall profile health
        self.profile_health = {
            "identity_strength": 0.0,
            "shadow_risk_level": 0.0,
            "dream_progress_rate": 0.0
        }
    
    def update_identity_pillar(self, pillar_name, status, note=""):
        """Update the status of an identity pillar"""
        if pillar_name in self.identity_pillars:
            self.identity_pillars[pillar_name]["current_status"] = max(0, min(10, status))
            if note:
                self.identity_pillars[pillar_name]["progress_notes"].append(note)
            self._update_profile_health()
    
    def trigger_shadow_warning(self, shadow_name):
        """Trigger a warning in the shadow archive"""
        if shadow_name in self.shadow_archive:
            from datetime import datetime
            self.shadow_archive[shadow_name]["active"] = True
            self.shadow_archive[shadow_name]["last_triggered"] = datetime.now().isoformat()
            self._update_profile_health()
    
    def clear_shadow_warning(self, shadow_name):
        """Clear a warning in the shadow archive"""
        if shadow_name in self.shadow_archive:
            self.shadow_archive[shadow_name]["active"] = False
            self._update_profile_health()
    
    def update_sunday_dream_progress(self, dream_name, progress):
        """Update progress toward a Sunday Dream"""
        if dream_name in self.sunday_dreams:
            self.sunday_dreams[dream_name]["current_progress"] = max(0.0, min(1.0, progress))
            self._update_profile_health()
    
    def _update_profile_health(self):
        """Update the overall profile health metrics"""
        # Calculate identity strength (average of all pillars)
        total_pillar_status = sum(
            pillar["current_status"] for pillar in self.identity_pillars.values()
        )
        self.profile_health["identity_strength"] = total_pillar_status / (len(self.identity_pillars) * 10)
        
        # Calculate shadow risk level (how many shadows are active)
        active_shadows = sum(1 for shadow in self.shadow_archive.values() if shadow["active"])
        self.profile_health["shadow_risk_level"] = active_shadows / len(self.shadow_archive)
        
        # Calculate dream progress rate (average of all dreams)
        total_dream_progress = sum(
            dream["current_progress"] for dream in self.sunday_dreams.values()
        )
        self.profile_health["dream_progress_rate"] = total_dream_progress / len(self.sunday_dreams)
    
    def get_profile_summary(self):
        """Get a comprehensive summary of the profile"""
        return {
            "identity_pillars": self.identity_pillars,
            "shadow_archive": self.shadow_archive,
            "sunday_dreams": self.sunday_dreams,
            "profile_health": self.profile_health
        }
    
    def get_risk_assessment(self):
        """Get a risk assessment based on shadow archive activity"""
        active_shadows = [name for name, data in self.shadow_archive.items() if data["active"]]
        
        if not active_shadows:
            return "Profile is healthy. No shadow risks detected."
        else:
            return f"Warning: Active shadow risks detected - {', '.join(active_shadows)}. Address these immediately."
    
    def get_priority_actions(self):
        """Get priority actions based on profile status"""
        actions = []
        
        # Check for low pillar status
        for pillar_name, pillar_data in self.identity_pillars.items():
            if pillar_data["current_status"] < 5:  # Below average
                actions.append(f"URGENT: {pillar_name.title()} pillar needs immediate attention. Current status: {pillar_data['current_status']}/10")
        
        # Check for unmet milestones
        for dream_name, dream_data in self.sunday_dreams.items():
            for milestone in dream_data["milestones"]:
                if not milestone["achieved"]:
                    actions.append(f"MILESTONE DUE: {milestone['target']} in {dream_name.replace('_', ' ').title()}. Deadline: {milestone['deadline']}")
        
        # Check for active shadows
        for shadow_name, shadow_data in self.shadow_archive.items():
            if shadow_data["active"]:
                actions.append(f"SHADOW ALERT: Address {shadow_name.replace('_', ' ').title()} trap immediately.")
        
        return actions if actions else ["All systems nominal. Continue current trajectory."]