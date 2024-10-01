from os.path import join, dirname, getmtime, exists
from polyglot_piranha import execute_piranha, PiranhaArguments
import logging
import os
from logging import info

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

directory_path = dirname(__file__)
print("feature_flag_dir : ",directory_path)

def run_java_ff_demo():
    info("Running the stale feature flag cleanup demo for Java")

    configuration_path = join(directory_path, "configurations")

    #for root, dirs, files in os.walk(directory_path):
    #  for file in files:
    #    logger.info(f"Found file: {os.path.join(root, file)}")


    args = PiranhaArguments(
        "java",
        substitutions={
            "stale_flag_name": "TenantConfigurationKey.FEATURE_SEQUENTIAL_NUMBERS_FOR_WARRANTY",
            "treated": "true",
            "treated_complement": "false",
        },
        paths_to_codebase=[directory_path],
        path_to_configurations=configuration_path,
    )
    output_summary_java = execute_piranha(args)
    print("output_summary_java : ",output_summary_java)

run_java_ff_demo();
print("Completed running the stale feature flag cleanup demo")