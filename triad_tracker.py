# Daily Tracking Module - The Triad Metrics
# Tracks three distinct "frequencies" of effort: Cognitive, Kinetic, and Moral

from datetime import datetime, timedelta
import json

class TriadTracker:
    """
    Daily Tracking: The Triad Metrics
    
    The app tracks three distinct "frequencies" of effort:
    
    The Cognitive Frequency (Academics): 
    - Encoding Hours: Not just reading, but active derivation (Physics from first principles, Molecular Biology logic).
    - Olympiad Rigor: Solving problems that require "Conceptual Absolute."
    
    The Kinetic Frequency (Innovation/Quaspace): 
    - MVP Progress: Daily code commits or data visualization tasks for Quaspace.
    - Execution vs. Note-taking: Did X build something real today?
    
    The Moral Frequency (Ethics/Governance):
    - World History/Ethics Study: Disciplined reading of civilizational rise and fall.
    - Islamic Ethics Alignment: Did today's pursuit of power remain ethical?
    """
    
    def __init__(self):
        self.daily_logs = {}  # Store logs by date
        self.weekly_average = {
            "cognitive": 0,
            "kinetic": 0,
            "moral": 0
        }
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        
    def log_cognitive_effort(self, hours, activity_type="study", notes=""):
        """
        Log cognitive effort (Academics)
        - hours: Time spent in hours
        - activity_type: "derivation", "problem_solving", "reading", etc.
        - notes: Specific details about the study
        """
        log_entry = {
            "frequency": "cognitive",
            "hours": hours,
            "activity_type": activity_type,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }
        
        if self.current_date not in self.daily_logs:
            self.daily_logs[self.current_date] = []
        
        self.daily_logs[self.current_date].append(log_entry)
        return log_entry
    
    def log_kinetic_effort(self, activity_type="development", progress_made=True, notes=""):
        """
        Log kinetic effort (Innovation/Quaspace)
        - activity_type: "coding", "design", "research", "meeting", etc.
        - progress_made: Boolean indicating if actual progress was made
        - notes: Details about the Quaspace work
        """
        log_entry = {
            "frequency": "kinetic",
            "activity_type": activity_type,
            "progress_made": progress_made,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }
        
        if self.current_date not in self.daily_logs:
            self.daily_logs[self.current_date] = []
        
        self.daily_logs[self.current_date].append(log_entry)
        return log_entry
    
    def log_moral_effort(self, topic_area="ethics_study", time_spent=0, notes=""):
        """
        Log moral effort (Ethics/Governance)
        - topic_area: "Islamic_Ethics", "World_History", "Governance", etc.
        - time_spent: Time in hours
        - notes: Specific content studied
        """
        log_entry = {
            "frequency": "moral",
            "topic_area": topic_area,
            "time_spent": time_spent,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }
        
        if self.current_date not in self.daily_logs:
            self.daily_logs[self.current_date] = []
        
        self.daily_logs[self.current_date].append(log_entry)
        return log_entry
    
    def calculate_daily_scores(self, target_date=None):
        """
        Calculate scores for each frequency for a given date
        Returns a dictionary with cognitive, kinetic, and moral scores
        """
        if target_date is None:
            target_date = self.current_date
            
        if target_date not in self.daily_logs:
            return {"cognitive": 0, "kinetic": 0, "moral": 0}
        
        daily_entries = self.daily_logs[target_date]
        
        cognitive_score = 0
        kinetic_score = 0
        moral_score = 0
        
        for entry in daily_entries:
            if entry["frequency"] == "cognitive":
                # Weight based on activity type and hours
                base_score = entry["hours"]
                if entry["activity_type"] in ["derivation", "first_principles"]:
                    base_score *= 1.5  # Bonus for deep thinking
                elif entry["activity_type"] == "problem_solving":
                    base_score *= 1.2  # Bonus for problem solving
                cognitive_score += base_score
                
            elif entry["frequency"] == "kinetic":
                # Score based on progress made and activity type
                if entry["progress_made"]:
                    if entry["activity_type"] == "coding":
                        kinetic_score += 3
                    elif entry["activity_type"] == "design":
                        kinetic_score += 2
                    else:
                        kinetic_score += 1
                        
            elif entry["frequency"] == "moral":
                # Score based on time spent and topic area
                base_score = entry["time_spent"]
                if "Islamic_Ethics" in entry["topic_area"]:
                    base_score *= 1.2  # Bonus for ethics focus
                moral_score += base_score
        
        # Cap scores to reasonable ranges
        return {
            "cognitive": min(cognitive_score, 10),
            "kinetic": min(kinetic_score, 10),
            "moral": min(moral_score, 10)
        }
    
    def get_weekly_trends(self, days_back=7):
        """
        Get weekly trends for the triad metrics
        """
        trends = {
            "dates": [],
            "cognitive": [],
            "kinetic": [],
            "moral": []
        }
        
        for i in range(days_back):
            date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            trends["dates"].append(date)
            
            daily_scores = self.calculate_daily_scores(date)
            trends["cognitive"].append(daily_scores["cognitive"])
            trends["kinetic"].append(daily_scores["kinetic"])
            trends["moral"].append(daily_scores["moral"])
        
        # Reverse to show oldest first
        trends["dates"].reverse()
        trends["cognitive"].reverse()
        trends["kinetic"].reverse()
        trends["moral"].reverse()
        
        return trends
    
    def get_weekly_average(self):
        """
        Calculate the weekly average for each frequency
        """
        trends = self.get_weekly_trends(7)
        
        cognitive_avg = sum(trends["cognitive"]) / len(trends["cognitive"])
        kinetic_avg = sum(trends["kinetic"]) / len(trends["kinetic"])
        moral_avg = sum(trends["moral"]) / len(trends["moral"])
        
        self.weekly_average = {
            "cognitive": round(cognitive_avg, 2),
            "kinetic": round(kinetic_avg, 2),
            "moral": round(moral_avg, 2)
        }
        
        return self.weekly_average
    
    def export_daily_log(self, target_date=None):
        """
        Export the daily log for analysis or review
        """
        if target_date is None:
            target_date = self.current_date
            
        if target_date not in self.daily_logs:
            return f"No logs found for {target_date}"
        
        daily_scores = self.calculate_daily_scores(target_date)
        
        export_data = {
            "date": target_date,
            "scores": daily_scores,
            "entries": self.daily_logs[target_date],
            "summary": {
                "total_entries": len(self.daily_logs[target_date]),
                "has_kinetic_progress": any(
                    entry["frequency"] == "kinetic" and entry["progress_made"] 
                    for entry in self.daily_logs[target_date]
                ),
                "focus_distribution": {
                    "cognitive": sum(1 for e in self.daily_logs[target_date] if e["frequency"] == "cognitive"),
                    "kinetic": sum(1 for e in self.daily_logs[target_date] if e["frequency"] == "kinetic"),
                    "moral": sum(1 for e in self.daily_logs[target_date] if e["frequency"] == "moral")
                }
            }
        }
        
        return export_data
    
    def reset_for_new_day(self):
        """
        Reset or move to the new day
        """
        self.current_date = datetime.now().strftime("%Y-%m-%d")

# Example usage class that combines all components
class MirrorDashboard:
    """
    The Mirror Dashboard - Combining all components
    """
    def __init__(self):
        self.profile = ProfileOfX()
        self.tracker = TriadTracker()
        self.mirror_system = MirrorSystem()
    
    def generate_daily_report(self):
        """
        Generate a comprehensive daily report combining all elements
        """
        # Get today's scores
        daily_scores = self.tracker.calculate_daily_scores()
        
        # Create daily logs for mirror system
        daily_logs = {
            'cognitive_effort': daily_scores['cognitive'],
            'kinetic_effort': daily_scores['kinetic'], 
            'moral_effort': daily_scores['moral'],
            'maintenance_check': daily_scores['cognitive'] > 2,  # Example condition
            'spike_factor': daily_scores['kinetic'] * 2 if daily_scores['kinetic'] > 0 else 0  # Example spike calculation
        }
        
        # Generate audit from mirror system
        audit_result = self.mirror_system.generate_daily_audit(daily_logs)
        
        # Generate first principles check (example)
        fp_feedback = self.mirror_system.check_first_principles_thinking(
            "Physics", 
            "first_principles" if daily_scores['cognitive'] > 3 else "memorization"
        )
        
        # Quaspace reality check
        quaspace_progress = self.mirror_system.quaspace_reality_check(daily_scores['kinetic'] > 0)
        
        # Shadow archive check
        failure_modes = {
            "polymath_trap": daily_scores['cognitive'] < 3,
            "dreamer_delay": daily_scores['kinetic'] == 0,
            "ethical_drift": daily_scores['moral'] < 1
        }
        shadow_warnings = self.mirror_system.shadow_archive_warning(failure_modes)
        
        # Combine everything into a daily report
        report = {
            "date": self.tracker.current_date,
            "audit_result": audit_result,
            "first_principles_feedback": fp_feedback,
            "quaspace_status": quaspace_progress,
            "shadow_warnings": shadow_warnings,
            "triad_scores": daily_scores,
            "weekly_average": self.tracker.get_weekly_average(),
            "priority_actions": self.profile.get_priority_actions(),
            "risk_assessment": self.profile.get_risk_assessment()
        }
        
        return report

# Import required classes for the dashboard to work properly
try:
    from profile_of_x import ProfileOfX
    from mirror_system import MirrorSystem
except ImportError:
    # Define placeholder classes if imports fail during creation
    class ProfileOfX:
        def get_priority_actions(self):
            return ["Placeholder: ProfileOfX module needed"]
        def get_risk_assessment(self):
            return "Placeholder: ProfileOfX module needed"
    
    class MirrorSystem:
        def generate_daily_audit(self, daily_logs):
            return {"placeholder": "MirrorSystem module needed"}
        def check_first_principles_thinking(self, subject_area, approach_type):
            return "Placeholder: MirrorSystem module needed"
        def quaspace_reality_check(self, progress_made):
            return "Placeholder: MirrorSystem module needed"
        def shadow_archive_warning(self, failure_modes_active):
            return ["Placeholder: MirrorSystem module needed"]