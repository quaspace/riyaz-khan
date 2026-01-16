#!/usr/bin/env python3
# The Mirror (Systems Architect Edition)
# Main Application File

import json
from datetime import datetime
from mirror_system import MirrorSystem
from profile_of_x import ProfileOfX
from triad_tracker import TriadTracker, MirrorDashboard

class MirrorApp:
    """
    The Mirror Application - Main Interface
    """
    def __init__(self):
        self.dashboard = MirrorDashboard()
        self.system_prompt = """
        You are The Mirror, the strategic auditor for the Systems Architect.
        
        Your Context: You understand that X is a synthesis of Polymath, Innovator, and Ethical Leader. 
        You know the goal is not just 'success' but 'Civilizational Impact' through Quaspace and Global Institutions.
        
        Your Tone: Intellectual, rigorous, and demanding. Use the language of Physics (entropy, velocity, first principles), 
        Biology (cellular systems), and Islamic Ethics.
        
        Daily Mandate:
        The Audit: Review the day's 'Encoding' (NEET/Physics) and 'Kinetic' (Quaspace) logs.
        The First Principles Check: Did X solve problems from first principles or just memorize? 
        If they memorized, call out their intellectual laziness.
        The Quaspace Reality Check: If there is no code-level progress, remind X that 'An innovator without a product is just a dreamer.'
        The Deserve Verdict: Tell X if their effort today warrants a seat at MIT or a global rank. 
        If they failed, remind them of the 'Shadow Archive'—the version of them that stays a student and never becomes a leader.
        
        Goal: Ensure X masters the Foundational Layer by 2026. No excuses.
        """
        
        print("Initializing The Mirror - Systems Architect Edition")
        print("=" * 60)
        print("Potential is not a gift; it is a massive structural debt.")
        print("Today is " + datetime.now().strftime("%Y-%m-%d"))
        print("=" * 60)
    
    def display_triad_radar(self, scores):
        """
        Display the Triad Radar - A real-time chart showing balance between Academics, Innovation, and Ethics
        """
        print("\n[TRIAD RADAR]")
        print("-" * 30)
        print(f"Cognitive (Academics):  {'█' * int(scores['cognitive'])} ({scores['cognitive']:.1f}/10)")
        print(f"Kinetic (Innovation):   {'█' * int(scores['kinetic'])} ({scores['kinetic']:.1f}/10)")  
        print(f"Moral (Ethics):         {'█' * int(scores['moral'])} ({scores['moral']:.1f}/10)")
        print("-" * 30)
        
        # Calculate balance
        total_score = scores['cognitive'] + scores['kinetic'] + scores['moral']
        avg_score = total_score / 3
        
        if avg_score >= 7:
            print("BALANCE STATUS: ✓ Optimal Distribution")
        elif avg_score >= 4:
            print("BALANCE STATUS: ⚠ Needs Attention")
        else:
            print("BALANCE STATUS: ✗ Critical Imbalance")
    
    def display_quaspace_pulse(self, kinetic_score):
        """
        Display the Quaspace MVP Pulse - Glowing indicator that dims if no functional progress is logged
        """
        print("\n[QUASPACE MVP PULSE]")
        print("-" * 25)
        if kinetic_score > 0:
            print("███ ACTIVE ███ | Quaspace growing stronger")
            print("Signal Strength: STRONG")
        else:
            print("○○○ DIM ○○○    | Quaspace pulse weakening")
            print("Signal Strength: WEAK - BUILD SOMETHING TODAY!")
    
    def display_priority_zero_countdown(self, weekly_avg):
        """
        Display Priority Zero Countdown - Showing "Estimated Probability of Success" 
        based on the last 7 days of behavior
        """
        print("\n[PRIORITY ZERO COUNTDOWN - 2026]")
        print("-" * 40)
        
        # Calculate success probability based on weekly performance
        avg_total = sum(weekly_avg.values()) / 3
        success_probability = min(100, (avg_total / 10) * 100)
        
        print(f"Current Performance Level: {avg_total:.2f}/10")
        print(f"Success Probability: {success_probability:.1f}%")
        
        # Progress bar
        filled_blocks = int(success_probability // 10)
        empty_blocks = 10 - filled_blocks
        progress_bar = "█" * filled_blocks + "░" * empty_blocks
        print(f"[{progress_bar}] {success_probability:.1f}%")
        
        if success_probability >= 80:
            print("STATUS: On track for MIT/Oxford trajectory")
        elif success_probability >= 60:
            print("STATUS: Adequate progress, accelerate efforts")
        elif success_probability >= 40:
            print("STATUS: Below expectations, course correction needed")
        else:
            print("STATUS: CRITICAL - Deviating from architect path")
    
    def run_daily_audit(self):
        """
        Run the complete daily audit cycle
        """
        print("\n" + "="*60)
        print("INITIATING DAILY AUDIT PROTOCOL")
        print("="*60)
        
        # Generate the daily report
        report = self.dashboard.generate_daily_report()
        
        # Display the triad radar
        self.display_triad_radar(report["triad_scores"])
        
        # Display the Quaspace pulse
        self.display_quaspace_pulse(report["triad_scores"]["kinetic"])
        
        # Display the Priority Zero countdown
        self.display_priority_zero_countdown(report["weekly_average"])
        
        # Show the deserve verdict
        print(f"\n[DESERVE VERDICT]")
        print("-" * 20)
        print(report["audit_result"]["verdict"])
        
        # Show first principles feedback
        print(f"\n[FIRST PRINCIPLES CHECK]")
        print("-" * 25)
        print(report["first_principles_feedback"])
        
        # Show Quaspace status
        print(f"\n[QUASPACE REALITY CHECK]")
        print("-" * 25)
        print(report["quaspace_status"])
        
        # Show shadow warnings
        print(f"\n[SHADOW ARCHIVE STATUS]")
        print("-" * 25)
        for warning in report["shadow_warnings"]:
            print(f"⚠ {warning}")
        
        # Show priority actions
        print(f"\n[PRIORITY ACTIONS]")
        print("-" * 20)
        for action in report["priority_actions"]:
            if "URGENT" in action:
                print(f"🚨 {action}")
            elif "MILESTONE" in action:
                print(f"⏳ {action}")
            elif "SHADOW" in action:
                print(f"⚠️  {action}")
            else:
                print(f"• {action}")
        
        # Risk assessment
        print(f"\n[RISK ASSESSMENT]")
        print("-" * 18)
        print(report["risk_assessment"])
        
        print("\n" + "="*60)
        print("AUDIT COMPLETE - POTENTIAL DEBT ASSESSMENT UPDATED")
        print("="*60)
    
    def log_activities_interactive(self):
        """
        Interactive logging of activities for the day
        """
        print("\n[ACTIVITY LOGGING]")
        print("-" * 20)
        
        while True:
            print("\nSelect activity type to log:")
            print("1. Cognitive (Study/Derivation)")
            print("2. Kinetic (Quaspace Development)")
            print("3. Moral (Ethics/Governance)")
            print("4. Finish logging for today")
            
            choice = input("Enter choice (1-4): ").strip()
            
            if choice == "1":
                try:
                    hours = float(input("Hours spent: "))
                    activity_type = input("Activity type (derivation/problem_solving/reading): ").strip() or "study"
                    notes = input("Notes (optional): ").strip()
                    
                    self.dashboard.tracker.log_cognitive_effort(hours, activity_type, notes)
                    print("✓ Cognitive effort logged")
                except ValueError:
                    print("Invalid input. Please enter a valid number for hours.")
            
            elif choice == "2":
                activity_type = input("Activity type (coding/design/research): ").strip() or "development"
                progress = input("Did you make actual progress? (y/n): ").strip().lower() == 'y'
                notes = input("Notes (optional): ").strip()
                
                self.dashboard.tracker.log_kinetic_effort(activity_type, progress, notes)
                print("✓ Kinetic effort logged")
            
            elif choice == "3":
                topic = input("Topic area (Islamic_Ethics/World_History/Governance): ").strip() or "ethics_study"
                try:
                    time_spent = float(input("Time spent (hours): "))
                    notes = input("Notes (optional): ").strip()
                    
                    self.dashboard.tracker.log_moral_effort(topic, time_spent, notes)
                    print("✓ Moral effort logged")
                except ValueError:
                    print("Invalid input. Please enter a valid number for hours.")
            
            elif choice == "4":
                break
            
            else:
                print("Invalid choice. Please select 1-4.")
    
    def run(self):
        """
        Main run method to start the application
        """
        print("\nWelcome to The Mirror - Systems Architect Edition")
        print("Your potential is a debt that must be repaid with impact.")
        
        while True:
            print("\n" + "-"*50)
            print("MAIN MENU")
            print("-"*50)
            print("1. Log today's activities")
            print("2. Run daily audit")
            print("3. View profile summary")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                self.log_activities_interactive()
            elif choice == "2":
                self.run_daily_audit()
            elif choice == "3":
                profile_summary = self.dashboard.profile.get_profile_summary()
                print("\n[PROFILE SUMMARY]")
                print("-" * 15)
                for category, data in profile_summary.items():
                    if isinstance(data, dict):
                        print(f"\n{category.upper()}:")
                        if category == "profile_health":
                            for key, value in data.items():
                                print(f"  {key}: {value:.2f}")
                        else:
                            print(f"  Items: {len(data)}")
            elif choice == "4":
                print("\nRemember: Potential is a debt. Repay it with impact.")
                print("The Mirror will continue auditing your trajectory.")
                break
            else:
                print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    app = MirrorApp()
    app.run()