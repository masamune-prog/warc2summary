"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner
import pandas as pd
from warc2summary import warc_processor,heuristics
import os
import pytest
import pandas as pd


@pytest.fixture
def target_path():
    # You might want to set this to a specific path or use a temporary directory
    return r"C:\Users\user\warc2summary\warc_files"

@pytest.fixture
def large_dataframe(target_path):
    # Create a large sample DataFrame by using WARC Processor on the target path
    df = warc_processor.process_warc_files(target_path)
    return df

@pytest.fixture
def h1_processed_dataframe(large_dataframe):
    # Process the large DataFrame to get the smaller one
    df = heuristics.heuristics_1(large_dataframe)
    return df
@pytest.fixture
def h2_processed_dataframe(large_dataframe):
    # Process the large DataFrame to get the smaller one
    df = heuristics.heuristics_2(large_dataframe)
    return df
@pytest.fixture
def h3_processed_dataframe(large_dataframe):
    # Process the large DataFrame to get the smaller one
    df = heuristics.heuristics_3(large_dataframe)
    return df
def test_h1_data(target_path, h1_processed_dataframe):
    # Get the list of files in the directory
    files = os.listdir(target_path)
    
    # Assert that the number of files matches the processed DataFrame length
    assert len(files) == len(h1_processed_dataframe), f"Number of files ({len(files)}) does not match actual processed DataFrame length ({len(h1_processed_dataframe)})"

def test_h2_data(target_path, h2_processed_dataframe):
    # Get the list of files in the directory
    files = os.listdir(target_path)
    
    # Assert that the number of files matches the processed DataFrame length
    assert len(files) == len(h2_processed_dataframe), f"Number of files ({len(files)}) does not match actual processed DataFrame length ({len(h2_processed_dataframe)})"

def test_h3_data(target_path, h3_processed_dataframe):
    # Get the list of files in the directory
    files = os.listdir(target_path)
    
    # Assert that the number of files matches the processed DataFrame length
    assert len(files) == len(h3_processed_dataframe), f"Number of files ({len(files)}) does not match actual processed DataFrame length ({len(h3_processed_dataframe)})"