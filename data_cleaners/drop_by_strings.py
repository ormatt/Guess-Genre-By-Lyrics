STRINGS_TO_DROP = ['']


def clean(df, _=None):
    remove_indice = []
    for col in df.columns.values:
        res = df.loc[df[col].isin(STRINGS_TO_DROP)]
        for index in res.index:
            remove_indice.append(index)

    df.drop(df.index[remove_indice], inplace=True)

    return df
