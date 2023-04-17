def retrun_statistics(data):
    print("*"*60)
    print('\n')
    print("Shape of data : \n\n",data.shape)
    print('\n')
    print("*"*60)
    print('\n')
    print("Head of data : \n\n",data.head(10))
    print('\n')
    print("*"*60)
    print('\n')
    print("Tail of data : \n\n",data.tail(10))
    print('\n')
    print("*"*60)
    print('\n')
    print("Null count of data : \n\n",data.isnull().sum())
    print('\n')
    print("*"*60)
    print('\n')
    print("Information of data : \n")
    print(data.info())
    print('\n')
    print("*"*60)
    print('\n')
    print("Description of data : \n\n",data.describe())
    
def seperate_columns_numerical_categorical(data):
    categoical_cols, numerical_cols = [], []
    for col in data.columns:
        if data[col].dtypes == 'object':
            categoical_cols.append(col)
        else:
            numerical_cols.append(col)
    return categoical_cols, numerical_cols
    
