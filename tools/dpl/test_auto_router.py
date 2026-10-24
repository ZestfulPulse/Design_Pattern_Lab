import unittest
from auto_router import classify_task

class RoutingTests(unittest.TestCase):
    def test_explicit_korean_ui(self):
        self.assertEqual(classify_task("MONA 인사이트 화면 가독성 개선").route, "design_team")
    def test_english_ui(self):
        self.assertEqual(classify_task("Improve the mobile layout").route, "design_team")
    def test_backend_is_skipped(self):
        self.assertEqual(classify_task("API 데이터베이스 마이그레이션").route, "skip")
    def test_ui_path_needs_inspection(self):
        self.assertEqual(classify_task("수정", ["src/components/Card.tsx"]).route, "inspect")
    def test_mixed_paths_need_inspection(self):
        self.assertEqual(classify_task("API 수정", ["src/components/Card.tsx"]).route, "inspect")
    def test_vendor_is_ignored(self):
        self.assertEqual(classify_task("Update dependencies", ["vendor/Card.tsx"]).route, "skip")
    def test_explicit_flag(self):
        self.assertEqual(classify_task("Fix issue", explicit_design=True).route, "design_team")
    def test_no_false_run_for_api(self):
        self.assertEqual(classify_task("API latency bug").route, "skip")

if __name__ == "__main__":
    unittest.main()
