import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import unittest
from unittest.mock import patch

import run


class BlindedComparisonTest(unittest.TestCase):
    def test_candidates_share_prompt_and_judge_gets_only_blinded_answers(self):
        skill, cases = run.load_inputs()
        case = cases[0]
        args = argparse.Namespace(
            openai_model="gpt-fixture",
            anthropic_model="claude-fixture",
            judge_model="judge-fixture",
        )
        calls = []

        def complete(provider, model, system, prompt):
            calls.append((provider, model, system, prompt))
            if model == args.judge_model:
                data = json.loads(prompt)
                self.assertEqual(data["task"], case["prompt"])
                self.assertEqual(data["rubric"], case["criteria"])
                self.assertEqual(set(data["answers"]), set("ABCD"))
                self.assertEqual(set(data["answers"].values()), {"Response from [model]."})
                return json.dumps({
                    label: {"criteria": [True] * len(case["criteria"]), "notes": "Example"}
                    for label in data["answers"]
                })
            self.assertEqual(prompt, case["prompt"])
            self.assertNotIn(case["criteria"][0], system)
            return f"Response from {model}."

        with patch.object(run, "complete", side_effect=complete):
            with ThreadPoolExecutor(max_workers=4) as pool:
                result = run.run_case(case, skill, args, pool)

        self.assertEqual(len(calls), 5)
        for provider in run.CLIS:
            contexts = [system for source, model, system, _ in calls
                        if source == provider and model != args.judge_model]
            self.assertCountEqual(contexts, [run.INSTRUCTIONS, f"{run.INSTRUCTIONS}\n\n{skill}"])
        self.assertEqual(
            {(answer["provider"], answer["with_skill"]) for answer in result["answers"].values()},
            {(provider, variant) for provider in run.CLIS for variant in (False, True)},
        )


if __name__ == "__main__":
    unittest.main()
