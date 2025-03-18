
import pandas as pd
from Bio import Phylo

def read_nwk_and_csv(nwk_file, csv_file):
    # 读取nwk
    tree = Phylo.read(nwk_file, "newick")

    # 读取csv
    categories = pd.read_csv(csv_file, index_col=0)

    return tree, categories

def calculate_category_proportions(categories):

    total = categories.shape[0]
    prop_0 = categories[categories['category'] == 0]['category'].count() / total
    prop_1 = categories[categories['category'] == 1]['category'].count() / total
    return prop_0, prop_1

def find_branches_with_both_categories(tree, categories):

    def contains_both_categories(clade):
        node_names = [term.name for term in clade.get_terminals()]
        node_categories = categories.loc[node_names]
        return all(c in node_categories.values for c in [0, 1])


    mixed_clades = [clade for clade in tree.find_clades() if contains_both_categories(clade)]
    return mixed_clades

def calculate_internal_category_proportions(mixed_clades, categories):
    # 计算分支的比例
    def clade_proportions(clade):
        node_names = [term.name for term in clade.get_terminals()]
        node_categories = categories.loc[node_names]
        total = node_categories.shape[0]
        prop_0 = node_categories[node_categories == 0].count() / total
        prop_1 = node_categories[node_categories == 1].count() / total
        return prop_0, prop_1

    clade_proportions_dict = {clade: clade_proportions(clade) for clade in mixed_clades}
    return clade_proportions_dict

def filter_and_save_higher_proportion_nodes(clade_proportions_dict, global_proportions, categories):

    def filter_higher_proportion_nodes(clade, clade_proportions, global_proportions):
        if clade_proportions[0] > global_proportions[0]:
            node_names = [term.name for term in clade.get_terminals()]
            node_categories = categories.loc[node_names]
            return node_categories[node_categories == 0]
        return pd.DataFrame()


    higher_nodes = pd.concat([filter_higher_proportion_nodes(clade, props, global_proportions)
                              for clade, props in clade_proportions_dict.items()])

    higher_nodes.to_csv("higher_proportion_nodes.csv")


nwk_file = ".nwk"
csv_file = ".csv"

tree, categories = read_nwk_and_csv(nwk_file, csv_file)
global_proportions = calculate_category_proportions(categories)
mixed_clades = find_branches_with_both_categories(tree, categories)
clade_proportions_dict = calculate_internal_category_proportions(mixed_clades, categories)
filter_and_save_higher_proportion_nodes(clade_proportions_dict, global_proportions, categories)

print("Script executed successfully.")
