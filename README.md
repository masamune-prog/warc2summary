# warc2summary

[![PyPI](https://img.shields.io/pypi/v/warc2summary.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/warc2summary.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/warc2summary)][pypi status]
[![License](https://img.shields.io/pypi/l/warc2summary)][license]

[![Read the documentation at https://warc2summary.readthedocs.io/](https://img.shields.io/readthedocs/warc2summary/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/masamune-prog/warc2summary/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/masamune-prog/warc2summary/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/warc2summary/
[read the docs]: https://warc2summary.readthedocs.io/
[tests]: https://github.com/masamune-prog/warc2summary/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/masamune-prog/warc2summary
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

Implementation of Heuristics to process WARC Files 

## Requirements

- Python3 

## Installation

You can install _warc2summary_ via [pip] from [PyPI]:

```console
pip install warc2summary
```



## Usage

There exists 3 parts to this library: WARC Processor, heuristics, Pipeline

#### WARC Processor

This module converts WARC Files to a Pandas DataFrame 


```python 
from warc2summary import warc_processor
#process WARC Files Directly
warc_processor.process_warc_files(folder_path, max_workers=4)
```

#### Heuristics
This module applies the 3 heuristics developed

Heuristic 1: Takes the about page of the website, else take shortest url(likely to be main page)

Heuristic 2: Takes the shortest url

Heuristic 3: Takes shortest url and applies a Regex Filter


```python 
from warc2summary import heuristics
#process dataframe
heuristics.heuristics_1(dataframe)
```

```python 
from warc2summary import heuristics
#process dataframe
heuristics.heuristics_2(dataframe)
```

```python 
from warc2summary import heuristics
#process dataframe
heuristics.heuristics_3(dataframe)
```
The dataframe must contain the url and the web text content

This module transforms the dataframe for processing using LLMs reducing costs by reducing number of tokens needed

Feel free to contribute

#### pipeline

This module merges the previous 2 modules and joins it with a ground truth dataset for llm evaluation. Only OpenAI api supported for now. This code requires a human labelled dataset. 

To combine all 3 parts and replicate our findings

```python
from warc2summary import pipeline
#process WARC Files Directly
pipeline.execute_pipeline(warc_df,human_df,prompt,heuristic,max_tokens=1000,temperature=0.5,top_p=0.95,frequency_penalty=0.0,presence_penalty=0.0,model="gpt-4o",debug=False)
```
To perform batch inference

```python
from warc2summary import pipeline
pipeline.batch_prompt(df, prompt ,max_tokens=150,temperature=0.5,top_p=0.95,frequency_penalty=0.0,presence_penalty=0.0,model="gpt-4o",debug=False)
```


## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_warc2summary_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.


<!-- github-only -->

[license]: https://github.com/masamune-prog/warc2summary/blob/main/LICENSE
[contributor guide]: https://github.com/masamune-prog/warc2summary/blob/main/CONTRIBUTING.md
[command-line reference]: https://warc2summary.readthedocs.io/en/latest/usage.html
