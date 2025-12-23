import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import time

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.security import SecurityManager
from core.automation import AutomationManager
from core.context_resolver import ContextResolver
from core.planning_system import PlanningSystem

class TestPrometheusFeatures(unittest.TestCase):
    def setUp(self):
        self.mock_app = MagicMock()
        self.mock_app.project_path = os.path.dirname(__file__) # Use test dir as project
        
    def test_planning_system(self):
        planner = PlanningSystem(self.mock_app)
        # Use a temp file for testing
        planner.planning_file = "test_planning.json"
        
        try:
            # Test Goal
            planner.update_goal("goal_1", "active", "Win the hackathon")
            self.assertEqual(planner.state["goals"][0]["id"], "goal_1")
            
            # Test Task
            tid = planner.add_task("Fix bugs", "coder", "high")
            self.assertTrue(tid.startswith("task_"))
            self.assertEqual(len(planner.get_pending_tasks()), 1)
            
            # Test Completion
            planner.complete_task(tid, "Done")
            self.assertEqual(len(planner.get_pending_tasks()), 0)
        finally:
            path = os.path.join(self.mock_app.project_path, "test_planning.json")
            if os.path.exists(path):
                os.remove(path)

    def test_security_manager(self):
        sec = SecurityManager(self.mock_app)
        # Should not be admin by default in test env
        # But we can check log_audit
        sec.log_audit("TEST_ACTION", "Details")
        self.assertTrue(len(sec.audit_log) > 0)
        self.assertEqual(sec.audit_log[-1]['action'], "TEST_ACTION")

    def test_automation_scheduler(self):
        auto = AutomationManager(self.mock_app)
        job_id, msg = auto.schedule_script("test_script.py", 1)
        # Should fail if script doesn't exist
        # Let's create a dummy script
        dummy_script = os.path.join(os.path.dirname(__file__), "dummy_auto.py")
        with open(dummy_script, 'w') as f:
            f.write("print('Hello Automation')")
            
        try:
            job_id, msg = auto.schedule_script(dummy_script, 1)
            self.assertIn("job_", job_id)
            self.assertIn(job_id, auto.scheduled_jobs)
            
            # Test validation
            valid, issues = auto.validate_script(dummy_script)
            self.assertTrue(valid)
        finally:
            if os.path.exists(dummy_script):
                os.remove(dummy_script)

    def test_context_resolver(self):
        resolver = ContextResolver(self.mock_app)
        
        # Create a dummy file to resolve
        dummy_file = "test_resolve.txt"
        with open(dummy_file, 'w') as f:
            f.write("Secret Content")
            
        try:
            message = "Please analyze #test_resolve.txt"
            resolved = resolver.resolve(message)
            
            self.assertIn("Secret Content", resolved)
            self.assertIn("File: test_resolve.txt", resolved)
        finally:
            if os.path.exists(dummy_file):
                os.remove(dummy_file)

if __name__ == '__main__':
    unittest.main()
