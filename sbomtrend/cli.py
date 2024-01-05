# Copyright (C) 2024 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import os
import pathlib
import sys
import textwrap
from collections import ChainMap

from lib4sbom.parser import SBOMParser

from sbomtrend.version import VERSION

# CLI processing


def main(argv=None):
    argv = argv or sys.argv
    app_name = "sbomtrend"
    parser = argparse.ArgumentParser(
        prog=app_name,
        description=textwrap.dedent(
            """
            SBOMTrend analyses a set of Software Bill of Materials within a
            directory and detects the changes in the components.
            """
        ),
    )
    input_group = parser.add_argument_group("Input")
    input_group.add_argument(
        "-d",
        "--directory",
        action="store",
        default="",
        help="Directory to be scanned",
    )
    input_group.add_argument(
        "-m",
        "--module",
        action="store",
        default="",
        help="identity of component",
    )
    input_group.add_argument(
        "--exclude-license",
        action="store_true",
        help="suppress detecting the license of components",
    )

    output_group = parser.add_argument_group("Output")
    output_group.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="add debug information",
    )
    output_group.add_argument(
        "-o",
        "--output-file",
        action="store",
        default="",
        help="output filename (default: output to stdout)",
    )

    parser.add_argument("-V", "--version", action="version", version=VERSION)

    defaults = {
        "module": "",
        "directory": "",
        "include_file": False,
        "exclude_license": False,
        "output_file": "",
        "debug": False,
    }

    raw_args = parser.parse_args(argv[1:])
    args = {key: value for key, value in vars(raw_args).items() if value}
    args = ChainMap(args, defaults)

    # Validate CLI parameters

    directory_location = args["directory"]

    if directory_location == "":
        # Assume current directory
        directory_location = os.getcwd()

    file_dir = pathlib.Path(directory_location)

    if not file_dir.exists():
        print("[ERROR] Directory not found.")
        return -1

    module_name = args["module"]

    if args["debug"]:
        print("Exclude Licences:", args["exclude_license"])
        print("Include Files:", args["include_file"])
        print("Output file:", args["output_file"])
        print("Directory:", directory_location)
        if module_name != "":
            print(f"Analysing {module_name}")

    sbom_packages = {}
    # Parse each SBOM file in directory
    for entry in file_dir.iterdir():
        parser = SBOMParser()
        # Load SBOM - will autodetect SBOM type
        parser.parse_file(str(entry))
        for package in parser.get_packages():
            # For each package, extract version and licence information
            name = package["name"]
            if module_name == "" or module_name == name:
                version = package.get("version", "MISSING")
                license = package.get("licenseconcluded", "NONE")
                package_data = sbom_packages.get(name)
                if package_data is None:
                    package_data = {}
                    package_data["version"] = {}
                    package_data["license"] = {}

                item = {}
                item["name"] = name
                item["count"] = package_data.get("count", 0) + 1
                version_data = package_data.get("version")
                version_data[version] = version_data.get(version, 0) + 1
                item["version"] = version_data
                if not args["exclude_license"]:
                    license_data = package_data.get("license")
                    license_data[license] = license_data.get(license, 0) + 1
                    item["license"] = license_data
                # store data
                sbom_packages[name] = item

    # Summarise
    if args["output_file"] == "":
        for package in sbom_packages.keys():
            print("Name", sbom_packages[package]["name"])
            print("Count", sbom_packages[package]["count"])
            version_info = sbom_packages[package]["version"]
            print("Versions", len(version_info))
            print("Version", dict(sorted(version_info.items())))
            if not args["exclude_license"]:
                print("Licenses", len(sbom_packages[package]["license"]))
                print("License", sbom_packages[package]["license"])
            # for element in sbom_packages[package].keys():
            #     print(element, sbom_packages[package][element])
            print("=" * 40)
    else:
        with open(args["output_file"], "w") as file:
            json.dump(sbom_packages, file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
