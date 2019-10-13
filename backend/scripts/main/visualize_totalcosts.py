import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.ticker as mtick

def generate_total_df(df):
    '''
    Input is predicted df with pred_categories.
    '''
    cat_cost = []
    categories = set(df['pred_categories'])
    for i in categories:
        filtered = df.loc[df['pred_categories'] == i]
        total_cost = sum(filtered['Cost'].values.tolist())
        cat_cost.append([i,total_cost])
    new_df = pd.DataFrame(cat_cost, columns = ['category', 'total_cost'])
    new_df = new_df.set_index('category')
#     new_df = new_df.set_index(new_df.iloc[0].values)
    return new_df


def main():
    path = 'G:/My Drive/NCSU/Hackathons/HackNC2019/MyPueblo/backend/'
    bank_df = pd.read_csv(path+'rentclassification/bankstatement_classification.csv')

    total_df = generate_total_df(bank_df)
    ax = total_df.plot.bar(rot=0)
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.xlabel('')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.savefig(path+'Figure/total_cost.png', dpi=1200)
    plt.show()

main()
