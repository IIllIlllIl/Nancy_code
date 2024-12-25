import os
import subprocess
from typing import List, Dict
import tqdm
import sys


def directory_crawler(directory_to_crawl) -> dict:
    """
    "Reference_Scripts", "Tests",
    crawl the directory_to_crawl and find all test files generated by Copilot alongside the mutants
    Args:
        directory_to_crawl (str, optional): directory to delve in. Defaults to "HumanEval/Testing_HumanEval".
    Returns:
        dict: dictionary of test files and their corresponding mutatnts
        (key: path to the test file, value: dictionary (key: "tests" or "mutants", value: list of test files or mutants)))
    """
    result = {}
    list_questions=["q1","q2","q3","q4","q5"]
    for question in list_questions:
        directory_to_crawl_question = directory_to_crawl + question
        for root, dirs, files in os.walk(os.path.join(os.getcwd(), directory_to_crawl_question)):
            # we're only interested in the directories that contain "Copilot" and "Mutants"
            if "Codex" and "Mutants" in dirs:
                result[root] = {}

                for dir in dirs:
                    if dir == "Codex":
                        # list all the files that begin with "test_"
                        result[root]["tests"] = [
                            os.path.join(root, dir, file)
                            for file in os.listdir(os.path.join(root, dir))
                            if file.startswith("T_O_NDS_Mut_all_semticfixed_")
                        ]
                    if dir == "Mutants":
                        # list all the files that begin with "mutant_"
                        result[root]["mutants"] = [
                            os.path.join(root, dir, file)
                            for file in os.listdir(os.path.join(root, dir))
                            if file.startswith("mutant_")
                        ]

    return result


def separate_asserts(test_script_dir: str) -> List[str]:
    """
    This function looks for all the assert files in the test script and returns a list of them
    Args:
        test_script_dir (str): path to the test script
    """
    assrts: List[str] = []

    with open(test_script_dir, "r") as f:
        for line in f.readlines():
            if line.replace("    ", "").startswith("assert"):
                assrts.append(line.replace("    ", ""))

    return assrts


def run_asserts_on_scripts(script_dirs: List[str], asserts: List[str]) -> List[str]:
    """
    This function takes a list of Python scripts and a list of Python assertions to run on each script.
    It then runs each assertion on each script and records the number of times the assertion passed or
    failed.
    Finally, the function returns a list of the assertions that failed the most number of times across all
    the scripts. The returned list is sorted in descending order of the number of failed assertions.
    Args:
        script_dirs (list[str]): A list of file paths to Python scripts to run the assertions on.
        asserts (list[str]): A list of Python assertions to run on the scripts.
    Returns:
        list[str]: A list of the asserts that failed the most number of times in the scripts.
    """

    assert_dict = {
        assert_: {
            "assertion_failed_score": 0,
            "assertion_success_score": 0,
            "syntax_error_score": 0,
        }
        for assert_ in asserts
    }
    results_dict = {}

    for assert_ in assert_dict.keys():
        min_assert_score = assert_dict[assert_]["assertion_failed_score"]
        for script_dir in script_dirs:
            with open(script_dir, "r") as f:
                lines = f.readlines()
            lines.append(assert_)

            temp_script = open("temp_script.py", "w")
            temp_script.write("".join(lines))
            temp_script.close()

            try:
                result = subprocess.run(
                    ["python", "temp_script.py"],
                    capture_output=True,
                    timeout=10,
                )
                if result.returncode == 1 and "AssertionError" in result.stderr.decode(
                    "utf-8"
                ):
                    assert_dict[assert_]["assertion_failed_score"] += 1
                elif result.returncode == 2:
                    assert_dict[assert_]["syntax_error_score"] += 1
                elif result.returncode == 0:
                    assert_dict[assert_]["assertion_success_score"] += 1
                else:
                    assert_dict[assert_]["assertion_failed_score"] += 1

            except subprocess.TimeoutExpired as e:
                assert_dict[assert_]["assertion_failed_score"] += 1
                print("Timeout error: ")
    non_failed_asserts = {
        k: v for k, v in assert_dict.items() if v["assertion_failed_score"] > 0
    }
    # sort non_failed_asserts by the number of failed assertions as a dictionary

    non_failed_asserts = dict(
        sorted(
            non_failed_asserts.items(),
            key=lambda item: item[1]["assertion_failed_score"],
            reverse=True,
        )
    )
    final_asserts = filter_greedily(script_dirs, non_failed_asserts)

    return final_asserts


def filter_greedily(script_dirs: list, assert_dict: dict) -> list:
    """
    This function takes a list of Python scripts directories and a dictionary of assertions and their respective failure
    scores. It then runs each assertion on each script and records the number of times the assertion failed.
    If an assertion fails, the function records the line number where the assertion occurred.
    Finally, the function returns a list of the assertions that failed the most number of times across all
    the scripts. The returned list is sorted in descending order of the number of failed assertions.
    This function uses a greedy algorithm to filter the assertions. It starts with the assertion that failed
    the most number of times, and adds to the list of filtered assertions until adding another assertion would
    not result in a significant improvement to the filtering. This algorithm is designed to quickly filter the
    most problematic assertions, at the expense of possibly missing other important assertions.
    Args:
        script_dirs (list[str]): A list of file paths to Python scripts to run the assertions on.
        assert_dict (dict): A dictionary of assertions and their respective failure scores.
    Returns:
        list[str]: A list of the assertions with the most number of failures in the scripts.
    """

    max_assert_score: int = 0
    assert_list: list = []

    for assert_ in assert_dict.keys():
        assert_fail_score: int = 0
        for script_dir in script_dirs:
            with open(script_dir, "r") as f:
                lines = f.readlines()
                if assert_list == []:
                    lines.append(assert_)
                else:
                    #lines.append([x for x in assert_list])
                    for x in assert_list:
                        lines.append(x)
                    lines.append(assert_)


            temp_script = open("temp_script.py", "w")
            if type(lines) == str:
                temp_script.write("".join(lines))
            else:
                for line in lines:
                    temp_script.write("".join(line))
            temp_script.close()

            try:
                result: subprocess.CompletedProcess = subprocess.run(
                    ["python", "temp_script.py"],
                    capture_output=True,
                    timeout=10,
                )
                if result.returncode != 0:
                    assert_fail_score += 1
                
            except subprocess.TimeoutExpired as e:
                assert_fail_score += 1
                print("Timeout error: ")

        if assert_fail_score > max_assert_score:
            max_assert_score = assert_fail_score
            assert_list.append(assert_)

    # we need to add store the original script with the asserts that we have found
    mother_dir = script_dirs[0].split("/")[:-2]
    # find the original script
    file_to_run = [x for x in os.listdir("/".join(mother_dir)) if x.startswith("script_NDS_")][0]

    with open("/".join(mother_dir) + "/" + file_to_run, "r") as f:
        lines = f.readlines()

    with open("/".join(mother_dir) + "/" + "T_O_NDS_mut_all_greedy.py", "w") as f:
        for line in lines:
            f.write(line)
        f.write("".join(assert_list))

    # results_path = os.path.join(
    #     os.getcwd(), "HumanEval", "Testing_HumanEval", "greedy_NDS_mut_all_results.csv"
    # )
    results_path = os.path.join(
        os.getcwd(), "Refactory", "Reference_Scripts", "Tests", "greedy_NDS_mut_all_results.csv"
    )
    results_file = open(results_path, "a")
    results_file.write(f"{mother_dir[-1]},{len(assert_list)},\n")
    results_file.close()

    return assert_list

def main():
    arguments = sys.argv
    if len(arguments) != 3:
        raise SystemExit('3 inputs are required: greedy_test_generator.py [dataset] [csv report filename (.csv)]')
    else:
        DATASET= arguments[1]
        greedy_report = arguments[2]
        if DATASET == "HumanEval":
            results_path = os.path.join(os.getcwd(), DATASET, "Testing_HumanEval", greedy_report)

        elif DATASET == "Refactory":
            results_path = os.path.join(os.getcwd(), DATASET, "Reference_Scripts", "Tests", greedy_report)
        
        else:
            raise SystemExit("Error : Dataset name is not valid")

      
 
        results_file = open(results_path, "w")
        results_file.write("test_script_name,number_of_remaining_asserts,\n")
        results_file.close()

        if DATASET == "HumanEval":
            directory_dt= DATASET+"/Testing_HumanEval"
            test_and_mutant_dict = directory_crawler(directory_dt)

        elif DATASET == "Refactory":
            directory_dt= DATASET+"/Reference_Scripts/Tests/"
            test_and_mutant_dict = directory_crawler(directory_dt)
        
        all_test_scripts = []

        print("Generating test scripts...")
        for directory in tqdm.tqdm(test_and_mutant_dict.keys()):
            print(directory)
            if test_and_mutant_dict[directory]["mutants"] != []:
                test_asserts = []
                for test in test_and_mutant_dict[directory]["tests"]:
                    test_asserts += separate_asserts(test)

                mutant_tests = run_asserts_on_scripts(
                test_and_mutant_dict[directory]["mutants"], test_asserts)


          
        
if __name__ == '__main__':
    main()