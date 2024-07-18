"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner
import pandas as pd
from warc2summary import warc_processor


@pytest.fixture
#add a fixed directory for the warc files
#check with ashwin which files can be released
def get_num_websites(directory) -> int:
    return len(directory.glob("*.warc.gz"))

def check_websites(get_num_websites) -> pd.DataFrame:
    """Check if the websites are all present."""
    #get the number of warcc files
    #check the shape of the dataframe
    #execute warc processor
    dataframe = warc_processor.process_warc_files(directory)
    shape = dataframe.shape[0]
    assert shape == get_num_websites





def test_main_succeeds(check_websites) -> None:
    """It exits with a status code of zero."""
    assert check_websites()
