import pandas as pd
import numpy as np
import json

def get_metadata_1(data):
    helper_dict = None
    helper_dict = {'dacat': [],
                   'dacat_name': [],
                   'meta':[],
                   'cr_item': [],
                   'cr_name': [],
                   'forks':[],
                   'commits':[],
                   'contributors':[]}

    for i in range (0, len(data)-1):
        helper_dict['dacat'].append(data[i]['properties(dc)']['id'])
        helper_dict['dacat_name'].append(data[i]['properties(dc)']['name'])
        try:
            helper_dict['meta'].append(data[i]['properties(cr)']['meta'])
            json_data = json.loads(data[i]['properties(cr)']['meta'])
            helper_data = json_data['id']
            helper_data_name = json_data['name']


            # Forks
            forks = json_data['forks']
            helper_dict['cr_item'].append(helper_data)
            helper_dict['cr_name'].append(helper_data_name)
            helper_dict['forks'].append(forks)

            # Commits
            commits = json_data['commits']['totalCommits']
            helper_dict['commits'].append(commits)

            # Contributors
            contributors = json_data['commits']['authors']
            helper_dict['contributors'].append(len(contributors))

        # Take care of empty spaces.
        except KeyError:
            helper_dict['meta'].append("None2")
            helper_dict['cr_item'].append("Missing")
            helper_dict['cr_name'].append("Missing")
            helper_dict['forks'].append("Missing")
            helper_dict['commits'].append("Missing")
            helper_dict['contributors'].append("Missing")


    meta_df = pd.DataFrame(helper_dict)
    meta_df = meta_df[meta_df['meta'] != "None2"]
    meta_df = meta_df[['dacat', 'dacat_name', 'cr_item', 'cr_name', 'forks', 'commits', 'contributors']]
    meta_df = meta_df.astype({'cr_item':'str', 'forks': 'int64', 'commits': 'int64', 'contributors': 'int64'})
    meta_df['cr_item'] = meta_df['cr_item']+'cr'
    meta_df['dacat'] = meta_df['dacat']+'dc'
    return meta_df


def create_df_subject(subject_data):
    helper_dict = None
    subject_dict = {'313': 'Atmospheric Science, Oceanography and Climate Research',
                '314': 'Geology and Palaeontology',
                '315': 'Geophysics and Geodesy',
                '317': 'Geography'}

    helper_dict = {'dacat': [],
                   'dacat_name':[],
                   'meta':[],
                   'cr_item': [],
                   'cr_name': [],
                   'forks':[],
                   'commits':[],
                   'contributors':[],
                   'subject':[]}

    for i in range (0, len(subject_data)-1):
        helper_dict['dacat'].append(subject_data[i]['properties(dc)']['id'])
        helper_dict['dacat_name'].append(subject_data[i]['properties(dc)']['name'])
        helper_dict['subject'].append(subject_data[i]['s.id'])

        try:
            helper_dict['meta'].append(subject_data[i]['properties(cr)']['meta'])
            json_data = json.loads(subject_data[i]['properties(cr)']['meta'])
            helper_data = json_data['id']
            helper_data_name = json_data['name']

            # Forks
            forks = json_data['forks']
            helper_dict['cr_item'].append(helper_data)
            helper_dict['cr_name'].append(helper_data_name)
            helper_dict['forks'].append(forks)

            # Commits
            commits = json_data['commits']['totalCommits']
            helper_dict['commits'].append(commits)

            # Contributors
            contributors = json_data['commits']['authors']
            helper_dict['contributors'].append(len(contributors))

        # Take care of empty spaces.
        except KeyError:
            helper_dict['meta'].append("None2")
            helper_dict['cr_item'].append("Missing")
            helper_dict['cr_name'].append("Missing")
            helper_dict['forks'].append("Missing")
            helper_dict['commits'].append("Missing")
            helper_dict['contributors'].append("Missing")


    meta_df = pd.DataFrame(helper_dict)
    meta_df = meta_df[meta_df['meta'] != "None2"]
    meta_df = meta_df[['dacat', 'dacat_name', 'cr_item', 'cr_name', 'forks', 'commits', 'contributors', 'subject']]
    meta_df = meta_df.astype({'cr_item':'str', 'forks': 'int64', 'commits': 'int64', 'contributors': 'int64', 'subject':'str'})
    meta_df['cr_item'] = meta_df['cr_item']+'cr'
    meta_df['dacat'] = meta_df['dacat']+'dc'
    meta_df['subject_str'] = meta_df['subject'].map(subject_dict)
    return meta_df

def create_all_df(all_data):
    helper_dict = None
    helper_dict = {'dacat': [],
                   'dacat_name':[],
                   'meta':[],
                   'cr_item': [],
                   'cr_name': [],
                   'forks':[],
                   'commits':[],
                   'contributors':[]}

    for i in range(0, len(all_data)-1):
        helper_dict['dacat'].append(all_data[i]['properties(dc)']['id'])
        helper_dict['dacat_name'].append(all_data[i]['properties(dc)']['name'])

        try:
            helper_dict['meta'].append(all_data[i]['properties(cr)']['meta'])
            json_data = json.loads(all_data[i]['properties(cr)']['meta'])
            helper_data = json_data['id']
            helper_data_name = json_data['name']

            # Forks
            forks = json_data['forks']
            helper_dict['cr_item'].append(helper_data)
            helper_dict['cr_name'].append(helper_data_name)
            helper_dict['forks'].append(forks)

            # Commits
            commits = json_data['commits']['totalCommits']
            helper_dict['commits'].append(commits)

            # Contributors
            contributors = json_data['commits']['authors']
            helper_dict['contributors'].append(len(contributors))

        # Take care of empty spaces.
        except KeyError:
            helper_dict['meta'].append("None2")
            helper_dict['cr_item'].append("Missing")
            helper_dict['cr_name'].append("Missing")
            helper_dict['forks'].append("Missing")
            helper_dict['commits'].append("Missing")
            helper_dict['contributors'].append("Missing")


    meta_df = pd.DataFrame(helper_dict)
    meta_df = meta_df[meta_df['meta'] != "None2"]
    meta_df = meta_df[['dacat', 'dacat_name', 'cr_item', 'cr_name', 'forks', 'commits', 'contributors']]
    meta_df = meta_df.astype({'cr_item':'str', 'forks': 'int64', 'commits': 'int64', 'contributors': 'int64'})
    meta_df['cr_item'] = meta_df['cr_item']+'cr'
    meta_df['dacat'] = meta_df['dacat']+'dc'

    return meta_df
