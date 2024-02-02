# SBOMTrend

SBOMTrend analyses a directory of SBOM (Software Bill of Materials) in either
[SPDX](https://www.spdx.org) and [CycloneDX](https://www.cyclonedx.org) formats.
It analyses all SBOM files within a directory and identifies license and version changes, for each component.

## Installation

To install use the following command:

`pip install sbomtrend`

Alternatively, just clone the repo and install dependencies using the following command:

`pip install -U -r requirements.txt`

The tool requires Python 3 (3.8+). It is recommended to use a virtual python environment especially
if you are using different versions of python. `virtualenv` is a tool for setting up virtual python environments which
allows you to have all the dependencies for the tool set up in a single environment, or have different environments set
up for testing using different versions of Python.


## Usage

```
usage: sbomtrend [-h] [-d DIRECTORY] [-f FORMAT] [-m MODULE] [--exclude-license] [--debug] [-o OUTPUT_FILE] [-V]

SBOMTrend analyses a set of Software Bill of Materials within a directory and detects the changes in the components.

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit

Input:
  -d DIRECTORY, --directory DIRECTORY
                        Directory to be scanned
  -f FORMAT, --format FORMAT
                        Date format (default is %d-%b-%Y (e.g. 01-Jan-2024))
  -m MODULE, --module MODULE
                        identity of component
  --exclude-license     suppress detecting the license of components

Output:
  --debug               add debug information
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        output filename (default: output to stdout)
```
					
## Operation

The `--directory` option is used to identify the directory to be scanned. If this option is not specified, the current directory is assumed.

The `--module` option can be used to restrict the reporting to a specific component. The default is to report for all components.

The tool reports the versions and licenses for each component in each SBOM. License reporting can be suppressed using the `--exclude-license` option.

The `--format` option can be used to format the date reporting for a specific component. The date formatting follows the [Python format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

The `--output-file` option is used to control the destination of the output generated by the tool. The
default is to report to the console but can be stored in a file (specified using `--output-file` option).

**Example**

The following command will report the changes

```bash
# sbomtrend -d <directory> --module rich
```

Produces the following output (output is clearly dependent on the contents if the SBOMs!)

```bash
Name rich
Count 48
Versions 16
Version {'13.0.0': 1, '13.0.1': 1, '13.1.0': 1, '13.2.0': 1, '13.3.1': 5, '13.3.2': 4, '13.3.3': 2, '13.3.4': 2, '13.3.5': 4, '13.4.1': 1, '13.4.2': 5, '13.5.0': 1, '13.5.2': 4, '13.5.3': 2, '13.6.0': 7, '13.7.0': 7}
Licenses 1
License {'MIT': 48}
========================================
```

The following command will report the version changes and store the result in a JSON file.

```bash
# sbomtrend -d <directory> --module rich -o <output file> 
```

The resulting file will be

```json
{
  "metadata": {                                                                                                                                                                                               
    "tool": "sbomtrend",                                                                                                                                                                                      
    "version": "0.2.0",                                                                                                                                                                                       
    "date": "2024-01-24T14:13:49Z"                                                                                                                                                                            
  },                                                                                                                                                                                                          
  "packages": {                                                                                                                                                                                               
    "rich": {                                                                                                                                                                                                 
      "name": "rich",                                                                                                                                                                                         
      "count": 48,                                                                                                                                                                                            
      "initial_version": "13.0.0",                                                                                                                                                                            
      "last_version": "13.7.0",                                                                                                                                                                               
      "versions": 16,                                                                                                                                                                                         
      "version_history": {                                                                                                                                                                                    
        "02-Jan-2023": 1,                                                                                                                                                                                     
        "09-Jan-2023": 2,                                                                                                                                                                                     
        "16-Jan-2023": 3,                                                                                                                                                                                     
        "23-Jan-2023": 4,                                                                                                                                                                                     
        "30-Jan-2023": 5,                                                                                                                                                                                     
        "06-Feb-2023": 5,                                                                                                                                                                                     
        "13-Feb-2023": 5,                                                                                                                                                                                     
        "21-Feb-2023": 5,                                                                                                                                                                                     
        "27-Feb-2023": 5,                                                                                                                                                                                     
        "06-Mar-2023": 6,                                                                                                                                                                                     
        "13-Mar-2023": 6,                                                                                                                                                                                     
        "20-Mar-2023": 6,                                                                                                                                                                                     
        "27-Mar-2023": 6,                                                                                                                                                                                     
        "03-Apr-2023": 7,                                                                                                                                                                                     
        "10-Apr-2023": 7,                                                                                                                                                                                     
        "17-Apr-2023": 8,                                                                                                                                                                                     
        "24-Apr-2023": 8,                                                                                                                                                                                     
        "08-May-2023": 9,                                                                                                                                                                                     
        "15-May-2023": 9,                                                                                                                                                                                     
        "22-May-2023": 9,                                                                                                                                                                                     
        "29-May-2023": 9,                                                                                                                                                                                     
        "05-Jun-2023": 10,                                                                                                                                                                                    
        "19-Jun-2023": 11,                                                                                                                                                                                    
        "26-Jun-2023": 11,                                                                                                                                                                                    
        "03-Jul-2023": 11,                                                                                                                                                                                    
        "10-Jul-2023": 11,                                                                                                                                                                                    
        "24-Jul-2023": 11,                                                                                                                                                                                    
        "31-Jul-2023": 12,                                                                                                                                                                                    
        "07-Aug-2023": 13,                                                                                                                                                                                    
        "14-Aug-2023": 13,                                                                                                                                                                                    
        "21-Aug-2023": 13,                                                                                                                                                                                    
        "11-Sep-2023": 13,                                                                                                                                                                                    
        "18-Sep-2023": 14,                                                                                                                                                                                    
        "25-Sep-2023": 14,                                                                                                                                                                                    
        "02-Oct-2023": 15,                                                                                                                                                                                    
        "09-Oct-2023": 15,                                                                                                                                                                                    
        "16-Oct-2023": 15,                                                                                                                                                                                    
        "23-Oct-2023": 15,                                                                                                                                                                                    
        "30-Oct-2023": 15,                                                                                                                                                                                    
        "06-Nov-2023": 15,                                                                                                                                                                                    
        "13-Nov-2023": 15,                                                                                                                                                                                    
        "27-Nov-2023": 16,                                                                                                                                                                                    
        "04-Dec-2023": 16,                                                                                                                                                                                    
        "11-Dec-2023": 16,                                                                                                                                                                                    
        "18-Dec-2023": 16,                                                                                                                                                                                    
        "25-Dec-2023": 16,                                                                                                                                                                                    
        "04-Jan-2024": 16,                                                                                                                                                                                    
        "09-Jan-2024": 16                                                                                                                                                                                     
      },                                                                                                                                                                                                      
      "version": {                                                                                                                                                                                            
        "13.0.0": 1,                                                                                                                                                                                          
        "13.0.1": 1,                                                                                                                                                                                          
        "13.1.0": 1,                                                                                                                                                                                          
        "13.2.0": 1,                                                                                                                                                                                          
        "13.3.1": 5,                                                                                                                                                                                          
        "13.3.2": 4,                                                                                                                                                                                          
        "13.3.3": 2,                                                                                                                                                                                          
        "13.3.4": 2,                                                                                                                                                                                          
        "13.3.5": 4,                                                                                                                                                                                          
        "13.4.1": 1,                                                                                                                                                                                          
        "13.4.2": 5,                                                                                                                                                                                          
        "13.5.0": 1,                                                                                                                                                                                          
        "13.5.2": 4,                                                                                                                                                                                          
        "13.5.3": 2,                                                                                                                                                                                          
        "13.6.0": 7,                                                                                                                                                                                          
        "13.7.0": 7                                                                                                                                                                                           
      },                                                                                                                                                                                                      
      "license": {                                                                                                                                                                                            
        "MIT": 48                                                                                                                                                                                             
      }                                                                                                                                                                                                       
    }                                                                                                                                                                                                         
  }                                                                                                                                                                                                           
}
```

if a module name is not specified, additional data relating to the number of packages and changes in each file is included.

```json
{
  "metadata": {                                                                                                                                                                                               
    "tool": "sbomtrend",                                                                                                                                                                                      
    "version": "0.2.0",                                                                                                                                                                                       
    "date": "2024-01-24T14:13:49Z"                                                                                                                                                                            
  },                                                                                                                                                                                                          
  "package_data": {                                                                                                                                                                                           
    "02-Jan-2023": {                                                                                                                                                                                          
      "count": 58,                                                                                                                                                                                            
      "change": 0                                                                                                                                                                                             
    },                                                                                                                                                                                                        
    "09-Jan-2023": {                                                                                                                                                                                          
      "count": 58,                                                                                                                                                                                            
      "change": 2                                                                                                                                                                                             
    },                                                                                                                                                                                                        
    "16-Jan-2023": {                                                                                                                                                                                          
      "count": 58,                                                                                                                                                                                            
      "change": 6                                                                                                                                                                                             
    },                                                                                                                                                                                                        
    ...CUT...,
    "09-Jan-2024": {                                                                                                                                                                                          
      "count": 67,                                                                                                                                                                                            
      "change": 3                                                                                                                                                                                             
    }                                                                                                                                                                                                         
  },                                                                                                                                                                                                          
  "packages": {                                                                                                                                                                                               
    "cve-bin-tool": {                                                                                                                                                                                         
      "name": "cve-bin-tool",                                                                                                                                                                                 
      "count": 48,
      ...CUT...
    }                                                                                                                                                                                                         
  }                                                                                                                                                                                                           
}
```

## Examples

The examples directory contains a number of sample scripts which process the output file to produce example charts using [Matplotlib](https://pypi.org/project/matplotlib/).

The examples are:

- **_analysis_** which analyses the version changes for each package
- **_summary_** which provides a summary of the number of packages and changes in each SBOM
- **_maintained_** which identifies the packages which have a single version and creates a chart which shows the time when the package was last updated. Packages more than 2 years old are highlighted.
- **_direct_** which identifies the version changes for direct package dependencies

## Licence

Licenced under the Apache 2.0 Licence.

## Limitations

This tool is meant to support software development and security audit functions. The usefulness of the tool is dependent on the SBOM data
which is provided to the tool. Unfortunately, the tool is unable to determine the validity or completeness of such a SBOM file; users of the tool
are therefore reminded that they should assert the quality of any data which is provided to the tool.

When processing and validating licenses, the application will use a set of synonyms to attempt to map some license identifiers to the correct [SPDX License Identifiers](https://spdx.org/licenses/). However, the
user of the tool is reminded that they should assert the quality of any data which is provided by the tool particularly where the license identifier has been modified.

## Feedback and Contributions

Bugs and feature requests can be made via GitHub Issues.