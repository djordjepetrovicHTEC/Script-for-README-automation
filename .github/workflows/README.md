# Workflows

## `workflow1.yaml`

<p>
Text
</p>

- ## Trigger
    - Text [link]()

- ## Input Parameters
    The workflow uses the following input parameters:

     - `rocm_version`: The ROCm release version, which is a required parameter.

     - `script_repo`: The script repository, which is an optional parameter.

     - `result_path`: The path where the result will be stored, which is an optional parameter.

     - `result_repo`: The repository where the result will be stored, which is an optional parameter.

- ## Environment Variables
    The workflow uses the following environment variables:

     - `SCRIPT_PATH`: The path to the script repository.

     - `RESULT_PATH`: The path to the result repository.

---

## `workflow2.yaml`

<p>
Text
</p>

- ## Trigger
    - Text [link]()

- ## Input Parameters
    The workflow uses the following input parameters:
     - `start_date`: The start date for the results analysis, which is a required parameter.

     - `end_date`: The end date for the results analysis, which is a required parameter.

     - `history_repo`: The repository where the history will be stored, which is a required parameter.

     - `benchmark_utils_repo`: The repository where the benchmark utilities are stored, which is a required parameter.

     - `organization`: The organization based on which the location of files will be different, which is a required parameter.

- ## Environment Variables
    The workflow uses the following environment variables:

     - `TEST_RESULTS_PATH`: The path to the test results directory.

     - `UTILS_DIR`: The directory where the benchmark utilities are stored.

     - `REPORTS_DIR`: The directory where the reports will be stored.

     - `REPORTS_PATH`: The path to the reports directory.

---


