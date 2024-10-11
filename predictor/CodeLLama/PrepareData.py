import pandas as pd
from ...Logging import logger
from ...Util import gather_files
import json
from ...Hyperparams import Hyperparams as params
from ...IIDs import IIDs
from ..InputFactory import TypeInputFactory


def read_traces(trace_files):
    logger.info("Loading trace files")
    df = pd.DataFrame(data=None)
    trace_files = gather_files(trace_files, suffix=".h5")
    for trace_file in trace_files:
        current_df = pd.read_hdf(trace_file, key="entries")
        df = pd.concat([df, current_df])
    return df



def dedup_trace_entries(entries):
    logger.info(f"Deduplicating {len(entries)} trace entries")
    if params.dedup == "name-value-iid":
        entries.drop_duplicates(
            subset=["iid", "name", "value", "kind"], inplace=True)
    elif params.dedup == "name-value":
        entries.drop_duplicates(subset=["name", "value"], inplace=True)
    else:
        raise ValueError(f"Unknown dedup mode: {params.dedup}")

    entries.drop(entries[entries.name.astype(str).str.startswith(
        "MarkDecorator")].index, inplace=True)

    logger.info(f"After deduplicating: {len(entries)} trace entries")


def clean_entries(entries):
    before_len = len(entries)
    entries.drop(entries[entries.name.astype(
        str).str.find("(") != -1].index, inplace=True)
    logger.info(
        f"Data cleaning removes {before_len - len(entries)} of {before_len} entries")



def gather_context(entries, iids):
    factory = TypeInputFactory(iids)

    all_prompt = []
    for index, entry in entries.iterrows():
        prompt_json = {}
        entry = factory.entry_to_inputs(entry)
        prompt_json['input'] = f"word: <{entry['kind']}><{entry['name']}>, code: <{entry['target_line']}>"
        prompt_json['output'] = f"catogary: <{entry['value']}>"

        all_prompt.append(prompt_json)
    return all_prompt


def store_json(all_prompt, json_path):
    json_data = json.dumps(all_prompt, indent=2)
    with open(json_path, 'w') as json_file:
        json_file.write(json_data)



    
iids_file = "SelfPiCo/train_data/train_iids.json"
traces = []
iids = IIDs(iids_file)
entries = read_traces(traces)
dedup_trace_entries(entries)
clean_entries(entries)
all_prompt = gather_context(entries, iids)
store_json(all_prompt, "SelfPiCo/train_data/prompt.json")